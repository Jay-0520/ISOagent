"""Collect questions asked in archive/ that the answer bank doesn't cover yet, and
rank them by importance = how many DISTINCT customers asked something similar.

    python build_reservoir.py              # -> answer_bank_reservoir.md (regenerated each run)

How it works:
1. Extract question text from every archive file (.md/.txt/.pdf/.docx/.xlsx),
   skipping files marked include: false in archive/sources.yaml.
2. Embed each question and compare it with every answer-bank entry (question
   text and full entry). Best similarity >= --cover-threshold -> covered.
3. Group the uncovered questions by similarity (>= --cluster-threshold) and
   score each group by the number of distinct customers (sources.yaml), then by
   total occurrences.

answer_bank_reservoir.md is generated: don't edit it. To "promote" a question,
write a reviewed answer into knowledge_base/answer_bank.md; on the next run
it's covered and drops off the list. Uses only the embedding model.
"""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

import chromadb
import numpy as np
import ollama
import openpyxl
import yaml

from loaders import answer_bank_entries, load_text

ARCHIVE = Path("archive")
BANK = Path("knowledge_base/answer_bank.md")
SOURCES = ARCHIVE / "sources.yaml"
OUT = Path("answer_bank_reservoir.md")
SUPPORTED = {".md", ".txt", ".pdf", ".docx", ".xlsx"}

_IMPERATIVE = re.compile(
    r"^(describe|list|explain|provide|detail|specify|indicate|outline|identify|confirm|state)\b", re.I)
_NOT_A_QUESTION = re.compile(
    r"^(yes|no|n/a|we |our |if |comment here|comments?$|please explain|please specify|"
    r"please list in the comments|please comment|please describe:?$|if other|if none|if yes|if no)", re.I)
_NUMBERING = re.compile(r"^\s*(?:\(?\d+(?:\.\d+)*\)?[.)]?\s*[-–:]?\s*|[a-z][.)]\s+|q\d+[.:)]\s*)", re.I)


def _clean(line: str) -> str:
    line = re.sub(r"\\([\\.()\-_&*#!\[\]{}+|])", r"\1", line)          # markdown escapes
    line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)                 # [text](link) -> text
    line = re.sub(r"\[[^\]]*(客户|high risk|Medium Risk|low risk)[^\]]*\]", "", line, flags=re.I)  # reviewer tags
    line = re.sub(r"[#*`>_~]+", " ", line)
    line = re.sub(r"\s+", " ", line).strip()
    return _NUMBERING.sub("", line).strip(" -–:|")


def _candidate(text: str) -> str | None:
    text = _clean(text)
    if "?" in text:
        text = text[: text.rfind("?") + 1]          # drop an answer printed after the question
        # Keep the question sentence(s) plus at most one sentence of lead-in context.
        sents = re.split(r"(?<=[.?!])\s+", text)
        first = next(i for i, x in enumerate(sents) if "?" in x)
        text = " ".join(sents[max(0, first - 1):])
    elif not _IMPERATIVE.match(text):
        return None
    words = len(text.split())
    if words < 4 or words > 90 or "http" in text or _NOT_A_QUESTION.match(text):
        return None
    return text


_BOILERPLATE = re.compile(
    r"^(comment here|comments?|please explain( / comment)?|please specify|please list in the comments|"
    r"if\b.{0,80}\bplease\b.*|supporting materials:?|evidence required.*)$", re.I)
_MAX_ANSWER = 1500


def _answer_text(parts: list[str]) -> str:
    """Join the lines that followed a question into one answer, dropping form
    boilerplate ("Comment here", "If Other, please specify") and evidence lists."""
    keep = []
    for part in parts:
        t = re.sub(r"\\([\\.()\-_&*#!\[\]{}+|])", r"\1", part)
        t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"[#*`>~]+", " ", t)
        t = re.sub(r"\(evidence required:[^)]*\)", "", t, flags=re.I)
        t = re.sub(r"\b(Additional Comments|Internal Use Only|Section Approval|Approval Conditions)\b", "", t)
        t = re.sub(r"\bif\b[^.?!]{0,80}\bplease (?:explain|specify|describe|comment)\b", "", t, flags=re.I)
        t = re.sub(r"\s+", " ", t).strip(" -–|")
        if not t or _BOILERPLATE.match(t):
            continue
        if re.match(r"^supporting materials", t, re.I):
            break                                        # evidence links follow; not part of the answer
        keep.append(t)
    return " ".join(keep)[:_MAX_ANSWER].strip()


