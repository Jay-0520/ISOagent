# Local InfoSec Questionnaire Agent

Runs entirely on your Mac. Nothing leaves the machine: the chat model, the
embedding model, and the vector database all run locally via Ollama.

## How it works

1. `ingest.py` reads everything in `knowledge_base/` (past completed
   questionnaires, security policies, SOC 2 excerpts, whatever you've
   answered before), chunks it, embeds it, and stores it in a local
   ChromaDB database (`chroma_db/`).
2. `parse_questionnaire.py` reads a new incoming questionnaire (.xlsx or
   .docx) and extracts the list of questions.
3. `answer.py` ties them together: for each question, it retrieves the most
   relevant chunks from your knowledge base and asks the local model to draft
   an answer *using only that context*. Every answer comes with a confidence
   score, its source, and a `Needs Review` flag. Low-confidence or
   no-context answers are always flagged, never silently filled in.

This is a draft generator, not a submission tool. You read, correct, and
approve every answer before it goes out. That's the only sane way to run
this on something with compliance/legal weight.

## Setup

```bash
# 1. Install Ollama
brew install ollama
ollama serve &   # or just open the Ollama app

# 2. Pull the models (see sizing table below for which chat model to pick)
ollama pull nomic-embed-text
ollama pull qwen2.5:14b

# 3. Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Model sizing (pick one, edit `config.yaml` -> models.chat)

| Your Mac's unified memory | Chat model                | Notes                          |
|---------------------------|----------------------------|---------------------------------|
| 8-16 GB                   | `phi4-mini` or `qwen2.5:7b`| Usable, occasionally shaky on nuanced questions |
| 16-32 GB                  | `qwen2.5:14b` (default)    | Good balance of quality/speed   |
| 32-48 GB                  | `qwen2.5:32b` or `llama3.3:70b-q4` | Noticeably better reasoning, slower |
| 64 GB+                    | `llama3.3:70b`             | Best quality, still fully local |

Run `sysctl hw.memsize` (bytes) or check About This Mac to confirm your RAM.
The embedding model (`nomic-embed-text`, ~270 MB) is small and fine on any tier.

## Usage

```bash
# One-time (and whenever your knowledge base changes):
python ingest.py ./knowledge_base

# For each new questionnaire:
python answer.py path/to/incoming_questionnaire.xlsx
# -> output/incoming_questionnaire.answered.xlsx
#    (original columns preserved, plus Draft Answer / Confidence / Needs Review / Source columns)

python answer.py path/to/incoming_questionnaire.docx
# -> output/incoming_questionnaire.answered.docx  (answers in the form's own answer cells)
#    output/incoming_questionnaire.review.xlsx    (question / answer / confidence / matched bank entries /
#                                                  supporting materials / bank sources per row)

# To sanity-check what got extracted before running the full pipeline on a
# new questionnaire template:
python parse_questionnaire.py path/to/incoming_questionnaire.xlsx
```

## Building the knowledge base

`knowledge_base/answer_bank.md` is the single source of truth: one reviewed
answer per question, grouped in `## N. Section` headings, each entry shaped as

```
### How is data encrypted in transit?
<answer>

**Supporting materials:** [Doc name](link); Screenshot section (screenshots)

*Sources:* where the answer came from (internal)
```

`ingest.py` indexes each `###` entry as one chunk. The model only sees the
question and answer; the Supporting materials and Sources lines are stored
as metadata and show up in the review sheet, never in drafted answers.

Past questionnaires and raw source documents live in `archive/` and are
**not** indexed, so old or conflicting wording can't leak into drafts. When a
new questionnaire is completed, fold any new or changed answers into the
bank (see `answer_bank_OPEN_DECISIONS.md` for how conflicts were handled),
then re-run `python ingest.py ./knowledge_base`. Chunks from files removed
from `knowledge_base/` are dropped automatically on the next ingest.

Other formats (.txt/.md/.docx/.pdf/.xlsx) placed in `knowledge_base/` still
work; they're split into ~1200-character chunks.

## Known limitations

- **Questionnaire parsing is heuristic.** It looks for a column/header
  containing words like "question" or "control." Unusual templates may need
  a tweak to `parse_questionnaire.py`'s header-matching logic — run it with
  `--json` first to check what it extracted.
- **.docx write-back needs a Question/Answer table.** For tables with a
  "Question" and an "Answer"/"Response" header (e.g. `Nº | QUESTION | ANSWER`),
  each draft is written into the answer cell of its own row
  (`output/<name>.answered.docx`; yellow cell = needs review), and the row's
  question text is re-checked before writing: any mismatch aborts the write.
  Already-filled answer cells are never overwritten. Questions found outside
  such a table (free paragraphs, label/value tables like "Supplier name:")
  are listed as "NOT PLACED" in `output/<name>.review.xlsx` for manual copy.
- **No answer here is authoritative.** Confidence scores are the model's
  self-assessment, not a certification of correctness. The model can still
  stretch a bank answer to fit a sharper question (e.g. "built-in MFA exists"
  drafted as "MFA is enforced for admin accounts"), so always compare the
  draft with the matched bank entries in the review sheet before approving.

## Extending it

- To also handle PDF-based questionnaires, add a PDF question-extraction
  path in `parse_questionnaire.py` (loaders.py already reads PDFs for the
  knowledge base side).
- To review answers in bulk rather than in Excel, add a small local web UI
  (Streamlit works well) over `output/*.answered.xlsx`.
- If you outgrow Ollama's throughput on large questionnaires (100+
  questions), look at vLLM as a drop-in faster local backend — same models,
  much higher throughput, more setup.
