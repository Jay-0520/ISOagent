# Chemical.AI / ChemAIRS – Information Security Answer Bank

Canonical answers for security questionnaires. One current answer per topic.
Last updated 2026-09-23. Sources, newest first: IFF Vendor Risk Assessment and
Solution Design Assessment (Aug 2026), Servier information security questionnaire,
Servier data privacy evaluation, Servier and Gilead email answers (Dec 2025),
Information_Security_Questions_Summary.md (Grunenthal), NOVA (Feb 2025), FMC,
Information_security_questionnaire, Merck evaluation. When sources disagreed, the
claim was removed here and listed for manual review.

Topics with unresolved conflicts are deliberately left out until confirmed;
see answer_bank_OPEN_DECISIONS.md in the project root.

Each entry ends with two lines:
- **Supporting materials:** evidence from Information_Security_Question_Supporting_Materials.md. Items marked
  "(screenshots)" are screenshot sections of that document and have no link of their own.
- **Sources:** the past questionnaires each answer was taken from (abbreviations as in
  answer_bank_OPEN_DECISIONS.md). Internal – remove before sharing.

Deployment models: answers describe the Chemical.AI-hosted SaaS unless stated.
For local (on-premise or customer-cloud) deployment, the customer hosts and
controls the environment and data; see section 16.

---

## 1. Certifications and assurance

### Which standards-based certifications do you hold?
Chemical.AI holds ISO/IEC 27001:2022 (information security management) and ISO 9001 (quality management). The current ISO 27001:2022 certificate was issued on 16 December 2024 and is valid through 21 December 2027; earlier certifications date back to at least 2022.