def _from_lines(lines) -> list[tuple[str, str]]:
    """Question lines and the answer text that follows each (until the next question)."""
    pairs, pending, buf = [], None, []
    for line in lines:
        cells = [c for c in line.split(" | ") if c.strip()] or [line]
        q = _candidate(cells[0])                         # table rows: the first cell holds the question
        if q:
            if pending:
                pairs.append((pending, _answer_text(buf)))
            pending, buf = q, []
            cleaned = _clean(cells[0])
            if "?" in cleaned:                           # "Question? Answer" on the same line
                buf.append(cleaned[cleaned.rfind("?") + 1:])
            buf += cells[1:]                             # other table cells hold the answer
        elif pending:
            buf.append(line)
    if pending:
        pairs.append((pending, _answer_text(buf)))
    return pairs


def _from_pdf(text: str) -> list[tuple[str, str]]:
    # PDF lines are wrapped mid-sentence: rejoin, then split into sentences.
    flat = re.sub(r"\s+", " ", text)
    sents = re.split(r"(?<=[?.!])\s+", flat)
    counts: dict[str, int] = {}
    for x in sents:
        counts[x] = counts.get(x, 0) + 1
    pairs, pending, buf = [], None, []
    for s in sents:
        if counts[s] >= 3:                               # repeated page headers/footers
            continue
        # A sentence can start with the tail of the previous answer: cut at the
        # last question number inside it ("... case-by-case 5.2 If SSO is ...").
        nums = list(re.finditer(r"(?:^|\s)\d+\.\d+\s+(?=[A-Z])", s))
        head = ""
        if nums:
            head, s = s[:nums[-1].start()], s[nums[-1].end():]
        q = _candidate(s)
        if q and q.endswith("?"):
            if pending:
                pairs.append((pending, _answer_text(buf + [head])))
            pending, buf = q, []
        elif pending:
            buf.append((head + " " + s).strip())
    if pending:
        pairs.append((pending, _answer_text(buf)))
    return pairs


_ANSWER_COLS = re.compile(r"answer|response|comment|yes|^no$|n/a", re.I)
_CUSTOMER_COLS = re.compile(r"ciso|risk|notes|description|requirement", re.I)


def _from_xlsx(path: Path) -> list[tuple[str, str]]:
    pairs = []
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        col, header, start = None, None, 0
        for r_i, r in enumerate(rows[:20]):             # header may sit below a title row
            for i, v in enumerate(r):
                if isinstance(v, str) and v.strip().lower() in ("question", "questions"):
                    col, header, start = i, r, r_i + 1
                    break
            if col is not None:
                break
        if col is None:
            continue
        ans_cols = [(i, str(h).strip()) for i, h in enumerate(header)
                    if i != col and isinstance(h, str) and _ANSWER_COLS.search(h) and not _CUSTOMER_COLS.search(h)]
        for r in rows[start:]:
            v = r[col] if col < len(r) else None
            if not isinstance(v, str):
                continue
            q = _clean(v)
            if len(q.split()) < 4 or _NOT_A_QUESTION.match(q):
                continue
            parts = []
            for i, h in ans_cols:
                a = r[i] if i < len(r) else None
                if a is None or (isinstance(a, str) and (not a.strip() or a.startswith("="))):
                    continue
                if h.lower() in ("yes", "no", "n/a"):
                    parts.append(h)                      # an "X" in the Yes / No / N/A column
                else:
                    parts.append(str(a))
            pairs.append((q, _answer_text(parts)))
    return pairs


def extract_pairs(path: Path) -> list[tuple[str, str]]:
    """(question, answer) pairs from one archive file; answer may be ''."""
    s = path.suffix.lower()
    if s == ".xlsx":
        pairs = _from_xlsx(path)
    elif s == ".pdf":
        pairs = _from_pdf(load_text(path))
    else:
        pairs = _from_lines(load_text(path).splitlines())
    seen, out = {}, []
    for q, a in pairs:
        k = re.sub(r"\W+", " ", q.lower()).strip()
        if k not in seen:
            seen[k] = len(out)
            out.append((q, a))
        elif a and not out[seen[k]][1]:
            out[seen[k]] = (q, a)                        # keep the copy that has an answer
    return out


def extract_questions(path: Path) -> list[str]:
    return [q for q, _ in extract_pairs(path)]


