# Answer Bank – Reservoir of Uncovered Questions

Generated 2026-09-24 by `build_reservoir.py` – **don't edit by hand**; it is rebuilt on every run.
Questions asked in `archive/` that `knowledge_base/answer_bank.md` doesn't cover yet, ranked by
**importance = number of distinct customers** who asked something similar (then by number of times asked).
To promote one: write a reviewed answer into `answer_bank.md` and re-run; covered questions drop off.

Settings: covered if similarity to a bank entry ≥ 0.75; questions grouped at similarity ≥ 0.8. Customers come from `archive/sources.yaml`.

**431 uncovered questions** (from 492 of 726 archive questions; 234 already covered by the bank). 158 are marked ⚠️ possibly already covered (similarity within 0.05 of the cut-off).

---

### 1. Can the service restrict access to client’s IPs?
**Importance:** 3 customers (FMC, NOVA Chemicals, Siegfried) · asked 3 times  
**Closest bank entry:** "How is remote access to your network secured?" (similarity 0.64)
**Also asked as:**
- "Can the service restrict access to NOVA IPs?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
- "Is it guaranteed that access to the services is restricted to specific IP addresses or domains?" — Siegfried (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
**Past answers (from archive – unreviewed, may be outdated):**
- If yes, how? YES, via AWS security group (Also used in ELB) — *FMC* (`FMC - Security Risk Assessment.pdf`)
- No Customer-configurable source-IP / domain allowlisting for tenant access is not available in the standard SaaS environment. Network-layer protections do exist (AWS WAF, anti-DDoS, internal-only VPC/ClusterIP with no public exposure beyond the web frontend, and database access restricted to specific IP ranges), but these are provider-managed and not a customer-defined IP restriction. IP-based access restriction can be evaluated for local/dedicated deployments. — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 2. How do you ensure subcontractors maintain the same standards as described above?
**Importance:** 3 customers (FMC, NOVA Chemicals, Servier) · asked 3 times  
**Closest bank entry:** "Do you use subcontractors or depend on critical third parties?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "How do you ensure subcontractors maintain the same standards as described above?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
- "How do you verify that your subcontractors meet your quality standards (e.g., through audits or periodic reviews)?" — Servier (`Servier_information_security_questionnaire (SaaS).md`)
**Past answers (from archive – unreviewed, may be outdated):**
- Inapplicable. — *FMC* (`FMC - Security Risk Assessment.pdf`)
- No subcontractors used - all software developed in-house. However, supplier management procedures exist. — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 3. (E.g., who logged in at what time) How can they be reviewed by the client for review?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "How are audit logs stored and reviewed?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "(E.g., who logged in at what time) How can they be reviewed by NOVA for review?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- Audit logs will be stored in exclusive database, only audit administrator can access it, it’s a one-time privilege which approved by CEO with business reasons. The client’s tenant administrator can submit a request to corresponding Business Directors for requesting the audit log review for the client. — *FMC* (`FMC - Security Risk Assessment.pdf`)
- Audit logs will be stored in exclusive database, only audit administrator can access it, it’s a one-time privilege which approved by CEO with business reasons. NOVA tenant administrator can submit a request to corresponding Business Directors for requesting the audit log review for NOVA users. — *NOVA Chemicals* (`NOVA Cloud Security Risk Assessment Template.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 4. Are firewalls in place to only allow the minimum ports required?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "How is the office network secured?" (similarity 0.64)
**Also asked as:**
- "Are firewalls in place to only allow the minimum ports required?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- YES. Only 443 and 80 is allowed. ChemAIRS is HTTPS only, but we still keep the 80 port open to redirect all HTTP traffic into HTTPS in force. — *FMC* (`FMC - Security Risk Assessment.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 5. Can SOC (Service Organization Controls) reports be provided to the client?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "Do you have a SOC 1 / SOC 2 / SOC 3 report?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Can SOC (Service Organization Controls) reports be provided to NOVA?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- SOC 1 – Related to Internal Control over Financial Reporting SOC 2 – Related to testing over the Trust Services Principles of Security, Availability, Processing Integrity, Confidentiality, and Privacy SOC 3 – A simplified report on the same principles in SOC 2 and available for public use Vendors management assertion We do not have the SOC 2 certification yet, because most of our clients choose local deployment rather than a SaaS over internet. If you need to deploy ChemAIRS locally, you don't have to worry about data security issues. ChemAIRS supports a completely private deployment and runs in an intranet environment with no Internet access after deployment, and the entire system is under your management and control, whether it's to the hardware, the application, or the system, all under your control. 3 Data Protection — *FMC* (`FMC - Security Risk Assessment.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 6. Can the data be accessed by PTC owned tools outside of those provided by the vendor?
**Importance:** 2 customers (IFF, PTC) · asked 2 times  
**Closest bank entry:** "Can government authorities access customer data?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Can the data be accessed by IFF owned tools outside of those provided by the vendor?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- PTC has full control of the data for local deployment — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 7. Describe in detail how you protect and recover from ransomware
**Importance:** 2 customers (PTC, Servier) · asked 2 times  
**Closest bank entry:** "Describe your disaster recovery and business continuity plans." (similarity 0.68)
**Also asked as:**
- "Do you implement ransomware detection and recovery measures?" — Servier (`Servier_information_security_questionnaire (SaaS).md`)
**Past answers (from archive – unreviewed, may be outdated):**
- Protection – to prevent ransomware from happening in the first place: antivirus/anti malware software;firewall and network segmentation; patch management and vulnerability scanning; access controls (least privilege); employee security awareness training; web application firewalls; intrusion detection systems.Recovery – recover from ransomware: backup strategy (frequency, number of copies, offsite storage); whether backups are isolated from the main network (so ransomware cannot encrypt them too); how quickly systems can be restored (RTO/RPO); incident response procedures; testing and drills to verify recovery capability Access Question | Yes | No | Notes — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
- Yes, ransomware risk is mitigated via advanced hardware firewalls, AWS GuardDuty, continuous anomaly monitoring, antivirus and malware controls, encrypted multi-copy backups across isolated availability zones, and DR procedures with defined RTO/RPO for rapid recovery. 《Information Security Management Policy Handbook》(Doc) ISMS-2-CL-006 Virus Management Policy with malware protection and continuous surveillance requirements 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section III: Dual-layer backup protection with encrypted storage in multiple physically isolated availability zones; Section V: Business Continuity with RTO ≤4 hours and RPO ≤1 hour for rapid recovery from security incidents — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 8. Describe the intrusion detection system in place?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.68)
**Also asked as:**
- "Describe the intrusion detection system in place?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- We are using the AWS GuardDuty. https://docs.aws.amazon.com/guardduty/latest/ug/what-is- guardduty.html — *FMC* (`FMC - Security Risk Assessment.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 9. Does the service support single sign on through use of the client’s internal IDP?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "Do you support single sign-on (SSO)?" (similarity 0.70)
**Also asked as:**
- "Does the service support single sign on through use of NOVA’s internal IDP?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- (E.g., SAML2.0/oAuth on Microsoft Azure/SAP) YES. Azure AD is fully tested. For other SSO providers, we will evaluate case-by-case If SSO is supported, how can identities be provisioned? (E.g., SCIM) ChemAIRS with Azure AD only supports pre-creation of users manually and validation of user login credentials via SSO, if SCIM or other requirements apply, we will evaluate case-by- case — *FMC* (`FMC - Security Risk Assessment.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 10. During the first-time data transfer (pre-load), how is the data encrypted?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "How is data encrypted in transit?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "During the first-time data transfer (pre-load), how is the data encrypted?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- ChemAIRS use enforced HTTPS protocol to ensure that requests are not coming from unauthorized access and uses TLS encryption during transmission to secure the content of the transmitted data 3 — *FMC* (`FMC - Security Risk Assessment.pdf`)
- ChemAIRS use enforced HTTPS protocol to ensure that requests are not coming from unauthorized access and uses TLS encryption during transmission to secure the content of the transmitted data — *NOVA Chemicals* (`NOVA Cloud Security Risk Assessment Template.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 11. During upgrades, how are vulnerabilities discovered before production deployment?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "During upgrades, how are vulnerabilities discovered before production deployment?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- ChemAIRS accesses SonarQube's quality management and vulnerability detection engine at code compilation time (CICD). Vulnerabilities in the reference chain are identified in daily reports and reviewed by the code security team before being submitted to the code owner for repair, and only after the repair is complete will the merge-in request be approved. At release time, the code artifact will be built as a container image and released to the pre-release project. In the privately deployed Harbor repository, we use the Trivy engine to scan the image, and once a risky vulnerability is found, it will be reviewed by the code security team and submitted to the Devops administrator for fixing. After the release of the version we will also quality management team is also for the pre-release environment and online formal environment from time to time security scanning, once any problem is found will be reported to the code security team to review and submit to the person in charge of the corresponding repair. — *FMC* (`FMC - Security Risk Assessment.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 12. How long is the process expected to take?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.62)
**Also asked as:**
- "How long is the process expected to take?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- Please refer to 3.8. Typically, it will take 1-3 weeks. 6 Subcontractors — *FMC* (`FMC - Security Risk Assessment.pdf`)
- Please refer to 3.8. Typically, it will take 1-3 weeks. 5.11 6 Subcontractors — *NOVA Chemicals* (`NOVA Cloud Security Risk Assessment Template.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 13. How will personal data be protected from accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data?
**Importance:** 2 customers (Acadia, IFF) · asked 2 times  
**Closest bank entry:** "Is data anonymized or pseudonymized?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Describe how in scope systems/data are protected against malicious or accidental data loss, data alteration, and data destruction." — Acadia (`Cybersecurity Questions.jay.acadia.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, you have full control of the data. For SaaS, we have AES-256 encryption at rest and TLS in transit; RBAC least-privilege access; multi-tenant logical isolation; comprehensive audit logging; AWS WAF, GuardDuty and firewalls; encrypted backups stored across multiple physically isolated AWS availability zones. — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- Layered controls: daily full backups (7 generations) stored across multiple physically isolated AWS availability zones, plus a remote disaster-recovery backup; backups are AES-256 encrypted and isolated to limit ransomware exposure, with regular automated recovery testing. Integrity and least-privilege controls include RBAC, tenant isolation, comprehensive audit logging (traceability of every action on data), AWS WAF/GuardDuty/firewalls and malware scanning. Data deletion occurs only through an authorized, audited workflow. — *Acadia* (`Cybersecurity Questions.jay.acadia.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 14. On what frequency are regular backups performed?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "How are backups tested?" (similarity 0.70)
**Also asked as:**
- "On what frequency are regular backups performed?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers:** none found in the archive
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 15. What administrative protections are in place to safeguard against unauthorized use, modification, copying, accessing, or processing of data?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "How is Chemical.AI staff access to customer data restricted?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "What administrative protections are in place to safeguard against unauthorized use, modification, copying, accessing, or processing of data?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- Please refer 3.6. Questions 5.6 – 5.10 apply to non-client managed authentication methods 7 — *FMC* (`FMC - Security Risk Assessment.pdf`)
- Please refer 3.6. Questions 5.6 – 5.10 apply to non-NOVA managed authentication methods — *NOVA Chemicals* (`NOVA Cloud Security Risk Assessment Template.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 16. What is the process to remove a user?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "Can data be deleted without Chemical.AI viewing it?" (similarity 0.64)
**Also asked as:**
- "What is the process to remove a user?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers:** none found in the archive
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 17. Which administrative functions performed by the vendor, and which are done by The client?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "Describe the product / software / service and its purpose." (similarity 0.61)
**Also asked as:**
- "Which administrative functions performed by the vendor, and which are done by NOVA Chemicals?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers:** none found in the archive
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 18. Which third-party data center is used?
**Importance:** 2 customers (FMC, NOVA Chemicals) · asked 2 times  
**Closest bank entry:** "Which cloud provider and services do you use?" (similarity 0.67)
**Also asked as:**
- "Which third-party data center is used?" — NOVA Chemicals (`NOVA Cloud Security Risk Assessment Template.pdf`)
**Past answers (from archive – unreviewed, may be outdated):**
- (Co-location, Azure, AWS, etc.) In AWS If applicable, what are the physical access restrictions to the data center? Internal only private network (VPC) based cluster deployment and limited authorized AWS management platform access. If applicable, how are data centers monitored? Integrated AWS CloudWatch and self-hosted Prometheus & Grafana monitoring system in EC2 instances If applicable, how is hardware kept up to date? ChemAIRS is based on the Kubernetes distributed container architecture, the underlying server can be very easy to expand and shrink the capacity, also includes changing the server instance to a newer hardware model. If applicable, how is hardware and/or data storage decommissioned? Please refer to 4.4. — *FMC* (`FMC - Security Risk Assessment.pdf`)
*First seen in:* `FMC - Security Risk Assessment.pdf`

### 19. What security features are enabled by default in your AI solution (safe by default)?
**Importance:** 1 customer (IFF) · asked 4 times  
**Closest bank entry:** "Are temperature, humidity, and other environmental factors monitored in real time?" (similarity 0.69)
**Also asked as:**
- "How do you ensure that your AI solution is designed with security in mind from the outset (safe by design)?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
- "How do you ensure that your OT solution is designed with security in mind from the outset (safe by design)?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
- "What security features are enabled by default in your OT solution (safe by default)?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- RBAC, encryption, and audit logging enabled by default; in customer-hosted deployment there is no external transmission of inputs, and customer data is never used for training. 9.5 AI Integrations: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Secure development lifecycle and ISO 27001 design/development controls; models operate on chemical-structure data only, with no personal data or profiling. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Not applicable — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 20. Describe your monitoring process for your application and services?
**Importance:** 1 customer (IFF) · asked 3 times  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Describe your process for network monitoring." — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
- "What application processes and services will need monitoring?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- Grafana/CloudWatch, health checks, and web-service monitoring. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- For local deployment, IFF to define — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Web, API, GPU, database, queue, and cache. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 21. Do you ensure that the use of AI in your solution is compliant with applicable data protection and privacy regulations?
**Importance:** 1 customer (IFF) · asked 3 times  
**Closest bank entry:** "How are AI results made transparent and governed?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "What steps do you take to ensure that your AI solution complies with ethical guidelines?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
- "Do you address data privacy and security issues related to AI during the AI training process?" — IFF (`Vendor Risk Assessment (VRA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒GDPR ☒CCPA ☒Country specific privacy legislation (e.g., Brazil’s LGPD, China’s PDPA, South Africa's POPIA, etc.) — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- The system operates on chemical-structure data only — no personal data, no profiling, and no automated decisions about individuals. All outputs are advisory, with a human in control of every decision (human-in-the-loop), and AI development is governed by Chemical.AI's ISO 27001-certified design and development controls. 9.8 AI Model Updates and Patch Management: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- ☒ Yes 11.8 - Please describe what measures are in place to prevent unauthorized access to Personal, Confidential, and Proprietary data used by the AI system. AES-256 encryption, RBAC least-privilege, multi-tenant isolation and full audit logging; customer data is not used for training and never leaves AWS us-west-1 in the SaaS model; models process chemical structures only, with no external transmission of customer inputs. Section 12 - Operational Technologies (OT) 8 Questions — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 22. Do you perform Information Security Incident Response Table-Top Exercises?
**Importance:** 1 customer (IFF) · asked 3 times  
**Closest bank entry:** "Do you have an incident response plan?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "How frequently do you perform Information Security Incident Response Table-Top Exercises?" — IFF (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- "At what organizational level do you perform Information Security Incident Response Table-Top Exercises?" — IFF (`Vendor Risk Assessment (VRA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- ☒Other Emergency drills conducted twice per year. — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- ☒InfoSec and IT — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 23. Do you store the client's data offsite to be viewed outside of the organization?
**Importance:** 1 customer (IFF) · asked 3 times  
**Closest bank entry:** "How are customers notified of a change in data storage location?" (similarity 0.68)
**Also asked as:**
- "Does your organization store IFF data in the cloud?" — IFF (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- "Does your organization share IFF data outside of your environment?" — IFF (`Vendor Risk Assessment (VRA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No / comment For local deployment, IFF has full control of the data — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- ☒ Yes AWS us-west-1, encrypted (AES-256 at rest, TLS in transit), with multi-tenant logical isolation. — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- ☒ No 7.7 - Is data encrypted: ☒In transit ☒At rest — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 24. Does the application require URL monitoring?
**Importance:** 1 customer (IFF) · asked 3 times  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.63)
**Also asked as:**
- "Does the application require web service monitoring?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
- "What URLs will need monitoring?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Application frontend and API endpoints. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 25. Does the software development standard ensure that the application has to maintain a user audit trail?
**Importance:** 1 customer (Grunenthal) · asked 3 times  
**Closest bank entry:** "Do you follow secure development standards?" (similarity 0.67)
**Also asked as:**
- "Does the software development standard ensure that the application has to maintain an admin audit trail?" — Grunenthal (`Information_Security_Questions_Summary.md`)
- "Does the software development standard ensure that the application has to maintain a data audit trail?" — Grunenthal (`Information_Security_Questions_Summary.md`)
**Past answers (from archive – unreviewed, may be outdated):**
- Provide supporting documentation as evidence to validate the implementation of the stated control Yes. All access to sensitive systems and data is logged and monitored. The tenant administrator can submit a request to review. audit logs include user indentification, event type, timestamp, source and destination (IP address, device, target system), and outcome (success or failure). We have internal audit logs that are not publicly available, but we can share them upon request. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
- Please provide evidence validating the implementation of the stated control. Yes. The system maintains admin audit trails. All access and operation records are retained and used as the basis for admin auditing. Admin-specific logging includes privileged access and system administration activities. 《ChemAIRS Admin Audit Log》 — *Grunenthal* (`Information_Security_Questions_Summary.md`)
- Please provide evidence validating the implementation of the stated control. Yes. Audit logs will be stored in exclusive databases, only audit administrators can access it. The logging includes, data access events, user who accessed the data, timestamp of access, source IP and device information, target data accessed, operation performed (read, modify, delete). Log retention is 6 months by default (depends on storage size), with logs stored in plain text format supported by third-party logging and monitoring platforms. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 26. How do you monitor the inputs provided to the OT systems to detect potential malicious or abnormal inputs?
**Importance:** 1 customer (IFF) · asked 3 times  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.69)
**Also asked as:**
- "How do you monitor the inputs provided to the AI system to detect potential malicious or abnormal inputs?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
- "How do you monitor the outputs of OT systems to identify anomalies or deviations from expected behavior?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Input monitoring Input validation/whitelisting, rate limiting, and audit logging of inputs. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Not applicable 10.2 Anomaly Detection and Threat Intelligence: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 27. How do you use threat intelligence to anticipate potential AI-related security attacks or vulnerabilities?
**Importance:** 1 customer (IFF) · asked 3 times  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.68)
**Also asked as:**
- "What mechanisms do you have in place to proactively respond to emerging threats in AI systems?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
- "How do you leverage threat intelligence to anticipate potential OT-related security attacks or vulnerabilities?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- Threat intelligence for identifying AI security attacks Threat-intel feeds, container CVE scanning, and standard application-security controls. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Methods to respond proactively to emerging AI threats Monitoring, patching, and security assessments. 9.4 Safe by Design and Default: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Not applicable 10.3 Safe by Design and Default: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 28. At what frequency do you perform vulnerability scanning?
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "Describe your vulnerability management program." (similarity 0.67)
**Also asked as:**
- "At what frequency do you perform network Penetration Testing?" — IFF (`Vendor Risk Assessment (VRA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒At least monthly — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- ☒Annually ☒Upon major infrastructure changes — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 29. Can the confidentiality requirements set out in the Cloud Strategy be implemented? - C1 Internal: Encrypted transport of data, secure and traceable deletion of data - C2 Confidential: Encrypted transport and storage of data, secure and traceable deletion of data - C3 Strictly confidential: In addition to C2, further security measures must be reviewed (e.g. location of the data center in Switzerland or the European Union, secured data center connection). Note: C3 Strictly Confidential requires an exception approval.
**Importance:** 1 customer (Siegfried) · asked 2 times  
**Closest bank entry:** "Is data anonymized or pseudonymized?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Can the data privacy requirements from the Cloud Strategy be implemented? - P0 no personal data: no additional measures - P1 personal data: confidentiality requirements for C2 - P2 personal data requiring special protection: confidentiality requirements for C3, further security measures must also be reviewed (e.g. location of the data center in Switzerland or the European Union, secured data center connection)." — Siegfried (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 30. Can/does the presentation layer and application layers run on separate processors?
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "Which work is synchronous and which is asynchronous?" (similarity 0.61)
**Also asked as:**
- "Can/does the application layer and data access layer run on separate processors?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 31. Could you please transfer the technical and functional documentation to us, including user manuals, technical architecture documents, and operational maintenance plans?
**Importance:** 1 customer (Servier) · asked 2 times  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.63)
**Also asked as:**
- "Could you please transfer the technical and functional documentation to us, including user manuals, technical architecture documents, and operational maintenance plans?" — Servier (`Servier_information_security_questionnaire (SaaS).md`)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we provide technical and functional documentation as follows: ChemAIRS_Local_Deployment_Instructions.pdf System_and_Hardware_Standards_and_Specifications_for_ChemAIRS_Local_Deployment.pdf Access Management — *Servier* (`Answers_to_Email_Questions_Servier.md`)
- Yes, we provide technical and functional documentation such as installation and local-deployment specifications, and SaaS environment management regulations 5. Access Management : — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Answers_to_Email_Questions_Servier.md`

### 32. Describe the recovery time objective (RTO) for in scope systems/data.
**Importance:** 1 customer (Acadia) · asked 2 times  
**Closest bank entry:** "What are your RTO and RPO?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Describe the recovery point objective (RPO) for in scope systems/data." — Acadia (`Cybersecurity Questions.jay.acadia.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ≤ 4 hours. — *Acadia* (`Cybersecurity Questions.jay.acadia.docx`)
- ≤ 1 hour. — *Acadia* (`Cybersecurity Questions.jay.acadia.docx`)
*First seen in:* `Cybersecurity Questions.jay.acadia.docx`

### 33. Do you allow IP whitelisting?
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "Describe your network security controls." (similarity 0.64)
**Also asked as:**
- "Do you allow IP blacklisting?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 34. Do you have a documented and tested high-level incident escalation process (who to notify, timelines, responsibilities)?
**Importance:** 1 customer (Servier) · asked 2 times  
**Closest bank entry:** "Do you have an incident response plan?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Do you have a documented process for reporting and resolving incidents?" — Servier (`Servier_information_security_questionnaire (SaaS).md`)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we maintain a documented and tested incident escalation and response process that covers incident assessment, recovery plan development, dual senior-management authorization, supervised execution, verification, and RTO ≤4 hours / RPO ≤1 hour, exercised through bi-annual drills. 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section V: Data Recovery and Emergency Response - Section 15: Recovery Process with incident assessment, plan development, dual senior management authorization, supervised execution, verification; Section 16: Business continuity with RTO ≤4 hours, RPO ≤1 hour, bi-annual drills 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-24: Accident and Incident Investigation and Handling Control Procedure; ZHKJ-QESP-25: Emergency Preparedness and Response Control Procedure with emergency response planning and preparedness procedures — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
- Yes, we operate a documented and systematic incident process covering reporting, assessment, dual senior-management authorization, supervised remediation, evidence preservation, root-cause analysis, corrective actions, and post-incident improvement. 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section V: Data Recovery and Emergency Response - Section 15: Recovery process with incident assessment, plan development, dual senior management authorization, supervised execution, verification 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-24: Accident and Incident Investigation and Handling Control Procedure with systematic approach for incident reporting, investigation, and analysis including evidence preservation and witness interview requirements; ZHKJ-QESP-26: Corrective and Preventive Action Control Procedure for addressing nonconformities and preventing recurrence — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 35. Do you perform administrator accounts and access reviews, and if so, how frequently? With recertification?
**Importance:** 1 customer (Servier) · asked 2 times  
**Closest bank entry:** "How often are access rights reviewed?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Do you perform administrator accounts and access reviews, and if so, how frequently? With recertification?" — Servier (`Servier_information_security_questionnaire (SaaS).md`)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, administrator accounts undergo enhanced oversight, with privileged access individually assigned and approved, separated from regular users via tenants and RBAC, fully traceable to specific individuals through comprehensive audit logging, and governed by emergency access procedures requiring documented justifications and reviews. If you manage several environments (such as sandbox, training, etc.): is access review conducted for all available environments? Are test, training, or other accounts deleted if not used for more than a specific period, and are passwords reset regularly? Yes, we manage DEV, Test, QA, and pre-release environments on separate infrastructure with isolated test clusters, apply consistent access controls and periodic reviews across all environments, and enforce user account lockout and password complexity policies to manage dormant accounts and maintain security hygiene. — *Servier* (`Answers_to_Email_Questions_Servier.md`)
*First seen in:* `Answers_to_Email_Questions_Servier.md`

### 36. Do you work with any third parties?
**Importance:** 1 customer (Servier) · asked 2 times  
**Closest bank entry:** "Do you use subcontractors or depend on critical third parties?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Do you work with any third parties?" — Servier (`Servier_information_security_questionnaire (SaaS).md`)
**Past answers (from archive – unreviewed, may be outdated):**
- For data hosting, software development, or software support… Yes, but with limited and clearly defined third-party relationships: no subcontractors (all software is developed in-house), AWS cloud infrastructure is used for hosting in SaaS deployments, independent third-party penetration testing is conducted regularly, and the local-deployment option eliminates third-party data concerns. — *Servier* (`Answers_to_Email_Questions_Servier.md`)
*First seen in:* `Answers_to_Email_Questions_Servier.md`

### 37. Does the CSP have policies and instructions in place to ensure that third parties (e.g., service providers or suppliers) that contribute to the services for provision of the cloud service meet the same cloud requirements as the CSP itself?
**Importance:** 1 customer (Siegfried) · asked 2 times  
**Closest bank entry:** "Does your cloud hosting provider provide independent audit reports (SOC)?" (similarity 0.69)
**Also asked as:**
- "Does the CSP have policies and instructions with technical and organizational measures for the secure development of the cloud service, especially regarding security in software development (requirements, design, implementation, testing and reviews)?" — Siegfried (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 38. Does the vendor have a release cycle for application enhancement?
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "How are releases delivered?" (similarity 0.70)
**Also asked as:**
- "Does the vendor have a release cycle for bug fixes?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes If Yes, what is the release cycle and how will they be communicated — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- ☒ Yes If Yes, what is the release cycle and how will they be communicated Hotfixes as needed, communicated by email. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 39. How do these capabilities align with our business needs and objectives?
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "How do users receive their credentials?" (similarity 0.61)
**Also asked as:**
- "How do these capabilities align with our industrial process needs and objectives?" — IFF (`Vendor Risk Assessment (VRA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ChemAIRS supports scientific analysis of chemical structures, including route scouting and feasibility, COGS/process optimization, impurity troubleshooting and building-block sourcing, and matching IFF's stated use (scientific analysis of chemical structure). 11.4 - Please provide use cases and success stories of your AI implementation in similar business environments. ChemAIRS is used by pharmaceutical organizations for retrosynthesis and route design. 11.5 - Which of the following AI solution industry-recognized AI standards and best practices does your company comply with: ☒ISO 27001 — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- 12.4 - Please provide use cases and success stories of your OT implementation in similar industrial environments — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 40. How many concurrent users are expected to connect to the database?
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "Does the software run independently of the installation account?" (similarity 0.58)
**Also asked as:**
- "What is the estimated of concurrent users accessing the application?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- IFF to define. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- IFF to define (licensed sizing). 7.12 The expected application response time is: Interactive; complex model compute takes longer. Target: IFF to define. 7.13 The one year user growth rate is: IFF to define. 7.14 The three year user growth rate is: IFF to define. 7.15 The application has seasonal usage variations. ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 41. Is a Data Loss Prevention (DLP) and Information Rights Management (IRM) solution integrated in the cloud platform, and can it be configured by Siegfried AG according to its needs?
**Importance:** 1 customer (Siegfried) · asked 2 times  
**Closest bank entry:** "Do you have data loss prevention controls?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Alternatively, can third-party solutions for DLP and IRM be integrated into the cloud platform?" — Siegfried (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
**Past answers (from archive – unreviewed, may be outdated):**
- No No dedicated DLP or IRM/DRM solution is integrated into the ChemAIRS platform for customer configuration. In-platform data protection is provided through data classification (Public/Internal/Sensitive/Confidential), RBAC and least-privilege access, tenant isolation, encryption at rest/in transit, and audit logging with log export/deletion controls. Endpoint controls (USB/clipboard/screenshot/file-transfer monitoring) exist on Chemical.AI's own workstations but are internal and not customer-configurable. For local deployment, data remains entirely within the customer's environment, allowing Siegfried to apply its own DLP/IRM controls. — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 42. Is an established procedure used for monitoring and controlling the availability of the systems provided?
**Importance:** 1 customer (Siegfried) · asked 2 times  
**Closest bank entry:** "Describe your disaster recovery and business continuity plans." (similarity 0.67)
**Also asked as:**
- "Is an established procedure for planning, monitoring and controlling capacities and resources (personnel and IT resources) in place?" — Siegfried (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 43. Provide the AWS environment, IT/DevOps liaison, and acceptance testing. More details are to be determined.
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "What does implementation look like?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Provide the AWS environment, IT/DevOps liaison, and acceptance testing. The Engineers/ DevOps from IFF must have solid knowledge of k8s, Docker and AWS resources." — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- 2.34 Resources required from IFF — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 44. The diagram is high-level and only takes into account end users (i.e., no admin user flow is included). Can you please review the diagram and confirm if it's accurate?
**Importance:** 1 customer (Gilead) · asked 2 times  
**Closest bank entry:** "How are AI results made transparent and governed?" (similarity 0.53)
**Also asked as:**
- "Can you please review the diagram and confirm if it's accurate?" — Gilead (`Gilead_follow_up_email_question.md`)
**Past answers (from archive – unreviewed, may be outdated):**
- Additionally, can you help us with the following questions — *Gilead* (`Gilead_follow_up_email_question.md`)
- The high-level diagram is largely accurate but I'd note a few clarifications: NET Core web cluster也要访问rds 数据库 RabbitMQ handles asynchronous processing requests to Java algorithm services but it's bidirectional. After computation, Java Algorithm Groups publish the results/status back to RabbitMQ. API layer listens on a queue to receive information (e.g., task progress, task completion, etc) RabbitMQ 有两个队列，一个是上传任务，一个获得结果 — *Gilead* (`Gilead_follow_up_email_question.md`)
*First seen in:* `Gilead_follow_up_email_question.md`

### 45. What APIs or protocols are supported for seamless integration?
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "Which work is synchronous and which is asynchronous?" (similarity 0.66)
**Also asked as:**
- "What communication protocols and interfaces are supported for seamless integration with our current systems?" — IFF (`Solutions Design Assessment (SDA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- REST/JSON API, SAML 2.0/OIDC, and HTTPS/TLS. 9.6 Incident Response and Recovery: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
- Not applicable 10.5 Incident Response and Recovery: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 46. Will Individuals have access to their PI, and the ability to correct, amend, or erase their PI?
**Importance:** 1 customer (Gilead) · asked 2 times  
**Closest bank entry:** "What personal data (PII) do you collect?" (similarity 0.66)
**Also asked as:**
- "You confirmed that individuals have access to their PI and the ability to correct, amend, or erase it. Could you please explain the procedure used to support these requests?" — Gilead (`Answers to Gilead Email Questions.md`)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Gilead* (`Chemical.AI PIA.xlsx`)
- Users manage their own PI and can update their personal information directly through the platform interface. We ensure that all operations follow GDPR-compliant procedures. — *Gilead* (`Answers to Gilead Email Questions.md`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 47. Will your application or systems access, process, or store IFF personal data?
**Importance:** 1 customer (IFF) · asked 2 times  
**Closest bank entry:** "Can government authorities access customer data?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Also asked as:**
- "Will your application or systems access, process, or store payment card data for IFF’s product sales?" — IFF (`Vendor Risk Assessment (VRA).jay.iff.docx`)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Comment here Only applicable for local deployment. For SaaS, limited personal data only (user-account name, email, and company). — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
- ☒ No 10.3 - Please state which of the following regulatory/industry requirements apply to your organization: ☒Privacy (e.g.; GDPR, UK GDPR, CCPA, etc.) ☒Country specific privacy legislation (e.g., Brazil’s LGPD, China’s PDPA, South Africa's POPIA, etc.) — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 48. You indicated that PI is systematically destroyed, erased, or anonymized when it is no longer required. Could you please provide details on the process or controls in place to ensure PI is securely deleted or destroyed once there is no longer a business or legal need to retain it?
**Importance:** 1 customer (Gilead) · asked 2 times  
**Closest bank entry:** "Can data be deleted without Chemical.AI viewing it?" (similarity 0.68)
**Also asked as:**
- "Is PI systematically destroyed, erased, or anonymized when it is no longer legally required to be retained or to fulfill the purpose(s) for which it was collected?" — Gilead (`Chemical.AI PIA.xlsx`)
**Past answers (from archive – unreviewed, may be outdated):**
- Customer data exists in two forms with different deletion strategies: Production Environment Data - customers can delete their own data directly through the platform interface (GDPR compliant), and when a user's account is deleted, their production data is automatically deleted; Backup Data - automatically destroyed after 7 days for local backups and 3 months for off-site disaster recovery backups, ensuring complete data sanitization across all storage locations. 2. Regarding explicit or affirmative consent: — *Gilead* (`Answers to Gilead Email Questions.md`)
- Yes For SaaS, PI is permanently deleted after the 6-month retention period following termination of usage agreement — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Answers to Gilead Email Questions.md`

### 49. You indicated that there is a defined procedure or mechanism to ensure PI is accurate and kept up to date. Could you please describe the process or mechanism in place?
**Importance:** 1 customer (Gilead) · asked 2 times  
**Closest bank entry:** "What personal data (PII) do you collect?" (similarity 0.61)
**Also asked as:**
- "Is there a defined procedure or mechanism to ensure that the PI being processed is accurate and will be kept up-to-date?" — Gilead (`Chemical.AI PIA.xlsx`)
**Past answers (from archive – unreviewed, may be outdated):**
- Users can directly update their own optional profile information through platform operations, with all backend data operations being idempotent and data consistency guaranteed through transactional mechanisms. For organizational accounts, tenant administrators handle account adjustments and email updates with proper authorization. — *Gilead* (`Answers to Gilead Email Questions.md`)
- Yes — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Answers to Gilead Email Questions.md`

### 50. Any Specific RTO requirements for the Databases for Production/DR environments?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What are your RTO and RPO?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment Not applicable for local deployment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 51. Are access permissions granted using the principles of least privilege and separation of duties?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Are physical access to DPCs granted only to minimum necessary personnel and are those access permits reviewed periodically?" (similarity 0.69)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 52. Are all network devices patched with all available high-risk security patches applied and verified?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. The patching process includes: There is no fixed frequency for system updating patches for infrastructure (determined by AWS push mechanism for SaaS deployments) Applications are built as container images with patches typically updated automatically with each version release (usually monthly) SonarQube integrated into CI/CD for vulnerability detection Trivy scanning for container images with the latest real-time CVE vulnerability database Regular security vulnerability scans by the quality management team All high-risk security patches are applied before release — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 53. Are appropriate measures taken to ensure that network-based attacks (e.g., DDoS) based on anomalous inbound or outbound traffic patterns are detected and mitigated in a timely manner?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 54. Are back-up and archiving encrypted?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is data encrypted at rest?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 55. Are Chemical.AI's APIs exposed to end users? Do users only have access to the user interface (Vue app)?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "How is Chemical.AI staff access to customer data restricted?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Chemical.AI’s APIs are available to end users, but they are protected by strict security controls. By default, API access is disabled and must be explicitly activated. Enabling API access requires a separate application process and involves additional licensing or purchase conditions. — *Gilead* (`Gilead_follow_up_email_question.md`)
*First seen in:* `Gilead_follow_up_email_question.md`

### 56. Are cloud vendors evaluated for security & compliance to appropriate regulations?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Does your cloud hosting provider provide independent audit reports (SOC)?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 57. Are data files protected from change to maintain Data Integrity?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "What happens to submitted data?" (similarity 0.67)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 58. Are documents available to PTC for IQ (Installation Qualification)/OQ Operational Qualification) of the system?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do you have a SOC 1 / SOC 2 / SOC 3 report?" (similarity 0.67)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 59. Are encryption methods used that reflect state-of-the-art technology and are these used on a risk-based basis?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How are encryption keys managed?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 60. Are established procedures used to ensure that - only authorized persons are granted physical access to premises, buildings and systems; - operation is ensured in the event of a failure in the supply of utilities?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How is physical access to offices controlled?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 61. Are external penetration tests performed? When was the last test conducted and is a report available to PTC?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do you undergo independent penetration testing?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- The last test was conducted on August 4, 2025. See attached file: Penetration_report_chemical_ai.pdf — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 62. Are functions other than presentation performed on the user device?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the product / software / service and its purpose." (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 63. Are individuals able to withdraw consent they previously provided?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "How is consent obtained?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- why withdrawal of consent is not applicable. No, consent is required to access the platform and a previous consent cannot be withdrawn. However, users can directly delete their production environment data themselves, and all backup data is guaranteed to be completely deleted within the established retention periods (7 days for local backups, 3 months for off-site disaster recovery backups). 3. Please share the consent form or provide a link to the webpage where consent is obtained, if applicable. Consent is obtained through ChemAIRS's Privacy Policy at: https://chemairs.chemical.ai/compliance/universal/privacy-policy.html. Users must review the privacy policy "prior to accessing our Services" and provide express acknowledgment: "By proceeding to use our Services, you expressly acknowledge that you have read, understood, and consented to the terms set forth in this policy." This ensures consent is obtained before or at the time of data collection in full GDPR compliance. — *Gilead* (`Answers to Gilead Email Questions.md`)
*First seen in:* `Answers to Gilead Email Questions.md`

### 64. Are individuals provided with a mechanism to change their preferences regarding the use of their PI?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "What personal data (PII) do you collect?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Please describe how this mechanism functions, or explain why it is not applicable. Yes, individuals can change their personal information usage preferences through: direct account settings for optional profile information (user name, company details). — *Gilead* (`Answers to Gilead Email Questions.md`)
*First seen in:* `Answers to Gilead Email Questions.md`

### 65. Are Information Security requirements specified and implemented when new systems are introduced, upgraded, or enhanced?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Who is responsible for information security?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS implements comprehensive security measures during development and deployment. ChemAIRS accesses SonarQube's quality management and vulnerability detection engine at code compilation time (CI/CD). Vulnerabilities in the reference chain are identified in daily reports and reviewed by the code security team before being submitted to the code owner for repair, and only after the repair is complete will the merge-in request be approved. At release time, the code artifact will be built as a container image and released to the pre-release project. In the privately deployed Harbor repository, we use the Trivy engine to scan the image, and once a risky vulnerability is found, it will be reviewed by the code security team and submitted to the Devops administrator for fixing. After the release of the version, we will also have a quality management team for the pre-release environment and online formal environment from time to time security scanning. Once any problem is found, it will be reported to the code security team to review and submit to the person in charge of the corresponding repair. Access Control — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 66. Are measures in place to guarantee that sensitive data is securely decommissioned and cannot be retrieved by unauthorized individuals from discarded storage hardware?
**Importance:** 1 customer (Merck) · asked 1 time  
**Closest bank entry:** "Do you have data loss prevention controls?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- We employ rigorous data sanitization methods to ensure complete and secure data deletion post-testing. All data are encrypted and stored on technologically advanced storage mediums with RAID 5 and LVM, accompanied by encrypted off-site backups, to negate any possibility of data retrieval by unauthorized parties from any discarded hardware. 7. It has been specified that account sharing is prohibited, with the requirement that it should be limited to individual users. — *Merck* (`Merck Chemical.ai evaluation filled.pdf`)
*First seen in:* `Merck Chemical.ai evaluation filled.pdf`

### 67. Are Network Intrusion Detection / Prevention Systems (NIDS/NIPS) used to detect and/or prevent intrusions into the network?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Describe your network security controls." (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS employs: AWS GuardDuty for intrusion detection Intrusion detection and firewalls deployed at network and hardware levels to detect abnormal behavior Real-time monitoring of system logs and network traffic with timely alert notifications AWS WAF for web application firewall protection — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 68. Are non-company managed computing devices used to connect to the company network?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you use wireless networks?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- If yes, provide a security concept! (Conditional Access Policy, MFA, read-only, encryption, etc…) No. Only accessed via company PC. Network Security — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 69. Are regular security reviews of internal and external employees who perform sensitive roles conducted?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How often are security policies reviewed and communicated?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 70. Are SysAdmins trained in Part 11/Annex 11 and related regulations?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do you have a SOC 1 / SOC 2 / SOC 3 report?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable. However, system administrators understand the compliance expectations that affect how they build and run IT systems in regulated environments—e.g., user access management, audit trail retention, backup/restore, change control, and supporting validated/qualified infrastructure — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 71. Are system and security patches tested before implementation in the production environment?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 72. Are the electronic records in this system configured for secure transmission?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How is the office network secured?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Describe. ChemAIRS enforces HTTPS for all web traffic. In addition to transport encryption, sensitive data content is encrypted using AES-256. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 73. Are the servers hosted by a third party?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Which components are exposed to the internet?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Amazon Web Services (AWS). — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 74. Are the signatures permanently bound to their respective record?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How long are logs retained, and are they encrypted?" (similarity 0.62)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 75. Are there any audit reports such as SSAE-16, ISO 27001 (or successor type) etc.?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Are you audited by an independent external party?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- If yes, provide the latest reports. See attached file: Chemical.AI ISO27001 EXP2027.png.pdf If the application involves data that is covered by Sarbanes-Oxley Act (SOX), does the vendor meet the regulatory requirements for data protection? Are there any procedures supporting this? If the application involves data that is covered by regulations such as the Health Insurance Portability and Accountability Act (HIPAA) and/or General Data Protection Regulation (GDPR), does the vendor meet the regulatory requirements for data protection? Are there any procedures supporting this? GxP Systems Question | Yes | No | Notes — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 76. Are there any controls to stop company information from being placed onto removable media devices (such as USB drives or laptops)?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are mobile devices managed?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment In-app export is RBAC-controlled and audited; endpoint/removable-media controls are enforced by IFF's own device policies. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 77. Are there any dependencies on critical third party service providers?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you use subcontractors or depend on critical third parties?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. For SaaS deployments, ChemAIRS depends on AWS services including RDS, EKS, and other cloud infrastructure components. However, we do not use subcontractors. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 78. Are there any industry-specific regulations and requirements with which your organization must comply?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Which standards-based certifications do you hold?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Please list them here and specify if you are compliant — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 79. Are there any inter-application data and process sharing capabilities?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- If so, describe what is being shared and by what technique / technology. ☒ No Optional — via API/ELN(or Buildingblock) integration. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 80. Are there any known hardware / software conflicts or capacity limitations caused by other application requirements or situations, which would affect the application users?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What are the platform requirements for local deployment?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- None known; standard browser. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 81. Are there any other 3rd party software constraints?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you use subcontractors or depend on critical third parties?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Standard open-source stack; no restrictive constraints. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 82. Are there controls in place to ensure that access to PI is restricted to the minimum number of authorized individuals necessary?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Is access to DPCs limited to authorized personnel with dedicated access control methods? With two-factor authentication?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, ChemAIRS implements comprehensive least privilege access controls: Environment Isolation with strict physical separation of production, development, and test environments plus network isolation through firewalls and VPN; Role-Based Access Control (RBAC) with minimum required permissions for different user roles. — *Gilead* (`Answers to Gilead Email Questions.md`)
*First seen in:* `Answers to Gilead Email Questions.md`

### 83. Are there defined retention period(s) for the PI being processed?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "How long are logs retained, and are they encrypted?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes For SaaS, the retention period is 6 months — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 84. Are there documented policies and procedures that define limits to the collection and use of personal information to authorized users regarding limiting the personal information collected and used by authorized users e.g., minimum necessary, need to know, job role?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Are unique IDs required? Are shared accounts allowed?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS has documented policies that follow the minimum necessary principle: ChemAIRS only collects minimal personal information necessary: name, email address, and company name Data access is controlled through RBAC (Role-Based Access Control) with different permission levels for different roles (researchers, project managers, administrators) Data access privilege is one-time and each access requires submission of business justification and CEO authorization System administrators have maintenance privileges but do NOT have access to specific client data Access rights are refined for operations such as data reading, editing, and deletion based on job role For sensitive data, access is restricted to specific roles only (note: we can use data processing agreement as evidence) Threat Management — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 85. Are there job descriptions for personnel involved in the administration of the system indicating their specific responsibilities?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Who is responsible for access management?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Change Control Question | Yes | No | Notes — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 86. Are there procedures for the orderly commissioning, decommissioning and management of assets?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you have an asset management program and data classification?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 87. Are there security standards, baseline configurations, patching, access control, and strong passwords for network devices such as Firewalls, Switches, Routers, and Wireless Access Points?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Describe your network security controls." (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Security standards include: Strong password policies (minimum 8 characters, at least 3 of 4 character types) Access control via RBAC (Role-Based Access Control) User tenant segregation Password policies enforced Access log auditing Regular patching (monthly for applications, AWS-managed for infrastructure) Network segmentation (VLAN segmentation and data isolation) — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 88. Are User System Requirements documented?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How do users receive their credentials?" (similarity 0.62)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 89. Are users trained in the electronic system?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How do users receive their credentials?" (similarity 0.64)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 90. Are we required to accept enhancements?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have a change management policy?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No For customer-hosted, IFF controls when to apply updates. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 91. Based on PTC’s business needs, will the system be used for GxP purposes?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "What is needed on the client side?" (similarity 0.58)
**Past answers (from archive – unreviewed, may be outdated):**
- If No, Skip section GxP Systems.Note: Attach GxP assessments performed. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 92. Can additional parallel application servers be easily added? If so, what is the load balancing mechanism?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Which work is synchronous and which is asynchronous?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 93. Can constituents access corporate e-mail using mobile devices? If yes, provide a security concept! (MDM, interface between e-mail apps allowed?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How are mobile devices managed?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ) Yes, employees can access corporate email using mobile devices. (note only for myself: no MDM and other limits at this moment） — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 94. Can data retention be managed, automatized and/or configured by you within the scope of your services according to SERVIER's requirements/instructions ?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "What is your data retention policy?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes Please describe data retention capabilities: ChemAIRS supports configurable data retention, and under the local deployment model these controls are exercised directly by Servier. The platform is deployed entirely within Servier's own infrastructure, and Servier retains full authority over the data lifecycle from creation through deletion — including storage location, backup strategy (timing, frequency, retention period, storage location), encryption configuration, and restoration operations. Retention settings can therefore be configured to Servier's requirements without dependency on Chemical.AI. User accounts and associated personal data can be deleted by Servier's tenant administrators, and audit log retention is likewise configured and managed by Servier. Chemical.AI can advise on and assist with retention configuration during deployment and supervised maintenance, but has no access to the deployed environment and does not itself manage, automate, or apply retention to Servier data. Where Chemical.AI processes limited personal data outside the deployed environment (for example, business contact details of Servier personnel), such data is handled in accordance with the Chemical.AI Privacy Policy and Data Processing Agreement, and is deleted within 10 business days of a written request following cessation of services. — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 95. Can interfaces be provided that support Identity Federation?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you support single sign-on (SSO)?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 96. Can Siegfried AG or a recognized company/organization commissioned by Siegfried AG be granted the "right to audit"?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Are you audited by an independent external party?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 97. Can the archiving requirements from the Cloud Strategy be implemented? - A0 No archiving: No measures - A1 Archiving: Storage in suitable format, traceability guaranteed in the event of changes, periodic checking of archived data
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Where are backups stored?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 98. Can the data be replicated to an IFF data center?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Where is data hosted and stored?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes IFF has a full control of its own data — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 99. Can the frozen zones and maintenance windows defined by Siegfried AG be incorporated individually?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Is there a DMZ?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 100. Can the integrity requirements set out in the Cloud Strategy be implemented? - I0 Basis: Detection of integrity violations using checksums, hash functions or certificates - I1 Extended: Encrypted transport and storage of data, logging of all data changes.
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you follow secure baseline configurations (CIS, NIST)?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 101. Can this application be placed on an application server independent of all other applications?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Does the software run independently of the installation account?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- If not, explain the dependencies. ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 102. Can you confirm the initiative/project/system which requires PI or SPI, collects and contains only the minimum that is required to meet the functionality of the particular use case, and must not be retained beyond what is required for that purpose?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "What personal data (PII) do you collect?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes For SaaS, ChemAIRS follows the minimum necessary principle for data collection. ChemAIRS collects only the minimal personal information necessary for functionality. Personal information is retained for 6 months after termination of the usage agreement. All personal information is permanently deleted at the end of the retention period. No other personal information beyond what's functionally necessary is stored. — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 103. Can you ensure that any obsolete personal information is deleted or securely destroyed, and that all Gilead account access is removed once the project or service is complete?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "What happens to data when the subscription ends?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 104. Can you explain how your AI models arrive at specific decisions or outcomes?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are AI results made transparent and governed?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Explain IA decision Outputs are traceable to reaction precedent (template extraction + neural ranking); each proposed step is inspectable against the literature/patent it derives from. The core engine is not a generative LLM, so it is auditable rather than opaque. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 105. Can you please outline how this search is completed / what is the technical basis for the search and retrieval? Also is the literature sourced from Chemical AI curated sources? … or from external sources? … or both?
**Importance:** 1 customer (Jazz) · asked 1 time  
**Closest bank entry:** "How does ChemAIRS use AI?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- We search literature references based on molecular similarity and reaction similarity. The literature source is curated by Chemical.ai. It is a collection of patents, peer-reviewed journals, and some other databases we have purchased and have the right to include in our reaction data. Together, it's close to a hundred million reaction data, and all of them are transferred to Jazz's server during the installation phase, so it stays on your server. We update our databases to capture the latest reactions twice a year, and we will put the new data in your server when we do the annual update. — *Jazz* (`Jazz_questionnaires.md`)
*First seen in:* `Jazz_questionnaires.md`

### 106. Can you prove that the test standards have been followed?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Which standards-based certifications do you hold?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Multiple mechanisms provide proof: Evidence of compliance: Audit trails: All access and operation records are retained and used as the basis for auditing CICD integration: Automated testing is integrated into the CICD pipeline, creating automatic documentation Daily vulnerability reports: Systematic generation of vulnerability reports provides documentation trail Security certifications: ISO 27001 certification (which requires documented evidence of testing procedures) Traceability: All actions are meticulously documented for integrity and traceability Third-party validation: Annual application security assessments and bi-annual penetration tests by external professionals provide independent verification Pre-release validation records: Automated recovery tests with documented verification results Nth Party Management — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 107. Could IFF support the application if we were required to bring the solution "in house"?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Can ChemAIRS be deployed locally?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes IFF operates the deployed instance post-deployment with Chemical.AI support; source/algorithm remain Chemical.AI IP. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 108. Describe Administrative tools for monitoring and filtering of alarms
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, it depends on IFF's AWS infrastructure — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 109. Describe and quantify the use of systems resources by application processes and threads.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Kubernetes-scaled; GPU for models; sizing per workload. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 110. Describe any services that your company offers to complement the proposed solution.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the product / software / service and its purpose." (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Training, custom deployment support, and integration support. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 111. Describe data and file restore services?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is customer data deleted?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, IFF has full control of the data — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 112. Describe data volumes being transferred to the client.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are customers notified of a change in data storage location?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Modest (query results/reports), rendered in the browser. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 113. Describe firewall and intrusion protection control needs
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your network security controls." (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, IFF to define 7.0 Application — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 114. Describe historical reliability and availability statistics as well as capabilities provided in the event of down time or telecom failures.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are backups tested?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Recovery objectives RTO ≤ 4h, RPO ≤ 1h; multi-AZ HA and load balancing. For this option, uptime depends on IFF's AWS infrastructure. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 115. Describe how each and every version of the software can be reproduced and re-deployed over time.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you manage software supply chain risk?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Versioned container images, Helm and Terraform. 9.0 AI (Artificial Intelligence) Only relevant for AI solutions. Solutions with AI Only 9.1 AI Model Summery and Transparency — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 116. Describe how support will be provided and coordinated for any aspects of your solution that are to be supported by a third party?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 117. Describe how system performance is impacted by the new solution
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.59)
**Past answers (from archive – unreviewed, may be outdated):**
- Runs in IFF's dedicated environment, sized to workload (GPU for model compute); isolated from IFF's other systems, so minimal external impact. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 118. Describe how the look and feel of your presentation layer compares to the look and feel of the other existing applications.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.59)
**Past answers (from archive – unreviewed, may be outdated):**
- Standard modern web UI. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 119. Describe how the presentation layer of the system is separated from other computational or data transfer layers of the system.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are the production and non-production environments separated?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- Micro-services; frontend separated from compute/data layers. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 120. Describe how the solution will cope if access to the Master Data is unavailable for a period of time. Address specific situations such as how the solution will respond if user authentication information is unavailable. This can become a problem for the application where services to select from Master Data are to be used. IF MDR becomes unavailable, this will need to be catered for in the application.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your disaster recovery and business continuity plans." (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- ChemAIRS separates its authentication/identity layer (the Auth-Platform, federated to IFF's Entra ID for SSO) from its application and reference-data layers, so a disruption in one does not cascade across the system. If the identity source is temporarily unavailable, new single-sign-on logins will be affected for the duration, but the failure is contained and handled gracefully rather than causing an application crash; users already holding valid sessions are unaffected until their session expires, and normal login resumes automatically once the identity source is restored. In the customer-hosted (Option 2) deployment, these components run within IFF's own AWS environment, so availability of the identity source and reference data also depends on IFF's infrastructure and network. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 121. Describe how the user navigates between this and other applications.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Browser-based; SSO enables app switching. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 122. Describe how your company monitors Data Center Availability?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What are the physical access restrictions to the data center?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, it depends on IFF's AWS infrastructure — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 123. Describe how your company’s customer service is organized and how it operates
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Dedicated business manager plus support team, escalating to DevOps and development leaders. 3.12 Options for help desk availability and response times Response within 1 business day; hours per agreement. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 124. Describe in as much detail as possible how PTC data is being processed from PTC to your network?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How is customer data segregated?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, PTC data never leaves PTC's own network or infrastructure. There is no data flow from PTC to Chemical.AI's network. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 125. Describe monitoring and reporting of patch management?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Trivy/SonarQube reports and email notifications of vulnerabilities and fixes. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 126. Describe remote monitoring of the OS, Connectivity, capacity management? Describe monitoring application outside of the standard server monitoring (e.g., windows service, web services, web sites, etc.)?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, it depends on IFF's AWS infrastructure — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 127. Describe system capability in generating automated alerts when experiencing downtime or connectivity issues for any external interface or application exceptions emanating from core platform.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, it depends on IFF's AWS infrastructure — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 128. Describe the current roadmap of new and enhanced features to your platform and expected GA (Generally Available) date (actual or by Quarter’YR). Please provide a visual timeline of this roadmap as appropriate.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What are your remediation timelines?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Continuous release cycle (two major updates per year); roadmap available on request. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 129. Describe the data and process help facility being provided.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- In-app help and tooltips, user manuals, and support. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 130. Describe the design that accommodates changes in the user base, stored data, and delivery system technology.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are customers notified of a change in data storage location?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Horizontally scalable, containerised, and modular. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 131. Describe the how many current or future users need to use the application in a mobile capacity or who need to work off-line.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are mobile devices managed?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- IFF to define. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 132. Describe the integration level and strategy with each application.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- API-based (REST/JSON), SSO federation, and file import/export. 7.36 Please provide context diagram is to be provided showing how the solution integrates with other applications. Also include any sources that may be required for master data. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 133. Describe the level of experience of your company’s help desk personnel
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Technical staff including security experts and DevOps engineers. 3.16 Availability and requirements for remote support Remote support with IFF authorisation; access is time-limited and logged. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 134. Describe the notification process and service level expectations outside of normal business hours?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable for local deployment. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 135. Describe the processes that have a dependency on the infrastructure.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have in place infrastructure redundancy measures, such as: disk mirroring, RAID, internet redundancy connections, failover telecommunications systems, etc.?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- GPU compute, database, message queue, and cache. 7.10 Does this application require any Batch Processing ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 136. Describe the responsibilities your company takes to implement patches or updates. Are they tested and certified in your lab?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Patches/updates are tested in QA/pre-release clusters replicating production before release; container-based delivery. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 137. Describe the screen to screen navigation technique.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are temperature, humidity, and other environmental factors monitored in real time?" (similarity 0.55)
**Past answers (from archive – unreviewed, may be outdated):**
- Standard web-UI navigation. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 138. Describe the security features of your solution including the number of places requiring a login.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your insider threat program." (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Single SSO login via Entra ID for the web app; RBAC enforced in-app; API uses separate token authentication. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 139. Describe the SLAs supported by your organization and any compensation provided for missed delivery.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- To be determined — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 140. Describe the technology components and applications of the proposed solution (e.g. Bedrock, Dataiku, Redshift, Veeva, LLMs)
**Importance:** 1 customer (Jazz) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- ChemAIRS is a self-contained chemistry R&D platform. It is not built on Bedrock, Dataiku, Redshift, or Veeva, and does not require integration with any of them. All models are proprietary to Chemical.AI and are packaged with the application. No LLM is used at this moment. Components (not all applicable to Jazz, depending on the licensed modules): Retrosynthetic analysis engine. Proprietary machine learning models (reaction template extraction plus neural ranking) trained on curated public and licensed reaction corpora, generating multiple synthetic routes per target with scoring on route viability, cost, and step count. Forward synthesis prediction and synthesizability (SA) scoring. Predicts likely products and rates how readily a proposed structure can be made. Impurity prediction. Flags probable side products ahead of analytical work. Process chemistry module. Cost accounting, solvent and reagent assessment, and scale-up considerations at the route level. Bayesian optimization. Reduces the number of experimental rounds required to reach target reaction conditions. Deployment and security: ChemAIRS is available as a local (on-premise or private VPC) deployment behind the customer's firewall, which is how the majority of our pharma customers run it. AES-256 encryption at rest and in transit. Role-based access control. ELN integration via API. In a local deployment, no structures, routes, or usage data are transmitted to Chemical.AI. Applications: route scouting and feasibilit — *Jazz* (`Jazz_questionnaires.md`)
*First seen in:* `Jazz_questionnaires.md`

### 141. Describe to what extent the client needs to support asynchronous and / or synchronous communication.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Which work is synchronous and which is asynchronous?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Both — synchronous UI plus asynchronous task queue. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 142. Describe your assets classification program to determine the level of criticality and up-time requirements of your systems and applications.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have an asset management program and data classification?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Asset criticality is scored via our Information Security Risk Assessment Methodology (a 5×5 likelihood × impact matrix aligned to ISO 27001:2022 and ISO 27005), driving risk-treatment and control decisions. Availability rests on multi-AZ high availability, with RTO ≤ 4 hours and RPO ≤ 1 hour. Section 4 - Human Resources Security 5 Questions — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 143. Describe your back-up and archiving process for intermediate and full backups?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Where are backups stored?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- IFF controls storage — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 144. Describe your change management process, including methods for backing out changes?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have a change management policy?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Formal change control with dual approval (development + data-security leads), tested in pre-release; versioned container images enable rollback. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 145. Describe your company's ability to provide pre-installation and post-installation consulting.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the product / software / service and its purpose." (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Deployment support, configuration, training, and ongoing maintenance support — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 146. Describe your company's test environment resources available for pre-testing any proposed changes to the system.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What is your testing strategy?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Separate DEV/Test/QA and pre-release clusters that replicate production. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 147. Describe your escalation procedures for critical issues and how IFF is kept informed throughout the process.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Documented incident process with email notifications and status updates throughout. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 148. Describe your implementation strategy
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What does implementation look like?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Environment prep → deploy containers → configure → validate/acceptance sign-off. 2.32 Average time frame of implementation Typically a matter of weeks. 2.33 Responsibilities of IFF during implementation — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 149. Describe your network or provide a network diagram showing your environment and any security devices?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your network security controls." (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- (Paragraph) Not applicable for local deployment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 150. Describe your physical protections for servers and network equipment.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your network security controls." (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- AWS physical security (SOC/ISO-audited) within IFF's account; no Chemical.AI-operated server room in scope. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 151. Describe your process for providing remote access for your employees?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is remote access to your network secured?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable for local deployment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 152. Describe your process to review user access.
**Importance:** 1 customer (Acadia) · asked 1 time  
**Closest bank entry:** "How often are access rights reviewed?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Access is role-based (RBAC) under the Access Control Policy and Privileged Access Management Policy, applying least-privilege and separation-of-duties. Permissions are reviewed on a defined cadence — quarterly for privileged accounts and semi-annually for regular users — with all permission changes recorded. All access to sensitive systems and data is logged and auditable; in SaaS, Chemical.AI data access requires a one-time, CEO-approved privilege with business justification. — *Acadia* (`Cybersecurity Questions.jay.acadia.docx`)
*First seen in:* `Cybersecurity Questions.jay.acadia.docx`

### 153. Describe your SDLC process including types and frequency of security checks
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- SonarQube SAST on every commit; Trivy container scans on every release; OWASP scans; dual code review; annual third-party penetration test. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 154. Describe your solution’s system administrator capabilities.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your insider threat program." (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Admin console for user/role management, configuration, and audit-log review/export. Maintenance admin roles do not include data access. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 155. Describe your systems management tools
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your vulnerability management program." (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployment, it depends on IFF's AWS infrastructure — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 156. Detail how AI/ML/LLM systems are used for in scope systems/data, to include model training and where automation is used to make decisions.
**Importance:** 1 customer (Acadia) · asked 1 time  
**Closest bank entry:** "How does ChemAIRS use AI?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ChemAIRS applies AI/ML to chemistry tasks only — retrosynthesis route prediction, forward synthesis, impurity prediction, condition optimization, and synthetic-feasibility analysis. It uses pre-trained models for inference only. In-scope/client data is never used to train or fine-tune models — no transfer learning, no data reuse, no contribution to Chemical.AI's general models. — *Acadia* (`Cybersecurity Questions.jay.acadia.docx`)
*First seen in:* `Cybersecurity Questions.jay.acadia.docx`

### 157. Did you implement any Virus Protection software with Chemical.ai?
**Importance:** 1 customer (Merck) · asked 1 time  
**Closest bank entry:** "Do you undergo independent penetration testing?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Indeed, advanced virus protection is implemented within our platform. We employ advanced hardware firewalls and our data security team conduct continuous surveillance for any signs of unusual activities. 3. During the evaluation, the developers' access to proprietary data should be blocked/prohibited. — *Merck* (`Merck Chemical.ai evaluation filled.pdf`)
*First seen in:* `Merck Chemical.ai evaluation filled.pdf`

### 158. Do developers have access to production environments?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are the production and non-production environments separated?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 159. Do electronic signatures include date & time stamps?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Does ChemAIRS support multi-factor authentication (MFA)?" (similarity 0.58)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 160. Do policies and instructions exist with specifications for protection against malicious programs, which cover the following points in particular: - Use of system-specific protection mechanisms - Operation and updating of protection programs on components in its area of responsibility - Operation and updating of protection programs for end devices of its employees
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Describe your insider threat program." (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 161. Do you allow IFF to dictate priority of recovered customer data?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is customer data deleted?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment For local deployment, IFF has full control of the data — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 162. Do you allow VPN services?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are unnecessary services disabled?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 163. Do you apply data protection measures (e.g., encryption, anonymization, segregation) for sensitive data?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Is data anonymized or pseudonymized?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, sensitive data is protected through AES-256 encryption at rest, TLS 1.2+ encryption in transit, encrypted backup storage, strict tenant isolation in multi-tenant SaaS, and hashed/salted passwords using private encryption algorithms. 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section II: Data Encryption - AES-256 for sensitive data, TLS 1.2+ for transmission, encrypted backup storage; Section II: Multi-tenant Data Management with tenant isolation, resource quotas, access boundaries; Section III: Data Transmission Security with TLS 1.2+ encryption, real-time monitoring, integrity verification — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 164. Do you apply security controls for cloud services (CSPM, CASB)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How is remote access to your network secured?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, cloud security controls through AWS native services including AWS GuardDuty for threat detection, AWS WAF for application protection, AWS CloudWatch for monitoring, VPC Network ACLs for traffic control, and security group configurations, though explicit CSPM/CASB tools not documented. 《AWS Network Security Configuration》(Screenshots) 16.2: AWS VPC Network ACL Configuration providing mandatory network-level protection with inbound and outbound traffic rules enforcing organizational policies for allowed or restricted communication — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 165. Do you document test results as part of quality documentation?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How is quality managed?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Please provide evidence validating the implementation of the stated control. Yes. Multiple forms of quality documentation: Evidence: Vulnerability reports: Vulnerabilities in the reference chain are identified in daily reports and reviewed by the code security team Security assessment documentation: Documentation of detailed strategy for each vulnerability (immediate repair, scheduling for next release, or justified non-action). All actions are meticulously documented for integrity and traceability Audit logs: All testing and deployment activities are logged and retained as basis for auditing Pre-release validation: Quality management team validates system availability and data integrity through automated tests with documented results Change documentation: The configuration and updates of ChemAIRS require an internal modification approval process. Changes can only be made after being reviewed and approved by the development lead and the data security lead — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 166. Do you embed security in SDLC (SAST, DAST, secure code review)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "What is your testing strategy?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we embed security in the SDLC using SonarQube SAST in CI/CD, Trivy container scanning, OWASP-aligned testing, mandatory peer reviews, and quality-gate enforcement that blocks merges/releases until security criteria are met. 《Development Security Pipeline》(Screenshots) 18.1: GitLab CI Pipeline Log showing SonarQube Static Code Analysis execution with quality gate status PASSED, scanning \ 1389 source files with secret detection and code quality checks 《Chemical.AI Security Development Principles and Coding Standards》 Software Security Development Lifecycle (SDL) integrating security into every development phase: requirements, design, coding, testing, and maintenance — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 167. Do you encrypt all IFF data at rest?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is data encrypted at rest?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Not applicable for local deployment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 168. Do you enforce MFA and secure connections (VPN, ZTNA) for remote access?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How is remote access to your network secured?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, remote access is secured with AWS security group controls, SSO (Azure AD) integration, enforced HTTPS/TLS, device- and source-based access restrictions, and MFA capabilities in development, all governed by remote-access and access-control policies. 《Information Security Management Policy Handbook》(Doc) ISMS-2-CL-012 Access Control Policy sections 5.7-5.8 covering remote access security requirements and multi-factor authentication procedures — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 169. Do you enforce secure retention and destruction of data and media?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "What is your data retention policy?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we enforce secure retention and destruction through a 6-month retention period after contract termination, 7-day encrypted local backups with automatic cleanup, 3-month remote DR retention with physical destruction afterward, and CEO-authorized data deletion procedures. 《Information Security Management Policy Handbook》(Doc) Section III: Data Backup Strategy - Section 8: Local Backup Management with 7-day retention, AES-256 encryption, automatic cleanup; Section 9: Remote Disaster Recovery Backup Management with 3-month retention, physical destruction after 3 months — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 170. Do you ensure that the software is running on supported OS and database releases?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Does the software run independently of the installation account?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS has specific requirements: Operating Systems: Supports most mainstream glibc-based Linux operating systems Recommended: Rocky Linux (8.9 - 9.3), Debian (11-12), CentOS 7.9, Ubuntu (18.04 - 22.04) These are thoroughly tested and validated systems Database: PostgreSQL minimum version: 14.0 PostgreSQL 14+ chosen for improved multi-threading and large-scale concurrent queries Cloud options: AWS RDS, Google Cloud SQL for PostgreSQL — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 171. Do you ensure that your DR facilities have all the same security controls implemented as your primary Data Center?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are physical access to DPCs monitored with video surveillance system (CCTV), alarms, or security guards?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Section 10 - Compliance 6 Questions — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 172. Do you evaluate, monitor, and require security commitments from your own subcontractors/suppliers?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you use subcontractors or depend on critical third parties?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we evaluate, monitor, and require security commitments from third-party suppliers. While Chemical.AI does not use subcontractors for core software development (all developed in-house), we do evaluate and monitor our critical third-party suppliers, particularly cloud infrastructure providers. 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 173. Do you follow change management procedures including security impact assessments?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you have a change management policy?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we enforce formal change management requiring internal modification approvals, dual authorization from development and data security leads, automated security impact checks, and documented change and release controls. 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section IV: Operations and Monitoring Management - Section 12: Operations Management with change management, release management, capacity planning, performance optimization procedures — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 174. Do you have a fall back plan for new releases?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Describe your disaster recovery and business continuity plans." (similarity 0.57)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Multiple fallback mechanisms: Backup before updates: Database operated and backed up before changes Pre-release testing: Deployed in test clusters that exactly replicate production settings Daily backups: 7 generations of daily backups maintained Automated recovery tests: Quality management team performs regular automated recovery tests Rollback capability: Container-based architecture allows easy rollback to previous versions Separation of environments: Pre-release environment tested before production deployment — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 175. Do you have a policy defining record retention applicable to cloud vendors?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "What is your data retention policy?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- If No, provide details. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 176. Do you have a policy for logging security violations?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Security events are captured in audit logs and reviewed regularly; logs are encrypted with ≥1-year retention (configurable by IFF in their environment). — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 177. Do you have a policy, procedure and a person responsible for managing personal data breach under GDPR (identification, notification, documentation, remedial action, reporting) ?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you have a Data Protection Officer?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes Please list the documents and specify how often those documents are reviewed and the contact name & function. As ChemAIRS is deployed locally within Servier's own infrastructure, Chemical.AI has no access to that environment and cannot detect breaches occurring within it; detection and regulatory notification rest with Servier as controller. The procedures below apply to Chemical.AI's own systems and to any incident arising during supervised maintenance performed at Servier's request, in which case Chemical.AI will notify Servier without undue delay and cooperate in investigation and remediation. Relevant documents: Information Security Management Policy Handbook (ISMS); ISMS-2-CL-009 (incident escalation and response); Employee Information Security Handbook ZH-IS-201 §6 (security incident reporting, 24-hour internal reporting requirement); ZHKJ-QESP-24 (incident investigation and handling); ZHKJ-QESP-25 (emergency preparedness and response); ZHKJ-QESP-26 (corrective and preventive action); and the Chemical.AI Data Processing Agreement, which commits Chemical.AI to notify the controller upon discovering a personal data breach. These documents are reviewed periodically under the ISO 27001:2022 management review cycle. Responsibility for personal data breach management sits with the designated Data Protection Officer within the Information Security Team, supported by the CEO/Data Security Administrator as risk owner and the DevOps Manager as technical lead. Responsible cont — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 178. Do you have a procedure in place for notification of customers/users for Cloud/Web-based system in the event of any excursions/breaches to your system? 1A. Have you experienced any breaches? If yes, please provide details.1B. If a procedure is available, within what time frame must you notify your customers? Please provide a copy for review.1C. Do you provide a documented investigation report and CAPA in event of any excursions/breaches to your system?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 179. Do you have a process to return or destroy company data, upon the termination of services?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What happens to data when the subscription ends?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Section 8 - Information Security Incident Management 7 Questions 8.1 - Do you have an Information Security Incident Response Plan that responds to: ☒Both — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 180. Do you have a Security Incident and Event Management (SIEM) solution?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Internal — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 181. Do you have a try before you buy program, where customers can test certain capabilities before they commit to purchase?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you offer trials?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment Evaluation/trial access or a scoped POC can be provided before commitment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 182. Do you have a validation process in place that identifies and manages risks associated with the critical functions of your products or services?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you have a documented risk assessment process?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, comprehensive risk management and validation processes: Risk Management Framework (ZHKJ-QESP-15): Risk identification, assessment, and management processes Risk criteria, evaluation methods, and treatment strategies Risk monitoring, review, and communication activities Risk registers with historical scores and year-over-year trend analysis Control effectiveness measurements Validation Processes: Design and Development Control (ZHKJ-QESP-06): Design input requirements, review stages, verification activities, validation requirements Risk Assessment: Annual comprehensive assessment (mandatory), plus assessments for major system changes, security incidents, and regulatory changes Quality Controls: Independent review by Data Security Administrator, cross-validation with automated tools, stakeholder review sessions Critical Functions Covered: Authentication and session management Data validation and integrity Network security and access controls Backup and disaster recovery Compliance with pharmaceutical industry standards 《ChemAIRS Information Security Risk Assessment Methodology》(Doc) 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-06 (Design and Development Control Procedure), ZHKJ-QESP-15 (Risk Control Procedure) Project Planning / Management — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 183. Do you have an approved Computer System Validation policy?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do you have a documented information security program and policy approved by management?" (similarity 0.69)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 184. Do you have any camera systems in place?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are systems configured for forensic investigation?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Inherited from AWS data-centre controls; not applicable to Chemical.AI. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 185. Do you have any security architecture documentation/diagram that could be shared with us?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- For example, describing which security tools / encryption are applied in each route or component. We do not currently maintain a formally published security architecture document. However, I have prepared a set of screenshots that illustrate some of the security controls. — *Gilead* (`Gilead_follow_up_email_question.md`)
*First seen in:* `Gilead_follow_up_email_question.md`

### 186. Do you have commitments to retain data due to legal and business requirements? If yes, please provide supported compliance models?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What is your data retention policy?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment Configurable retention supporting IFF's retention needs; ISO 27001-aligned. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 187. Do you have customer data archiving and recovery solutions?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is customer data deleted?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Not applicable for local deployment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 188. Do you have formal procedures governing user account creation/deletion?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How do users receive their credentials?" (similarity 0.65)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 189. Do you have formal procedures in place for access to network and server(s) used for electronic records?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Is there a formal procedure for visitor access to the data centre?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 190. Do you have put in place means upstream of projects to apply the principle of privacy by design?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Describe your privacy program." (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Please specify the means in place. Privacy considerations are addressed upstream through Chemical.AI's Design and Development Control Procedure (ZHKJ-QESP-06), which governs design inputs, staged design reviews, verification and validation, and control of design changes for new products and features. Design inputs include applicable regulatory and customer requirements, identified through the Legal and Regulatory Identification and Update Control Procedure (ZHKJ-QESP-19) and assessed under the Compliance Evaluation Control Procedure (ZHKJ-QESP-20). Risks are identified and treated under the Risk Control Procedure (ZHKJ-QESP-15), with mandatory annual risk assessment and additional assessment triggered by major system changes or deployments, security incidents, and regulatory changes. The principles are reflected in the architecture itself. ChemAIRS applies data minimisation: only the minimum information required to deliver the service is collected, namely basic user account details (name, email address) and molecular data input by users. Privacy by default is enforced through role-based access control and least privilege, with read-only database roles for non-administrative functions and privileged accounts issued individually, subject to approval, and traceable to named users. Security is built in by default rather than configured after the fact — AES-256 encryption at rest, TLS 1.2/1.3 in transit, and multi-layer isolation at the physical, network and application layer — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 191. Do you have SLAs for Disaster recovery?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your disaster recovery and business continuity plans." (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Not applicable for local deployment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 192. Do you have someone in your organization that is responsible for managing your privacy program?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe your privacy program." (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Albert Ai, Data Protection Manager (internal), oversees the information security program Section 3 - Asset Management 4 Questions — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 193. Do you have standards for test planning and execution?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "What is your testing strategy?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- （Please provide evidence validating the implementation of the stated control.） Yes. ChemAIRS has comprehensive testing standards implemented through their SDLC: Evidence of testing standards: Separate test environments: DEV, Test, QA, and Pre-release environments are maintained separately from production Pre-release testing: Pre-release environments are deployed in proprietary test clusters under the same AZ, replicating the base settings of the official environment to ensure that no unexpected failures will occur due to differences in the environments Quality management team: Dedicated team performs regular security vulnerability scans and testing Automated recovery tests: The quality management team performs automated recovery tests on the backup copies on a regular basis to verify the availability of the recovered system Please provide examples of test plans for each phase (structure test (white box test), module and integration test). Example: Structure Test (White Box Test) Scope: Individual component code analysis and internal logic verification Test Plan Activities: Static Code Analysis: Automated scanning of source code for security vulnerabilities and coding standard violations before merge Code Review: Mandatory peer review of all code changes focusing on: Input validation implementation SQL injection prevention (parameterized queries verification) Error handling without exposing sensitive data Proper implementation of authentication/authorization logic Unit Testing — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 194. Do you have systems/policy in place for minimum password complexity & strength and password change frequency?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "What is your password policy?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- If yes, provide details. Complexity & Strength: minimum length of 8 characters; must include at least 3 of the following 4 character types: uppercase letters, lowercase letters, numbers, and special characters; and prohibited passwords including user account names, email addresses and common/simple passwords. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 195. Do you have, or plan to provide, a specific data privacy awareness-raising or training program for its your employees, as part of this outsourcing service to SERVIER, to inform them of their role and responsibilities in this area ?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Describe your privacy program." (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Please specify the nature of this awareness-raising program and frequency, or failing that, the measures taken to raise data protection/privacy awareness of personnel involved in the services delivered to SERVIER. Chemical.AI provides bi-annual information security and data privacy awareness training to all employees, together with role-specific technical training, under its Training Management Control Procedure (ZHKJ-QESP-29) and Human Resources Control Procedure (ZHKJ-QESP-04). Training covers data protection and privacy obligations, secure handling and classification of data, and incident reporting responsibilities. Chemical.AI can provide supplementary briefing to personnel assigned to the Servier engagement on Servier-specific requirements where required. — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 196. Do you maintain a Security Assurance Plan (SAP) or equivalent document describing your security commitments to clients?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you have a SOC 1 / SOC 2 / SOC 3 report?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we maintain a comprehensive set of security policies and client-facing commitments, including detailed SaaS environment data security regulations and a GDPR-compatible Data Processing Agreement. 《Information Security Management Policy Handbook》(Doc) 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section I: General Provisions (Scope of Application, Basic Principles - Security first, ISO 27001 compliance, least privilege, transparency and control) Section II: SaaS Production Environment Data Management (Environment Isolation, Multi-tenant Data Management, Access Control) Sections covering: Data encryption policies, backup strategy, operations management, business continuity planning specific to SaaS environment 《Chemical.AI Data Processing Agreement》 GDPR-compatible Data Processing Agreement for SaaS clients — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 197. Do you maintain an inventory of your company assets?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have an asset management program and data classification?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 198. Do you maintain and test a BCP/DRP that includes information security aspects?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you have a documented information security program and policy approved by management?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we maintain and test a comprehensive BCP/DRP with RTO ≤4 hours and RPO ≤1 hour, dual-layer backups (local + remote DR) protected by AES-256, and well-defined procedures for force majeure, system failures, and security incidents, validated via bi-annual drills. 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section V: Data Recovery and Emergency Response - Section 16: Business continuity with RTO ≤4 hours, RPO ≤1 hour, bi-annual drills, regular plan updates; Section 14: Data recovery conditions for force majeure, system failures, security incidents; Section 15: Recovery process with dual senior management authorization and supervised execution Section III: Data Backup Strategy - Sections 7-9: Dual-layer protection with local backup + remote disaster recovery, full backup strategy, 7-day retention, AES-256 encryption — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 199. Do you maintain records of processing activities as it relates to services provided to SERVIER?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How are audit logs stored and reviewed?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes Please specify the tool maintained to record processing activities (e.g. excel sheets, compliance tool). Records of processing activities are maintained in a controlled spreadsheet register (Microsoft Excel), managed under Chemical.AI's document and record control procedures (ZHKJ-QESP-01 / ZHKJ-QESP-02) within our ISO 27001:2022-certified ISMS. The register is version-controlled, access-restricted to authorised compliance personnel, and reviewed on change and at defined intervals. No dedicated third-party privacy compliance platform (e.g. OneTrust) is currently in use. — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 200. Do you manage the full lifecycle of user accounts and access rights?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Who is responsible for access management?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we manage the full lifecycle of accounts and access rights via RBAC, privilege separation, MFA (in development), periodic reviews, password policies, privileged-access controls, and long-term audit logs. 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section II: SaaS Production Environment Data Management - Section 5: Access Control with multi-factor authentication, privilege separation, audit logs (1+ year retention), privilege review procedures 《Information Security Management Policy Handbook》(Doc) ISMS-2-CL-001: Password Policy with regular password changes and complexity requirements; ISMS-2-CL-003: Privileged Access Management Policy with rules for creating, using, controlling, and removing accounts with special access privileges — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 201. Do you need guaranteed data delivery or update, or the system tolerate failure?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Async queue with retry and audit trail; tolerant of transient failures. 7.43 Are there any logs produced by the application. What information is available in the log files and for what period are they required to be kept. Application/security/audit logs; IFF to define the retention period. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 202. Do you operate a SOC or equivalent detection tools?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, security operations capabilities through AWS GuardDuty for intrusion detection, AWS WAF for application protection, real-time monitoring with Grafana Loki and AWS CloudWatch, H3C SecPath Intrusion Prevention System with thousands of active detection signatures, and continuous network traffic monitoring. 《On-Premises Network Security Infrastructure (Huawei & H3C)》 H3C SecPath F1000-E-XI Intrusion Prevention System (IPS) Signature Library with CVE-related exploit signatures, attack categorization, severity levels; H3C SecPath Firewall Operation Monitor Dashboard showing real-time system resource usage and session statistics 《AWS Network Security Configuration》 — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 203. Do you perform internal audits as part of the privacy program?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Describe your privacy program." (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Please provide the audit privacy program plan and the frequency. Internal audits are conducted under the Internal Audit Control Procedure (ZHKJ-QESP-11), covering audit planning, auditor independence, execution, reporting and follow-up, with findings tracked through the Corrective and Preventive Action Control Procedure (ZHKJ-QESP-26). Data protection and legal compliance are assessed under the Compliance Evaluation Control Procedure (ZHKJ-QESP-20). Frequency: annual internal audit under the ISO 27001:2022 and ISO 9001 certified management systems, plus an annual comprehensive risk assessment, bi-annual security assessments, and annual external surveillance audit by the certification body. Additional audits are triggered by major system changes, security incidents, or regulatory changes. Oversight rests with the Data Protection Officer within the Information Security Team. — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 204. Do you process or subprocess (transfer, store, and/or allow access to) Servier personal data outside the European Economic Area (EEA) ?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- No. If you are proposing to sub-contract any part of the work which involves the processing of Personal Data, that it will carry out on our behalf, do you have a contract in place with your sub-contractor that includes data processing obligations? No If personal data is subprocessed (transfered, stored, and/or allowed access to) outside the European Economic Area (EEA), have you implemented the Standard Contractual Clauses of the European Commission, BCRs or adequacy decision or is it belonging to the EU-US Data Privacy Framework? No Not applicable to the deployed system. Under local deployment, SERVIER personal data resides exclusively within SERVIER's own infrastructure and is not transferred to, stored by, or accessible to Chemical.AI or any subprocessor outside the EEA. No subprocessors are engaged for this deployment model. Where limited personal data (e.g. administrator contact details for support purposes) is processed by Chemical.AI, the EU Standard Contractual Clauses (Module Two, Controller-to-Processor) apply as incorporated in our Data Processing Agreement. — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 205. Do you provide access to SERVIER's personal data on a clear 'need to know' basis?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Can government authorities access customer data?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Please specify the measures in place to ensure your its compliance with this principle (e.g. acces control, level of clearance). ChemAIRS is deployed within SERVIER's own infrastructure; Chemical.AI has no access to SERVIER personal data. Access is enforced on a need-to-know, least-privilege basis via role-based access control integrated with SERVIER's identity provider (Azure AD / Entra ID, SAML 2.0 / OAuth 2.0), so provisioning and revocation follow SERVIER's own identity governance. Non-administrative database roles are read-only. All privileged actions are recorded in the ChemAIRS audit log within SERVIER's environment. Any Chemical.AI support access requires SERVIER to grant it explicitly on a time-limited basis. — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 206. Do you provide artificial intelligence components to SERVIER?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Is customer data used to train models?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. the governance system set up in accordance to the IA Act. ChemAIRS provides AI-driven retrosynthesis and synthesis route prediction. The models operate solely on chemical structure data and do not process personal data, do not perform profiling or automated decision-making affecting individuals, and are not used for any purpose within Annex III of the EU AI Act. On that basis the system is assessed as minimal-risk under the AI Act rather than high-risk. Customer data is never used to train or fine-tune Chemical.AI models. Under local deployment, models run entirely within Servier's infrastructure with no external connectivity, and outputs are advisory only — proposed synthetic routes are reviewed and validated by Servier's chemists before any experimental use, so a human remains in control of all decisions. Model development and changes are governed by the Design and Development Control Procedure (ZHKJ-QESP-06) and Risk Control Procedure (ZHKJ-QESP-15) under Chemical.AI's ISO 27001:2022-certified management system, with versioned releases and documented change control. — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 207. Do you provide automatic load-balancing, across data centers?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have in place infrastructure redundancy measures, such as: disk mirroring, RAID, internet redundancy connections, failover telecommunications systems, etc.?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 208. Do you provide group mapping via SAML 2.0 or OIDC?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are identities provisioned? Do you support SCIM?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment Today: manual user pre-creation with SSO credential validation; SCIM/automated group mapping evaluated case-by-case. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 209. Do you require any exception from industry security standards, and why is this required?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you follow secure development standards?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- None requested. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 210. Do you require disk encryption on your end-point devices?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have antivirus / endpoint protection?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 211. Do you Require Network Connectivity?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you use wireless networks?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes 2.0 Architecture & Technology — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 212. Do you secure connected devices and industrial systems?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How are mobile devices managed?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, although IoT/OT is limited, we secure endpoints and mobile devices with mobile-device policies, password requirements, restrictions against storing important data, network segmentation, and endpoint audit software on company computers. 《Information Security Management Policy Handbook》(Doc) ISMS-2-CL-011 Mobile Device Management Policy establishing rules for mobile device use including approved device requirements and wireless data transmission restrictions 《User Endpoint Policy Enforcement Overview》 Centralized endpoint security system monitoring software usage, website access, USB and peripheral device access, file transfer risks, and time-based workstation policy enforcement — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 213. Do you support both logical and physical encryption?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is data encrypted at rest?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes how each is implemented, including examples of services or infrastructure components that use logical (e.g., IAM policies, software-based encryption) and physical (e.g., HSMs, dedicated hardware) encryption. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 214. Do you track lessons learned from incidents and update security controls?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you track security KPIs?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we track lessons learned via formal post-incident investigation and improvement processes that analyze causes, define corrective and preventive actions, verify effectiveness, and feed results into continuous improvement. 《Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-24: Accident and Incident Investigation and Handling Control Procedure with post-incident investigation and corrective action procedures; ZHKJ-QESP-14: Improvement Control Procedure defining systematic approach for continual improvement with metrics for measuring improvement effectiveness and sustainable implementation; ZHKJ-QESP-26: Corrective and Preventive Action Control Procedure with root cause analysis and effectiveness verification — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 215. Do you undertake to notify SERVIER of any individual data request (= exercice of data subject's rights under GDPR) as soon as possible and no later than 48 hours from the receipt of the request ?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How are data subject rights handled?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 216. Do you undertake to process SERVIER's personal data in accordance with SERVIER's instructions (including the purpose, the data concerned, the retention period) as defined in contractual data protection clauses and to prohibit any reuse of SERVIER's data without SERVIER's consent?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How are data subject rights handled?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- yes — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 217. Do you use a syslog server for network devices?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you use wireless networks?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes For local deployment, IFF to define — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 218. Do you use metadata or telemetry for model improvement?
**Importance:** 1 customer (Jazz) · asked 1 time  
**Closest bank entry:** "Is customer data used to train models?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- No. Our algorithm improvement is independent from any client engagement. — *Jazz* (`Jazz_questionnaires.md`)
*First seen in:* `Jazz_questionnaires.md`

### 219. Do you use subprocessors to assist in providing your services to IFF that will have access to and/or process personal data?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you assist customers with DPIAs?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Amazon Web Services (AWS) provides the underlying cloud infrastructure (compute, database, storage). AWS holds SOC 1/2/3 and ISO 27001/27017/27018. No other subprocessors or subcontractors are used; data content is encrypted. — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 220. Do you use threat intelligence feeds to improve monitoring?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we subscribe to up-to-date threat intelligence feeds for malware and exploit activity and integrate real-time CVE vulnerability repositories into Trivy container scanning for proactive security posture management. 《Container Vulnerability Management》(Screenshots) Harbor Vulnerability Scanner using latest real-time CVE vulnerability repository through Trivy automation tool; Component-Level Vulnerability Scan showing integration with current vulnerability databases and threat intelligence for container security — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 221. Does a concept exist for dealing with vulnerabilities that describes both the technical and organizational measures, particularly with regard to: - Regular identification of vulnerabilities - Documentation and assessment of vulnerabilities - Definition and implementation of prioritized measures to eliminate vulnerabilities - Reporting including trends
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "What are your remediation timelines?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 222. Does an asset inventory exist that shows the respective status of assets (active, inactive, planned, etc.)? Please provide evidence of the asset inventory.
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you have an asset management program and data classification?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 223. Does it ensure 24/7 that events are analyzed and tracked in a timely manner?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 224. Does PTC have an option to deny patches on our instance?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- PTC Specific N/A (If this checkbox is selected, skip this section.) Question | Yes | No | Notes — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 225. Does solution make use of interfaces other than secure web browsing. Like API's, EDI, IoT, File shares, Mail, FTP, etc?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What is needed on the client side?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒HTTPS ☒API ☒Browser — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 226. Does solution provide SSO integration with IFF via SAML 2.0 or OIDC?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you support single sign-on (SSO)?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Note: To be used to integrate the solution with IFF MFA authentication through MS Entra ID ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 227. Does solution support mobile platforms?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What are the platform requirements for local deployment?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No If Yes, provide details Web UI works in mobile browsers; no dedicated native mobile app. 2.23 Does solution require a special setting, web browser add-on, additional software, or devices on IFFs infrastructure. ☒ No If Yes, provide details — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 228. Does the application have Virtualization constraints?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Is there a limit on input size (molecules)?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No / comment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 229. Does the application require web usage reporting?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What is needed on the client side?" (similarity 0.59)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 230. Does the application support role-based access?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are unnecessary services disabled?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 231. Does the application use a content accelerators / caching component?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment Redis caching (optional CDN). — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 232. Does the change control system require impact assessment, risk analysis, and authorization?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do you have a change management policy?" (similarity 0.69)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 233. Does the CSP ensure that the logging data created allows unique identification of user accesses at tenant level to support (forensic) analysis in the event of a security incident?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Are systems configured for forensic investigation?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 234. Does the CSP have a documented complaint management procedure?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you have an incident response plan?" (similarity 0.59)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 235. Does the CSP operate a target group-oriented awareness and training program which all its internal and external employees undergo on a regular basis?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Is security awareness training required?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 236. Does the CSP provide interfaces to the Siegfried AG SOC for logging data?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Does your cloud hosting provider provide independent audit reports (SOC)?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- No Audit-log export is available (7-day default, up to 30-day) for customer review on request. A direct real-time SIEM/SOC log feed to Siegfried is not currently provided but can be evaluated case-by-case. — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 237. Does the development standard ensure possible transfer of the application to another platform?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you follow secure development standards?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS is built with platform portability: Uses containerized architecture (Kubernetes-based) which enables platform independence Supports deployment in multiple environments: AWS cloud services Local deployment on customer infrastructure Multiple Linux distributions (Rocky Linux, Debian, CentOS, Ubuntu) Database portability: Uses PostgreSQL which is platform-independent Docker containers: Ensures consistent deployment across platforms Configuration-driven deployment enables adaptation to different platforms To transfer ChemAIRS to another platform, the following requirements must be fulfilled: x86_64 architecture with at least one NVIDIA GPU server; supported Linux distributions (Rocky Linux 8.9-9.3, Debian 11-12, CentOS 7.9, or Ubuntu 18.04-22.04) with kernel ≥3.10.x; Kubernetes orchestration (RKE2 or cloud-managed services like AWS EKS/Google GKE/Azure AKS) with containerd engine; PostgreSQL 14.0+ supporting 512 concurrent connections (self-hosted or cloud service); persistent storage supporting Kubernetes PV/PVC with RWX permissions (NFS/Local storage for on-premises, or AWS EFS/Google Cloud Storage/Azure Disk for cloud); Redis and RabbitMQ middleware with proper authentication configured; network infrastructure with static IP, DNS, and appropriate firewall configurations; NVIDIA GPU drivers, Container Toolkit, and CUDA runtime for GPU functionality; and access to ChemAIRS deployment configuration files and container registry credentials. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 238. Does the organization facilitate the implementation of endpoint security controls?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you have antivirus / endpoint protection?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, the organization implements endpoint security controls on employee computers: Audit software installed: All company employee computers have audit software installed Operation tracking: The audit software enables tracking and auditing of operations performed on endpoint devices Traceability: Operations can be traced and audited retrospectively for security and compliance purposes 《Information Security Management Policy Handbook》ISMS-2-CL-006, ISMS-2-CL-011 and ISMS-2-CL-001 《User Endpoint Policy Enforcement Overview》 — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 239. Does the organization restrict the connection of personally-owned, mobile devices to organizational systems and networks?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How are mobile devices managed?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, the organization implements strict network segmentation to restrict personally-owned devices. Personal devices are segregated from organizational systems and networks through this VLAN separation, preventing access to internal company resources. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 240. Does the software support secure authentication methods and protocols (LDAPS, SAML, OAuth)?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you support single sign-on (SSO)?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS supports multiple secure authentication methods: SSO (Single Sign-On): Integrated SSO support, Azure AD fully tested OAuth: Supports OAuth 2.0 (Others that satisfy OAuth 2.0 are also supported) SAML: Supported through Azure AD integration LDAP: Supported as integrated SSO authentication Password authentication with security policies (complexity, expiry) MFA (Multi-Factor Authentication): In development (like Google Authenticator) API authentication: Supports Token or API Key methods, Bearer token in API call scenarios — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 241. Does the system provide for a secured, date/time stamped audit trail (event log) to track all changes and can it be printed/exported in a readable format?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How are audit logs stored and reviewed?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- If a COTS is used, how do you customize it? Do you use VBA (Visual Basic for Applications), macros, etc. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 242. Does the validation cover the life cycle of the system?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Are environmental protection systems subject to periodic tests and maintenance? How often?" (similarity 0.57)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 243. Does the vendor provide redundancy and load balancing for firewalls, intrusion prevention and other critical security elements?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do you have in place infrastructure redundancy measures, such as: disk mirroring, RAID, internet redundancy connections, failover telecommunications systems, etc.?" (similarity 0.70)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 244. Does your company provide a public website to view outages (current & historical)?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How will customers be notified of a disaster or outage?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No / comment 3.20 Are upgrades included in the subscription fees Yes 3.21 How and how often upgrades are conducted Periodic major releases (twice per year); onsite/remote/self-service — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 245. Does your organization manage user access rights based on a need-to-know basis?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Who is responsible for access management?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 246. Does your OT solution comply with applicable industry standards for securing industrial control systems?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you follow secure development standards?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 247. Does your solution need to connect to IFF Applications (example SAP)?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Does Chemical.AI access customer data in a local deployment?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No / comment 1.1.6 Required Environments ☒Production ☒Quality Assurance ☒Development — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 248. Explain the on-boarding process for new customer’s and how you go about learning their environment Explain the level of documentation?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What does implementation look like?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Environment prep → deployment → validation/acceptance Documentation: installation/deployment specs, user manuals, technical architecture, and O&M plans. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 249. Explain which and how roles and responsibilities will be defined and implemented for the new solution.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the product / software / service and its purpose." (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Role-based access control (e.g., researcher, project manager, administrator), defined at deployment and enforced in-app. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 250. For external software developer, is there a contractual relationship that defines obligations especially regading secure software development standards?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you follow secure development standards?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- No external software developers are used. ChemAIRS develops all software in-house with their own development team. OTHERS — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 251. For what purposes is the personal data being processed?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What personal data (PII) do you collect?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Only for SaaS, account creation and authentication — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 252. Given the considerable number of chemists interested in the evaluation, what is the maximum number of accounts that can be generated for the trial?
**Importance:** 1 customer (Merck) · asked 1 time  
**Closest bank entry:** "Do you offer trials?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- We understand the importance of individual user experiences during the trial and are prepared to accommodate as many users as necessary. While ensuring that the number of accounts remains within reasonable bounds, we strictly enforce single-device login policies to maintain data integrity and security, automatically logging out previous sessions upon new logins to prevent account sharing. — *Merck* (`Merck Chemical.ai evaluation filled.pdf`)
*First seen in:* `Merck Chemical.ai evaluation filled.pdf`

### 253. Has management approved a policy for remote access to scoped systems and data communicated to constituents?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How is remote access to your network secured?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. For remote access: Connection sources to dedicated servers are strictly restricted, allowing only specific devices All remote connections must be used in conjunction with access authorization For SaaS: AWS security group controls (also used in ELB) The system can restrict access to client IPs via AWS security group SSO integration supported (Azure AD fully tested) MFA is in development 《Information Security Management Policy Handbook》ISMS-2-CL-012 (sections 5.7-5.8) — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 254. Has management approved an access control policy, communicated it to constituents, appointed an owner to maintain it, and reviewed it?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Who is responsible for access management?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS has implemented: User tenant and RBAC (Role-Based Access Control) Account management policies Password policies Access log auditing Access rights can be set per user and per administrator — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 255. Has management approved and communicated a Cybersecurity Incident Management Program with a designated owner to maintain and review it?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you have a documented information security program and policy approved by management?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS has established a professional incident response team is set up to monitor and alert the main recipients and observers of information, responsible for monitoring, identifying and responding to security threats. Team members include security experts, operations and maintenance personnel, and development leaders. Clearly formulated emergency response process, including steps such as incident categorization, initial assessment, threat isolation and impact mitigation. Analysis and improvement will also be carried out afterwards to thoroughly investigate security incidents, analyze the causes, and optimize existing security policies and response plans. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 256. Has management approved, communicated, and enforced a password policy for systems that transmit, process, or store scoped data on all platforms and network devices including specific length and complexity requirements and require keeping passwords confidential?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How are mobile devices managed?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. The password policy includes: Minimum length: 8 characters Complexity: Must include at least 3 of the following 4 types: English uppercase letters English lowercase letters Numbers Special characters Prohibited passwords: User account names, user email addresses, common simple passwords, or historical passwords are banned Storage: Passwords stored in hashed and salted format 《Information Security Management Policy Handbook》ISMS-2-CL-001, ISMS-2-CL-007 (Doc) — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 257. Have all individuals in the project responsible for PI data, completed appropriate training on the proper handling, storing, and reporting of potential incidents relating to such data?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Is security awareness training required?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes All employees undergo two mandatory security training every year to ensure they understand and comply with information security policies. Bi-annual awareness training, technical skills training, and emergency drills are conducted. — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 258. Have all relevant activities and responsibilities been covered in a quality agreement?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How is quality managed?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 259. Have all relevant activities and responsibilities been covered in a service level agreement?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 260. Have all relevant regulato-ry and legal requirements, in particular with regard to data protection (e.g. DSG in Switzerland, GDPR in Europe), been implement-ed both at an organiza-tional and technical level? e.g. EU Cloud code of Conduct
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you comply with GDPR? Which privacy laws apply?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 261. Have formal procedures for business continuity been developed and documented?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Describe your disaster recovery and business continuity plans." (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS runs in high availability SaaS services with multi-copy instances in different availability zones to guarantee fast recovery and switching in case of disaster. If the cloud provider's high availability service fails, their application and data separation with distributed containerized architecture can be quickly recovered in a newly built cluster. We have documented notification procedures for disaster events. (Note: we can use this doc ChemAIRS SaaS Environment Data Security Management Regulations ) Endpoint Security — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 262. Have you been inspected by any regulatory authorities, such as, FDA, EMEA or successor type, etc. within the past 3 years?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Which standards-based certifications do you hold?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- If yes, provide date(s) of last inspection and agency and audit reports. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 263. Have you completed a controls audit or certification?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are you audited by an independent external party?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ISO 27001 certification Note: If the SOC2 report or the ISO 27001 certification is available to share, please attach it to this questionnaire. — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 264. Have you set specific quality goals? If so, how are they specified and tracked internally? Do you use internal quality standards? What processes are covered by these standards?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How is quality managed?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, Chemical.AI has established specific quality goals and tracking mechanisms: Quality Metrics Tracked: New vulnerabilities: 0 (SonarQube dashboard) Security Hotspots: 0 Quality Gate: PASSED status Code coverage, reliability, and maintainability ratings Performance metrics including incident response times and vulnerability remediation rates Internal Quality Standards Cover: Document Control (ZHKJ-QESP-01) Risk Management (ZHKJ-QESP-15) Data Analysis and KPI measurement (ZHKJ-QESP-13, ZHKJ-QESP-22) Continuous Improvement (ZHKJ-QESP-14) Customer Satisfaction Measurement (ZHKJ-QESP-10) 《Quality Management System Procedures Compilation》 《Development Security Pipeline》(Screenshots) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 265. How are components of an application release identified and tracked?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How are releases delivered?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Systematic release tracking through automated pipeline and audit logging Release Component Tracking: GitLab CI/CD pipeline tracks all release components Container images built and versioned for each release Trivy scanning performed on all release images Admin audit log records all release activities with full traceability Release Management Process: Code artifacts built as container images Pre-release deployment in test clusters Harbor repository management for container versioning Quality management team validation before production release 《Development Security Pipeline》GitLab CI Pipeline 《ChemAIRS Admin Audit Log》(Screenshots) 《Container Vulnerability Management》(Screenshots) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 266. How are customer complaints handled?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Systematic customer complaint handling with comprehensive tracking and resolution procedures Customer Complaint Handling Process: Customer Communication Control Procedure (ZHKJ-QESP-05) - Defines processes for handling customer inquiries, feedback, and complaints Customer Satisfaction Measurement Control Procedure (ZHKJ-QESP-10) - Customer feedback collection, analysis, and reporting processes Customer surveys, complaint analysis, and satisfaction metrics tracking Trending analysis and improvement action planning based on complaints Systematic approach to understanding customer perceptions and resolving issues 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-05, ZHKJ-QESP-10 — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 267. How are projects managed (definition of activity, processes, documentation, responsibilities)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How is quality managed?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Provide quality and project plan templates if not attached to the business proposal. Systematic project management through multiple control procedures Project Management Elements: Process planning, resource allocation, and workflow management Design input requirements, review stages, and verification activities Project planning, implementation, and monitoring with defined metrics Stakeholder communication and expectation management Document identification, version control, and approval processes 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-06, ZHKJ-QESP-08, ZHKJ-QESP-14, ZHKJ-QESP-16 — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 268. How are software and data configured mapped to the service and system configuration?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Where is data hosted and stored?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Version-controlled (GitLab) with configuration records. Deployment and infrastructure are defined as code via Helm and Terraform. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 269. How are software components managed (identification, version, author)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How are mobile devices managed?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Comprehensive software component management through version control and documentation Component Management System: GitLab CI/CD pipeline with version tracking Document identification and version control procedures Container image management with Harbor repository Admin audit log capturing all component changes with timestamps and user identification Version Control Features: Systematic document creation, approval, distribution, and maintenance Version control with obsolete document management Master lists and distribution records for all controlled documents Container images tagged and tracked through CI/CD pipeline 《Development Security Pipeline》GitLab CI Pipeline 《ChemAIRS Admin Audit Log》(Screenshots) 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-01 Document Control Procedure — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 270. How are staff trained (general training, training in best practices, quality, safety, traceability, review)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Is security awareness training required?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Comprehensive training program with multiple components: Training Management (ZHKJ-QESP-29): Systematic approach for training planning, delivery, and evaluation Competency-based training programs and certification requirements Training record maintenance and competency verification Orientation, technical skills, safety training, and ongoing professional development Specific Training Areas: Security Awareness: Bi-annual mandatory training for all employees Technical Skills: Specialized training for key positions Emergency Preparedness: Emergency drills and response training Quality Training: Regular security bulletins and best practices Training Effectiveness: Evaluation and continuous improvement 《ChemAIRS SaaS Environment Data Security Management Regulations》(Doc) Section VI Section 19 (Training and Education) 《Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-29 (Training Management Control Procedure) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 271. How are the software and documents related to the delivered version archived?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How are releases delivered?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Comprehensive archiving system through document control and record management procedures Software and Document Archiving Components: Document Control Procedure (ZHKJ-QESP-01) - Systematic approach for document creation, approval, distribution, and maintenance Record Control Procedure (ZHKJ-QESP-02) - Creation, identification, storage, and retention of quality records GitLab CI/CD pipeline maintaining version history and build artifacts Harbor repository for container image archiving with versioning Admin audit log providing downloadable records with full traceability 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) 《ChemAIRS Admin Audit Log》(Screenshots) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 272. How are upgrades to the application and or hardware delivered?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are releases delivered?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Container-image based; delivered onsite, remotely, or self-service. Major releases twice per year. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 273. How are your activities documented?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you have a documented risk assessment process?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Please provide examples. Comprehensive documentation system with multiple levels: Examples of Documentation: Vulnerability Reports: Daily vulnerability reports reviewed by code security team Audit Logs: All testing and deployment activities logged and retained for auditing Code Analysis Reports: Static code analysis with SonarQube (27,694 lines analyzed) Test Reports: ChemAIRS System Test Report (Version 3.5.0) with 44 major functional tests, 100% pass rate Penetration Test Reports: Annual third-party assessment (ZWAY-PET-202508-01) Quality Records: Document control with version management, retention schedules, and master lists 《ChemAIRS-backend Code Analysis Report》 《ChemAIRS Penetration Test Report》 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-01 (Document Control Procedure), ZHKJ-QESP-02 (Record Control Procedure) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 274. How are your products designed and configured to comply with pharmaceutical agency regulatory requirements for electronic registrations and signatures?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Does ChemAIRS support multi-factor authentication (MFA)?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Pharmaceutical regulatory compliance through comprehensive governance and validation frameworks Regulatory Compliance Framework: ISO 27001:2022 certification covering pharmaceutical industry standards GDPR-compliant data processing agreement template Comprehensive audit trail with electronic signature capabilities Data sovereignty and complete customer control options Electronic Records and Signatures Support: Admin audit log with complete traceability (username, timestamp, operation type) Document control procedures ensuring regulatory compliance Legal and regulatory identification and update control procedures Compliance evaluation control procedures with systematic monitoring Pharmaceutical-Specific Features: Local deployment option providing complete customer control Data Processing Agreement addressing pharmaceutical data protection requirements Risk assessment methodology aligned with pharmaceutical industry standards Quality management procedures designed for regulatory environments Project Delivery / Completion — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 275. How can users outside the native delivery environment access your applications and data?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Does Chemical.AI access customer data in a local deployment?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Browser over HTTPS with SSO; access controllable by IP/VPN via IFF's AWS security groups. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 276. How do you address ethical concerns related to the use of OT systems in critical industries?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have an asset management program and data classification?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 277. How do you address issues related to bias in AI algorithms and data sets?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are AI results made transparent and governed?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Models are trained on curated public and licensed reaction corpora in the chemistry domain (not personal/social data); outputs are validated by chemists. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 278. How do you control access to visitors?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Is there a formal procedure for visitor access to the data centre?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒Visitor Identification badge ☒Escorted at all times ☒Logged in and out times 5.3 - Is your facility wired directly to ☒Other Not applicable for local deployment. But for SaaS, production is hosted in AWS data centers / professional IDC facilities with their own monitoring and fire/security systems; the corporate office relies on building-level security and monitoring. Section 6 - Communications and Operations Management 16 Questions — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 279. How do you handle updates and patches for AI models to address security vulnerabilities?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Versioned model releases under change control, delivered via container images. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 280. How do you monitor and analyze the outputs of generative AI systems to ensure they comply with ethical guidelines and do not generate harmful or inappropriate content?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are AI results made transparent and governed?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Output monitoring Not applicable in the generative sense — outputs are advisory synthetic routes reviewed by chemists, not free-form generated content. 9.3 Anticipating Attacks and Threat Intelligence: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 281. How do you protect critical systems to ensure their availability?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you manage software supply chain risk?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒High-Availability ☒Redundant locations ☒Offsite backup storage — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 282. How do you provide communication on Service Standards and results?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Reports, periodic reviews, and email notifications. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 283. How does the company ensure that secure data deletion mechanisms, such as data sanitization and/or physical destruction, are implemented upon testing?
**Importance:** 1 customer (Merck) · asked 1 time  
**Closest bank entry:** "Can data be deleted without Chemical.AI viewing it?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Merck Chemical.ai evaluation filled.pdf`

### 284. How does the document workflow (writing, review, approval) work?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Who reviews code and how?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Structured document workflow with multiple approval levels: Document Control Process (ZHKJ-QESP-01): Systematic approach for document creation, approval, distribution, and maintenance Document identification and version control Obsolete document management Master lists and distribution records Code Review Workflow: Dual approval requirement: Development lead AND Data security lead review Only current, approved documents used throughout organization External documents control (standards, regulations, customer specifications) Configuration changes require internal modification approval process 《ChemAIRS-backend Code Analysis Report》 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-01 (Document Control Procedure) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 285. How does your AI solution integrate with our existing security infrastructure?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Is there an early warning system in place?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- SSO/Entra ID, audit logs exportable to IFF's SIEM, and AWS-native controls. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 286. How does your OT solution integrate with our existing IT and OT security infrastructure?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Who are the supplier IT & security contacts?" (similarity 0.59)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 287. How frequently do you release updates, and how are they delivered?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Periodic releases (two major releases per year); onsite, remote, or self-service. 10.0 OT (Operational Technology) Questions Relevant for OT solutions (factory and R&D solutions). OT Solutions Only 10.1 Monitoring of Input and Outputs: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 288. How geographically distributed is the user base?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Is there a limit on input size (molecules)?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- IFF to define — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 289. How is it ensured that the asset inventory is maintained up to date?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have an asset management program and data classification?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Maintained by the internal information security team as part of the ISO 27001 ISMS. 3.3 - Please state the Data Classification level that IFF information will have to ensure an appropriate level of protection: ☒Confidential — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 290. How is the planning and monitoring of the project carried out (tools, reports)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- Comprehensive monitoring and reporting framework Planning and Monitoring Tools: GitLab CI/CD pipeline for development workflow tracking SonarQube for code quality monitoring and reporting AWS CloudWatch for infrastructure monitoring Risk Assessment Worksheet and Asset Inventory Template Quarterly reports to internal stakeholders Annual comprehensive reviews for customers 《ChemAIRS Information Security Risk Assessment Methodology》(Doc) 《Development Security Pipeline》 Software Development — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 291. How is this and other applications launched from the user device?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are mobile devices managed?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- Via browser URL with SSO. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 292. How is your help desk reached?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.57)
**Past answers (from archive – unreviewed, may be outdated):**
- Via email and a dedicated business-manager contact. 3.14 Process for handling escalations Tiered: support → DevOps/development leaders → management. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 293. How long has your quality management guideline been in place?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How is quality managed?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Current ISO 27001:2022 certification was issued on December 16, 2024, with previous certifications showing ongoing quality management since at least 2022. — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 294. How much in advance PTC will be notified for patch releases?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Typically two weeks in advance. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 295. How often are operational controls independently audited by either your internal or external auditors?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are you audited by an independent external party?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒Annually — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 296. How often are restore procedures tested?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are recovery tests carried out in the DPC? How often are those drills performed? And are documented?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment Quarterly. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 297. How often do you perform BCP Table-Top Exercises?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are recovery tests carried out in the DPC? How often are those drills performed? And are documented?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒Annually — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 298. How often do you perform DR testing of critical applications and systems?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are environmental protection systems subject to periodic tests and maintenance? How often?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒Quarterly — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 299. How often do you provide software increments / new releases?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Monthly. Applications are built as container images whose patches are typically updated automatically with each version release, usually at a frequency of once a month — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 300. How often would you like Backup retention?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What is your data retention policy?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Not Applicable Please Comment if Not Applicable — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 301. How often would you like to refresh your DB data?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What is your data retention policy?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Not Applicable — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 302. How often, and by whom (what group) is the list of authorized users verified that the same list of people continues to require access to any of the resources previously applied for?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How often are access rights reviewed?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable for local deployment. For SaaS, privileged accounts reviewed quarterly; regular users semi-annually. Reviews performed by the Data Security Administrator (and tenant administrators for customer accounts). Section 7 - Systems Acquisition, Development & Maintenance 13 Questions — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 303. How quickly can you respond to and recover from OT security incidents?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable 10.6 OT System Updates and Patch Management: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 304. How will the PI data be stored / processed?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "What personal data (PII) do you collect?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Cloud provider For SaaS, personal information is stored on AWS cloud servers in the United States. For local deployments, PI data is stored and maintained by the client. — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 305. Identify and describe the role of any third parties that your company plans to employ to implement all or specific parts of the proposed solution.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you use subcontractors or depend on critical third parties?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- None — implemented in-house by Chemical.AI (AWS is IFF's own provider). — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 306. In case of an In-house solution, how are you securing the Servers and Infrastructure from unauthorized access? Are there any special considerations to enter the DC or server room?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is the office network secured?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Hosted in IFF's AWS (AWS physical controls inherited); no Chemical.AI server room in scope. Logical account access controlled by IFF. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 307. In the system description and the contractual agreements, does the CSP provide comprehensible and transparent information on its jurisdiction and the locations where data are processed or stored?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How are customers notified of a change in data storage location?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 308. In which countries are servers that store personal data located?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- For SaaS, United States — AWS us-west-1 (North California) — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 309. In which countries will the PI be accessible or viewable?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Which components are exposed to the internet?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 310. In which countries will third-party access be granted?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- No applicable — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 311. Is a test checked by a second person?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you undergo independent penetration testing?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Multiple review levels are implemented: Evidence of dual review: Code security team review: Vulnerabilities in the reference chain are identified in daily reports and reviewed by the code security team before being submitted to the code owner for repair Approval process: Only after the repair is complete will the merge-in request be approved Dual approval for changes: Changes can only be made after being reviewed and approved by the development lead AND the data security lead (two separate reviewers) Quality management team: Separate team that performs security vulnerability scans distinct from development team This demonstrates a clear separation of duties with multiple review checkpoints. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 312. Is an established procedure used for the definition, application and conformance control of standardized and secure configurations?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you follow secure baseline configurations (CIS, NIST)?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 313. Is an established process used for planning, risk assessment, testing, approval, and implementation of changes (including major changes such as new releases)?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you have a change management policy?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 314. Is an impact assessment performed and documented for potential loss of GxP data/files due to disaster recovery?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Is there a documented disaster recovery plan at the DPC?" (similarity 0.67)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 315. Is an information security management system (ISMS) operated according to a recognized standard (e.g. ISO/IEC 27001) and does the scope include the organizational units, locations and procedures for providing the cloud service?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you have a documented information security program and policy approved by management?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 316. Is application development performed?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Is development outsourced?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS is actively developed software with continuous updates and improvements. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 317. Is every connection to an external network terminated at a firewall e.g., the Internet, partner networks?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Is there a DMZ?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. The system employs: Advanced hardware firewalls AWS GuardDuty and WAF services Only ports 443 and 80 are allowed (80 redirects to HTTPS) All services except frontend web services are only internally accessible 《Information Security Management Policy Handbook》ISMS-2-CL-012 (section 5.3.4.2) 《AWS Network Security Configuration》 《On-Premises Network Security Infrastructure (Huawei & H3C)》 — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 318. Is High Availability a requirement?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have in place infrastructure redundancy measures, such as: disk mirroring, RAID, internet redundancy connections, failover telecommunications systems, etc.?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 319. Is it ensured that components relevant for Siegfried AG are hardened?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you follow secure baseline configurations (CIS, NIST)?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 320. Is it ensured that internal employees, external service providers and suppliers who have access to the instances and data of Siegfried AG have signed the necessary non-disclosure and confidentiality agreements?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Do you perform background checks and confidentiality agreements?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 321. Is it possible for Siegfried AG to autonomously manage the identities of users on behalf of the tenant?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How are password resets performed?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- No Not fully autonomous in the standard SaaS model. With Azure AD SSO, Siegfried manages authentication/identities in its own IdP, and the ChemAIRS tenant administrator can reset passwords and manage roles/permissions (RBAC) within the tenant. However, user records must be pre-created on the ChemAIRS side — account creation is vendor-assisted on request (no SCIM auto-provisioning) and user removal is request-based ( 1–3 weeks). Automated/self-service provisioning (SCIM) can be evaluated case-by-case. — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 322. Is logging data automatically evaluated to detect events that may lead to the violation of protection goals?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 323. Is MFA enabled for email account access?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Does ChemAIRS support multi-factor authentication (MFA)?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Cloud Computing N/A (If this checkbox is selected, skip this section.) Question | Yes | No | Notes — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 324. Is scoped data backed up and stored offsite?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Where are backups stored?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Daily full backups are performed (7 generations), with data stored in multiple physically isolated availability zones. For SaaS environments, copies of data are dumped into dedicated storage servers. The backup policy ensures safety and reliability of business-critical data. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 325. Is the application configurable by IFF?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Can ChemAIRS be deployed locally?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 326. Is the Application self-hosted or with a third-party provider (e.g. AWS, Azure, etc.)?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Can ChemAIRS be deployed locally?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 327. Is the archiving methodology recorded in a procedure (process, functional control, traceability of the actions implemented)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Are systems configured for forensic investigation?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, archiving methodology is formally documented in multiple procedures with comprehensive traceability Documented Archiving Procedures: Document identification, version control, and obsolete document management Master lists and distribution records for all controlled documents Record legibility, retrievability, and protection requirements with retention periods Electronic and physical record storage systems with disposal procedures Comprehensive administrative audit trail capturing all actions with timestamps 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-01, ZHKJ-QESP-02 — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 328. Is the cloud environment continuously checked for vulnerabilities (e.g. internal audits, regular vulnerability scanning, penetration test, red teaming)? Please provide evidence of the last vulnerability check.
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 329. Is the complete and irrevocable deletion of data or the proper destruction of hardware and data media (including backup media) supported (e.g., through "crypto-shredding")?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Can data be deleted without Chemical.AI viewing it?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 330. Is the project management methodology referenced in a procedure?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you have an incident response plan?" (similarity 0.53)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, project management methodology is referenced in multiple quality management procedures Project Management Components: Design and Development Control Procedure (ZHKJ-QESP-06) - Controls design and development of new products and services Product Realization Control Procedure (ZHKJ-QESP-08) - Controls overall product realization process from planning to delivery Risk Control Procedure (ZHKJ-QESP-15) - Controls improvement project planning, implementation, and monitoring Communication Control Procedure (ZHKJ-QESP-16) - Establishes internal and external communication processes — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 331. Is the system Commercial Off the Shelf COTS? Or Customized COTS? Or an OPEN system?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Are IT assets / hardware in the DPCs (servers, disks, cabling, ports, racks, etc.) inventoried and labelled?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- If YES, select the appropriate check box COTS Customized COTS Open System — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 332. Is the System considered “Part 11 Compliant” as per the requirements of Annex 11 (EU) and/or 21CFR11 (FDA)?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Which standards-based certifications do you hold?" (similarity 0.61)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 333. Is the system periodically evaluated to assure the system remains in a validated state and is compliant?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Are environmental protection systems subject to periodic tests and maintenance? How often?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 334. Is the trial conducted in your production environment or development environment?
**Importance:** 1 customer (Merck) · asked 1 time  
**Closest bank entry:** "How are the production and non-production environments separated?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- For trial phases, we assure you that the environment is strictly production-based. Our development team has no access to proprietary data during this phase. To protect your valuable data, we implement robust security measures like access controls, AES256 encryption, and data anonymization, which are closely monitored to prevent any unauthorized access. 4. — *Merck* (`Merck Chemical.ai evaluation filled.pdf`)
*First seen in:* `Merck Chemical.ai evaluation filled.pdf`

### 335. Is there a 24 X 7 Service Desk available? What is the minimum expected response time for Service requests?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- All requests will be responded within 1 day Security & Disaster Recovery Question | Yes | No | Notes — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 336. Is there a defined training program?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do developers receive secure development training?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Including but not limited to, authentication, electronic signatures, qualification, change control, etc. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 337. Is there a formal change control process and are changes tested in a Development or Testing environment prior to being moved to Production?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do you have a change management policy?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 338. Is there a formal, documented information technology disaster recovery exercise and testing program in place?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Is there a documented disaster recovery plan at the DPC?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Operations such as emergency recovery and system rebuilding for failures are practiced from time to time to ensure the recoverability and availability of backups. The quality management team performs automated recovery tests on backup copies on a regular basis to verify the availability of the recovered system and data integrity. (Note: we can use this doc ChemAIRS SaaS Environment Data Security Management Regulations ) — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 339. Is there a management system in place for archiving and identifying the contents of each release/approved version?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How are releases delivered?" (similarity 0.70)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 340. Is there a monthly review with customers to discuss issues, status and proactive recommendations as well as three moth planning and 6 months planning and adjustments? Is this included as part of your service?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Regular review cadence can be arranged; scope of recurring reviews is a commercial matter — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 341. Is there a process for identifying, maintaining, and reviewing access e.g., periodical review, role changes etc.?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How often are access rights reviewed?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS has: Account management rules that include periodic reviews IDs issued individually with minimum access rights Shared accounts are generally prohibited Each account can only be logged in on one device — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 342. Is there a QMS (Quality Management System) policy in place which includes systems?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How is quality managed?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Customer Service (for cloud/web-based systems) Question | Yes | No | Notes — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 343. Is there a quality structure? What are its roles and responsibilities? How many people?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How is quality managed?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, Chemical.AI has an established quality management structure with defined roles and responsibilities: Assessment Team: CEO/Data Security Administrator (Risk Owner), DevOps Manager and Development Leaders (Technical Assessors), Operations and customer-facing staff (Business Stakeholders), plus External Validation through third-party assessors (annual) Quality Management Team: Dedicated team performing regular security vulnerability scans and testing, separate from development team Code Security Team: Reviews daily vulnerability reports and submits issues to code owners for repair Information Security Team: Data Protection Officer (DPO) and security management team 《ChemAIRS Information Security Risk Assessment Methodology》(Doc) 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 344. Is there a records retention policy and retention schedule covering paper and electronic records, including email in support of applicable regulations, standards, and contractual requirements?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "What is your data retention policy?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS has the following retention policies: Personal information retention: 6 months after termination of the usage agreement Audit log retention: 6 months (default, depends on storage size) System log retention: 60 days Data backup: Daily full backups with 7 generations [Note: remove "partially"] Human Resources Security — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 345. Is there a secure software development lifecycle policy that has been approved by management, communicated to appropriate constituents and an owner to maintain, and review the policy?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you follow secure development standards?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. ChemAIRS has a comprehensive secure SDLC with multiple security controls: SonarQube integrated into CI/CD flow for code review and vulnerability identification Trivy automation tool scans container images for vulnerabilities before release (with the latest real-time CVE vulnerability database) Quality management team performs regular security vulnerability scans Code security team reviews vulnerabilities before submission to code owners Configuration and updates require internal modification approval process Changes only made after being reviewed and approved by development lead and data security lead Annual application security assessments combining tools and manual testing (note: 我们先用ChemAIRS SaaS Environment Data Security Management Regulations试一下) which does not work well 《Chemical.AI Security Development Principles and Coding Standards》 — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 346. Is there a security baseline configuration that is applied to all deployed network and local devices?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Do you follow secure baseline configurations (CIS, NIST)?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 347. Is there a service or SIEM in place?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 348. Is there a specific methodology to regularly review events on scoped systems or systems containing scoped data to uncover potential incidents?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. A monitoring system is deployed to monitor business, system logs, and network traffic in real-time with timely alert notifications. The ChemAIRS team uses Grafana Loki and AWS CloudWatch for real-time monitoring. Intrusion detection and firewalls are deployed at the network and hardware levels to detect abnormal behavior. The company also subscribes to the latest threat intelligence feeds. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 349. Is there a wireless policy or program that has been approved by management, communicated to appropriate constituents and an owner to maintain, and review the policy?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you have a documented information security program and policy approved by management?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable. — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 350. Is there an acceptable use policy for information and associated assets that has been approved by management, communicated to appropriate constituents, and assigned an owner to maintain and periodically review the policy?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you have an acceptable use policy?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- This answer is the same as Question 5 above Yes. The organization has an asset management program: Dedicated information security team: Internal specialized team responsible for daily information security and asset management Clear ownership: Information security team maintains, reviews, and manages asset controls ISO 27001 certification: Requires documented asset management policies, regular reviews, and management approval Scope: Covers employee computers, network devices, servers, databases, applications, and security tools 《Information Security Management Policy Handbook》ISMS-2-CL-004 (Email), ISMS-2-CL-011 (Mobile Devices) (Doc) — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 351. Is there an anti-malware policy or program including a means of protection through the use of electronic transfer, that has been approved by management, communicated to appropriate constituents and has an owner to maintain, and review the policy?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you have a documented information security program and policy approved by management?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- [客户标注 high risk，客户评论 Please provide evidence of anti-malware policy Yes. ChemAIRS has anti-malware protection: Advanced hardware firewalls employed Data security team conducts continuous surveillance for unusual activities AWS GuardDuty used for threat detection AWS WAF for application-level protection Malware scans on data and databases are also performed 《Information Security Management Policy Handbook》ISMS-2-CL-006 《Container Vulnerability Management》 《Application Pod Running with Non-Privileged User (nobody) 》 Cloud Services — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 352. Is there an asset management program approved by management, communicated to constituents and an owner to maintain, review, and manage asset controls?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you have an asset management program and data classification?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. The organization has an asset management program: Dedicated information security team: Internal specialized team responsible for daily information security and asset management Clear ownership: Information security team maintains, reviews, and manages asset controls ISO 27001 certification: Requires documented asset management policies, regular reviews, and management approval Scope: Covers employee computers, network devices, servers, databases, applications, and security tools — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 353. Is there an established procedure for logging and monitoring events on components relevant to Siegfried AG?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 354. Is there an SOP for the physical security of the system?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Are physical access to DPCs monitored with video surveillance system (CCTV), alarms, or security guards?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- If yes, provide detailed documentation. See attached file: Company_Physical_Access_Control_Security_Management_Procedures.pdf — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 355. Is there any front-end layer before the .NET cluster?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- (e.g., a React or Vue app) 1. 3.5.0 前端和后端合成一个镜像 2. Vue 框架来写网页 — *Gilead* (`Gilead_follow_up_email_question.md`)
*First seen in:* `Gilead_follow_up_email_question.md`

### 356. Is there compensation for Failure to meet Service level guarantees?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No / comment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 357. Is there or will there be an approved set of requirements for any design specifically for PTC?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "What is needed on the client side?" (similarity 0.68)
**Past answers:** none found in the archive
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 358. Is this a cloud-based or web-based system as proposed?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Which cloud provider and services do you use?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Cloud Web If this is a cloud-based system, is it a 3rd party system or privately hosted? | 3rd Party Private — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 359. Is this a multi-tenant or single tenant environment?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.59)
**Past answers (from archive – unreviewed, may be outdated):**
- Single-tenant for local and multi-tenant for SaaS. If multi-tenant, what are the controls used to ensure the separation of data and security information between customer applications? | For SaaS, logical tenant isolation via tenant_id and tokens. Training & Personnel Question | Yes | No | Notes — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 360. Is this a SAAS solution?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Can ChemAIRS be deployed locally?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No If Yes, does the vendor provide other offerings like an on-premise solution. 2.15 Does the vendor host the infrastructure themselves or is the data center provided by a third party Please provide details about data center. ☒ No / comment 2.16 Where are the Data Centers located. Please explain where the data centers are located The AWS region chosen by IFF (their AWS account). IFF controls data residency. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 361. Is your all staff used to delivering services to SERVIER subject to contractual obligations of confidentiality which comply with GDPR?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you comply with GDPR? Which privacy laws apply?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes. Please provide copies of relevant confidentiality and data processing clauses used in the agreements with your employees/sub-processors. SI-23_Chemical.AI_Data_Processing_Agreement.pdf — *Servier* (`_Evaluation Risk-Data Privacy Questionnaire.md`)
*First seen in:* `_Evaluation Risk-Data Privacy Questionnaire.md`

### 362. Is your environment segmented (internal, DMZ, external)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Is there a DMZ?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, there is comprehensive network segmentation across cloud and on-prem environments using AWS VPCs with Network ACLs, internal core services on private IPs without external exposure, zone-based firewall policies (Trust/Untrust/DMZ/Local), and VLAN segmentation for office-network isolation. 《AWS Network Security Configuration》(Screenshots) 《On-Premises Network Security Infrastructure (Huawei & H3C)》 《Internal Core Services & Network Segmentation》 — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 363. Is your solution for the Operational Technologies (OT) environment?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What does implementation look like?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 364. List 3rd party software recommended minimum requirements
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What are the platform requirements for local deployment?" (similarity 0.59)
**Past answers (from archive – unreviewed, may be outdated):**
- Kubernetes, PostgreSQL, GPU drivers; per installation spec. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 365. List all third-party organizations (fourth-party to Acadia) that have access to in scope systems/data.
**Importance:** 1 customer (Acadia) · asked 1 time  
**Closest bank entry:** "Do you use subcontractors or depend on critical third parties?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- For SaaS, the sole fourth party is Amazon Web Services (AWS), providing infrastructure services (RDS, EKS, S3 for limited static assets, CloudWatch, GuardDuty, WAF) in us-west-1; AWS provides the hosting layer and does not access application data content. No other subcontractors are used. — *Acadia* (`Cybersecurity Questions.jay.acadia.docx`)
*First seen in:* `Cybersecurity Questions.jay.acadia.docx`

### 366. List any current cybersecurity or privacy certifications, attestations, or independent assessments relevant to the proposed solution (e.g., SOC 2, ISO 27001, HITRUST).
**Importance:** 1 customer (Acadia) · asked 1 time  
**Closest bank entry:** "Do you have a SOC 1 / SOC 2 / SOC 3 report?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Chemical.AI holds ISO/IEC 27001 (information security management) and ISO 9001 (quality management). The SaaS platform runs on AWS, which maintains SOC 1/2/3 and ISO 27001 / 27017 / 27018. Independent assurance is provided through bi-annual external penetration tests and annual application security assessments combining automated and manual testing. — *Acadia* (`Cybersecurity Questions.jay.acadia.docx`)
*First seen in:* `Cybersecurity Questions.jay.acadia.docx`

### 367. OWASP ASVS, OWASP Top 10 etc.) are adhered during the application development process?
**Importance:** 1 customer (Merck) · asked 1 time  
**Closest bank entry:** "Do you follow secure development standards?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes, we adhere to the leading industry practices and secure coding standards during our application development process. Our data security team rigorously conducts standard OWASP scans with each software version release, proactively addressing critical vulnerabilities. We also manage other vulnerabilities based on security assessments, with a detailed strategy for each—immediate repair, scheduling for the next release, or justified non-action for no-impact findings. All actions are meticulously documented for integrity and traceability. 2. — *Merck* (`Merck Chemical.ai evaluation filled.pdf`)
*First seen in:* `Merck Chemical.ai evaluation filled.pdf`

### 368. Provide a description of your proposed solution architecture, including network components and diagrams. Include a description of telecom requirements and how the solution will interface with existing technology.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- ChemAIRS is organized into four logical layers: Access, Middleware, Computing, and Database (Figure 1 and Table 1). Users authenticate through the Auth Platform and submit tasks via the Application. Computational tasks are queued in RabbitMQ and consumed by compute services, with progress and transient workflow state tracked in Redis (Figure 1 and 2). Reference chemistry lookups are performed against the ChemicalInfo database, and final user-visible results are persisted in the business database (chemairs). — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 369. Provide estimates on the volume of data to be transferred to and from the solution. This should include size for current demands and future growth.
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Is there a limit on input size (molecules)?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- IFF to define (usage-dependent). — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 370. Provide specifics on how the provider will use IFF data (including internal analysis)
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Is customer data used to train models?" (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- None — Chemical.AI does not access or use IFF data, and IFF data is never used to train models — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 371. The application receives data from which Sources?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- User-input structures, building-block/chemical-info databases (locally deployed), and optional ELN/import. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 372. The application will feed data to which Targets?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Reports/exports 7.7 The application has job scheduling requirements and will utilize Job Scheduler Name Asynchronous task queue (RabbitMQ); batch jobs for bulk operations. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 373. Were any deficiencies discovered during the last audit? Please provide evidence of the action plan to address these deficiencies.
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "How are audit logs stored and reviewed?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- No — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 374. What access control rules or methods are in use to ensure that access is only granted to users with a legitimate need to access files and data?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are unique IDs required? Are shared accounts allowed?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- RBAC least-privilege; non-administrative database roles are read-only; encrypted storage; access audit-logged. 4.11 Third Party Management and Access Physical and Environmental Security — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 375. What access controls are to be implemented on the network level? Are there policies that relate usage from specific machines or locations?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is remote access to your network secured?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- AWS security groups and VPC segmentation; IP restriction; only ports 80/443 (80→443 redirect). — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 376. What are the considerations around using the application from off IFF internal network?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Can ChemAIRS be deployed locally?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- Access via HTTPS + SSO; restrictable by IP/VPN through IFF's AWS security groups. 3.27 Physical or logical access to systems by suppliers for support should be monitored and changes authorized using the change management process. Protection of system test data and access to program source code security control. Is this system managed by a third party if so who and how do we contact them. How do they access the system and who in IFF do they report to. Chemical.AI support access is IFF-authorised, time-limited and logged, with no standing access; coordinated with IFF IT. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 377. What are the incentives and penalties for service level violations?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- The software will be deployed within PTC’s local environment and will subsequently be operated and maintained by PTC. Upon completion of service deployment, PTC will conduct and sign off on a final quality control and acceptance evaluation. Service level violation terms, including incentives, service credits, or other remedies, should be negotiated and formally defined as part of the contract or service agreement. These remedies would apply specifically to uptime or performance SLA breaches that are within the scope of the software provider’s control and maintenance responsibilities. SLA penalties would not apply to incidents resulting from PTC-managed infrastructure issues, local configuration changes, or other factors outside of the software provider’s operational control. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 378. What are the peak and non-peak performance periods?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- IFF to define. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 379. What are the specific AI capabilities offered by your solution?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How does ChemAIRS use AI?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Retrosynthetic analysis engine (ML reaction-template extraction + neural ranking) generating scored synthetic routes; forward-synthesis prediction and synthesizability (SA) scoring; impurity prediction; process-chemistry module (cost/solvent/scale-up); Bayesian optimization of reaction conditions. — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 380. What are the specific production OT capabilities offered by your organization?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How are the production and non-production environments separated?" (similarity 0.62)
**Past answers:** none found in the archive
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 381. What authentication services do you support?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Does ChemAIRS support multi-factor authentication (MFA)?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Azure AD/Entra ID (SAML 2.0 / OAuth 2.0 / OIDC), LDAP, local password auth, and API token/key. 4.8 Privileged Access Requirements — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 382. What business areas are represented in your Information Security Incident Response Team?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have an incident response plan?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒IT — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 383. What computing resources are needed to provide system service to users inside the enterprise? Outside the enterprise and using enterprise computing assets? Outside the enterprise and using their own assets?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What are the platform requirements for local deployment?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Kubernetes cluster plus GPU node(s) and PostgreSQL in IFF's AWS; exact sizing depends on user count/workload, and joint scoping with Jay. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 384. What external dependencies does this application have? What impact would an external outage have on the functions of the application?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How will customers be notified of a disaster or outage?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- What depends on this system and how would an outage of this application impact on other systems. Depends on AWS (IFF's account) and Entra ID for SSO; otherwise isolated from IFF's other systems. 6.0 Network Security — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 385. What interfaces are available to start and stop the application. What documentation is available to operators to check the status of the application? Are there any checks or dependencies that need to be considered before the application can be started or stopped?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What is needed on the client side?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- Standard Kubernetes/container controls; O&M documentation; health checks; documented dependencies (database, queue). 8.0 Client — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 386. What is Primary and Secondary Data center location?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Where is data hosted and stored?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable for local deployment — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 387. What is the expected storage growth rate over the next year?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Is there a limit on input size (molecules)?" (similarity 0.58)
**Past answers (from archive – unreviewed, may be outdated):**
- IFF to define. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 388. What is the guaranteed performance response time? Can this be audited?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- Within 1day. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 389. What is the method of delivery of a product (methodology, control, documentation to be given to the customer for the delivery of qualified components in a qualified environment, proof of adequate functional tests)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Describe the product / software / service and its purpose." (similarity 0.68)
**Past answers (from archive – unreviewed, may be outdated):**
- Systematic product delivery methodology with comprehensive documentation and testing validation Product Delivery Methodology: Product Realization Control Procedure (ZHKJ-QESP-08) - Controls overall product realization process from planning to delivery Production and Service Control Procedure (ZHKJ-QESP-09) - Controls production operations and service delivery processes Customer Communication Control Procedure (ZHKJ-QESP-05) - Manages contract review, order processing, and delivery coordination Quality and Testing Documentation: Pre-release environments deployed in test clusters replicating production settings Comprehensive functional testing with documented test results and validation Container vulnerability scanning and security validation before release 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-05, ZHKJ-QESP-08, ZHKJ-QESP-09 《Container Vulnerability Management》(Screenshots) Support / Maintenance — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 390. What is the process for handling anomalies and customer requests (identification, traceability, resolution, delivery)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Comprehensive anomaly and customer request handling process with systematic identification and resolution Anomaly and Request Handling Process: Customer Communication Control Procedure (ZHKJ-QESP-05) - Systematic approach for customer interaction and handling inquiries, feedback, and complaints Nonconforming Product Control Procedure (ZHKJ-QESP-12) - Controls identification, segregation, and disposition of nonconforming products Vulnerability management process with daily reports reviewed by code security team Traceability and Resolution: All ChemAIRS application level vulnerabilities notified to administrators via email Hotfix and new releases provided by administrators via email Complete audit trail with username, timestamp, operation type, and resolution tracking 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) ZHKJ-QESP-05, ZHKJ-QESP-12 — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 391. What is the scheduled release cycle?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How are releases delivered?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Historically, twice per year (Q1 and Q3) for local deployment. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 392. What is the SLA - uptime and availability?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "Are Uninterruptible Power Supply (UPS) and electric generators systems in place? How long can they operate?" (similarity 0.57)
**Past answers (from archive – unreviewed, may be outdated):**
- (should be better than 99.95%) Local: uptime is fully dependent on the customer's own infrastructure and is not applicable to Chemical.AI's SLA. — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 393. What is the strategic importance of this system to other user communities inside or outside the enterprise?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Can ChemAIRS be deployed locally?" (similarity 0.56)
**Past answers (from archive – unreviewed, may be outdated):**
- IFF to define — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 394. What is the typical length of requests that are transactional?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Interactive queries in seconds; complex route computation longer. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 395. What is your process for testing and implementing updates without disrupting critical operations?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How and how often are systems patched?" (similarity 0.69)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable 10.7 OT Ethics and Safety: — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 396. What is your process when SLAs are not met?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have a SOC 1 / SOC 2 / SOC 3 report?" (similarity 0.56)
**Past answers (from archive – unreviewed, may be outdated):**
- Per contract — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 397. What mechanisms do you have in place to secure databases and application access to the data?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Is an API available and how is it secured?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Multiple security mechanisms: Database Security: Access control: Only authorized administrators with proper authorization can access databases Password protection: All databases require strong passwords Encryption: Data encrypted at rest using private encryption algorithm, hashed and salted format Network isolation: Database access restricted to specific IP CIDR ranges Connection security: TLS encryption for database connections Parameterized queries: Prevents SQL injection Minimum privileges: Accounts granted minimum necessary access rights Audit logging: All database access logged and monitored Application Access: RBAC (Role-Based Access Control) Tenant isolation in SaaS environment Authentication required for all access Session management: Auto logout after 30 minutes idle Single device login: Each account can only be logged in on one device VPC isolation: Internal-only private network access Encryption in transit: HTTPS with TLS 1.3/1.2 — *Grunenthal* (`Information_Security_Questions_Summary.md`)
*First seen in:* `Information_Security_Questions_Summary.md`

### 398. What method or guideline do you use for quality management? What is the specific procedure you follow?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "How is quality managed?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Chemical.AI follows multiple quality management frameworks: ISO Standards: ISO 9001 and ISO 27001:2022 certified (valid through December 21, 2027) Quality Management System: 29 documented procedures (ZHKJ-QESP-01 through ZHKJ-QESP-29) covering core quality processes Software Development: Software Security Development Lifecycle (SDL) integrating security into every development phase (requirements, design, coding, testing, maintenance) OWASP Standards: Following OWASP Top 10, OWASP ASVS for secure coding recommendations 《Chemical.AI ISO27001 EXP2027》 《Chemical.AI Security Development Principles and Coding Standards》 《程序文件(汇编) - Quality Management System Procedures Compilation》(Doc) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 399. What methods and technologies do you use for anomaly detection in the OT environment?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 400. What other applications and/or systems require integration with yours?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Describe the application architecture." (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Optional, IFF to define. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 401. What proprietary technology (hardware and software) is needed for this system?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What are the platform requirements for local deployment?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- ChemAIRS containerised software; GPU compute for AI models; PostgreSQL; standard AWS services. No proprietary hardware required. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 402. What provisions do you make in the software to reduce the upgrade risk?
**Importance:** 1 customer (Grunenthal) · asked 1 time  
**Closest bank entry:** "Do you manage software supply chain risk?" (similarity 0.67)
**Past answers:** none found in the archive
*First seen in:* `Information_Security_Questions_Summary.md`

### 403. What resources/components of Chemical.AI are facing public internet and what are in a private network / VPC? Are storage resources / databases facing public internet?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Which components are exposed to the internet?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Only the web frontend is exposed to the public internet—specifically via HTTPS on ports 80/443 (with port 80 redirecting to 443). All backend components operate exclusively inside a private network or VPC. These include: backend microservices, databases, storage resources, RabbitMQ, Redis, and monitoring systems. — *Gilead* (`Gilead_follow_up_email_question.md`)
*First seen in:* `Gilead_follow_up_email_question.md`

### 404. What safety measures are in place to prevent accidents or malfunctions in the OT environment?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Is there an early warning system in place?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Not applicable Full Name: | Full Name: Jay Huang Company: International Flavors & Fragrances Inc. | Company: ChemicalAI Title: | Title: Platform Engineer Signature: | Signature: Jay Huang — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 405. What service level guarantees are offered? (problem severity / types and definitions of severities)?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is support organized? What are the response times?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Chemical.AI classifies issues into four severity levels with corresponding response targets: S1 (Critical) — service down or unusable for all users with no workaround — responded to within 1 business day; S2 (High) — a major function severely impaired or degraded for many users with limited workaround — within 1 business day; S3 (Medium) — a minor function affected with a workaround available and limited user impact — within 1 business days; and S4 (Low) — cosmetic issues, questions, or enhancement requests — addressed in the next release cycle or as scheduled. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 406. What types of management or monitoring reports are available for customers?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do you monitor for security events?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Audit-log exports, monitoring dashboards, fully managed by IFF. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 407. What types of personal information will you be processing?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What personal data (PII) do you collect?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Please list in the comments: Only for SaaS, limited personal data only (Name, email address, company name) — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 408. When accessing your systems, are users required to input a user ID and password?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How do users receive their credentials?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes 6.12 - Who (what group) is responsible for assigning access to internal systems, applications, networks, etc. The DevOps/Operations team via an internal approval workflow, under the Access Control and Privileged Access Management policies. — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 409. When is the solution ready for testing and for a security review to verify this questionnaire?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What is your testing strategy?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Available for security review now (documentation, pen-test report, questionnaires). — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 410. When using Master Data within the Solution’s own schemas. How quickly will this data have to be refreshed? Eg real time, within an hour, overnight etc. Is there the potential for an adverse effect on performance where a data transfer is running between datacenters?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How quickly are incidents reported and customers notified?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- Building-block/chemical-info databases updated per release or import. Refresh cadence: IFF to define. 5.6 Define the owners and groups for the application/system and the generic, administrative and/or system user logins and their functions, if any. Include any third party access requirements. Identify the job position that has ownership and administrative responsibility for the application/system. As 4.9 — IFF-designated owner and tenant administrator. 5.7 Business Requirement for Access Control. Define access control policy RBAC least-privilege; documented access-control policy. 5.8 Can IFF readily export or import its data in one or more well-known and usable industry formats. ☒ Yes / comment — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 411. Which of the following communications channels are monitored (i.e. email, web, USB, etc.)?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Which components are exposed to the internet?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒E-mail ☒Web — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 412. Which of these techniques are used to harden systems?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you follow secure baseline configurations (CIS, NIST)?" (similarity 0.61)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒Disable or rename default admin accounts ☒Change default admin passwords ☒Remove unnecessary services — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 413. Which project documents vary depending on the project concerned (general design, functional specifications, etc.)?
**Importance:** 1 customer (Servier) · asked 1 time  
**Closest bank entry:** "Do you follow secure development standards?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- Give examples. Project documentation varies based on scope and requirements Variable Project Documents: Design input requirements and specifications (project-specific) Risk Assessment Worksheet (tailored to project scope) Asset Inventory Template (project-specific assets) Design output documentation and validation requirements Design history files (maintained per project) — *Servier* (`Servier_information_security_questionnaire (SaaS).md`)
*First seen in:* `Servier_information_security_questionnaire (SaaS).md`

### 414. Which user sessions does the application maintain?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "What session controls are in place?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Authenticated web sessions (token/cookie-based). — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 415. Who within your organization will have access to the personal data and for what purposes?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.74)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Only for SaaS, access is restricted to authorized administrators 2.5 - Please briefly describe your internal privacy program Governed by Personal Information Security Policy, the internal ChemAIRS Privacy Policy, and a GDPR-compatible Data Processing Agreement (Art. 28 terms, Art. 32 measures). Overseen by an internal DPO within the information security team; a Privacy Impact Assessment is completed per engagement; bi-annual privacy/security awareness training for all staff. 2.6 - Please mark which of the following elements of a privacy program are implemented in your organization: ☒Annual privacy training ☒Employee privacy policy ☒Data protection impact assessment ☒Data breach response plan — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

### 416. Will a privacy notice be provided to individuals? (e.g., how the PI will be processed in compliance with data protection principles)?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Describe your privacy program." (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Before or at the time of collection — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 417. Will any third-parties have access to the PI?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- No — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 418. Will any work being performed for IFF be sub-contracted to another firm?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you use subcontractors or depend on critical third parties?" (similarity 0.64)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No 3.4 If yes to previous question, what is your process for verifying their security? — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 419. Will Individuals have access to a structured and commonly used machine readable copy of their PI to request for transfer to another data controller?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.65)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes However, individuals do not have direct self-service access to machine-readable copies of their PI. Users must go through tenant administrators to request data access or changes. — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 420. Will it be stored in a backdoor database (or any other storage media)?
**Importance:** 1 customer (Merck) · asked 1 time  
**Closest bank entry:** "Where are backups stored?" (similarity 0.75)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Upon submission of chemical molecular information, the data flows securely; using HTTPS for transmission to our backend services, where it's immediately encrypted with RSA256 before being stored. We ensure that your data is not replicated, reused, or distributed, ensuring confidentiality from the point of entry to its secure, encrypted storage. 6. — *Merck* (`Merck Chemical.ai evaluation filled.pdf`)
*First seen in:* `Merck Chemical.ai evaluation filled.pdf`

### 421. Will PTC receive the data at the end of the contract for no additional fees?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "What happens to data when the subscription ends?" (similarity 0.73)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- PTC has full control of the data for local deployment — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 422. Will solution send emails?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do you have antivirus / endpoint protection?" (similarity 0.59)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No If yes, describe destination, content, source name, and Domain — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 423. Will storage need to be shared between different components and tiers?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "How is customer data segregated?" (similarity 0.60)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes / comment Shared database/NFS as needed. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 424. Will the application will utilize SAN or cloud storage?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Which cloud provider and services do you use?" (similarity 0.62)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 425. Will the CSP enable Siegfried AG to export data and containers or transfer them to another provider in the event of termination of the contractual relationship?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "What happens to data when the subscription ends?" (similarity 0.66)
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 426. Will the CSP provide comprehensible and transparent information on how it handles investigation requests from government agencies regarding access to or disclosure of Siegfried AG data?
**Importance:** 1 customer (Siegfried) · asked 1 time  
**Closest bank entry:** "Can government authorities access customer data?" (similarity 0.71)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- Yes — *Siegfried* (`Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`)
*First seen in:* `Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx`

### 427. Will the Jazz data/corpora be used to further train or improve the proprietary machine learning models in CHEMAIRS and how can this be verified?
**Importance:** 1 customer (Jazz) · asked 1 time  
**Closest bank entry:** "Is customer data used to train models?" (similarity 0.72)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- No. You do not share any data with us, because Jazz's version of CHEMAIRS is hosted in your own server. We have zero access to your data. — *Jazz* (`Jazz_questionnaires.md`)
*First seen in:* `Jazz_questionnaires.md`

### 428. Will Third Party (non-iff) access be required?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Do third parties have access to personal data? Is data transferred internationally?" (similarity 0.67)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ No 5.0 Data Security 5.1 Define any output artifacts such as reports, files, screen displays, data transfers to database tables, or third party applications, etc. Include comments regarding frequency of output or transfer and any requirements to automate processes, such as overnight batch processing. Synthetic-route reports, SA scores, JSON/CSV/Excel exports, audit-log exports. 5.2 Define requirements for each environment including folder structures, file store locations, database elements ‐ schemas, tables, packages, triggers and sequences, as applicable. PostgreSQL schemas (ChemAIRS main, Auth-Platform, ChemicalInfo, Building-block) and container volumes/NFS. Detailed in the installation spec. — *IFF* (`Solutions Design Assessment (SDA).jay.iff.docx`)
*First seen in:* `Solutions Design Assessment (SDA).jay.iff.docx`

### 429. Will you be copying or accessing an existing set of PI to use in a test environment or for testing purposes?
**Importance:** 1 customer (Gilead) · asked 1 time  
**Closest bank entry:** "What is your testing strategy?" (similarity 0.63)
**Past answers (from archive – unreviewed, may be outdated):**
- No No existing PI sets are copied for testing. — *Gilead* (`Chemical.AI PIA.xlsx`)
*First seen in:* `Chemical.AI PIA.xlsx`

### 430. Will you permit an on-site / remote audit of your systems/ processes? If yes, list any restrictions?
**Importance:** 1 customer (PTC) · asked 1 time  
**Closest bank entry:** "How are audit logs stored and reviewed?" (similarity 0.70)  
⚠️ *Possibly already covered – check the closest bank entry before writing a new one.*
**Past answers (from archive – unreviewed, may be outdated):**
- For local deployments, the client has full autonomous control and can self-audit without restrictions — *PTC* (`Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`)
*First seen in:* `Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx`

### 431. Would you allow our auditing of your data centers, applications, and network infrastructure?
**Importance:** 1 customer (IFF) · asked 1 time  
**Closest bank entry:** "Are physical access to DPCs recorded at the employee entrance / exit and are those access logs reviewed periodically?" (similarity 0.70)
**Past answers (from archive – unreviewed, may be outdated):**
- ☒ Yes Audit rights are available under the DPA for the application/security program, supported by documentation, questionnaires, pen-test reports and certifications. Section 11 - Artificial Intelligence (AI) 8 Questions — *IFF* (`Vendor Risk Assessment (VRA).jay.iff.docx`)
*First seen in:* `Vendor Risk Assessment (VRA).jay.iff.docx`

---

## Extraction summary

| File | Customer | Questions extracted |
|---|---|---|
| Answers to Gilead Email Questions.md | Gilead | 6 |
| Answers_to_Email_Questions_Servier.md | Servier | 8 |
| Chemical.AI PIA.xlsx | Gilead | 15 |
| Cybersecurity Questions.jay.acadia.docx | Acadia | 12 |
| Esteve.md | ESTEVE | 16 |
| FMC - Security Risk Assessment.pdf | FMC | 41 |
| Filled_Vendor Supplier Questionnaire for Computer - Automated Systems.jay.ptc.docx | PTC | 66 |
| Gilead_follow_up_email_question.md | Gilead | 8 |
| Grunenthal_information_security_check.pdf | excluded in sources.yaml | 0 |
| Information_Security_Question_Supporting_Materials.md | excluded in sources.yaml | 0 |
| Information_Security_Questions_Summary.md | Grunenthal | 71 |
| Information_security_questionnaire.pdf | excluded in sources.yaml | 0 |
| Jazz_questionnaires.md | Jazz | 4 |
| Merck Chemical.ai evaluation filled.pdf | Merck | 10 |
| NOVA Cloud Security Risk Assessment Template.pdf | NOVA Chemicals | 41 |
| Selection and qualification of cloud service providers questionnaire.jay.siegfried.xlsx | Siegfried | 58 |
| Servier_information_security_questionnaire (SaaS).md | Servier | 71 |
| Solutions Design Assessment (SDA).jay.iff.docx | IFF | 208 |
| Vendor Risk Assessment (VRA).jay.iff.docx | IFF | 71 |
| _Evaluation Risk-Data Privacy Questionnaire.md | Servier | 20 |
