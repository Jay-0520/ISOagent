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
- If the context is partial, answer what you can and say what's missing.
- If the context does not address the question at all, say exactly: \
"NO_MATCHING_CONTEXT" as the answer, and nothing else.
- Never invent specifics (certifications, dates, tool names, percentages) \
that are not in the context.
- Keep answers under {max_words} words.
Respond ONLY as JSON: {{"answer": "...", "confidence": 0.0-1.0}}
confidence reflects how directly and completely the context supports the \
answer, not how fluent the answer sounds.
"""


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
            hits.append({"text": doc, "score": score, "source": meta.get("source", "?")})
    return hits


def draft_answer(cfg: dict, question: str, hits: list[dict]) -> dict:
    if not hits:
        return {"answer": "NO_MATCHING_CONTEXT", "confidence": 0.0, "sources": []}

    context = "\n\n".join(f"[{h['source']}]\n{h['text']}" for h in hits)
    prompt = (
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Respond with the JSON object only."
    )
    system = SYSTEM_PROMPT.format(max_words=cfg["answering"]["max_answer_words"])
    resp = ollama.chat(
        model=cfg["models"]["chat"],
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        format="json",
    )
    raw = resp["message"]["content"]
    try:
        parsed = json.loads(raw)
        answer = str(parsed.get("answer", "")).strip()
        confidence = float(parsed.get("confidence", 0.0))
    except (json.JSONDecodeError, ValueError, TypeError):
        answer, confidence = raw.strip(), 0.3  # model didn't follow JSON format; keep but distrust it

    return {"answer": answer, "confidence": confidence, "sources": [h["source"] for h in hits]}


def process_questions(cfg: dict, questions: list[Question]) -> list[dict]:
    client = chromadb.PersistentClient(path=cfg["chroma"]["persist_dir"])
    collection = client.get_or_create_collection(
        cfg["chroma"]["collection"], metadata={"hnsw:space": "cosine"}
    )

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
            results.append({**base, "answer": q.existing_answer, "confidence": None,
                            "sources": "", "needs_review": False, "kept_existing": True})
            continue
        hits = retrieve(collection, cfg, q.prompt_text)
        draft = draft_answer(cfg, q.prompt_text, hits)
        needs_review = (
            draft["answer"] == "NO_MATCHING_CONTEXT"
            or draft["confidence"] < cfg["answering"]["low_confidence_threshold"]
        )
        results.append(
            {
                **base,
                "answer": "" if draft["answer"] == "NO_MATCHING_CONTEXT" else draft["answer"],
                "confidence": round(draft["confidence"], 2),
                "sources": ", ".join(draft["sources"]),
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
        ws.cell(row=header_row, column=answer_col, value="Draft Answer (AI)")
        ws.cell(row=header_row, column=conf_col, value="Confidence")
        ws.cell(row=header_row, column=review_col, value="Needs Review")
        ws.cell(row=header_row, column=src_col, value="Source(s)")

        for r in rows:
            ws.cell(row=r["row"], column=answer_col, value=r["answer"])
            ws.cell(row=r["row"], column=conf_col, value=r["confidence"])
            ws.cell(row=r["row"], column=review_col, value="YES" if r["needs_review"] else "")
            ws.cell(row=r["row"], column=src_col, value=r["sources"])

    wb.save(out_path)


REVIEW_FILL = "FFF2CC"  # light yellow cell shading = "AI draft, needs review"


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
            _shade_cell(cell, REVIEW_FILL)

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
            "Confidence": r["confidence"],
            "Needs Review": "YES" if r["needs_review"] else "",
            "Source(s)": r["sources"],
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
        print(f"Wrote: {out_path}  (yellow cells = needs review)")
        print(f"Wrote: {review_path}  (question/answer/confidence/sources side by side)")
        if unplaced:
            print(f"NOTE: {unplaced} questions had no answer cell in the document; "
                  f"see 'NOT PLACED' rows in the review sheet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