def _neutralize(q: str, names: list[str]) -> str:
    """Replace customer names with "the customer" before comparing, so "Do you encrypt
    all IFF data at rest?" matches the bank as well as "...all customer data..." would."""
    for n in names:
        q = re.sub(rf"\b{re.escape(n)}(?:'s|’s)?\b", "the customer", q, flags=re.I)
    return q


def _embed(texts: list[str], model: str) -> np.ndarray:
    v = np.array([ollama.embeddings(model=model, prompt=t)["embedding"] for t in texts])
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def main() -> int:
    ap = argparse.ArgumentParser(description="Rank archive questions the answer bank doesn't cover.")
    ap.add_argument("--cover-threshold", type=float, default=0.75,
                    help="similarity to a bank entry at/above which a question counts as covered")
    ap.add_argument("--cluster-threshold", type=float, default=0.80,
                    help="similarity at/above which two uncovered questions count as the same question")
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    embed_model = yaml.safe_load(open(args.config))["models"]["embed"]
    sources = yaml.safe_load(SOURCES.read_text()) if SOURCES.exists() else {}

    # 1. Extract
    items, untagged, per_file = [], [], []
    for path in sorted(ARCHIVE.iterdir()):
        if (path.suffix.lower() not in SUPPORTED or path.name.startswith("~$")
                or path.name.endswith(".review.xlsx")):
            continue
        meta = sources.get(path.name) or {}
        if meta.get("include", True) is False:
            per_file.append((path.name, "excluded in sources.yaml", 0))
            continue
        customer = meta.get("customer")
        if not customer:
            customer = path.stem
            untagged.append(path.name)
        pairs = extract_pairs(path)
        use_answers = meta.get("answers", True) is not False  # answers: false -> questions only
        per_file.append((path.name, customer, len(pairs)))
        items += [{"q": q, "a": a if use_answers else "", "file": path.name, "customer": customer}
                  for q, a in pairs]
    print(f"Extracted {len(items)} questions from {sum(1 for f in per_file if f[2])} files.")

    # 2. Coverage against the bank
    bank = answer_bank_entries(BANK.read_text(encoding="utf-8"))
    print(f"Embedding {len(bank)} bank entries and {len(items)} archive questions...")
    B_q, B_full = _embed([e["question"] for e in bank], embed_model), _embed([e["text"] for e in bank], embed_model)
    names = {m.get("customer") for m in sources.values() if isinstance(m, dict) and m.get("customer")}
    names |= {n.split()[0] for n in names}           # "NOVA Chemicals" -> also "NOVA"
    names = sorted(names | {"the client", "Chemical AI Inc"} - {"Chemical AI Inc"}, key=len, reverse=True)
    Q = _embed([_neutralize(it["q"], names) for it in items], embed_model)
    sim = np.maximum(Q @ B_q.T, Q @ B_full.T)
    for it, row in zip(items, sim):
        j = int(row.argmax())
        it["best_bank"], it["best_score"] = bank[j]["question"], float(row[j])
    uncovered = [i for i, it in enumerate(items) if it["best_score"] < args.cover_threshold]
    print(f"Covered by the bank: {len(items) - len(uncovered)}; not covered: {len(uncovered)}")

    # 3. Group similar uncovered questions (greedy, against each group's mean vector)
    groups: list[dict] = []
    for i in uncovered:
        v = Q[i]
        best, best_s = None, -1.0
        for g in groups:
            c = g["sum"] / np.linalg.norm(g["sum"])
            s = float(v @ c)
            if s > best_s:
                best, best_s = g, s
        if best is not None and best_s >= args.cluster_threshold:
            best["members"].append(i); best["sum"] = best["sum"] + v
        else:
            groups.append({"members": [i], "sum": v.copy()})
    for g in groups:
        c = g["sum"] / np.linalg.norm(g["sum"])
        g["rep"] = max(g["members"], key=lambda i: float(Q[i] @ c))
        g["customers"] = sorted({items[i]["customer"] for i in g["members"]})
        g["score"] = len(g["customers"])
        seen, answers = set(), []
        for i in [g["rep"]] + [m for m in g["members"] if m != g["rep"]]:
            a = items[i]["a"]
            k = re.sub(r"\W+", " ", a.lower())[:200]
            if a and k not in seen:
                seen.add(k)
                answers.append((a, items[i]["customer"], items[i]["file"]))
        g["answers"] = answers
    groups.sort(key=lambda g: (-g["score"], -len(g["members"]), items[g["rep"]]["q"].lower()))

    # 4. Write
    L = [
        "# Answer Bank – Reservoir of Uncovered Questions",
        "",
        f"Generated {date.today().isoformat()} by `build_reservoir.py` – **don't edit by hand**; it is rebuilt on every run.",
        "Questions asked in `archive/` that `knowledge_base/answer_bank.md` doesn't cover yet, ranked by",
        "**importance = number of distinct customers** who asked something similar (then by number of times asked).",
        "To promote one: write a reviewed answer into `answer_bank.md` and re-run; covered questions drop off.",
        "",
        f"Settings: covered if similarity to a bank entry ≥ {args.cover_threshold}; "
        f"questions grouped at similarity ≥ {args.cluster_threshold}. "
        f"Customers come from `archive/sources.yaml`.",
        "",
        f"**{len(groups)} uncovered questions** (from {len(uncovered)} of {len(items)} archive questions; "
        f"{len(items) - len(uncovered)} already covered by the bank). "
        f"{sum(1 for g in groups if items[g['rep']]['best_score'] >= args.cover_threshold - 0.05)} are marked ⚠️ "
        f"possibly already covered (similarity within 0.05 of the cut-off).",
        "",
    ]
    if untagged:
        L += ["**Not tagged in `archive/sources.yaml` (each counted as its own customer):** "
              + ", ".join(f"`{u}`" for u in untagged), ""]
    L += ["---", ""]
    for n, g in enumerate(groups, 1):
        rep = items[g["rep"]]
        L += [
            f"### {n}. {rep['q']}",
            f"**Importance:** {g['score']} customer{'s' if g['score'] != 1 else ''} "
            f"({', '.join(g['customers'])}) · asked {len(g['members'])} time{'s' if len(g['members']) != 1 else ''}  ",
            f"**Closest bank entry:** \"{rep['best_bank']}\" (similarity {rep['best_score']:.2f})"
            + ("  \n⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*"
               if rep["best_score"] >= args.cover_threshold - 0.05 else ""),
        ]
        others = [i for i in g["members"] if i != g["rep"]]
        if others:
            L.append("**Also asked as:**")
            L += [f"- \"{items[i]['q']}\" — {items[i]['customer']} (`{items[i]['file']}`)" for i in others[:6]]
            if len(others) > 6:
                L.append(f"- … and {len(others) - 6} more")
        if g["answers"]:
            L.append("**Past answers (from archive – unreviewed, may be outdated):**")
            L += [f"- {a} — *{c}* (`{f}`)" for a, c, f in g["answers"][:3]]
        else:
            L.append("**Past answers:** none found in the archive")
        L += [f"*First seen in:* `{rep['file']}`", ""]
    L += ["---", "", "## Extraction summary", "", "| File | Customer | Questions extracted |", "|---|---|---|"]
    L += [f"| {f} | {c} | {n} |" for f, c, n in per_file]
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")

    # Index reservoir entries that have a past answer, for answer.py's second tier.
    cfg = yaml.safe_load(open(args.config))
    client = chromadb.PersistentClient(path=cfg["chroma"]["persist_dir"])
    name = cfg["chroma"].get("reservoir_collection", "infosec_reservoir")
    try:
        client.delete_collection(name)                   # rebuilt from scratch every run
    except Exception:
        pass
    col = client.create_collection(name, metadata={"hnsw:space": "cosine"})
    answered = [g for g in groups if g["answers"]]
    if answered:
        docs = [f"Q: {items[g['rep']]['q']}\nA: {g['answers'][0][0]}" for g in answered]
        col.add(
            ids=[f"reservoir::{n}" for n in range(len(answered))],
            embeddings=_embed([_neutralize(items[g["rep"]]["q"], names) for g in answered], embed_model).tolist(),
            documents=docs,
            metadatas=[{
                "source": "answer_bank_reservoir.md",
                "question": items[g["rep"]]["q"],
                "customers": ", ".join(g["customers"]),
                "answers": "\n---\n".join(f"[{c}] {a}" for a, c, _ in g["answers"][:3]),
                "bank_sources": "; ".join(sorted({f for _, _, f in g["answers"]})),
            } for g in answered],
        )
    print(f"Indexed {len(answered)} reservoir entries with past answers into collection '{name}'.")
    print(f"Wrote {OUT}: {len(groups)} uncovered questions, top importance {groups[0]['score'] if groups else 0}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
