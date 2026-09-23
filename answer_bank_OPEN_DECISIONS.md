# Answer Bank – Conflicts for Manual Review

Every place where the knowledge-base documents disagree. For each conflict, the
contested claim has been **removed** from `knowledge_base/answer_bank.md`. Until
you decide, the agent finds no answer for it and flags that question for review.

Nothing here has been settled for you: not by which document is newer, by how many
documents agree, or by what looks like an obvious typo. Notes add neutral context
only.

This file sits outside `knowledge_base/`, so it is never indexed.

**To decide one:** write your answer under "Decision", add it to `answer_bank.md`,
then re-run `python ingest.py ./knowledge_base`.

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

## A. Authentication and access

### C1. Built-in MFA in the ChemAIRS application
- NOVA 5.3, FMC 5.3, InfoSec Q34: "In development."
- Grü-PDF/md Q33: "MFA is in development"; Q55: "MFA (Multi-Factor Authentication): In development (like Google Authenticator)"
- Servier-Q Q5.2 and Q18: "multi-factor authentication (in development)"; Q32: "will be protected by MFA capabilities under our access-control roadmap"
- Acadia: "MFA is enabled for the ChemAIRS application via time-based one-time passwords (TOTP) using an authenticator app"
- IFF-SDA 4.3: SSO via Entra ID "to integrate the solution with IFF MFA authentication"
- SuppMat, SaaS Regulations §5: "Access Control - Multi-factor authentication, privilege separation, audit logs (1+ year retention), privilege review"
- SuppMat, Coding Standards 2.4.1 (a development requirement): "Anomaly detection: Multi-factor auth for unusual login locations"
- SuppMat, Penetration Test Report, test categories: "Authentication Security: Multi-factor authentication, session management, password policies…" (lists MFA as a test category; does not state it exists)

