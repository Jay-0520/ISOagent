"""Offline smoke test for the ingest -> retrieve -> answer pipeline.

Mocks Ollama's embeddings/chat calls (no local model available in this
sandbox) with a simple bag-of-words embedding and a canned-but-realistic
chat response, so we can verify the *pipeline logic* — chunking, retrieval
scoring, thresholding, review-flagging, xlsx output — end to end without
needing a real model. Swap in the real Ollama calls on your Mac and this
same code path runs unchanged.
"""
import hashlib
import json
import re
import shutil
from pathlib import Path
from unittest import mock

import numpy as np

VOCAB_SIZE = 4096
STOPWORDS = {
    "the", "a", "an", "is", "are", "do", "does", "you", "your", "have", "has",
    "of", "to", "and", "or", "in", "on", "for", "with", "using", "at", "as",
    "this", "that", "all", "any", "be", "it", "its", "was", "were", "what",
    "name", "organization", "company",
}


def fake_embed_text(text: str) -> list[float]:
    """Deterministic character-trigram embedding over content words (stopwords
    dropped): good enough to make related text score higher than unrelated
    text (and tolerate encrypt/encrypted-style word-form differences), which
    is all this pipeline test needs. A real embedding model is semantic, not
    lexical, but this is a fair stand-in for exercising the retrieval/
    threshold/flagging logic offline."""
    vec = np.zeros(VOCAB_SIZE)
    words = [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOPWORDS]
    for word in words:
        padded = f"  {word}  "
        for i in range(len(padded) - 2):
            trigram = padded[i:i + 3]
            idx = int(hashlib.md5(trigram.encode()).hexdigest(), 16) % VOCAB_SIZE
            vec[idx] += 1.0
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec.tolist()


def fake_ollama_embeddings(model, prompt):
    return {"embedding": fake_embed_text(prompt)}


def fake_ollama_chat(model, messages, format=None):
    user_msg = messages[-1]["content"]
    # Extract the context and question the same way the real prompt does.
    if "Context:\n" not in user_msg:
        answer = {"answer": "NO_MATCHING_CONTEXT", "confidence": 0.0}
    else:
        context = user_msg.split("Context:\n")[1].split("\n\nQuestion:")[0]
        if "AES-256" in context or "incident response" in context.lower():
            answer = {
                "answer": "Yes. " + context.strip().splitlines()[0][:150],
                "confidence": 0.9,
            }
        else:
            answer = {"answer": "NO_MATCHING_CONTEXT", "confidence": 0.0}
    return {"message": {"content": json.dumps(answer)}}


def test_docx_writeback():
    """Word Q/A table: every question found (incl. ones without '?'), each
    answer lands in its own row's answer cell, pre-filled cells are kept, and a
    shifted position aborts the write instead of misplacing answers."""
    from docx import Document

    from parse_questionnaire import numbering_gaps, parse_questionnaire
    import answer as answer_mod

    test_dir = Path("test_run_docx")
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()

    src = test_dir / "form.docx"
    doc = Document()
    doc.add_paragraph("Supplier Assessment Form")
    table = doc.add_table(rows=1, cols=3)
    for cell, h in zip(table.rows[0].cells, ["Nº", "QUESTION", "ANSWER"]):
        cell.text = h
    rows = [
        ("1", "Encryption", ""),
        ("1.1", "Is data encrypted at rest?", ""),
        ("1.2", "Is data encrypted in transit?", "Yes, TLS 1.2+ (already answered)"),
        ("2", "Certifications", "*Attach evidence"),
        ("2.1", "ISO 27001/27002", ""),
        ("2.2", "SOC 2 Type II", ""),
    ]
    for values in rows:
        cells = table.add_row().cells
        for cell, v in zip(cells, values):
            cell.text = v
    doc.save(str(src))

    questions = parse_questionnaire(src)
    assert [q.id for q in questions] == ["1.1", "1.2", "2.1", "2.2"], [q.id for q in questions]
    assert questions[2].section == "Certifications"
    assert questions[1].existing_answer.startswith("Yes, TLS")
    assert numbering_gaps(questions) == []
    print(f"[docx parse] extracted {len(questions)} questions, no numbering gaps")

    results = [
        {"id": q.id, "sheet": q.sheet, "row": q.row, "section": q.section,
         "question": q.text, "answer_col": q.answer_col,
         "answer": "" if q.id == "2.2" else f"Draft for {q.id}",
         "confidence": 0.9, "sources": "", "needs_review": q.id == "2.2",
         "kept_existing": bool(q.existing_answer)}
        for q in questions
    ]
    out = test_dir / "form.answered.docx"
    answer_mod.write_docx_output(src, results, out)
    t = Document(str(out)).tables[0]
    by_num = {r.cells[0].text: r.cells[2] for r in t.rows}
    assert by_num["1.1"].text == "Draft for 1.1"
    assert by_num["1.2"].text == "Yes, TLS 1.2+ (already answered)"
    assert by_num["2"].text == "*Attach evidence"
    assert by_num["2.1"].text == "Draft for 2.1"
    assert by_num["2.2"].text == "" and by_num["2.2"]._tc.xpath(".//w:shd/@w:fill") == [answer_mod.REVIEW_FILL]
    print("[docx write] answers placed in their own rows; existing answers kept")

    results[0]["row"] += 1  # simulate a stale/shifted position
    try:
        answer_mod.write_docx_output(src, results, test_dir / "shifted.docx")
        raise AssertionError("expected a shifted row to abort the write")
    except RuntimeError:
        assert not (test_dir / "shifted.docx").exists()
    print("[docx write] shifted position aborted the write")


