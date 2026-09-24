# Answer Bank – Conflicts for Manual Review

Conflicts already integrated into `knowledge_base/answer_bank.md` have been removed from this file (removed 2026-09-23: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C14, C15, C16, C17, C18, C19, C20, C22, C23, C24, C25, C26, C27, C28, C29, C30, C31, C32, C34, C35; removed 2026-09-24: C36).

Every place where the knowledge-base documents disagree. For each conflict, the
contested claim has been **removed** from `knowledge_base/answer_bank.md`. Until
you decide, the agent finds no answer for it and flags that question for review.

Nothing here has been settled for you: not by which document is newer, by how many
documents agree, or by what looks like an obvious typo. Notes add neutral context
only.

This file sits outside `knowledge_base/`, so it is never indexed.

**To decide one:** write your answer under "Decision", add it to `answer_bank.md`,
then re-run `python ingest.py ./knowledge_base`. Each conflict ends with a **Status** line.

Source abbreviations and dates (where the document states one):

| Short name | File | Date |
|---|---|---|
| NOVA | NOVA Cloud Security Risk Assessment Template.pdf | 10 Feb 2025 |
| FMC | FMC - Security Risk Assessment.pdf (same text as NOVA) | – |
| InfoSec | Information_security_questionnaire.pdf (NOVA and Merck merged) | – |
| Merck | Merck Chemical.ai evaluation filled.pdf | – |
| Grü-PDF / Grü-md | Grunenthal_information_security_check.pdf / Information_Security_Questions_Summary.md | – |
| Acadia | Cybersecurity Questions.jay.acadia.docx | – |
| Jazz | Jazz_questionnaires.md | – |
| PIA | Chemical.AI PIA.xlsx (Gilead) | – |
| Gilead-email | Answers to Gilead Email Questions.md | – |
| Gilead-FU | Gilead_follow_up_email_question.md | sent 1 Dec 2025 |
| Servier-Q | Servier_information_security_questionnaire (SaaS).md | – |
| Servier-email | Answers_to_Email_Questions_Servier.md | – |
| Servier-Priv | _Evaluation Risk-Data Privacy Questionnaire.md | – |
| IFF-VRA / IFF-SDA | Vendor Risk Assessment / Solution Design Assessment (IFF) | 6 Aug 2026 |
| SuppMat | Information_Security_Question_Supporting_Materials.md (summaries of internal policies, reports and screenshots) | – |

---

## C. Data retention, deletion and location

### C13. Backup design and disaster-recovery backup location
- NOVA/FMC 3.9: "full backups are performed on a daily basis, after which copies of the data are re-created and continue to be dumped into a dedicated storage server"
- Grü Q22 and Q47: "Daily full backups … (7 generations), with data stored in multiple physically isolated availability zones"
- Acadia: "daily full backups (7 generations) stored across multiple physically isolated AWS availability zones, plus a remote disaster-recovery backup"
- Servier-Q Q17, Q25, Q38: "dual-layer backups (local + remote DR)"; "3-month remote DR retention with physical destruction afterward"
- Merck Q6: "stored on technologically advanced storage mediums with RAID 5 and LVM, accompanied by encrypted off-site backups"
- Servier-email: "no SaaS data is stored outside the U.S."
- SuppMat, SaaS Regulations §7–9: "Dual-layer protection: local backup + remote disaster recovery"; local: "7-day retention, AES-256 encryption, automatic cleanup"; remote: "3-month retention, TLS 1.2 + AES-256, physical destruction after 3 months"
- SuppMat, ISMS-2-CL-002 Backup Policy: "Off-site backup storage requirements", "Annual review of off-site storage providers"
- ESTEVE questionnaire (2026-09), DPC access answer: "All data is stored in the US, in AWS data centres." (sentence left out of the merged bank until C13 is decided)

*Note:* no source says where the remote DR backup is (another AWS region? the IDC?) or what "physical destruction" applies to. If the DR copy sits outside the US, it conflicts with the US-only storage claim.
*Removed from bank:* the backup entry and the "No SaaS data is stored outside the U.S." sentence.

**Decision:**
mark unknown for now.

Updated 2026-09-24: all data, including backups, is stored in the US, in AWS data centres.

**Status:** ✅ Location integrated into answer_bank.md (2026-09-24). Not decided: what "physical destruction" of DR backups means (the bank says backups are overwritten).

---

## E. Security testing and operations

### C21. SIEM
- IFF-VRA 6.10 ("Do you have a SIEM solution?"): ☒ Internal
- IFF-SDA 3.5 ("Is there a service or SIEM in place?"): ☒ No
- Servier-Q Q28 (SOC or detection tools): lists GuardDuty, WAF, Grafana Loki, CloudWatch and the H3C IPS; no SIEM product named

*Removed from bank:* nothing was claimed (the bank describes central log monitoring without the word SIEM).

**Decision:**
No SIEM claim

**Status:** ✅ No change to the bank, as decided (no SIEM claim).

---

## I. New conflicts from the Supporting Materials document

### C33. Unit testing and code coverage
- Grü Q65: white-box testing includes "Unit Testing: Developer-created tests for individual functions and methods"; success criteria "Minimum 80% code coverage for security-critical components"
- Servier-Q Q59: "Structure Test (White Box): Static code analysis, mandatory peer review, unit testing"
- SuppMat, ChemAIRS-backend Code Analysis Report (SonarQube, 2024-09-14): "Test Coverage: 0.0% (no tests implemented)"; also 43 "Critical" code smells (maintainability, not security; "No security vulnerabilities found")

*Removed from bank:* "unit tests" and "at least 80% coverage". Also corrected: the bank's "zero critical static-analysis findings" now reads "zero critical security vulnerabilities from static analysis", matching Grü Q65.

**Decision:**
Leave this as-is. The bank's statement is correct: there are zero critical security vulnerabilities from static analysis. The other statements about unit testing and code coverage are not supported by the source documents.

**Status:** ✅ No change to the bank, as decided.

---

## J. Errors inside single source documents (they don't affect the bank)

Consider fixing these in the source files, or archiving the files:
- **Copy-paste errors in NOVA/FMC/InfoSec:**
  - 3.12 (breach notification) has the catastrophic-failure text
  - 3.13 (change of location) has the breach text
  - 3.8 repeats a sentence
  - 4.5 answers decommissioning with "Please refer to 4.4"
  - InfoSec Q41 "refer to 3.8" (that numbering no longer exists)
- **FMC 3.5** still says "stored outside of Canada" (left over from NOVA).
- **Jazz:**
  - reaction data updated "twice a year" vs. "when we do the annual update" in the same answer
  - (h) answers "No." and then describes a contract that does address data ownership
  - (e) "Limited … No."
- **PIA** data portability: "Yes" + "However, individuals do not have direct self-service access".
- **Internal notes left in:**
  - Grü `[Note: remove "partially"]`
  - Grü `(note: 我们先用 … 试一下)` ("let's try … first")
  - Grü-md `(note only for myself …)`
  - InfoSec Q2 "Questions still remain?"
  - Gilead-FU Chinese notes and the struck-through draft
- **Grü Q51:** says ISO 27001 certification "provides independent, third-party verification that environment separation controls are properly implemented".