*Note:* the SaaS Regulations list MFA as an access-control requirement; that states a requirement, not whether it is live.
*Removed from bank:* any statement on built-in MFA. (Kept, because no source disputes it: the customer's IdP can enforce MFA through SSO.)

**Decision:**

### C2. MFA for remote access to Chemical.AI's own network
- IFF-VRA 6.4: ticked ☒VPN Access ☒Username and password ☒Multi-factor authentication
- Servier-Q Q23 ("Do you enforce MFA … for remote access?"): "…and MFA capabilities in development"

*Removed from bank:* "requires … multi-factor authentication" in the remote-access answer.

**Decision:**

### C3. Access review frequency
- Grü-PDF/md Q12, Servier-Q Q5.3: "periodic reviews" (no frequency)
- Acadia: "quarterly for privileged accounts and semi-annually for regular users"
- IFF-VRA 6.16: "privileged accounts reviewed quarterly; regular users semi-annually"
- Servier-Q Q32 and Q33: "quarterly reviews for privileged users"
- SuppMat, ISMS-2-CL-012 Access Control Policy: "Permission maintenance and review (quarterly for privileged users, semi-annually for regular users)"

*Note:* no source gives a different number; the older ones give no number at all.
*Removed from bank:* the "How often are access rights reviewed?" entry.

**Decision:**

### C4. Password policy: expiry and length (application vs. corporate)
- NOVA 5.7, Grü Q11 (the ChemAIRS password policy): length, complexity, banned passwords; **no expiry**
- Grü Q55: "Password authentication with security policies (complexity, expiry)"
- IFF-VRA 6.15: ticked ☒Password expiration
- Servier-Q Q18: "ISMS-2-CL-001: Password Policy with regular password changes"
- SuppMat, ISMS-2-CL-001 Password Policy: "Regular password changes"
- SuppMat, ISMS-2-CL-007 Secret Authentication Information Policy: "Regular password changes", "Minimum length of 6 characters"
- SuppMat, Employee Information Security Handbook: "12+ character complexity, 180-day rotation"
- SuppMat, Coding Standards 2.1 / 2.4: "8+ characters with mixed case, numbers, special characters"

*Removed from bank:* "corporate password policy also requires regular password changes".

*Note:* the answer bank now labels its password entry "ChemAIRS application password policy" (8 characters, from NOVA 5.7 and Grü Q11). The corporate policies above give different lengths (6 vs. 12+) and rotation rules.

**Decision:** (does the ChemAIRS app enforce expiry? what is the corporate policy: length, rotation?)

### C5. Group mapping via SAML/OIDC
- IFF-SDA 4.4 "Do you provide group mapping via SAML 2.0 or OIDC?": ticked ☒ Yes; comment in the same answer: "Today: manual user pre-creation with SSO credential validation; SCIM/automated group mapping evaluated case-by-case."

*Removed from bank:* nothing was claimed.

**Decision:**

### C6. Who is the named information security lead?
- IFF-VRA 1.6: "Percentage of time dedicated to Information Security 25% / Name Jay Huang / Title Platform Engineer"
- Servier-Q Q13 ("person responsible for information security (CISO or equivalent)"): "the CEO/Data Security Administrator serves as Risk Owner for information security"
- IFF-VRA 2.11: "Albert Ai, Data Protection Manager (internal)"; Servier-Priv: "Albert Ai, Data Protection Officer"
- SuppMat, Risk Assessment Methodology: "Risk Owner: CEO/Data Security Administrator"

*Removed from bank:* the "Who is responsible for information security?" entry. (DPO entry kept as "Data Protection Officer"; note the title difference above.)

**Decision:**

---

## B. Encryption

### C7. Encryption at rest
- NOVA/FMC 3.2, InfoSec Q7: "1. Private encryption algorithm 2. Hashed and salted format"
- Grü Q47 and Q57: "at rest (private encryption algorithm, hashed and salted)"
- Grü Q14 and Q31: "We use AES 256 encryption for important and sensitive data at rest"
- Merck Q5: "immediately encrypted with RSA256 before being stored"
- Acadia: "AES-256 for sensitive data, with data stored using a private encryption algorithm in hashed-and-salted form"
- Jazz: "AES-256 encryption at rest and in transit"
- Servier-Q Q24: "AES-256 encryption at rest … and hashed/salted passwords using private encryption algorithms"
- IFF-VRA 2.7 and 7.5: "AES-256 encryption at rest"
- Servier-Priv: "AES-256 encryption at rest, TLS 1.2/1.3 in transit"
- SuppMat, SaaS Regulations §6: "Data Encryption - AES-256 for sensitive data, TLS 1.2+ for transmission, encrypted backup storage"
- SuppMat, Coding Standards 2.6 (standard, not a description of ChemAIRS): "Symmetric: AES-128+ (recommended)"; 2.7: "Database encryption for PII"

*Note:* hashing is one-way, so it is not encryption of data. "RSA256" usually names a signature scheme (RS256), not data encryption. Scope also varies: "important and sensitive data" vs. all data.
*Removed from bank:* the at-rest entry, and AES-256 mentions in key management and backups.

**Decision:** (algorithm, and whether it covers all data or sensitive fields only)

### C8. Encryption in transit (TLS versions)
- NOVA/FMC 3.1, InfoSec Q6: "1. TLS 1.3 (preferred) and 1  2. AES 256"
- Grü Q14, Q29, Q31; Acadia: "TLS 1.3 (preferred), TLS 1.2 minimum"
- Servier-Q Q24: "TLS 1.2+"
- Jazz: "AES-256 encryption at rest and in transit"
- SuppMat, SaaS Regulations §6 and §10: "TLS 1.2+"
- SuppMat, Coding Standards 2.6: "HTTPS everywhere: TLS 1.2+ required for all web traffic"
- SuppMat, AWS ALB screenshot: HTTPS:443 listener "applies the AWS security policy ELBSecurityPolicy-2016-08"

*Note:* "and 1" may be a cut-off "1.2" or may mean TLS 1.0. AES-256 is a cipher, not a transport protocol.
*Note:* per AWS documentation, the predefined ELBSecurityPolicy-2016-08 accepts TLS 1.0, 1.1 and 1.2.
*Removed from bank:* specific TLS versions (the bank now says "HTTPS with TLS").

**Decision:**

---

## C. Data retention, deletion and location

### C9. What happens to data at contract end / retention periods
- NOVA/FMC 3.10, InfoSec Q15: "expired user accounts and their data will not be deleted or returned automatically … The function of automatic data removal for expired accounts is under development"
- PIA: "Personal information is retained for 6 months after termination of the usage agreement. All personal information is permanently deleted at the end of the retention period."
- Grü Q5: "Personal information retention: 6 months after termination of the usage agreement"
- Servier-Q Q25: "a 6-month retention period after contract termination, 7-day encrypted local backups with automatic cleanup, 3-month remote DR retention with physical destruction afterward, and CEO-authorized data deletion procedures"
- Gilead-email Q1: "Backup Data – automatically destroyed after 7 days for local backups and 3 months for off-site disaster recovery backups"
- IFF-VRA 7.13 (process to return or destroy data at termination): ☒ Yes
- Servier-Priv: business contact data held by Chemical.AI is "deleted within 10 business days of a written request"
- SuppMat, DPA summary: "Data Deletion: 10-business-day deletion requirement after service cessation with written certification" (the DPA summary doesn't limit this to contact data, unlike Servier-Priv)

*Removed from bank:* the retention-policy and end-of-contract entries.

**Decision:** (customer research data and personal data at contract end; is data returned? in what format?)

### C10. How deletion works: self-service or a request process
- Gilead-email Q1: "customers can delete their own data directly through the platform interface … when a user's account is deleted, their production data is automatically deleted"
- NOVA/FMC 3.8, InfoSec Q13: deletion needs a tenant-admin request "audited by ChemAIRS's data security team, submitted to the operator and authorized to the CEO", executed in a maintenance window
- NOVA/FMC 5.10: removing a user "Typically, it will take 1-3 weeks"
- Servier-Q Q25: "CEO-authorized data deletion procedures"

*Removed from bank:* both deletion entries, and "users can delete their production data directly" in the data-subject-rights answer.

**Decision:**

### C11. Access to SaaS data from outside the US (China)
- Servier-Priv: "People's Republic of China (location of Chemical.AI development, support and maintenance personnel) — Cybersecurity Law, Data Security Law, and PIPL"
- Acadia: "for SaaS there is no international data transfer (data remains in AWS us-west-1)"
- PIA ("In which countries will the PI be accessible or viewable?"): "Not applicable"
- Servier-email: "no SaaS data is stored outside the U.S."
- NOVA 3.6: data access is a one-time privilege with CEO authorization (location of the staff not stated)
- SuppMat, DPA summary: "Data Transfer: No international transfers for SaaS"

*Note:* under GDPR, remote access from a third country counts as a transfer even when storage stays in the US.
*Removed from bank:* the sub-processor / international-transfer entry.

**Decision:**

### C12. Does any third party have access to personal data?
- PIA ("Will any third-parties have access to the PI?"): "No"; third-party access countries: "No applicable"
- Acadia: AWS "provides the hosting layer and does not access application data content"
- IFF-VRA 2.10 ("Do you use subprocessors … that will have access to and/or process personal data?"): ☒ Yes — "Amazon Web Services (AWS)"
- Servier-Q Q2 ("Do you work with any third parties?"): "Yes, but with limited and clearly defined third-party relationships"

*Removed from bank:* same entry as C11.

**Decision:**

### C13. Backup design and disaster-recovery backup location
- NOVA/FMC 3.9: "full backups are performed on a daily basis, after which copies of the data are re-created and continue to be dumped into a dedicated storage server"
- Grü Q22 and Q47: "Daily full backups … (7 generations), with data stored in multiple physically isolated availability zones"
- Acadia: "daily full backups (7 generations) stored across multiple physically isolated AWS availability zones, plus a remote disaster-recovery backup"
- Servier-Q Q17, Q25, Q38: "dual-layer backups (local + remote DR)"; "3-month remote DR retention with physical destruction afterward"
- Merck Q6: "stored on technologically advanced storage mediums with RAID 5 and LVM, accompanied by encrypted off-site backups"
- Servier-email: "no SaaS data is stored outside the U.S."
- SuppMat, SaaS Regulations §7–9: "Dual-layer protection: local backup + remote disaster recovery"; local: "7-day retention, AES-256 encryption, automatic cleanup"; remote: "3-month retention, TLS 1.2 + AES-256, physical destruction after 3 months"
- SuppMat, ISMS-2-CL-002 Backup Policy: "Off-site backup storage requirements", "Annual review of off-site storage providers"

*Note:* no source says where the remote DR backup is (another AWS region? the IDC?) or what "physical destruction" applies to. If the DR copy sits outside the US, it conflicts with the US-only storage claim.
*Removed from bank:* the backup entry and the "No SaaS data is stored outside the U.S." sentence.

**Decision:**

### C14. Anonymization
- Merck Q3: "we implement robust security measures like access controls, AES256 encryption, and data anonymization"
- Servier-Priv: "Chemical.AI does not apply formal anonymization or pseudonymization techniques"

*Removed from bank:* the anonymization entry.

**Decision:**

### C15. Log retention and log encryption
- Grü Q5: "Audit log retention: 6 months (default, depends on storage size); System log retention: 60 days"
- Grü Q54: "Log retention is 6 months by default … with logs stored in plain text format"
- Servier-Q Q22 and Q41: "stored in encrypted form with ≥1-year retention"
- IFF-SDA 3.1: "logs are encrypted with ≥1-year retention"
- SuppMat, SaaS Regulations §13: "System/application/security logs (no sensitive molecular data), encrypted storage, 1+ year retention"
- SuppMat, Coding Standards 2.10: "Retention: Keep network logs for 6+ months (per Cybersecurity Law Article 21)"
- SuppMat, System Test Report v3.5.0: "Audit log export (7-day default, 30-day max)"

*Removed from bank:* all log retention periods and "encrypted log storage".

**Decision:**

---

## D. Continuity

### C16. RTO / RPO vs. daily backups
- Acadia, Servier-Q Q15 and Q17, IFF-VRA 3.4, IFF-SDA 2.2 and 5.35: "RTO ≤ 4 hours, RPO ≤ 1 hour"
- Every backup description (NOVA 3.9, Grü Q22, Acadia, Servier-Q): full backups **daily**
- NOVA/FMC, Grü: no RTO/RPO stated
- SuppMat, SaaS Regulations §16: "RTO ≤4 hours, RPO ≤1 hour, bi-annual drills, regular plan updates"

*Note:* daily full backups alone support an RPO of up to 24 hours. A 1-hour RPO needs something like point-in-time recovery, which no document mentions.
*Removed from bank:* the RTO/RPO entry.

**Decision:**

### C17. Backup restore and DR test frequency
- NOVA/FMC 3.9: automated recovery tests "on a regular basis"; NOVA 1.2: drills "practiced from time to time"
- IFF-VRA 9.6: DR testing ☒Quarterly
- IFF-SDA 5.15: restore tests "Quarterly"; 5.41: "Quarterly backup/restore tests and bi-annual drills"
- Servier-Q Q38: "quarterly/bi-annual restoration testing"
- SuppMat, SaaS Regulations §18: "quarterly backup testing"
- SuppMat, ISMS-2-CL-002 Backup Policy: "Regular testing of backup media viability"

*Removed from bank:* "Disaster recovery is tested quarterly" and "Restores are tested quarterly".

**Decision:**

---

## E. Security testing and operations

### C18. Penetration test frequency
- Grü Q40: "Third-party penetration tests: Conducted every 6 months"; Q69: "bi-annual penetration tests"
- Acadia: "bi-annual external penetration tests"
- Servier-Q Q30: "at least annually (in practice bi-annual)"; Q50: "Annual third-party assessment (ZWAY-PET-202508-01)"; Q59: "Annual third-party penetration testing"
- IFF-VRA 7.9: ☒Annually ☒Upon major infrastructure changes
- IFF-SDA 7.1 and Servier-Priv: "annual third-party penetration test(ing)"
- SuppMat, Risk Assessment Methodology: "Penetration Testing: Annual external assessments"; "External Validation: Third-party assessors (annual)"
- SuppMat, SaaS Regulations §18: "Bi-annual security assessment"
- SuppMat, Penetration Test Report: testing dates "August 1-4, 2025" (a single report)

*Note:* "bi-annual" can mean twice a year or every two years.
*Removed from bank:* every penetration-test frequency.

**Decision:**

### C19. Vulnerability remediation timelines
- Grü Q32: "All high-risk security patches are applied before release"; IFF-SDA 3.37: "High-risk fixes applied before release"
- IFF-VRA 7.10: HIGH ☒30 days, MEDIUM ☒90 days

*Removed from bank:* the remediation-timelines entry.

**Decision:**

### C20. Release and patch cadence
- Grü Q60: "Monthly … usually at a frequency of once a month"; Servier-Q Q20: "monthly patched container image releases"
- IFF-SDA 2.8, 3.21, 9.8: "Major releases twice per year"; 2.30: "two major updates per year"; 7.38: "Hotfixes as needed"

*Removed from bank:* "monthly" and "two major releases per year".

**Decision:**

### C21. SIEM
- IFF-VRA 6.10 ("Do you have a SIEM solution?"): ☒ Internal
- IFF-SDA 3.5 ("Is there a service or SIEM in place?"): ☒ No
- Servier-Q Q28 (SOC or detection tools): lists GuardDuty, WAF, Grafana Loki, CloudWatch and the H3C IPS; no SIEM product named

*Removed from bank:* nothing was claimed (the bank describes central log monitoring without the word SIEM).

**Decision:**

---

## F. People and devices

### C22. Security training frequency
- PIA, Grü Q6, Acadia, Servier-Q Q11, IFF-VRA 1.4 comment: training "twice per year" / "two mandatory security training every year"
- PIA, Servier-Q Q16, Q52, Servier-Priv: "bi-annual" training
- IFF-VRA 4.4: ☒ "Mandatory Security Awareness online training annually"; 2.6: ☒ "Annual privacy training"; 1.5: ☒ Annually, with comment "re-affirmed through the twice-yearly mandatory security training cycle"
- SuppMat, SaaS Regulations §19: "Bi-annual awareness training, technical skills training, emergency drills"
- SuppMat, Employee Information Security Handbook: "Mandatory for all employees, specialized training for key positions" (no frequency)

*Removed from bank:* the training frequency (now "on a recurring schedule").

**Decision:**

### C23. Mobile device management
- Grü Q26 (MDM program?): "Yes, we have but not explicitly documented."
- Grü-PDF Q27: "(note: no MDM and other limits at this moment)"; Grü-md Q27: "(note only for myself: no MDM and other limits at this moment)"
- Servier-Q Q37: "governed via mobile-device and endpoint policies … though full MDM with encryption and remote wipe is only partially documented"
- IFF-VRA 1.1: ☒ Mobile Devices policy
- SuppMat, ISMS-2-CL-011 Mobile Device Management Policy: "Only approved mobile devices can access information resources", "Password protection required", "Important data should not be stored on mobile devices"

*Removed from bank:* no MDM entry was written.

**Decision:**

### C24. Wireless network
- Grü Q36 (wireless policy?): "Not applicable."
- IFF-VRA 6.5: ☒ Yes (using wireless), ☒ WPA2; 1.1: ☒ Network & WiFi Security policy
- Servier-Q Q37: wireless communications limited "to approved protocols"
- SuppMat, ISMS-2-CL-012 Access Control Policy: "Wireless network restrictions based on job position"

*Removed from bank:* the WPA2 sentence.

**Decision:**

### C25. Acceptable use policy
- Grü Q4 (acceptable use policy?): answered with the asset-management text from Q3 (copy-paste); Grü-md says "This answer is the same as Question 5 above"
- IFF-VRA 1.1: ☒ Acceptable Use Policy; 1.5: acknowledged ☒ Annually / "on hire and re-affirmed through the twice-yearly … training cycle"

*Kept in bank:* the policy exists and is acknowledged on hire (no source disputes that). The frequency was removed (see C22).

**Decision:**

---

## G. Local deployments, AI and product

### C26. Chemical.AI access to customer data in local deployments
- Jazz: "We have zero access to your data."
- Servier-Priv: "Chemical.AI has no ability to access, retrieve, transfer or disclose personal data … Chemical.AI personnel access the deployed environment only for scheduled maintenance, only with Servier IT personnel present"
- InfoSec Q2 (internal note): "we only remote control with client IT personnel presents -> so it's fine in general"
- IFF-SDA 3.27 and 4.8: "Chemical.AI support access is IFF-authorised, time-limited and logged, with no standing access"
- SuppMat, Local Deployment Data Security Management §1.1: "100% user control, zero vendor access"; §10.2: "Restricted remote access, transparent auditing, data access prohibition"; §11.1: "Never access, backup, transmit, or analyze user data"

*Removed from bank:* the local-deployment access entry.

**Decision:**

### C27. Use of customer data for model training
- Merck Q4: local deployment enables "secure integration with internal systems for data reuse and algorithm retraining"
- Acadia: "In-scope/client data is never used to train or fine-tune models"
- Jazz, IFF-VRA 11.8, IFF-SDA 5.11, Servier-Priv: customer data is never used for training

*Removed from bank:* the training entry and "never used to train" in the data-flow answer.

**Decision:**

### C28. Front-end layer (Gilead architecture review)
- Gilead-FU, email as sent 1 Dec 2025: "yes - we use the Vue framework"
- Gilead-FU, draft section: "No separate front-end service is shown in front of the .NET Core web cluster … the .NET Core web apps are the front-end"
- Gilead-FU, Chinese note: "3.5.0 前端和后端合成一个镜像" (in 3.5.0 the front end and back end are combined into one image)
- Condition optimization: listed as **async** in the draft's RabbitMQ list, but as **sync** in the sent email

*Removed from bank:* the Vue sentence and the condition-optimization example.

**Decision:**

### C29. Cloud provider SOC reports
- Grü-PDF Q48: "No, we have the ISO27001 certificate in lieu of the SOC certification"
- Grü-md Q48: "Yes, AWS has all certificates required."
- Acadia, IFF-VRA 2.10: "AWS maintains SOC 1/2/3 and ISO 27001/27017/27018"
- SuppMat, "AWS SOC1 SOC2 SOC3 ISO-27001 ISO-27017 ISO-27018 Reports": "We can log into AWS account and download" the ISO 27001/27017/27018 certificates and SOC 1/2/3 reports

*Removed from bank:* the "Does your cloud hosting provider provide SOC reports?" entry.

**Decision:**

### C30. Breach notification commitment
- NOVA/FMC 3.12: channel only (Ops-system emails plus business manager); no time limit
- Acadia: "the DPA commits Chemical.AI to prompt breach notification"
- Servier-Priv: "Yes" to notifying "no later than 48 hours from the discovery"; for supervised maintenance, "without undue delay"; ZH-IS-201 §6: "24-hour internal reporting requirement"
- SuppMat, DPA summary: "Breach Notification: Immediate notification to customer upon discovering personal data breaches"
- SuppMat, Employee Information Security Handbook: "Immediate reporting within 24 hours" (internal reporting)

*Note:* the sources don't contradict each other; the open question is what standard commitment to state.
*Removed from bank:* "we can commit to notification within 48 hours". (Kept: "without undue delay, as committed in our DPA" and the 24-hour internal reporting.)

**Decision:**

---

## H. Unanswered in all sources

### C31. Notice of a change in data storage location
NOVA/FMC 3.13 was answered with the data-breach text; no other source addresses it.

**Decision:**

---

## I. New conflicts from the Supporting Materials document

### C32. Pandemic plan
- Grü Q21: "Yes, we have a plan according to municipal and regional regulations, but not explicitly internally documented."
- SuppMat: lists "Chemical.AI Pandemic Response Plan (Doc)" with a link (https://chemical-ai.feishu.cn/docx/STQQdUVPaoCB8txfI4FclUMVndb); no summary of its content

*Removed from bank:* the pandemic-plan entry.

**Decision:**

### C33. Unit testing and code coverage
- Grü Q65: white-box testing includes "Unit Testing: Developer-created tests for individual functions and methods"; success criteria "Minimum 80% code coverage for security-critical components"
- Servier-Q Q59: "Structure Test (White Box): Static code analysis, mandatory peer review, unit testing"
- SuppMat, ChemAIRS-backend Code Analysis Report (SonarQube, 2024-09-14): "Test Coverage: 0.0% (no tests implemented)"; also 43 "Critical" code smells (maintainability, not security; "No security vulnerabilities found")

*Removed from bank:* "unit tests" and "at least 80% coverage". Also corrected: the bank's "zero critical static-analysis findings" now reads "zero critical security vulnerabilities from static analysis", matching Grü Q65.

**Decision:**

### C34. Account lockout threshold
- NOVA 5.9: "User account will be locked after 5 incorrect entries"; Grü Q66: "Account lockout after 5 incorrect password entries (It should be unlocked by enterprise tenant administrators)"
- SuppMat, System Test Report v3.5.0: "Login limits (5 attempts/day)"; "Daily login failure limit (5 attempts)"; "Account unlock functionality"
- SuppMat, Coding Standards 2.4.1 (a development requirement): "Account-based: 3 failures → lock for 30 min OR show CAPTCHA"; "IP-based: 5 attempts in 5 seconds → 30-min block"
- Employee Information Security Handbook: "failed login lockouts" (no number)

*Removed from bank:* the number of attempts (the bank now says "after repeated failed login attempts").

**Decision:**

### C35. What ISMS-2-CL-009 is
- Servier-Priv: "ISMS-2-CL-009 (incident escalation and response)"
- Grü-md Q16 materials: "ISMS-2-CL-009 (Fire Management)"
- SuppMat, Policy Handbook table of contents: "9. ISMS-2-CL-009 Fire Management Policy (消防管理策略)"

*Removed from bank:* CL-009 from the policy list and from the incident-response answer.

**Decision:**

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
