# Local InfoSec Questionnaire Agent

Drafts answers to customer security questionnaires (Word or Excel) for
Chemical.AI / ChemAIRS, from a reviewed answer bank. Runs entirely on your
Mac: the chat model, the embedding model and the vector database all run
locally via Ollama, and nothing leaves the machine.

This is a draft generator, not a submission tool. You read, correct and
approve every answer before it goes out.

## Project layout

| Path | What it is |
|---|---|
| `knowledge_base/answer_bank.md` | **The golden source.** One reviewed answer per question. The only file that is indexed as a reviewed source. |
| `answer_bank_OPEN_DECISIONS.md` | Conflicts between old documents that you still need to decide. Not indexed. |
| `answer_bank_reservoir.md` | **Generated.** Questions from `archive/` that the bank doesn't cover yet, ranked by importance, with past answers. Don't edit by hand. |
| `archive/` | Every past questionnaire and filled-out form. Source of the reservoir. |
| `archive/sources.yaml` | Which customer each archive file belongs to (and which files to skip). |
| `output/` | Results of `answer.py` runs. |
| `chroma_db/` | Local search index (rebuilt by the scripts, not in git). |
| `converted_docx/` | Word copies of older PDF/Markdown source documents, for reference. |
| `answer.py` | Drafts answers for a questionnaire. |
| `ingest.py` | Indexes the answer bank. |
| `build_reservoir.py` | Builds the reservoir and its index from `archive/`. |
| `parse_questionnaire.py` | Finds the questions (and answer cells) in a questionnaire. |
| `loaders.py` | Reads .md/.txt/.docx/.pdf/.xlsx files; splits the bank into entries. |
| `config.yaml` | Models, retrieval and answering settings. |
| `test_pipeline.py` | Offline tests (no model calls). |

## Setup

```bash
# 1. Install Ollama
brew install ollama
ollama serve &   # or just open the Ollama app

# 2. Pull the models
ollama pull qwen3.5:9b          # chat model, ~6.6 GB
ollama pull nomic-embed-text    # embedding model, ~270 MB

# 3. Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Build both indexes
python ingest.py ./knowledge_base
python build_reservoir.py
```

## Models

| Role | Model | Size | Set in `config.yaml` |
|---|---|---|---|
| Drafting answers | `qwen3.5:9b` | ~6.6 GB | `models.chat` |
| Search (embeddings) | `nomic-embed-text` | ~270 MB | `models.embed` |

- Qwen 3.5 is a "thinking" model. `models.chat_think: false` (the default)
  makes it answer directly; `true` makes it reason step by step first, which
  can help on tricky questions but makes every question slower.
- `qwen3.5:9b` fits comfortably on a 16 GB Mac.
- Changing the chat model needs no re-indexing. Changing the embedding model
  does: re-run `ingest.py` and `build_reservoir.py` afterwards.

## Workflow

### For each new questionnaire

1. **Check the questions are found.** It lists every question it will answer:
   ```bash
   python parse_questionnaire.py "path/to/questionnaire.docx"
   ```
2. **Draft the answers** (about 25 seconds per question):
   ```bash
   python answer.py "path/to/questionnaire.docx"
   ```
3. **Review** `output/<name>.answered.docx` together with
   `output/<name>.review.xlsx`:
   - Every shaded cell needs a look: yellow = from the answer bank but
     low-confidence or partial, blue = from a past archive answer
     (unreviewed), orange = written by the model alone (check every fact,
     replace every `[CONFIRM: …]`).
   - For each question the review sheet shows the answer source, confidence,
     the bank entries used, their supporting materials, and a Reviewer Note
     with anything the draft couldn't cover.
   - Questions with no answer cell in the document are marked "NOT PLACED"
     in the review sheet; copy those answers by hand.
4. **Send** the reviewed form to the customer.

### After sending

5. **Archive the form and tag it:**
   ```bash
   mv "output/<name>.answered.docx" archive/
   open -e archive/sources.yaml
   ```
   Add a line with the customer name. If the answers were sent without
   review, add `answers: false` so they're never reused as past answers.
6. **Rebuild the reservoir** (embedding model only, 1–2 minutes):
   ```bash
   python build_reservoir.py
   ```

### Growing the answer bank

7. **Work through `answer_bank_reservoir.md` from the top.** The most important
   questions (asked by the most customers) come first, each with past
   answers and the closest existing bank entry. Items marked ⚠️ may already
   be covered by the bank; check before adding.
8. **Write a reviewed answer into `knowledge_base/answer_bank.md`** in the
   entry format below. If sources disagree, decide yourself rather than
   taking the newest document (past conflicts and decisions are in
   `answer_bank_OPEN_DECISIONS.md`).
9. **Re-index both**, so the new answer is used and leaves the reservoir:
   ```bash
   python ingest.py ./knowledge_base
   python build_reservoir.py
   ```

## How answers are produced

`answer.py` tries three sources in order for each question:

