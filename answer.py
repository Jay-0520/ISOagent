"""Retrieve relevant context for each question and draft an answer with a
local chat model. Nothing here auto-submits anything: every answer is written
back with a confidence score and a REVIEW flag, and you read/edit before
sending. Treat this as a first-draft generator, not a submission pipeline.

Usage:
    python answer.py incoming_questionnaire.xlsx
    -> writes output/incoming_questionnaire.answered.xlsx
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

import chromadb
import ollama
import openpyxl
import yaml
from docx import Document as DocxDocument
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from tqdm import tqdm

from parse_questionnaire import numbering_gaps, parse_questionnaire, Question

SYSTEM_PROMPT = """You are drafting answers to a vendor information security \
questionnaire on behalf of the company, using ONLY the provided context \
(prior answers, policy excerpts). Rules:
- If the context clearly answers the question, give a direct, factual answer \
in the company's voice (e.g. "We encrypt data at rest using AES-256...").
- If the context is partial, answer only what the context supports. Put what \
is missing in "gaps" (a note for the internal reviewer), never in "answer".
- If the context does not address the question at all, say exactly: \
"NO_MATCHING_CONTEXT" as the answer, and nothing else.
- Never invent specifics (certifications, dates, tool names, percentages) \
that are not in the context.
- Keep answers under {max_words} words.
- Write the answer itself, ready to paste into the questionnaire. Never mention \
"the context", the entries, or where the information came from.
- Context entries are numbered [1], [2], ... List the numbers of the entries \
your answer actually relies on in "used".
Respond ONLY as JSON: {{"answer": "...", "confidence": 0.0-1.0, "used": [1, 2], "gaps": ""}}
("gaps" is an empty string when the context fully answers the question.)
confidence reflects how directly and completely the context supports the \
answer, not how fluent the answer sounds.
"""


RESERVOIR_NOTE = """The numbered context below is PAST answers Chemical.AI gave to other \
customers (unreviewed; may be outdated, and may disagree with each other). If they \
disagree on a fact, do not pick one: answer only what they agree on and describe \
the disagreement in "gaps".
"""

LLM_PROMPT = """You are drafting an answer to a vendor information security \
questionnaire question on behalf of Chemical.AI (product: ChemAIRS). There is NO \
reviewed answer for this question. The numbered background entries are reviewed \
facts about the company; use them where relevant. Rules:
- Never invent company-specific facts (certifications, dates, names, numbers, \
tools, frequencies, locations). Where the answer needs such a fact that the \
background does not give, write a placeholder like [CONFIRM: backup frequency].
- Keep answers under {max_words} words, in the company's voice, ready to paste. \
Never mention the background, the entries, or where information came from.
- List every placeholder or unsupported claim in "gaps".
- In "used", list the background entries you relied on (may be empty).
Respond ONLY as JSON: {{"answer": "...", "confidence": 0.0-1.0, "used": [1, 2], "gaps": ""}}
confidence reflects how much of the answer is supported by the background.
"""

TIER_LABEL = {"bank": "Answer bank", "reservoir": "Reservoir (archive, unreviewed)", "llm": "Model only (unverified)"}


def load_config(path: str = "config.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def embed_query(model: str, text: str) -> list[float]:
    return ollama.embeddings(model=model, prompt=text)["embedding"]


def retrieve(collection, cfg: dict, question: str):
    vec = embed_query(cfg["models"]["embed"], question)
    res = collection.query(query_embeddings=[vec], n_results=cfg["retrieval"]["top_k"])
    docs = res["documents"][0] if res["documents"] else []
    dists = res["distances"][0] if res["distances"] else []
    metas = res["metadatas"][0] if res["metadatas"] else []
    # Chroma returns distance (lower = closer); convert to a 0-1 similarity-ish score.
    hits = []
    for doc, dist, meta in zip(docs, dists, metas):
        score = max(0.0, 1.0 - dist)
        if score >= cfg["retrieval"]["min_score"]:
            hits.append({
                "text": doc,
                "score": score,
                "source": meta.get("source", "?"),
                # Answer-bank chunks carry the matched question plus evidence as metadata.
                "question": meta.get("question", ""),
                "materials": meta.get("materials", ""),
                "bank_sources": meta.get("bank_sources", ""),
                "answers": meta.get("answers", ""),        # reservoir entries: past answers by customer
                "customers": meta.get("customers", ""),
            })
    return hits


def _label(hit: dict) -> str:
    return f"{hit['source']} › {hit['question']}" if hit.get("question") else hit["source"]


def _md_links_to_text(s: str) -> str:
    # "[Name](https://x)" -> "Name: https://x" so links survive in Excel cells.
    return re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1: \2", s)


def _collect(hits: list[dict], key: str) -> str:
    seen, out = set(), []
    for h in hits:
        for item in (x.strip() for x in h.get(key, "").split(";")):
            if item and item not in seen:
                seen.add(item)
                out.append(item)
    return "\n".join(out)


_REVIEWER_NOTE_RE = re.compile(
    r"\bcontext\b|\bnot (?:specified|mentioned|provided|stated|detailed|available|covered|addressed)\b"
    r"|\b(?:is|are) missing\b|\bno (?:information|details?) (?:on|about|regarding)\b",
    re.I,
)


def _split_reviewer_notes(answer: str) -> tuple[str, str]:
    """Safety net for the customer-facing text: move sentences that talk about
    the retrieved context or what it lacks ("The context does not specify...")
    out of the answer and into the reviewer note."""
    sentences = re.split(r"(?<=[.!?])\s+", answer.strip())
    keep = [s for s in sentences if not _REVIEWER_NOTE_RE.search(s)]
    notes = [s for s in sentences if _REVIEWER_NOTE_RE.search(s)]
    return " ".join(keep).strip(), " ".join(notes).strip()


def draft_answer(cfg: dict, question: str, hits: list[dict], tier: str = "bank") -> dict:
    """tier: "bank" (reviewed entries), "reservoir" (past answers from the archive) or
    "llm" (model alone, with bank entries as background only)."""
    if not hits and tier != "llm":
        return {"answer": "NO_MATCHING_CONTEXT", "confidence": 0.0, "sources": [],
                "materials": "", "bank_sources": "", "gaps": ""}

    def entry_text(h):
        if tier == "reservoir":
            return f"Q: {h['question']}\nPast answers:\n{h['answers']}"
        return h["text"]
    context = "\n\n".join(f"[{i}] ({_label(h)})\n{entry_text(h)}" for i, h in enumerate(hits, 1)) or "(none)"
    prompt = (
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Respond with the JSON object only."
    )
    words = cfg["answering"]["max_answer_words"]
    if tier == "llm":
        system = LLM_PROMPT.format(max_words=words)
    else:
        system = SYSTEM_PROMPT.format(max_words=words) + (RESERVOIR_NOTE if tier == "reservoir" else "")
    resp = ollama.chat(
        model=cfg["models"]["chat"],
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        format="json",
        options={"num_ctx": cfg["answering"].get("num_ctx", 8192)},
        # Only sent when configured: models without a thinking mode may reject it.
        **({"think": cfg["models"]["chat_think"]} if "chat_think" in cfg["models"] else {}),
    )
    raw = resp["message"]["content"]
    try:
        parsed = json.loads(raw)
        answer = str(parsed.get("answer", "")).strip()
        confidence = float(parsed.get("confidence", 0.0))
        used_ids = [int(i) for i in parsed.get("used", []) if str(i).isdigit()]
        gaps = str(parsed.get("gaps", "") or "").strip()
    except (json.JSONDecodeError, ValueError, TypeError):
        answer, confidence = raw.strip(), 0.3  # model didn't follow JSON format; keep but distrust it
        used_ids, gaps = [], ""
    # Evidence comes only from the entries the model says it used (fallback: the top match).
    used = [hits[i - 1] for i in dict.fromkeys(used_ids) if 1 <= i <= len(hits)] or (hits[:1] if tier != "llm" else [])
    if answer == "NO_MATCHING_CONTEXT":
        used = []  # no answer drafted, so no evidence to show
    else:
        answer, notes = _split_reviewer_notes(answer)
        gaps = " ".join(x for x in (gaps, notes) if x)
        if not answer:  # the whole draft was a note about missing information
            answer, used = "NO_MATCHING_CONTEXT", []

    return {
        "answer": answer,
        "confidence": confidence,
        "sources": [_label(h) for h in used],
        "materials": _md_links_to_text(_collect(used, "materials")),
        "bank_sources": _collect(used, "bank_sources"),
        "gaps": gaps,
    }


def _open_collection(client, name: str):
    try:
        return client.get_collection(name)
    except Exception:
        return None


def process_questions(cfg: dict, questions: list[Question]) -> list[dict]:
    client = chromadb.PersistentClient(path=cfg["chroma"]["persist_dir"])
    bank = client.get_or_create_collection(cfg["chroma"]["collection"], metadata={"hnsw:space": "cosine"})
    reservoir = _open_collection(client, cfg["chroma"].get("reservoir_collection", "infosec_reservoir"))
    if reservoir is None:
        print("NOTE: no reservoir index found (run build_reservoir.py); tier 2 is skipped.")
    weights = cfg["answering"].get("source_weights", {"bank": 1.0, "reservoir": 0.6, "llm": 0.3})
    llm_fallback = cfg["answering"].get("llm_fallback", True)
    reservoir_cfg = {**cfg, "retrieval": {**cfg["retrieval"], "top_k": cfg["retrieval"].get("reservoir_top_k", 6)}}

    results = []
    for q in tqdm(questions, desc="Drafting answers"):
        base = {
            "id": q.id,
            "sheet": q.sheet,
            "row": q.row,
            "section": q.section,
            "question": q.text,
            "answer_col": q.answer_col,
        }
        if q.answer_col is not None and q.existing_answer:
            # The answer cell is already filled in the document; never overwrite it.
            results.append({**base, "answer": q.existing_answer, "confidence": None, "model_confidence": None,
                            "tier": "", "sources": "", "materials": "", "bank_sources": "", "gaps": "",
                            "needs_review": False, "kept_existing": True})
            continue

        # 1. reviewed answer bank -> 2. reservoir of past answers -> 3. model alone
        bank_hits = retrieve(bank, cfg, q.prompt_text)
        tier, draft = "bank", draft_answer(cfg, q.prompt_text, bank_hits, "bank")
        if draft["answer"] == "NO_MATCHING_CONTEXT" and reservoir is not None and reservoir.count():
            reservoir_hits = retrieve(reservoir, reservoir_cfg, q.prompt_text)
            tier, draft = "reservoir", draft_answer(cfg, q.prompt_text, reservoir_hits, "reservoir")
        if draft["answer"] == "NO_MATCHING_CONTEXT" and llm_fallback:
            background = bank_hits[: cfg["retrieval"].get("reservoir_top_k", 6)]
            tier, draft = "llm", draft_answer(cfg, q.prompt_text, background, "llm")

        answered = draft["answer"] != "NO_MATCHING_CONTEXT"
        final = round(draft["confidence"] * weights.get(tier, 0.0), 2) if answered else 0.0
        needs_review = (
            not answered
            or tier != "bank"                          # unreviewed source: always check
            or final < cfg["answering"]["low_confidence_threshold"]
            or bool(draft["gaps"])                     # partially answered: a reviewer must fill the gap
        )
        results.append(
            {
                **base,
                "answer": draft["answer"] if answered else "",
                "tier": TIER_LABEL[tier] if answered else "",
                "model_confidence": round(draft["confidence"], 2) if answered else 0.0,
                "confidence": final,
                "sources": "\n".join(draft["sources"]),
                "materials": draft["materials"],
                "bank_sources": draft["bank_sources"],
                "gaps": draft["gaps"],
                "needs_review": needs_review,
                "kept_existing": False,
            }
        )
    return results


def write_xlsx_output(original: Path, results: list[dict], out_path: Path) -> None:
    shutil.copy(original, out_path)
    wb = openpyxl.load_workbook(out_path)

    by_sheet: dict[str, list[dict]] = {}
    for r in results:
        by_sheet.setdefault(r["sheet"], []).append(r)

    for sheet_name, rows in by_sheet.items():
        ws = wb[sheet_name]
        # Figure out where to put new columns: right after the existing header row.
        header_row = 1
        next_col = ws.max_column + 1
        answer_col = next_col
        conf_col = next_col + 1
        review_col = next_col + 2
        src_col = next_col + 3
        mat_col = next_col + 4
        tier_col = next_col + 5
        ws.cell(row=header_row, column=answer_col, value="Draft Answer (AI)")
        ws.cell(row=header_row, column=conf_col, value="Confidence")
        ws.cell(row=header_row, column=review_col, value="Needs Review")
        ws.cell(row=header_row, column=src_col, value="Matched Bank Entries")
        ws.cell(row=header_row, column=mat_col, value="Supporting Materials")
        ws.cell(row=header_row, column=tier_col, value="Answer Source")

        for r in rows:
            ws.cell(row=r["row"], column=answer_col, value=r["answer"])
            ws.cell(row=r["row"], column=conf_col, value=r["confidence"])
            ws.cell(row=r["row"], column=review_col, value="YES" if r["needs_review"] else "")
            ws.cell(row=r["row"], column=src_col, value=r["sources"])
            ws.cell(row=r["row"], column=mat_col, value=r["materials"])
            ws.cell(row=r["row"], column=tier_col, value=r.get("tier", ""))

    wb.save(out_path)


REVIEW_FILL = "FFF2CC"  # yellow: from the answer bank, but needs review (low confidence / gaps / blank)
TIER_FILL = {
    TIER_LABEL["reservoir"]: "DDEBF7",  # blue: from past archive answers (unreviewed)
    TIER_LABEL["llm"]: "FCE4D6",     # orange: model only, unverified - check every fact
}


def _shade_cell(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    for old in tc_pr.findall(qn("w:shd")):
        tc_pr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def _write_text(paragraph, text: str) -> None:
    # Append to the cell's existing (empty) paragraph so it keeps the template's
    # formatting; line breaks inside the answer become soft breaks.
    run = paragraph.add_run()
    for i, line in enumerate(text.splitlines()):
        if i:
            run.add_break()
        run.add_text(line)


def write_docx_output(original: Path, results: list[dict], out_path: Path) -> None:
    """Write each draft into the exact answer cell its question came from.

    Placement is by (table, row, answer column) recorded at parse time, and every
    write first re-checks that the row still contains the question text; any
    mismatch aborts the whole write rather than risk a shifted answer. Drafts
    flagged for review get a yellow cell background. Cells that already had
    text are left untouched."""
    doc = DocxDocument(str(original))

    mismatches = []
    targets = []
    for r in results:
        if r["answer_col"] is None or r["kept_existing"]:
            continue
        table = doc.tables[int(r["sheet"].removeprefix("table"))]
        row = table.rows[r["row"]]
        if not any(c.text.strip() == r["question"] for c in row.cells):
            mismatches.append(r["id"])
            continue
        targets.append((row.cells[r["answer_col"]], r))
    if mismatches:
        raise RuntimeError(f"Question text not found at its recorded position for: "
                           f"{', '.join(mismatches)}. Nothing was written.")

    for cell, r in targets:
        if cell.text.strip():
            continue
        if r["answer"]:
            _write_text(cell.paragraphs[0], r["answer"])
        if r["needs_review"]:
            _shade_cell(cell, TIER_FILL.get(r.get("tier", ""), REVIEW_FILL))

    doc.save(str(out_path))


def write_review_sheet(results: list[dict], out_path: Path) -> None:
    """One row per question, in document order, for side-by-side review."""
    import pandas as pd

    rows = []
    for r in results:
        if r["kept_existing"]:
            status = "kept existing answer"
        elif r["answer_col"] is None:
            status = "NOT PLACED - copy manually"
        else:
            status = "written to document"
        rows.append({
            "ID": r["id"],
            "Section": r["section"],
            "Question": r["question"],
            "Draft Answer (AI)": r["answer"],
            "Answer Source": r.get("tier", ""),
            "Confidence": r["confidence"],
            "Model Confidence": r.get("model_confidence"),
            "Needs Review": "YES" if r["needs_review"] else "",
            "Reviewer Note (gaps)": r.get("gaps", ""),
            "Matched Bank Entries": r["sources"],
            "Supporting Materials": r["materials"],
            "Bank Sources (internal)": r["bank_sources"],
            "Placement": status,
        })
    pd.DataFrame(rows).to_excel(out_path, index=False)


def main() -> int:
    ap = argparse.ArgumentParser(description="Draft answers for a questionnaire using the local KB.")
    ap.add_argument("questionnaire", help="Path to .xlsx or .docx questionnaire")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--out-dir", default="output")
    args = ap.parse_args()

    cfg = load_config(args.config)
    path = Path(args.questionnaire)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(exist_ok=True)

    questions = parse_questionnaire(path)
    if not questions:
        print("No questions found. Check that the file matches an expected layout "
              "(see parse_questionnaire.py --json to debug).")
        return 1

    print(f"Found {len(questions)} questions.")
    gaps = numbering_gaps(questions)
    if gaps:
        print(f"WARNING: numbering gaps, possibly missed questions: {', '.join(gaps)}")
    print("Drafting answers from local knowledge base...")
    results = process_questions(cfg, questions)

    flagged = sum(1 for r in results if r["needs_review"])
    kept = sum(1 for r in results if r["kept_existing"])
    by_tier = {label: sum(1 for r in results if r.get("tier") == label) for label in TIER_LABEL.values()}
    print("Answer sources: " + ", ".join(f"{k}: {v}" for k, v in by_tier.items())
          + f", unanswered: {sum(1 for r in results if not r['kept_existing'] and not r['answer'])}")
    print(f"Done. {len(results) - flagged - kept} drafted with reasonable confidence, "
          f"{flagged} flagged for manual review, {kept} already answered (left as is).")

    if path.suffix.lower() == ".xlsx":
        out_path = out_dir / f"{path.stem}.answered.xlsx"
        write_xlsx_output(path, results, out_path)
        print(f"Wrote: {out_path}")
    else:
        out_path = out_dir / f"{path.stem}.answered.docx"
        write_docx_output(path, results, out_path)
        review_path = out_dir / f"{path.stem}.review.xlsx"
        write_review_sheet(results, review_path)
        unplaced = sum(1 for r in results if r["answer_col"] is None)
        print(f"Wrote: {out_path}  (needs review: yellow = answer bank, blue = past archive answer, "
              f"orange = model only)")
        print(f"Wrote: {review_path}  (question/answer/confidence/sources side by side)")
        if unplaced:
            print(f"NOTE: {unplaced} questions had no answer cell in the document; "
                  f"see 'NOT PLACED' rows in the review sheet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