def test_answer_bank_entries():
    """Answer bank: one record per ### question; evidence lines kept out of the text."""
    from loaders import answer_bank_entries

    bank = (
        "# Bank\n\nEditor notes that must not be indexed.\n\n---\n\n"
        "## 1. Encryption\n\n"
        "### How is data encrypted in transit?\nHTTPS with TLS 1.2 and TLS 1.3.\n\n"
        "**Supporting materials:** [Cert](https://x/cert); Screens (screenshots)\n\n"
        "*Sources:* NOVA 3.1; Decision C8\n\n"
        "### Have you had a breach?\nNo.\n\n"
        "**Supporting materials:** none in the Supporting Materials document\n\n"
        "*Sources:* IFF-VRA 8.7\n\n---\n\n"
        "## 2. People\n\n"
        "### Is training required?\n- On hire\n- Twice per year\n\n*Sources:* IFF-VRA 4.4\n"
    )
    e = answer_bank_entries(bank)
    assert [x["question"] for x in e] == ["How is data encrypted in transit?", "Have you had a breach?", "Is training required?"]
    assert e[0]["section"] == "Encryption" and e[2]["section"] == "People"
    assert e[0]["answer"] == "HTTPS with TLS 1.2 and TLS 1.3."
    assert e[0]["materials"] == "[Cert](https://x/cert); Screens (screenshots)"
    assert e[0]["bank_sources"] == "NOVA 3.1; Decision C8"
    assert e[1]["materials"] == ""  # "none in the Supporting Materials document" -> empty
    assert e[2]["answer"] == "- On hire\n- Twice per year"
    for x in e:
        assert "Sources" not in x["text"] and "Supporting materials" not in x["text"]
        assert "Editor notes" not in x["text"]
    assert answer_bank_entries("# Plain notes\n\nNo question entries here.") == []
    print("[answer bank] 3 entries split; evidence kept out of chunk text")


def main():
    test_answer_bank_entries()
    test_docx_writeback()

    import chromadb
    import yaml

    from loaders import chunk_text, load_text, iter_knowledge_base_files
    from parse_questionnaire import parse_questionnaire
    import answer as answer_mod

    test_dir = Path("test_run")
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()

    cfg = yaml.safe_load(open("config.yaml"))
    cfg["chroma"]["persist_dir"] = str(test_dir / "chroma_db")

    with mock.patch("ollama.embeddings", side_effect=fake_ollama_embeddings), \
         mock.patch("ollama.chat", side_effect=fake_ollama_chat):

        # --- ingest ---
        client = chromadb.PersistentClient(path=cfg["chroma"]["persist_dir"])
        collection = client.get_or_create_collection(
            cfg["chroma"]["collection"], metadata={"hnsw:space": "cosine"}
        )
        kb_dir = Path("knowledge_base")
        total = 0
        for path in iter_knowledge_base_files(kb_dir):
            text = load_text(path)
            chunks = list(chunk_text(text, cfg["chunking"]["chunk_size_chars"], cfg["chunking"]["chunk_overlap_chars"]))
            if not chunks:
                continue
            rel = str(path.relative_to(kb_dir))
            ids = [f"{rel}::{i}" for i in range(len(chunks))]
            metas = [{"source": rel, "chunk": i} for i in range(len(chunks))]
            vecs = [fake_embed_text(c) for c in chunks]
            collection.add(ids=ids, embeddings=vecs, documents=chunks, metadatas=metas)
            total += len(chunks)
        print(f"[ingest] indexed {total} chunks")
        assert total > 0, "expected at least one chunk from knowledge_base/"

        # --- parse ---
        questions = parse_questionnaire(Path("sample_questionnaire.xlsx"))
        print(f"[parse] extracted {len(questions)} questions")
        assert len(questions) == 3

        # --- answer ---
        results = answer_mod.process_questions(cfg, questions)
        for r in results:
            print(f"  Q: {r['question'][:70]}")
            print(f"     answer={r['answer'][:80]!r} confidence={r['confidence']} "
                  f"needs_review={r['needs_review']} sources={r['sources']}")

        encrypt_result = next(r for r in results if "encrypt" in r["question"].lower())
        incident_result = next(r for r in results if "incident" in r["question"].lower())
        pet_result = next(r for r in results if "pet" in r["question"].lower())

        assert not encrypt_result["needs_review"], "encryption question should be answered confidently"
        assert encrypt_result["answer"], "encryption question should have a non-empty answer"
        assert not incident_result["needs_review"], "incident response question should be answered confidently"
        assert pet_result["needs_review"], "unrelated question should be flagged for review"
        assert pet_result["answer"] == "", "unrelated question should not get a fabricated answer"

        # --- write xlsx output ---
        out_path = test_dir / "sample_questionnaire.answered.xlsx"
        answer_mod.write_xlsx_output(Path("sample_questionnaire.xlsx"), results, out_path)
        assert out_path.exists()

        import openpyxl
        wb = openpyxl.load_workbook(out_path)
        ws = wb["Security"]
        header = [c.value for c in ws[1]]
        assert "Draft Answer (AI)" in header
        assert "Needs Review" in header
        print(f"[write] output written to {out_path}, header={header}")

    print("\nALL CHECKS PASSED")


if __name__ == "__main__":
    main()