**Supporting materials:** [Chemical.AI ISO 27001 Certificate (EXP2027)](https://chemical-ai.feishu.cn/file/VVcfbiipZoFuA6xqgr0c4AfgnOc)

*Sources:* NOVA 1.1; FMC 1.1; Acadia; Servier-Q Q6, Q47, Q48; IFF-VRA 10.4; SuppMat (ISO certificate)

### Do you have a SOC 1 / SOC 2 / SOC 3 report?
Chemical.AI does not currently hold its own SOC 2 report, because most of our clients choose local (on-premise) deployment rather than SaaS. Our ISO/IEC 27001:2022 certification provides independent assurance of our information security management system. We are not currently pursuing additional certifications.

**Supporting materials:** [Chemical.AI ISO 27001 Certificate (EXP2027)](https://chemical-ai.feishu.cn/file/VVcfbiipZoFuA6xqgr0c4AfgnOc)

*Sources:* NOVA 2.2; FMC 2.2; Servier-Q Q7

### Are you audited by an independent external party?
Yes. The ISO 27001 certification body performs an annual external surveillance audit. We also run an annual internal audit under the ISO 27001 and ISO 9001 management systems, and engage external security firms for penetration testing and security assessments.

**Supporting materials:** [Chemical.AI ISO 27001 Certificate (EXP2027)](https://chemical-ai.feishu.cn/file/VVcfbiipZoFuA6xqgr0c4AfgnOc); [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-11 Internal Audit; [ChemAIRS Penetration Test Report (ZWAY-PET-202508-01)](https://chemical-ai.feishu.cn/file/JEtJbPq1EoeqEyx03BcczFSznzd)

*Sources:* Servier-Q Q8; Servier-Priv (internal audits); IFF-VRA 10.5

### Do you undergo independent penetration testing?
Yes. Independent third-party penetration tests are conducted following an OWASP-based methodology. The most recent report (ZWAY-PET-202508-01, August 2025, by Zhiwang Anyun) found 3 vulnerabilities, all fixed, with an overall assessment of "strong security protection measures". A redacted report can be shared on request.

**Supporting materials:** [ChemAIRS Penetration Test Report (ZWAY-PET-202508-01)](https://chemical-ai.feishu.cn/file/JEtJbPq1EoeqEyx03BcczFSznzd)

*Sources:* Servier-Q Q30, Q50; SuppMat (Penetration Test Report)

### Do you have cyber insurance?
Yes. Our business insurance includes network security liability coverage for cyber incidents.

**Supporting materials:** Chemical.AI Business Insurance Coverage 

*Sources:* Servier-Q Q10; IFF-VRA 8.6

### Have you experienced an information security breach?
No.

*Sources:* IFF-VRA 8.7

---

## 2. Governance, policies and risk management

### Do you have a documented information security program and policy approved by management?
Yes. We operate an ISO 27001:2022-certified ISMS. The Information Security Management Policy Handbook includes the Password (ISMS-2-CL-001), Backup (CL-002), Privileged Access Management (CL-003), Email (CL-004), Capacity Management (CL-005), Virus Management (CL-006), Secret Authentication Information (CL-007), Clean Desk and Clear Screen (CL-008), Personal Information Security (CL-010), Mobile Device Management (CL-011) and Access Control (CL-012) policies. Policy areas also include acceptable use, endpoint protection, network and Wi-Fi security, secure development, vulnerability management, data classification, cryptography, change management, clean desk, business continuity, personnel and physical security, third-party risk, remote access, monitoring and audit logging, and data retention. SaaS operations are governed by the ChemAIRS SaaS Environment Data Security Management Regulations.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe); [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz); [Chemical.AI ISO 27001 Certificate (EXP2027)](https://chemical-ai.feishu.cn/file/VVcfbiipZoFuA6xqgr0c4AfgnOc)

*Sources:* Grü Q1; Servier-Q Q11; IFF-VRA 1.1; Servier-Priv; SuppMat (policy handbook contents)

### How often are security policies reviewed and communicated?
Policies are reviewed at least annually under the ISO 27001 management review (top management reviews system effectiveness annually under procedure ZHKJ-QESP-03), and are also updated in response to emerging threats. They are communicated on hire and on every update, and reinforced through mandatory security training twice per year.

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-03 Management Review; [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe)

*Sources:* Grü Q1; IFF-VRA 1.3, 1.4; Servier-Priv

### Do you have an acceptable use policy?
Yes. Employees acknowledge the acceptable use policy on hire and re-affirm it through the mandatory security training cycle.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-004 Email, ISMS-2-CL-011 Mobile Devices; [Employee Information Security Handbook (ZH-IS-201)](https://chemical-ai.feishu.cn/file/GElDbRiKSoNk7jxTBGbcWFBsnVe) – Network Usage Standards

*Sources:* IFF-VRA 1.1, 1.5; Grü-md Q4 (materials list)

### Do you have a documented risk assessment process?
Yes. We use the ChemAIRS Information Security Risk Assessment Methodology: a 5×5 likelihood × impact matrix aligned with ISO 27001:2022 and ISO 27005, under the Risk Control Procedure (ZHKJ-QESP-15). A comprehensive risk assessment is mandatory every year, with additional assessments after major system changes, security incidents or regulatory changes. Risk registers keep historical scores for year-over-year trend analysis.

**Supporting materials:** [ChemAIRS Information Security Risk Assessment Methodology](https://chemical-ai.feishu.cn/docx/EXHKdKe7Jof8DCxBTn6cEZ6gnVg); [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-15 Risk Control

*Sources:* IFF-VRA 3.4; IFF-SDA 3.8; Servier-Q Q46, Q54; Servier-Priv; SuppMat (Risk Methodology)

### Do you have an asset management program and data classification?
Yes. The information security team maintains the asset inventory as part of the ISMS, covering employee computers, network devices, servers, databases, applications and security tools. Asset criticality is scored with the risk methodology above. Customer information is classified as Confidential.

**Supporting materials:** [ChemAIRS Information Security Risk Assessment Methodology](https://chemical-ai.feishu.cn/docx/EXHKdKe7Jof8DCxBTn6cEZ6gnVg) – Asset Inventory Template

*Sources:* Grü Q3; IFF-VRA 3.1–3.4

### Do you have a change management policy?
Yes. All configuration changes and updates require internal modification approval, with dual approval by the development lead and the data security lead, automated security checks, and testing in pre-release clusters that replicate production. Versioned container images allow changes to be rolled back.

**Supporting materials:** [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §12 Operations Management; Development Security Pipeline (GitLab CI, SonarQube) (screenshots)

*Sources:* Grü Q8; Servier-Q Q21; IFF-SDA 3.9

### Do you track security KPIs?
Yes. We track incident response times, vulnerability remediation rates, new vulnerabilities and security hotspots, and quality gate status (SonarQube dashboards, CloudWatch metrics), and report them to management.

**Supporting materials:** Development Security Pipeline (GitLab CI, SonarQube) (screenshots); Runtime Monitoring & Logging Infrastructure (Grafana Loki, CloudWatch) (screenshots); [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-13 Data Analysis

*Sources:* Grü Q1; Servier-Q Q45, Q49

### Do you follow secure baseline configurations (CIS, NIST)?
We do not maintain explicit CIS or NIST baseline documents. Hardening is implemented through ISO 27001 controls, non-privileged container execution, removal of unnecessary services, changing or disabling default admin accounts and passwords, endpoint audit software, and internal secure coding standards.

**Supporting materials:** Kubernetes Security Configuration (screenshots); User Endpoint Policy Enforcement Overview (screenshots); [Chemical.AI Security Development Principles and Coding Standards](https://chemical-ai.feishu.cn/file/YOlrbjrKzoB2F5xiWL7cQOkznJe)

*Sources:* Servier-Q Q31; IFF-VRA 7.12

### Have you adopted Zero Trust principles?
Partially: least privilege and minimum-user policies, continuous monitoring with real-time alerts, strict network segmentation with internal-only access for core services, tenant-isolated RBAC in SaaS, and access to servers through JumpServer.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-012 Access Control; [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §II; On-Premises Network Security Infrastructure (Huawei & H3C) (screenshots); PostgreSQL Role Privilege Configuration (screenshots); JumpServer User Account Management (screenshots)

*Sources:* Servier-Q Q33

---

## 3. People security

### Do you perform background checks and confidentiality agreements?
Yes. All employees are background-checked before employment; consultants are checked the same way. All employees sign a confidentiality agreement on hire.

**Supporting materials:** [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b) – personnel confidentiality undertakings

*Sources:* IFF-VRA 4.1–4.3, 4.5

### Is security awareness training required?
Yes. All employees complete mandatory security awareness training on hire and on a recurring schedule. This covers information security, data privacy, secure data handling and incident reporting, and is complemented by newsletters, advisory messages, and role-specific training for developers and IT. Emergency drills are also run twice a year. Training is managed under the Training Management Control Procedure (ZHKJ-QESP-29), with effectiveness evaluation.

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-29 Training Management, ZHKJ-QESP-04 Human Resources; [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §19 Training and Education; [Employee Information Security Handbook (ZH-IS-201)](https://chemical-ai.feishu.cn/file/GElDbRiKSoNk7jxTBGbcWFBsnVe) – Security Awareness & Training

*Sources:* IFF-VRA 4.4; Servier-Q Q16, Q52; Servier-Priv; SaaS Regulations §19

### Do developers receive secure development training?
Yes. All developers and development managers are required to take secure development training.

*Sources:* IFF-VRA 7.2

### Describe your insider threat program.
- Least privilege: system administrators hold maintenance privileges only and cannot access client data. Access to client data is a one-time privilege requiring a business justification and CEO authorization, and every access is logged.
- Developers have no access to the production environment.
- Individual accounts only; shared accounts are prohibited; single-device login.
- Endpoint auditing: all company computers run endpoint security and audit software that monitors software use, web access, USB and peripheral use, and file transfers. Data loss prevention covers email and web.
- Real-time monitoring, intrusion detection and threat intelligence; a dedicated incident response team.

**Supporting materials:** User Endpoint Policy Enforcement Overview (screenshots); [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-003 Privileged Access Management; ChemAIRS Admin Audit Log (screenshots); JumpServer User Account Management (screenshots)

*Sources:* NOVA 1.2, 3.6; Grü Q24, Q39; IFF-VRA 6.9, 7.4

---

## 4. Physical and environmental security

### How is physical access to offices controlled?
Role-based electronic access cards with default permissions by department. Additional access requires multi-level approval. Sensitive areas (labs, server rooms, executive offices) are segregated, card use is logged, and access is revoked immediately on termination or role change. Visitors wear identification badges, are escorted at all times, and their entry and exit times are logged.

**Supporting materials:** [Company Physical Access Control Security Management Procedures](https://chemical-ai.feishu.cn/file/SnFsbClo3oCH4xxYI3PcveWbngc)

*Sources:* Servier-Q Q42; IFF-VRA 5.1, 5.2

### What are the physical access restrictions to the data center?
The SaaS platform runs in AWS data centers, whose physical security is managed by AWS. ChemAIRS is deployed as an internal-only private network (VPC) cluster, and access to the AWS management platform is limited to authorized personnel. Our own physical servers (development and testing) are hosted in professional IDC (Internet Data Center) facilities.

**Supporting materials:** AWS SOC 1/2/3 and ISO 27001/27017/27018 reports (downloaded from the AWS account)

*Sources:* NOVA 4.2; Grü Q7; IFF-SDA 2.18, 2.20

### How is the office network secured?
VLAN segmentation isolates the office network, and personal devices are segregated so they cannot reach internal resources. Zone-based firewall policies (Trust/Untrust/DMZ/Local) are enforced on H3C SecPath firewalls with an intrusion prevention system.

**Supporting materials:** On-Premises Network Security Infrastructure (Huawei & H3C) (screenshots); Panabit NTM Traffic Monitoring Dashboard (screenshots); Internal Core Services & Network Segmentation (NGINX, DNS, AD) (screenshots)

*Sources:* Grü Q7, Q25; Servier-Q Q26, Q28

---

## 5. Hosting, architecture and data location

### Where is data hosted and stored?
For SaaS, all customer data is hosted in the United States, in the AWS North California region (us-west-1), with instances replicated across multiple availability zones. For local deployment, all data stays in the customer's own infrastructure, so customers who need data localization can choose local deployment.

**Supporting materials:** [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b) – Data Storage; AWS Network Security Configuration (NACL, security groups, ALB) (screenshots)

*Sources:* NOVA 3.4; Grü Q47; Servier-email; IFF-VRA 2.8

### Which cloud provider and services do you use?
AWS: RDS (PostgreSQL, high availability), EKS (Kubernetes), CloudWatch (monitoring), GuardDuty (threat detection), WAF (web application firewall), VPC network ACLs and security groups.

**Supporting materials:** AWS Network Security Configuration (NACL, security groups, ALB) (screenshots); Runtime Monitoring & Logging Infrastructure (Grafana Loki, CloudWatch) (screenshots)

*Sources:* NOVA 4.1; Grü Q47; Acadia; Servier-Q Q36

### Describe the application architecture.
ChemAIRS is a containerized micro-services application on Kubernetes. The .NET Core web cluster serves the web application and REST API and connects to the database (AWS RDS PostgreSQL). Long-running work is queued through RabbitMQ to Java algorithm services and a GPU service, and Redis provides caching. Deployment and infrastructure are defined as code (GitLab, Helm, Terraform).

**Supporting materials:** Kubernetes Security Configuration (screenshots)

*Sources:* Gilead-FU (email as sent); Grü Q59; IFF-SDA 2.12, 7.3, 7.7, 8.15

### Which work is synchronous and which is asynchronous?
Asynchronous (queued via RabbitMQ): retrosynthesis route search, forward synthesis, GPU-accelerated similarity search and deep-learning model inference. Synchronous (direct API response): loading pages, project lists, saved tasks, routes and reports, simple lookups, user and permission queries, and lightweight calculations.

*Sources:* Gilead-FU (email as sent)

### Which components are exposed to the internet?
Only the web front end, over HTTPS on port 443 (port 80 only redirects to 443). All back-end components (micro-services, databases, storage, RabbitMQ, Redis, monitoring) run only inside the private network / VPC.

**Supporting materials:** AWS Network Security Configuration (NACL, security groups, ALB) (screenshots); Kubernetes Security Configuration (screenshots)

*Sources:* Gilead-FU; NOVA 4.10; Grü Q30

### How are the production and non-production environments separated?
DEV, Test and QA environments run on our own physical servers in the data center. Pre-release (staging) environments run in dedicated test clusters in the same AWS availability zone, replicating the production configuration. Production and non-production are separated by firewalls and VLAN segmentation, each environment has its own database instance, and developers have no access to production. Testing uses synthetic data only.

**Supporting materials:** [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §3 Environment Isolation; On-Premises Network Security Infrastructure (Huawei & H3C) (screenshots)

*Sources:* NOVA 4.6; Grü Q29, Q51, Q65; IFF-VRA 6.6, 7.3, 7.4; IFF-SDA 5.27

### Is there a limit on input size (molecules)?
There is no fixed molecule-size limit; the platform supports a wide range of molecular sizes and structural complexity.

**Supporting materials:** none in the Supporting Materials document

*Sources:* Gilead-FU

---

## 6. Data protection and encryption

### How is data encrypted in transit?
HTTPS with TLS is enforced for all traffic. Database connections also use TLS. Port 80 only redirects to HTTPS. SSL certificates are renewed annually.

**Supporting materials:** ChemAIRS Production Domain Certificate Details (screenshots); AWS Network Security Configuration (NACL, security groups, ALB) (screenshots); [Chemical.AI Security Development Principles and Coding Standards](https://chemical-ai.feishu.cn/file/YOlrbjrKzoB2F5xiWL7cQOkznJe) – 2.6 Transmission Security

*Sources:* NOVA 3.3, 4.10; Grü Q57; Servier-Q Q27

### How are encryption keys managed?
In customer-hosted deployments, the customer manages the encryption keys and backup encryption settings. A fully documented, HSM-backed key lifecycle (generation, rotation, revocation) is only partially defined today.

**Supporting materials:** [ChemAIRS Software Local Deployment Data Security Management](https://chemical-ai.feishu.cn/wiki/Dx0XwJoT0iyEASkjsADcpnGbnYd) – §2.2, §3.3

*Sources:* Servier-Q Q27; IFF-SDA 5.23

### What personal data (PII) do you collect?
Only the minimum needed to run the service: name, email address and company name, used for account creation and authentication. ChemAIRS does not process sensitive (special-category) personal data, payment card data, patient or clinical data.

**Supporting materials:** [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b); [Chemical.AI Privacy Policy](https://www.chemical.ai/privacy-policy)

*Sources:* NOVA 3.5; Grü Q39; IFF-VRA 2.2, 10.2; Servier-Priv

### How is customer data segregated?
In SaaS, each customer is a separate tenant with independent storage and access; tenants cannot access each other's data.

**Supporting materials:** [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §4 Multi-tenant Data Management

*Sources:* NOVA 3.7; Grü Q47

### How is Chemical.AI staff access to customer data restricted?
System administrators have maintenance privileges only (system, network, database engines) and cannot access customer data. Access to customer data is a one-time privilege that requires a business justification and CEO authorization. Non-administrative database roles are read-only. All access and operations are logged for audit. Customer data is never shared outside our environment.

**Supporting materials:** PostgreSQL Role Privilege Configuration (screenshots); [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-003 Privileged Access Management; ChemAIRS Admin Audit Log (screenshots)

*Sources:* NOVA 3.6; Grü Q39; IFF-VRA 7.6; IFF-SDA 4.10

### What happens to submitted data?
Data is sent over HTTPS to our back-end services and encrypted before storage. Submitted data is not replicated, reused or distributed.

**Supporting materials:** none in the Supporting Materials document

*Sources:* Merck Q5

### Do you have data loss prevention controls?
Yes. Data loss prevention covers email and web. Endpoint controls monitor USB/peripheral use and file transfers. In-app data export is RBAC-controlled and audited.

**Supporting materials:** User Endpoint Policy Enforcement Overview (screenshots)

*Sources:* IFF-VRA 6.9; IFF-SDA 5.19; Servier-Q Q43

---

## 7. Privacy and GDPR

### Do you have a Data Protection Officer?
Yes. An internal Data Protection Officer, Albert Ai (aiy@chemical.ai), sits within the information security organization. The DPO oversees GDPR and other data protection compliance, maintains data protection policies, advises on risks and impact assessments, coordinates data subject requests and personal data breaches, and is the contact point on privacy matters.

**Supporting materials:** [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §17 Organizational Guarantee

*Sources:* Servier-Priv; IFF-VRA 2.11

### Do you comply with GDPR? Which privacy laws apply?
Yes. Applicable laws: GDPR (extraterritorially under Art. 3(2) where EU data subjects use the service), UK GDPR and the Data Protection Act 2018; the California Consumer Privacy Act as amended by CPRA and other US law (Chemical AI Inc. is a Delaware company, and SaaS is hosted in California); and the PRC Cybersecurity Law, Data Security Law and Personal Information Protection Law, since development, support and maintenance personnel are in China. Our supervisory authority of reference is the U.S. Federal Trade Commission.

**Supporting materials:** [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b); [Chemical.AI Privacy Policy](https://www.chemical.ai/privacy-policy); [ChemAIRS Information Security Risk Assessment Methodology](https://chemical-ai.feishu.cn/docx/EXHKdKe7Jof8DCxBTn6cEZ6gnVg) – Compliance

*Sources:* Servier-Priv

### Describe your privacy program.
It is governed by the Personal Information Security Policy (ISMS-2-CL-010), the published ChemAIRS Privacy Policy (last updated 22 August 2025), and a GDPR-compatible Data Processing Agreement (Art. 28 processor terms, Art. 32 security measures, sub-processor authorization, data subject rights assistance, breach notification, DPIA assistance and audit rights). A Privacy Impact Assessment is completed for each engagement and repeated if the purpose of processing changes. Records of processing activities are kept in a controlled, version-controlled register. Privacy training is part of the mandatory security training. We have not adopted Binding Corporate Rules.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-010 Personal Information Security; [Chemical.AI Privacy Policy](https://www.chemical.ai/privacy-policy); [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b)

*Sources:* Servier-Priv; IFF-VRA 2.5, 2.6; PIA

### How is consent obtained?
Through the ChemAIRS Privacy Policy (https://chemairs.chemical.ai/compliance/universal/privacy-policy.html). Users must expressly acknowledge that they have read, understood and consented to the policy before accessing the service, so consent is obtained before or at the time of collection.

**Supporting materials:** none in the Supporting Materials document

*Sources:* Gilead-email Q2.3; PIA

### How are data subject rights handled?
Users can view and update their own profile information in the platform, and tenant administrators handle account changes and email updates. Under the DPA, Chemical.AI assists the controller with rights requests and notifies the controller of any request received directly from a data subject; we can commit to notifying the customer within 48 hours of receipt. Portability requests go through the tenant administrator. ChemAIRS makes no automated decisions about individuals in the sense of Article 22 GDPR.

**Supporting materials:** [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b) – Data Subject Rights

*Sources:* Gilead-email Q3, Q4; Servier-Priv; PIA

### How is personal data kept accurate?
Users update their own profile information directly. Back-end operations are idempotent and transactional to guarantee data consistency. For organizational accounts, tenant administrators handle account adjustments with proper authorization.

**Supporting materials:** none in the Supporting Materials document

*Sources:* Gilead-email Q3

### Do you assist customers with DPIAs?
Yes. Under the DPA we provide reasonable assistance with DPIAs and prior consultation (GDPR Art. 35–36). This includes documentation of data categories, data flows, retention and deletion, and security measures; completed questionnaires with evidence (ISO 27001 certificate, penetration test reports, platform PIA); and architecture documentation. Requests are coordinated by the DPO.

**Supporting materials:** [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b) – Impact Assessments; [Chemical.AI ISO 27001 Certificate (EXP2027)](https://chemical-ai.feishu.cn/file/VVcfbiipZoFuA6xqgr0c4AfgnOc); [ChemAIRS Penetration Test Report (ZWAY-PET-202508-01)](https://chemical-ai.feishu.cn/file/JEtJbPq1EoeqEyx03BcczFSznzd)

*Sources:* Servier-Priv

### Can government authorities access customer data?
For local deployments, Chemical.AI hosts, stores and backs up no customer data and has no technical means of accessing it, so no foreign disclosure regime (e.g. the US CLOUD Act, the Stored Communications Act, the PATRIOT Act or FISA) can compel Chemical.AI to produce it.

**Supporting materials:** [ChemAIRS Software Local Deployment Data Security Management](https://chemical-ai.feishu.cn/wiki/Dx0XwJoT0iyEASkjsADcpnGbnYd) – §8.2 Data Sovereignty Guarantee

*Sources:* Servier-Priv

---

## 8. Backup, disaster recovery and business continuity

### Describe your disaster recovery and business continuity plans.
ChemAIRS runs on high-availability AWS services with instances in multiple availability zones and load balancing. If the provider's high availability fails, the containerized architecture can be rebuilt quickly in a new cluster from encrypted backups. The documented recovery process covers incident assessment, recovery plan development, dual senior-management authorization, supervised execution and verification, and addresses force majeure, system failures and security incidents. Emergency drills are held twice a year, and a business continuity tabletop exercise is held annually. DR facilities have the same security controls as the primary site.

**Supporting materials:** [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §14–16 Data Recovery and Emergency Response; [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-25 Emergency Preparedness

*Sources:* NOVA 3.11; Grü Q23; Servier-Q Q17, Q40; IFF-VRA 9.3–9.5, 9.7; IFF-SDA 2.2

### How will customers be notified of a disaster or outage?
The ChemAIRS team emails affected users through our Ops system, and the customer's dedicated business manager contacts the customer directly with progress and resolution updates. There is no public outage status page.

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-16 Communication

*Sources:* NOVA 3.11; IFF-SDA 3.19

---

## 9. Identity, authentication and access control

### Do you support single sign-on (SSO)?
Yes. SSO with Azure AD / Microsoft Entra ID is production-ready (SAML 2.0, OAuth 2.0, OIDC). LDAP-based federated identity is supported; other SSO providers are evaluated case by case. With SSO, the customer's own identity provider can enforce its MFA policy.

**Supporting materials:** [ChemAIRS System Test Report (v3.5.0)](https://chemical-ai.feishu.cn/file/UHALbVEYRojvBtxo5t0cdPjcn5e) – SSO login for local deployments

*Sources:* NOVA 5.1; Grü Q55; Servier-Q Q1; Acadia; IFF-SDA 4.3, 4.7

### How are identities provisioned? Do you support SCIM?
Users are pre-created manually and authenticated through SSO. SCIM is not currently supported; automated provisioning requirements are evaluated case by case.

**Supporting materials:** none in the Supporting Materials document

*Sources:* NOVA 5.2; IFF-SDA 4.4 comment

### How do users receive their credentials?
The business manager agrees the accounts needed with the customer and submits an internal request. The Ops platform creates the accounts and emails each user their account information and initial password.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-012 user password management

*Sources:* NOVA 5.6

### What is the ChemAIRS application password policy?
- Minimum length of 8 characters
- At least 3 of 4 character types: uppercase, lowercase, numbers, special characters
- User account names, email addresses, common simple passwords and previously used passwords are prohibited
- Passwords stored hashed and salted

**Supporting materials:** [Chemical.AI Security Development Principles and Coding Standards](https://chemical-ai.feishu.cn/file/YOlrbjrKzoB2F5xiWL7cQOkznJe) – 2.1, 2.4 password requirements

*Sources:* NOVA 5.7; Grü Q11

### What is your account lockout policy?
Accounts are locked after repeated failed login attempts and must be unlocked by the customer's tenant administrator. CAPTCHA protection is under development.

**Supporting materials:** [ChemAIRS System Test Report (v3.5.0)](https://chemical-ai.feishu.cn/file/UHALbVEYRojvBtxo5t0cdPjcn5e) – login failure limit, account unlock

*Sources:* NOVA 5.9; Grü Q66

### How are password resets performed?
Only the customer's tenant administrators can reset passwords for users in their tenant. If a tenant administrator forgets their password, the customer emails a request, and our account management team resets it after the business manager verifies the owner's identity.

**Supporting materials:** none in the Supporting Materials document

*Sources:* NOVA 5.8

### What session controls are in place?
Sessions end after 30 minutes of inactivity. Each account can be logged in on one device only; a new login ends the previous session, which prevents account sharing.

**Supporting materials:** [Chemical.AI Security Development Principles and Coding Standards](https://chemical-ai.feishu.cn/file/YOlrbjrKzoB2F5xiWL7cQOkznJe) – 2.3 Session Management

*Sources:* Grü Q57; Merck Q7

### Who is responsible for access management?
The CEO / Data Security Administrator provides governance. The DevOps/Operations team grants internal access through an approval workflow under the Access Control and Privileged Access Management policies. On the customer side, the tenant administrator manages accounts and password resets; the business manager coordinates account creation; the account management team assists with credential resets.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-012 Access Control, ISMS-2-CL-003 Privileged Access Management

*Sources:* Servier-Q Q5.1; Servier-email; IFF-VRA 6.12

### How are privileged accounts controlled?
Privileged accounts are issued individually, approved formally, kept separate from regular users, and traceable to named individuals. All privileged actions are recorded in the admin audit log (username, timestamp, operation type, API request URL, parameters and execution time). Server access goes through JumpServer. Emergency access requires documented justification and review.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-003 Privileged Access Management; ChemAIRS Admin Audit Log (screenshots); JumpServer User Account Management (screenshots)

*Sources:* Grü Q13; Servier-Q Q5.4, Q32

### Are unique IDs required? Are shared accounts allowed?
Every user has an individual ID with minimum necessary rights. Shared accounts are prohibited, and privileged IDs are traceable to specific people.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-007 Secret Authentication Information; [Employee Information Security Handbook (ZH-IS-201)](https://chemical-ai.feishu.cn/file/GElDbRiKSoNk7jxTBGbcWFBsnVe) – Corporate Accounts & Password Security

*Sources:* Grü Q12, Q13

### How is remote access to your network secured?
Remote access to our network and cloud services requires VPN and username/password, and connections to dedicated servers are limited to specific authorized devices. For customers, ChemAIRS access can be restricted to the customer's IP addresses through AWS security groups.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-012 remote work policy; [Employee Information Security Handbook (ZH-IS-201)](https://chemical-ai.feishu.cn/file/GElDbRiKSoNk7jxTBGbcWFBsnVe) – Remote Work Security; AWS Network Security Configuration (NACL, security groups, ALB) (screenshots)

*Sources:* NOVA 4.11; Grü Q33; IFF-VRA 6.4

---

## 10. Logging, monitoring and detection

### How are audit logs stored and reviewed?
Audit logs are kept in a dedicated database accessible only to the audit administrator, as a one-time privilege approved by the CEO. They capture user identity, event type, timestamp, source and destination, data accessed, the operation (read, modify, delete) and the outcome. System and security logs are designed to exclude sensitive molecular data. Customers can request an audit log review through their business director, and logs can be exported or shared on request.

**Supporting materials:** ChemAIRS Admin Audit Log (screenshots); [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §13 Log Management

*Sources:* NOVA 2.1; Grü Q52, Q54; Servier-Q Q22

### How do you monitor for security events?
Logs are collected and monitored centrally with Grafana Loki, Prometheus/Grafana and AWS CloudWatch, with multi-level real-time alerts. Detection tools include AWS GuardDuty and AWS WAF in the cloud and an H3C SecPath intrusion prevention system (CVE-based signatures) with firewalls on the corporate network. We subscribe to threat intelligence feeds and feed real-time CVE data into container scanning.

**Supporting materials:** Runtime Monitoring & Logging Infrastructure (Grafana Loki, CloudWatch) (screenshots); On-Premises Network Security Infrastructure (Huawei & H3C) (screenshots); Container Vulnerability Management (Harbor / Trivy) (screenshots)

*Sources:* NOVA 4.3, 4.9; Grü Q17; Servier-Q Q22, Q28, Q29

### Do you have antivirus / endpoint protection?
Yes. Endpoint security with antivirus protects workstations, laptops, email and web. It updates automatically and users cannot disable it. Email is protected against spam, spoofing and phishing, and malware scans are also run on data and databases.

**Supporting materials:** [Information Security Management Policy Handbook](https://chemical-ai.feishu.cn/file/TD0tbp7HYok6XuxSEGgcEI9bnIe) – ISMS-2-CL-006 Virus Management; On-Premises Network Security Infrastructure (Huawei & H3C) (screenshots); Container Vulnerability Management (Harbor / Trivy) (screenshots)

*Sources:* Grü Q46; IFF-VRA 6.1–6.3

### Are systems configured for forensic investigation?
Yes. Centralized log collection, restricted audit-administrator access, and detailed audit trails (user, timestamp, operation, API and parameters) support forensic analysis. Evidence preservation is part of the incident investigation procedure (ZHKJ-QESP-24).

**Supporting materials:** ChemAIRS Admin Audit Log (screenshots); [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-24 Incident Investigation

*Sources:* Servier-Q Q41

---

## 11. Network security

### Describe your network security controls.
- HTTPS enforced; only ports 443 and 80 open, with 80 redirecting to HTTPS
- Internal-only private network (VPC) cluster with network ACLs and security groups
- Kubernetes services use ClusterIP (internal only) except the web front end, which is exposed through Ingress-Nginx
- Databases, Redis and RabbitMQ are not reachable from outside the cluster; database access is restricted to specific IP CIDR ranges
- Firewalls at the perimeter, between production and non-production, and around sensitive environments; intrusion detection at the perimeter
- IP allow-listing and block-listing supported

**Supporting materials:** AWS Network Security Configuration (NACL, security groups, ALB) (screenshots); Kubernetes Security Configuration (screenshots); On-Premises Network Security Infrastructure (Huawei & H3C) (screenshots)

*Sources:* NOVA 4.10; Grü Q29, Q30, Q57; IFF-VRA 6.6, 6.7; IFF-SDA 6.6, 6.7

### Is there a DMZ?
The cloud environment is segmented so that only the web front end is externally reachable, through Ingress-Nginx. The corporate network uses zone-based firewall policies (Trust/Untrust/DMZ/Local).

**Supporting materials:** On-Premises Network Security Infrastructure (Huawei & H3C) (screenshots); Internal Core Services & Network Segmentation (NGINX, DNS, AD) (screenshots); Kubernetes Security Configuration (screenshots)

*Sources:* Grü Q35; Servier-Q Q26

### Are default passwords changed before production?
Yes. Default admin accounts are disabled or renamed and default passwords changed. All middleware requires credentials before deployment (for example, Redis is given an access password and RabbitMQ default credentials are replaced).

**Supporting materials:** Kubernetes Security Configuration (screenshots)

*Sources:* Grü Q38, Q44; IFF-VRA 7.12

### Are unnecessary services disabled?
Yes. Unneeded functions are disabled through role permissions, and all containers except the web front end are internal-only.

**Supporting materials:** Kubernetes Security Configuration (screenshots)

*Sources:* Grü Q43

---

## 12. Vulnerability and patch management

### Describe your vulnerability management program.
- SonarQube static analysis (SAST) on each commit in GitLab CI, with quality gates that block merges and releases
- Daily vulnerability reports reviewed by the code security team; fixes required before merge
- Trivy scans of every container image in our private Harbor registry against the latest CVE database before release
- OWASP scans on every release; vulnerability scanning at least monthly
- Third-party application security assessments and independent penetration tests
- Documented decision for every finding: immediate fix, next release, or justified no action

**Supporting materials:** Container Vulnerability Management (Harbor / Trivy) (screenshots); Development Security Pipeline (GitLab CI, SonarQube) (screenshots); [ChemAIRS Penetration Test Report (ZWAY-PET-202508-01)](https://chemical-ai.feishu.cn/file/JEtJbPq1EoeqEyx03BcczFSznzd); [ChemAIRS-backend Code Analysis Report](https://chemical-ai.feishu.cn/file/Cvx9bCU5eojHBExvqWvcyrDinWg)

*Sources:* NOVA 4.7; Grü Q40; Servier-Q Q20; IFF-VRA 7.8

### How and how often are systems patched?
Patched container images are released regularly, with hotfixes as needed. Patches are tested in QA and pre-release environments before production. For SaaS infrastructure, AWS-managed components follow AWS's update mechanism. Application-level vulnerabilities and fixes are communicated to administrators by email.

**Supporting materials:** Container Vulnerability Management (Harbor / Trivy) (screenshots)

*Sources:* NOVA 4.8; Grü Q45; Servier-Q Q67; IFF-SDA 3.22

### Do you manage software supply chain risk?
Yes. All dependencies and container images are scanned with Trivy before deployment, dependency-chain vulnerabilities are reviewed daily, and all software is developed in-house.

**Supporting materials:** Container Vulnerability Management (Harbor / Trivy) (screenshots); [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-07 Procurement

*Sources:* Grü Q41, Q70

---

## 13. Secure development and quality management

### Do you follow secure development standards?
Yes. Our Security Development Principles and Coding Standards define a secure development lifecycle covering requirements, design, coding, testing and maintenance. We follow OWASP Top 10, OWASP ASVS and CWE. Development is governed by the Design and Development Control Procedure (ZHKJ-QESP-06).

**Supporting materials:** [Chemical.AI Security Development Principles and Coding Standards](https://chemical-ai.feishu.cn/file/YOlrbjrKzoB2F5xiWL7cQOkznJe); [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-06 Design and Development; Development Security Pipeline (GitLab CI, SonarQube) (screenshots)

*Sources:* Servier-Q Q34, Q47; IFF-VRA 7.1

### How do you prevent code injection?
Strict input validation with whitelisting; parameterized queries for all database access; .NET Core EF Core and JDBC data access; Content Security Policy and CSRF protection; authentication on APIs.

**Supporting materials:** [Chemical.AI Security Development Principles and Coding Standards](https://chemical-ai.feishu.cn/file/YOlrbjrKzoB2F5xiWL7cQOkznJe) – 2.2 Input Validation; [ChemAIRS Penetration Test Report (ZWAY-PET-202508-01)](https://chemical-ai.feishu.cn/file/JEtJbPq1EoeqEyx03BcczFSznzd)

*Sources:* NOVA 4.12; Grü Q56

### Who reviews code and how?
Mandatory peer review before merge; automated SonarQube analysis; the code security team reviews daily vulnerability reports; merges are approved only after fixes; changes need dual approval from the development lead and the data security lead; the quality management team runs independent scans.

**Supporting materials:** Development Security Pipeline (GitLab CI, SonarQube) (screenshots); [Chemical.AI Security Development Principles and Coding Standards](https://chemical-ai.feishu.cn/file/YOlrbjrKzoB2F5xiWL7cQOkznJe)

*Sources:* Grü Q58; Servier-Q Q58

### What is your testing strategy?
- White-box testing: static analysis, peer review and security tests
- Module testing: database layer, middleware, API endpoints
- Integration testing: end-to-end workflows
- Security testing: SAST, container scanning, penetration testing
- Pre-release testing in clusters that replicate production

Testing uses synthetic data only. Success criteria include 100% code review before merge and zero critical security vulnerabilities from static analysis. Results are documented; for example, the ChemAIRS System Test Report for version 3.5.0 covers 44 major functional tests with a 100% pass rate.

**Supporting materials:** [ChemAIRS System Test Report (v3.5.0)](https://chemical-ai.feishu.cn/file/UHALbVEYRojvBtxo5t0cdPjcn5e); Development Security Pipeline (GitLab CI, SonarQube) (screenshots); [ChemAIRS Penetration Test Report (ZWAY-PET-202508-01)](https://chemical-ai.feishu.cn/file/JEtJbPq1EoeqEyx03BcczFSznzd)

*Sources:* Grü Q65; Servier-Q Q59

### How is quality managed?
We are ISO 9001-certified, with 29 documented quality procedures (ZHKJ-QESP-01 to -29) covering document and record control, design and development, risk, KPIs, continual improvement, customer communication and satisfaction, and nonconforming products. Software versions and components are tracked through GitLab CI/CD and the Harbor registry.

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g); [Chemical.AI ISO 27001 Certificate (EXP2027)](https://chemical-ai.feishu.cn/file/VVcfbiipZoFuA6xqgr0c4AfgnOc)

*Sources:* Servier-Q Q47, Q61

### How are releases delivered?
Container images are delivered onsite, remotely or self-service. Hotfixes are released as needed and announced by email. Every release is versioned and reproducible (container images, Helm, Terraform), and rollback to the previous version is supported.

**Supporting materials:** Development Security Pipeline (GitLab CI, SonarQube) (screenshots)

*Sources:* Grü Q62; Servier-Q Q67; IFF-SDA 2.8, 7.38, 8.16

### Is development outsourced?
No. All software is developed in-house.

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-07 Procurement

*Sources:* Grü Q70; Servier-Q Q53

---

## 14. Incident management

### Do you have an incident response plan?
Yes. It covers internal and external incidents. A dedicated incident response team (security experts, operations and maintenance staff, development leads) follows a documented process: reporting, categorization, initial assessment, threat isolation and impact mitigation, dual senior-management authorization for recovery, supervised remediation, evidence preservation, root-cause analysis, and corrective and preventive action. Relevant procedures: ZHKJ-QESP-24, -25 and -26. The plan is exercised through emergency drills twice a year, and lessons learned feed into continual improvement (ZHKJ-QESP-14).

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-24, -25, -26, -14; [ChemAIRS SaaS Environment Data Security Management Regulations](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz) – §15 Recovery Process; [Employee Information Security Handbook (ZH-IS-201)](https://chemical-ai.feishu.cn/file/GElDbRiKSoNk7jxTBGbcWFBsnVe) – Security Incident Reporting & Response

*Sources:* NOVA 1.2; Grü Q15, Q16; Servier-Q Q19, Q40, Q44; IFF-VRA 8.1–8.5

### How quickly are incidents reported and customers notified?
Employees must report security incidents internally within 24 hours. Customers are notified of a personal data breach under the terms of our Data Processing Agreement. Notification goes out by email through our Ops system, and the customer's business manager provides direct updates until resolution.

**Supporting materials:** [Employee Information Security Handbook (ZH-IS-201)](https://chemical-ai.feishu.cn/file/GElDbRiKSoNk7jxTBGbcWFBsnVe) – Security Incident Reporting & Response; [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b) – Breach Notification

*Sources:* NOVA 3.12; Servier-Priv

---

## 15. Third parties

### Do you use subcontractors or depend on critical third parties?
No subcontractors and no external developers. For SaaS, AWS is our only infrastructure provider. We evaluate and monitor critical suppliers, particularly cloud providers, under our supplier management procedures. Independent penetration testers are engaged for assessments only. Local deployments involve no third party.

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-07 Procurement; [Chemical.AI Data Processing Agreement](https://chemical-ai.feishu.cn/file/BkT0bakGPoH3sux4qNWcFsoDn6b) – Subprocessing

*Sources:* NOVA 6.1; Grü Q20; Servier-Q Q14; Servier-email

---

## 16. Local and customer-hosted deployment

### Can ChemAIRS be deployed locally?
Yes. ChemAIRS can run as SaaS or be deployed in the customer's own environment (on-premise, or the customer's own cloud account such as AWS). A local deployment can run in an isolated intranet with no internet access after deployment. The customer controls the hardware, application, data, storage location, backups, encryption keys, log retention and update timing.

**Supporting materials:** [ChemAIRS Software Local Deployment Data Security Management](https://chemical-ai.feishu.cn/wiki/Dx0XwJoT0iyEASkjsADcpnGbnYd)

*Sources:* NOVA 2.3; Merck Q4; Servier-Priv; IFF-SDA 1.1.3

### What are the platform requirements for local deployment?
x86_64 with at least one NVIDIA GPU server; Rocky Linux 8.9–9.3, Debian 11–12, CentOS 7.9 or Ubuntu 18.04–22.04 (kernel ≥ 3.10); Kubernetes (RKE2 or managed EKS/GKE/AKS) with containerd; PostgreSQL 14.0+ supporting 512 concurrent connections; persistent storage with Kubernetes PV/PVC RWX (NFS/local on-premise, or EFS/Cloud Storage/Azure Disk in the cloud); Redis and RabbitMQ with authentication configured; static IP, DNS and firewall configuration; NVIDIA drivers, Container Toolkit and CUDA runtime.

**Supporting materials:** none in the Supporting Materials document

*Sources:* Grü Q59, Q61

### What does implementation look like?
Environment preparation, container deployment, configuration, then validation and acceptance sign-off, typically within a few weeks. The customer provides the environment, an IT/DevOps contact and acceptance testing. Documentation includes installation and local-deployment specifications, system and hardware standards, user manuals, technical architecture, and operations and maintenance plans.

**Supporting materials:** none in the Supporting Materials document

*Sources:* IFF-SDA 2.4, 2.31–2.33; Servier-email

---

## 17. Trials, support and service levels

### Do you offer trials?
Yes. Evaluation access or a scoped proof of concept is available before purchase. SaaS trials run in production, the development team has no access to trial data, and single-device login prevents account sharing. As many individual trial accounts as the evaluation needs can be created, within reasonable limits.

**Supporting materials:** none in the Supporting Materials document

*Sources:* Merck Q3, Q7; IFF-SDA 2.6

### How is support organized? What are the response times?
A dedicated business manager plus a support team, escalating to DevOps and development leads and then to management. Support is reached by email and through the business manager. Issues fall into four severity levels: S1 critical, S2 high and S3 medium receive a response within 1 business day; S4 low (cosmetic issues and enhancement requests) is handled in the next release cycle. Support hours are set by agreement.

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-05 Customer Communication

*Sources:* Servier-Q Q68; IFF-SDA 3.11–3.14, 3.32

---

## 18. Artificial intelligence

### How does ChemAIRS use AI?
AI is used only for chemistry: a retrosynthesis engine (reaction-template extraction plus neural ranking) that generates scored synthetic routes, forward-synthesis prediction and synthesizability (SA) scoring, impurity prediction, process chemistry (cost, solvent and reagent assessment, scale-up), and Bayesian optimization of reaction conditions. No generative LLM is used in the core engine.

**Supporting materials:** none in the Supporting Materials document

*Sources:* Jazz; Acadia; IFF-VRA 11.2

### How are AI results made transparent and governed?
Each proposed step can be traced to the literature or patent reaction it derives from, and routes are scored on viability, cost and step count. Outputs are advisory and reviewed by chemists (human in the loop). The system processes chemical structures only, with no personal data or profiling, and makes no automated decisions about individuals. We assess it as minimal-risk under the EU AI Act (it falls outside Annex III). Model changes are versioned and governed by ZHKJ-QESP-06 and ZHKJ-QESP-15. Inputs are protected by validation, rate limiting and audit logging.

**Supporting materials:** [Quality Management System Procedures Compilation](https://chemical-ai.feishu.cn/file/GP9ib0v8yoqXlhxrlhEcBngsn8g) – ZHKJ-QESP-06, ZHKJ-QESP-15

*Sources:* Jazz; Servier-Priv; IFF-SDA 9.1–9.7

---

## 19. API and client

### Is an API available and how is it secured?
Yes, a RESTful JSON API. API access is disabled by default and requires a separate application (and may involve additional licensing). Requests authenticate with an X-Api-Key header or bearer token, and invalid credentials receive HTTP 401. API keys are scoped to specific APIs, rate limits apply per account, all traffic uses HTTPS/TLS, inputs are strictly validated, and API activity is logged.

**Supporting materials:** Postman Request – Timeout / 401 / 200 (screenshots); [ChemAIRS Penetration Test Report (ZWAY-PET-202508-01)](https://chemical-ai.feishu.cn/file/JEtJbPq1EoeqEyx03BcczFSznzd)

*Sources:* Grü Q64; Servier-Q Q35; Gilead-FU

### What is needed on the client side?
A modern browser (Microsoft Edge or Google Chrome). No local installation or add-ons are needed. The web UI works in mobile browsers; there is no native mobile app.

**Supporting materials:** none in the Supporting Materials document

*Sources:* NOVA 4.13; IFF-SDA 2.22, 2.23, 8.9

### Does the software run independently of the installation account?
Yes. Containers run as a non-privileged user (UID/GID 65534, "nobody"), the database uses a dedicated postgres user, and Kubernetes services use service accounts.

**Supporting materials:** Kubernetes Security Configuration (screenshots)

*Sources:* Grü Q63

