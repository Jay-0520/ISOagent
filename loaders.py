"""Document loading and chunking for the knowledge base."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterator

from docx import Document as DocxDocument
from pypdf import PdfReader


def load_text(path: Path) -> str:
    """Extract raw text from a .txt, .md, .docx, .pdf, or .xlsx file."""
    suffix = path.suffix.lower()
    if suffix in (".txt", ".md"):
        return path.read_text(encoding="utf-8", errors="ignore")
    if suffix == ".docx":
        return docx_text(DocxDocument(str(path)))
    if suffix == ".pdf":
        reader = PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if suffix == ".xlsx":
        # One line per row (e.g. "Question | Answer | Notes"), so a past
        # question and its answer stay together in the same chunk.
        import pandas as pd

        parts = []
        for sheet, df in pd.read_excel(path, sheet_name=None, header=None, dtype=str).items():
            parts.append(f"[{sheet}]")
            for _, row in df.fillna("").iterrows():
                cells = [str(v).strip() for v in row if str(v).strip()]
                if cells:
                    parts.append(" | ".join(cells))
        return "\n".join(parts)
    raise ValueError(f"Unsupported file type for knowledge base: {path.name}")


_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
_BOX_RE = re.compile(r"(?=[☐☒])")


def _xml_text(el) -> str:
    # Every w:t / w:tab under the element, so text inside content controls
    # (w:sdt: dropdowns, checkboxes, date pickers) is included; python-docx's
    # Paragraph.text skips those, which is where form answers usually live.
    out = []
    for node in el.iter(f"{_W}t", f"{_W}tab", f"{_W}br"):
        out.append(node.text or "" if node.tag == f"{_W}t" else " ")
    return _checked_only("".join(out)).strip()


def _checked_only(text: str) -> str:
    """Form checkboxes render as ☒ (ticked) / ☐ (unticked) glyphs followed by
    a label. Keep ticked options, drop unticked ones, so "☒ISO 27001 ☐SOC 2"
    reads as "☒ISO 27001" instead of listing every option as if it applied."""
    if "☐" not in text and "☒" not in text:
        return text
    return " ".join(seg.strip() for seg in _BOX_RE.split(text)
                    if seg.strip() and not seg.startswith("☐"))


def _block_lines(el) -> list[str]:
    tag = el.tag
    if tag == f"{_W}p":
        t = _xml_text(el)
        return [t] if t else []
    if tag == f"{_W}tbl":
        lines = []
        for tr in el.iter(f"{_W}tr"):
            if tr.getparent() is not el:
                continue  # nested tables are covered by their parent cell's text
            cells = [_xml_text(tc) for tc in tr.findall(f"{_W}tc")]
            cells = [c for c in cells if c]
            if cells:
                lines.append(" | ".join(cells))
        return lines
    if tag == f"{_W}sdt":  # block-level content control wrapping paragraphs/tables
        content = el.find(f"{_W}sdtContent")
        return [l for child in (content if content is not None else []) for l in _block_lines(child)]
    return []


def docx_text(doc) -> str:
    """Document-order text of a .docx: paragraphs and table rows interleaved as
    they appear, including content-control values and only ticked checkboxes."""
    return "\n".join(l for child in doc.element.body.iterchildren() for l in _block_lines(child))


def chunk_text(text: str, chunk_size_chars: int, overlap_chars: int) -> Iterator[str]:
    """Split text into overlapping chunks on paragraph/sentence boundaries where possible."""
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not text:
        return
    if len(text) <= chunk_size_chars:
        yield text
        return

    start = 0
    n = len(text)
    while start < n:
        end = min(start + chunk_size_chars, n)
        # Try to break on a paragraph or sentence boundary near the end.
        window = text[start:end]
        break_at = max(window.rfind("\n\n"), window.rfind(". "))
        if break_at > chunk_size_chars * 0.5:
            end = start + break_at + 1
        chunk = text[start:end].strip()
        if chunk:
            yield chunk
        if end >= n:
            break
        start = max(end - overlap_chars, start + 1)


_MATERIALS_RE = re.compile(r"^\*\*Supporting materials:\*\*\s*(.*)$", re.M)
_SOURCES_RE = re.compile(r"^\*Sources:\*\s*(.*)$", re.M)


def answer_bank_entries(text: str) -> list[dict]:
    """Split an answer bank (## sections, ### question entries) into one record
    per question. The chunk text the model sees is the question plus answer only;
    'Supporting materials' and 'Sources' lines are returned separately so they
    travel as metadata (for the review sheet) and can't leak into drafted answers.
    Returns [] for markdown that isn't shaped like an answer bank."""
    if not re.search(r"^### ", text, re.M) or not _SOURCES_RE.search(text):
        return []
    entries = []
    section = ""
    for block in re.split(r"(?m)^(?=## |### )", text):
        if block.startswith("## "):
            section = re.sub(r"^\d+\.\s*", "", block.splitlines()[0][3:]).strip()
            continue
        if not block.startswith("### "):
            continue  # preamble: instructions for editors, not answers
        lines = block.splitlines()
        question = lines[0][4:].strip()
        body = "\n".join(lines[1:])
        m_mat, m_src = _MATERIALS_RE.search(body), _SOURCES_RE.search(body)
        cut = min(m.start() for m in (m_mat, m_src) if m) if (m_mat or m_src) else len(body)
        answer = re.sub(r"\n---\s*$", "", body[:cut]).strip()
        if not answer:
            continue
        materials = m_mat.group(1).strip() if m_mat else ""
        if materials.startswith("none in the Supporting Materials"):
            materials = ""
        entries.append({
            "question": question,
            "section": section,
            "answer": answer,
            "text": f"{section}\nQ: {question}\nA: {answer}",
            "materials": materials,
            "bank_sources": m_src.group(1).strip() if m_src else "",
        })
    return entries


def iter_knowledge_base_files(kb_dir: Path) -> Iterator[Path]:
    exts = {".txt", ".md", ".docx", ".pdf", ".xlsx"}
    for path in sorted(kb_dir.rglob("*")):
        if path.is_file() and path.suffix.lower() in exts:
            yield path