| Tier | Source | When it's used | Weight | Word shading when flagged |
|---|---|---|---|---|
| 1 | Answer bank (`answer_bank.md`) | Always tried first | 1.0 | yellow |
| 2 | Reservoir (past answers in `archive/`) | The bank has no answer | 0.6 | blue |
| 3 | Model only, with bank entries as background | Neither has an answer | 0.3 | orange |

- **Confidence** = the model's own confidence × the source weight
  (`answering.source_weights` in `config.yaml`).
- **Needs Review** is set for anything not from the bank, anything below
  `low_confidence_threshold` (0.6), and any partial answer.
- In tier 2, if past answers disagree, the draft keeps only what they agree
  on and the disagreement goes to the Reviewer Note.
- In tier 3, company facts the bank doesn't give become `[CONFIRM: …]`
  placeholders instead of being invented. Set `llm_fallback: false` to skip
  tier 3 and leave those questions blank.
- The model reports which entries it used; only those feed the evidence
  columns. Notes about missing information ("the context does not
  specify…") are kept out of the answer and moved to the Reviewer Note.
- Retrieval takes the 12 most similar bank entries (`retrieval.top_k`) and
  6 reservoir entries (`retrieval.reservoir_top_k`).

## The answer bank

`knowledge_base/answer_bank.md` is grouped in `## N. Section` headings. Each
entry looks like this:

```
### How is data encrypted in transit?
<answer>

**Supporting materials:** [Doc name](link); Screenshot section (screenshots)

*Sources:* where the answer came from (internal)
```

- `ingest.py` indexes each `###` entry as one chunk. The model only sees the
  question and answer; Supporting materials and Sources are stored with the
  entry and shown in the review sheet, never written into answers.
- Supporting materials link to the evidence documents (Feishu). Sources
  (e.g. `Decision C8`, `IFF-VRA 6.4`) record where the answer came from and
  are for internal use only.
- Chunks from files removed from `knowledge_base/` are dropped automatically
  on the next ingest.

## The reservoir

`build_reservoir.py` extracts the questions and answers from every file in
`archive/`, drops the questions the bank already covers, groups similar ones,
and writes `answer_bank_reservoir.md`, ranked by **importance = number of
distinct customers** who asked something similar (then by how often it was
asked). It also indexes the questions that have past answers as a second
search collection (`infosec_reservoir`) for tier 2.

- **`archive/sources.yaml`** maps each file to a customer, so copies and
  follow-ups from one customer count once. `include: false` skips a file
  entirely (not a questionnaire, or a duplicate); `answers: false` counts
  its questions but never reuses its answers. Untagged files count as their
  own customer and are listed at the top of the reservoir.
- **Matching is by embedding similarity:** a question counts as covered at
  ≥ 0.75 and two questions count as the same at ≥ 0.80 (calibrated on this
  archive; change with `--cover-threshold` / `--cluster-threshold`).
- Past answers in the reservoir are unreviewed and may be outdated.
- Don't edit `answer_bank_reservoir.md`; it's rebuilt every run.

## Output files

| File | Contents |
|---|---|
| `output/<name>.answered.docx` | The customer's form with drafts in its own answer cells; flagged cells shaded by source |
| `output/<name>.review.xlsx` | One row per question: draft, Answer Source, Confidence, Model Confidence, Needs Review, Reviewer Note, matched entries, supporting materials, internal sources, placement |
| `output/<name>.answered.xlsx` | For Excel questionnaires: the original sheet plus Draft Answer, Confidence, Needs Review, Matched Bank Entries, Supporting Materials and Answer Source columns |

Only `.answered.docx` / `.answered.xlsx` files go into `archive/`, not
`.review.xlsx`.

## Tests

Offline checks, with no model calls:

```bash
python -c "import test_pipeline as t; t.test_answer_bank_entries(); t.test_tiered_answering(); t.test_docx_writeback()"
```

## Known limitations

- **Question detection is heuristic.** Word forms need a table with a
  "Question" and an "Answer"/"Response" header for answers to be written
  back. Excel forms need the "Question" header in **row 1** (the Siegfried
  form, with its header in row 2, isn't supported by `answer.py` yet).
  Cover-page fields like "Supplier name:" aren't filled in. Always run
  `parse_questionnaire.py` first on a new template.
- **The model can overstate.** It can stretch a bank answer to fit a sharper
  question (e.g. "built-in MFA exists" drafted as "MFA is enforced for admin
  accounts"). Compare each draft with its matched entries.
- **Reservoir answers can be outdated.** The archive still contains answers
  that were later corrected in the bank; tier-2 drafts are always flagged.
- **Speed:** about 25 seconds per question, more for questions that fall
  through to tiers 2 and 3. Lowering `retrieval.top_k` speeds it up at some
  cost to recall.
- **Similarity scores are approximate.** The reservoir may list a question the
  bank already answers (marked ⚠️) or group two different questions.

## Extending it

- Detect the header row in Excel questionnaires (like `build_reservoir.py`
  already does) so forms like Siegfried's can be answered.
- Fill cover-page label/value fields ("Supplier name:") from the supplier
  entries in the bank.
- Add a small local review UI (e.g. Streamlit) over `output/*.review.xlsx`.
