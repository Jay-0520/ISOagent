"""Index knowledge base documents (past questionnaire answers, policies, SOC 2
excerpts, etc.) into a local ChromaDB collection using a local Ollama embedding
model. Re-running this is safe: chunks are keyed by file path + chunk index, so
re-ingesting a changed file replaces its old chunks, and chunks from files that are
no longer in the directory are removed.

An answer bank (markdown with ### question entries and *Sources:* lines) is indexed
one question per chunk; its Supporting materials / Sources lines are stored as
metadata rather than in the text the model sees.

Usage:
    python ingest.py ./knowledge_base
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import chromadb
import ollama
import yaml
from tqdm import tqdm

from loaders import answer_bank_entries, chunk_text, iter_knowledge_base_files


def load_config(path: str = "config.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def embed(model: str, texts: list[str]) -> list[list[float]]:
    vectors = []
    for t in texts:
        resp = ollama.embeddings(model=model, prompt=t)
        vectors.append(resp["embedding"])
    return vectors


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest knowledge base docs into ChromaDB.")
    parser.add_argument("kb_dir", help="Directory of source documents (.txt, .md, .docx, .pdf)")
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    kb_dir = Path(args.kb_dir)
    if not kb_dir.exists():
        print(f"Knowledge base directory not found: {kb_dir}", file=sys.stderr)
        return 1

    client = chromadb.PersistentClient(path=cfg["chroma"]["persist_dir"])
    collection = client.get_or_create_collection(
        cfg["chroma"]["collection"], metadata={"hnsw:space": "cosine"}
    )

    files = list(iter_knowledge_base_files(kb_dir))
    if not files:
        print(f"No .txt/.md/.docx/.pdf files found under {kb_dir}")
        return 0

    total_chunks = 0
    for path in tqdm(files, desc="Indexing files"):
        try:
            from loaders import load_text
            text = load_text(path)
        except Exception as e:
            print(f"  skipped {path.name}: {e}", file=sys.stderr)
            continue

        rel = str(path.relative_to(kb_dir))
        # Answer banks are indexed one question per chunk, with supporting
        # materials / sources as metadata; everything else is split by size.
        entries = answer_bank_entries(text) if path.suffix.lower() == ".md" else []
        if entries:
            chunks = [e["text"] for e in entries]
            metadatas = [
                {"source": rel, "chunk": i, "question": e["question"], "section": e["section"],
                 "materials": e["materials"], "bank_sources": e["bank_sources"]}
                for i, e in enumerate(entries)
            ]
        else:
            chunks = list(
                chunk_text(
                    text,
                    cfg["chunking"]["chunk_size_chars"],
                    cfg["chunking"]["chunk_overlap_chars"],
                )
            )
            metadatas = [{"source": rel, "chunk": i} for i in range(len(chunks))]
        if not chunks:
            continue

        # Remove any previously indexed chunks for this file before re-adding.
        existing = collection.get(where={"source": rel})
        if existing["ids"]:
            collection.delete(ids=existing["ids"])

        ids = [f"{rel}::{i}" for i in range(len(chunks))]
        vectors = embed(cfg["models"]["embed"], chunks)
        collection.add(ids=ids, embeddings=vectors, documents=chunks, metadatas=metadatas)
        total_chunks += len(chunks)

    # Drop chunks from files that are no longer in the knowledge base (moved or deleted).
    current = {str(p.relative_to(kb_dir)) for p in files}
    stale = collection.get(include=["metadatas"])
    stale_ids = [i for i, m in zip(stale["ids"], stale["metadatas"]) if m.get("source") not in current]
    if stale_ids:
        collection.delete(ids=stale_ids)
        gone = sorted({m["source"] for m in stale["metadatas"] if m.get("source") not in current})
        print(f"Removed {len(stale_ids)} stale chunks from {len(gone)} files no longer in {kb_dir}:")
        for g in gone:
            print(f"  - {g}")

    print(f"Indexed {total_chunks} chunks from {len(files)} files into "
          f"'{cfg['chroma']['collection']}' at {cfg['chroma']['persist_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
