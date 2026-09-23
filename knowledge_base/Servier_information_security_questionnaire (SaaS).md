# Servier\_information\_security\_questionnaire \(SaaS\)

1. **As part of our security policies, we require the use of Single Sign\-On \(SSO\) for accessing our systems \(including SaaS applications\)\. Could you please confirm if your solution supports SSO integration?**

    Yes, ChemAIRS supports Single Sign\-On \(SSO\) integration with production\-ready Azure AD, support for SAML 2\.0 and OAuth 2\.0, manual user pre\-creation with SSO credential validation, LDAP\-based federated identity, and evaluation of other SSO providers on a case\-by\-case basis\. 

2. **Do you work with any third parties? for data hosting, software development, or software support\.\.\.**

    Yes, but with limited and clearly defined third\-party relationships: no subcontractors \(all software is developed in\-house\), AWS cloud infrastructure is used for hosting in SaaS deployments, independent third\-party penetration testing is conducted regularly, and the local\-deployment option eliminates third\-party data concerns\. 

3. **In which countries are your servers located and where will our data be hosted?**

    For SaaS, all customer data is hosted in the United States, specifically in the AWS North California \(us\-west\-1\) region, stored on AWS database servers with multi\-copy instances across different availability zones, and no SaaS data is stored outside the U\.S\.; customers needing data localization can instead select local deployment\. 

4. **Could you please transfer the technical and functional documentation to us, including user manuals, technical architecture documents, and operational maintenance plans?**

    Yes, we provide technical and functional documentation such as installation and local\-deployment specifications, and SaaS environment management regulations

5. **Access Management :**

    1. **Who is responsible of access management and access controls?**

        Yes, we operate a multi\-level access management structure where the CEO/Data Security Administrator provides overall governance, the Tenant Administrator manages customer\-side accounts and password resets, the Business Manager coordinates account creation and communication, the DevOps Manager implements technical access, and the Account Management Team assists with credential resets and verification\. 

    2. **How do you manage access controls?**

        Comprehensive access control is enforced through tenant\-level RBAC, individual account assignment with the minimum\-rights principle, privileged access requiring formal approval, multi\-factor authentication \(in development\), an account lockout policy after 5 failed attempts, and prohibition of shared accounts, with each account limited to one device\. 

    3. **Do you perform user accounts and access reviews, and if so, how frequently?**

        Yes, user accounts are subject to systematic and periodic reviews as defined in account management rules, ensuring individual IDs follow minimum\-rights principles, account usage and access patterns are regularly monitored, and tenant administrators oversee user lifecycle management\.

    4. **Do you perform administrator accounts and access reviews, and if so, how frequently? With recertification?**

        Yes, administrator accounts undergo enhanced oversight, with privileged access individually assigned and approved, separated from regular users via tenants and RBAC, fully traceable to specific individuals through comprehensive audit logging, and governed by emergency access procedures requiring documented justifications and reviews\. 

    5. **If you manage several environments \(such as sandbox, training, etc\.\): is access review conducted for all available environments? Are test, training, or other accounts deleted if not used for more than a specific period, and are passwords reset regularly?**

        Yes, we manage DEV, Test, QA, and pre\-release environments on separate infrastructure with isolated test clusters, apply consistent access controls and periodic reviews across all environments, and enforce user account lockout and password complexity policies to manage dormant accounts and maintain security hygiene\. 

---

6. **Do you hold recognized information security certifications **\(e\.g\., ISO 27001, SOC 2 Type II, PCI\-DSS, HDS\)? \(Evidence required: Valid certificate with the scope and all locations concerned by the certificate\.\)

Yes, ChemAIRS \(Chemical\.AI\) maintains ISO 9001 and ISO 27001 certifications that cover our information security and quality management systems\.

Supporting Materials:

- [《Chemical\.AI ISO27001 EXP2027》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EOyTd9La6oBUhOxdBaccUfuYnCh)

7. **Are you currently undergoing a certification process in information security **\(e\.g\., ISO 27001, SOC 2\) \(Evidence required: Engagement letter, audit plan, pre\-certification report\.\)

No, we are not currently undergoing additional information security certification processes; we rely on our established ISO 27001 certification for our ISMS\.

Supporting Materials:

- [《Chemical\.AI ISO27001 EXP2027》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EOyTd9La6oBUhOxdBaccUfuYnCh)

8. **Are you audited at least once a year by an independent external party or certification body for information security?** \(Evidence required: External audit report, attestation letter\)

Yes, we are audited at least annually by independent external bodies for ISO 27001 and also engage external security firms for penetration testing and security assessments\. 

Supporting Materials:

- [《Chemical\.AI ISO27001 EXP2027》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EOyTd9La6oBUhOxdBaccUfuYnCh)

- [《ChemAIRS Penetration Test Report》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CLJAdko8Wo1BtXxFkUxcgwUWnzg)    

9. **Do you maintain a Security Assurance Plan \(SAP\) or equivalent document describing your security commitments to clients?** \(Evidence required: SAP, client security annexes, commitment charter\.\)

Yes, we maintain a comprehensive set of security policies and client\-facing commitments, including detailed SaaS environment data security regulations and a GDPR\-compatible Data Processing Agreement\.

Supporting Materials:

- [《Information Security Management Policy Handbook》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-BcoLdeTEvoyxZGxi2xicC0F6ngg)

- [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

    - Section I: General Provisions \(Scope of Application, Basic Principles \- Security first, ISO 27001 compliance, least privilege, transparency and control\)

    - Section II: SaaS Production Environment Data Management \(Environment Isolation, Multi\-tenant Data Management, Access Control\)

    - Sections covering: Data encryption policies, backup strategy, operations management, business continuity planning specific to SaaS environment

- [《Chemical\.AI Data Processing Agreement》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-DEiGd90dJo1cnzxy8k7cTDe9nDb)

    - GDPR\-compatible Data Processing Agreement for SaaS clients

10. **Do you have valid cyber insurance covering security incidents \(e\.g\., ransomware, data breaches, service outage\)?** \(Evidence required: Valid insurance certificate\.\)

Yes, we maintain business insurance that includes network security liability coverage for cyber incidents\.

Supporting Materials:

- [《Chemical\.AI Business Insurance Coverage》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-Iiu6d1FYKokwNHxgeYWcSYgGngb)

11. **Do you have a formally defined and approved information security policy that is communicated to all employees?** \(Evidence required: Policy extract, proof of communication\.\)

Yes, we operate formally defined, approved, and communicated information security policies \(passwords, backup, privileged access, email, antivirus, personal information, mobile devices, access control\) supported by SaaS\-specific regulations and training/HR procedures across the organization\.

Supporting Materials:

- [《Information Security Management Policy Handbook》\(Doc\) ](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-HNCmdUcsPor7Pcx5Wj1cKlyFnQb)

    - ISMS\-2\-CL\-001 Password Policy, ISMS\-2\-CL\-002 Backup Policy, ISMS\-2\-CL\-003 Privileged Access Management Policy, ISMS\-2\-CL\-004 Email Management Policy, ISMS\-2\-CL\-006 Virus Management Policy, ISMS\-2\-CL\-010 Personal Information Security Policy, ISMS\-2\-CL\-011 Mobile Device Management Policy, ISMS\-2\-CL\-012 Access Control Policy

- [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

    - Basic Principles \(Security first, ISO 27001 compliance, least privilege, transparency and control\)

    - Multi\-factor authentication requirements

    - Audit logs \(1\+ year retention\) and privilege review procedures

- [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

    - ZHKJ\-QESP\-29: Training Management Control Procedure \(security training and competency\-based programs\)

    - ZHKJ\-QESP\-04: Human Resources Control Procedure

- Communication evidence: Policies reviewed regularly by CEO, Data Security Administrator, and DevOps Manager; mandatory security training for all employees twice yearly; bi\-annual security awareness training

12. **Are you compliant with GDPR, HIPAA, PCI\-DSS, or other relevant standards?** \(Evidence required: Compliance reports, regulator audit results, DPO statement\.\)

    Yes\.  ChemAIRS complies with GDPR and ISO\-aligned security requirements for SaaS through multi\-tenant isolation, DPO responsibilities, ISO 27001\-based controls, China Cybersecurity Law compliance, and a GDPR\-compatible Data Processing Agreement leveraging AWS compliance reports\. 

Supporting Materials:

- [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

    - Section II: Multi\-tenant data management with tenant isolation and data boundaries

    - Data Protection Officer \(DPO\) appointment in organizational structure

    - ISO 27001 compliance explicitly stated in basic principles for SaaS environment

    - China Cybersecurity Law compliance for SaaS operations

- [《Chemical\.AI Data Processing Agreement》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-DEiGd90dJo1cnzxy8k7cTDe9nDb)

    - Complete GDPR\-compatible Data Processing Agreement for SaaS clients

- 《AWS SOC1 SOC2 SOC3 ISO\-27001 ISO\-27017 ISO27018 Reports》\(Doc\)

- [《Chemical\.AI ISO27001 EXP2027》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EOyTd9La6oBUhOxdBaccUfuYnCh)

13. **Have you appointed a person responsible for information security \(CISO or equivalent\)?** \(Evidence required: Organizational chart, role description\.\) 

    Yes, the CEO/Data Security Administrator serves as Risk Owner for information security, supported by the DevOps Manager and Development Leaders as technical assessors and an information security team including a Data Protection Officer for SaaS operations\.

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section VI: Organizational Guarantee \- Information security team, Data Protection Officer \(DPO\), security management team

14. **Do you evaluate, monitor, and require security commitments from your own subcontractors/suppliers? **\(Evidence required: Supplier questionnaire, contract clause, supplier risk assessment\.\)

    Yes, we evaluate, monitor, and require security commitments from third\-party suppliers\. While Chemical\.AI does not use subcontractors for core software development \(all developed in\-house\), we do evaluate and monitor our critical third\-party suppliers, particularly cloud infrastructure providers\.

    Supporting Materials:

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

    

15. **Do you have a documented and tested high\-level incident escalation process \(who to notify, timelines, responsibilities\)?** \(Evidence required: Escalation plan, incident simulation report\.\)

    Yes, we maintain a documented and tested incident escalation and response process that covers incident assessment, recovery plan development, dual senior\-management authorization, supervised execution, verification, and RTO ≤4 hours / RPO ≤1 hour, exercised through bi\-annual drills\.

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section V: Data Recovery and Emergency Response \- Section 15: Recovery Process with incident assessment, plan development, dual senior management authorization, supervised execution, verification; Section 16: Business continuity with RTO ≤4 hours, RPO ≤1 hour, bi\-annual drills

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-24: Accident and Incident Investigation and Handling Control Procedure; ZHKJ\-QESP\-25: Emergency Preparedness and Response Control Procedure with emergency response planning and preparedness procedures

16. **Do you run regular security awareness training \(e\.g\., phishing simulations, mandatory e\-learning\)?** \(Evidence required: Training program, attendance records, phishing test report\.\)

    Yes, all employees participate in bi\-annual mandatory security awareness, technical skills, and emergency\-drill training under a structured competency\-based training management program with effectiveness evaluation\. 

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section VI: Supervision and Management \- Section 19: Training and Education with bi\-annual awareness training, technical skills training, emergency drills

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-29: Training Management Control Procedure with systematic approach for training planning, delivery, and evaluation; competency\-based training programs and certification requirements; training effectiveness evaluation and continuous improvement

17. **Do you maintain and test a BCP/DRP that includes information security aspects? **\(Evidence required: BCP/DRP document, test report\.\)

    Yes, we maintain and test a comprehensive BCP/DRP with RTO ≤4 hours and RPO ≤1 hour, dual\-layer backups \(local \+ remote DR\) protected by AES\-256, and well\-defined procedures for force majeure, system failures, and security incidents, validated via bi\-annual drills\.

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section V: Data Recovery and Emergency Response \- Section 16: Business continuity with RTO ≤4 hours, RPO ≤1 hour, bi\-annual drills, regular plan updates; Section 14: Data recovery conditions for force majeure, system failures, security incidents; Section 15: Recovery process with dual senior management authorization and supervised execution

        - Section III: Data Backup Strategy \- Sections 7\-9: Dual\-layer protection with local backup \+ remote disaster recovery, full backup strategy, 7\-day retention, AES\-256 encryption

18. **Do you manage the full lifecycle of user accounts and access rights?** \(Evidence required: Access management policy, periodic review logs\.\)

    Yes, we manage the full lifecycle of accounts and access rights via RBAC, privilege separation, MFA \(in development\), periodic reviews, password policies, privileged\-access controls, and long\-term audit logs\.

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section II: SaaS Production Environment Data Management \- Section 5: Access Control with multi\-factor authentication, privilege separation, audit logs \(1\+ year retention\), privilege review procedures

    - [《Information Security Management Policy Handbook》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-Ueqyddv38ojoN4xn8fxcAgS3nzc)

        - ISMS\-2\-CL\-001: Password Policy with regular password changes and complexity requirements; ISMS\-2\-CL\-003: Privileged Access Management Policy with rules for creating, using, controlling, and removing accounts with special access privileges

19. **Do you have a documented process for reporting and resolving incidents? **\(Evidence required: Incident response plan, anonymized incident report\.\)

    Yes, we operate a documented and systematic incident process covering reporting, assessment, dual senior\-management authorization, supervised remediation, evidence preservation, root\-cause analysis, corrective actions, and post\-incident improvement\. 

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section V: Data Recovery and Emergency Response \- Section 15: Recovery process with incident assessment, plan development, dual senior management authorization, supervised execution, verification

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-24: Accident and Incident Investigation and Handling Control Procedure with systematic approach for incident reporting, investigation, and analysis including evidence preservation and witness interview requirements; ZHKJ\-QESP\-26: Corrective and Preventive Action Control Procedure for addressing nonconformities and preventing recurrence

20. **Do you have a systematic vulnerability and patching process? **\(Evidence required: Patching policy, vulnerability scan results, patch logs\.\)

    Yes, our vulnerability and patch management process includes SonarQube SAST integrated into CI/CD, Trivy container image scanning with real\-time CVE databases, daily vulnerability reports reviewed by the security team, and monthly patched container image releases\.

    Supporting Materials:

    - [《Container Vulnerability Management》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EajmdX9ZdoXeKWxpxoOcFdMXnNe)

        - Harbor Vulnerability Scanner with Trivy configuration, Container Image Scan Result Summary showing severity categorization and fixable vulnerabilities, CVE List and Affected Packages with detailed vulnerability findings

    - [《Development Security Pipeline》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-LviPdBwOYobntJxJfHtcoWfpnYb)

        - GitLab CI Pipeline Log showing SonarQube Static Code Analysis execution, Continuous SonarQube Security Scanning with passed quality gates

21. **Do you follow change management procedures including security impact assessments?** \(Evidence required: Change management policy, change tickets with security validation\.\)

    Yes, we enforce formal change management requiring internal modification approvals, dual authorization from development and data security leads, automated security impact checks, and documented change and release controls\. 

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section IV: Operations and Monitoring Management \- Section 12: Operations Management with change management, release management, capacity planning, performance optimization procedures

22. **Are logs collected, monitored, and protected against tampering? **\(Evidence required: Log management policy, SIEM screenshot, log retention configuration\.\)

    Yes, logs are centrally collected and monitored using Grafana Loki and AWS CloudWatch, stored in encrypted form with ≥1\-year retention, accessible only to authorized audit administrators, and include detailed audit trails for tamper\-evident forensics\. 

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section IV: Operations and Monitoring Management \- Section 13: Log Management with system/application/security logs \(no sensitive molecular data\), encrypted storage, 1\+ year retention, compliance requirements; Section 11: System Monitoring with performance, security, business monitoring with multi\-level alerts

    - [《Runtime Monitoring \& Logging Infrastructure \(Screenshots\)》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-L3QydjhXwoKva9xej8ZcP6txnIh)

    - [《ChemAIRS Admin Audit Log》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-DSeYdE4WxoqXGmxMW9NcJr9sn5e)

23. **Do you enforce MFA and secure connections \(VPN, ZTNA\) for remote access?** \(Evidence required: Remote access policy, technical configuration, audit report\.\)

    Yes, remote access is secured with AWS security group controls, SSO \(Azure AD\) integration, enforced HTTPS/TLS, device\- and source\-based access restrictions, and MFA capabilities in development, all governed by remote\-access and access\-control policies\. 

    Supporting Materials:

    - [《Information Security Management Policy Handbook》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-BcoLdeTEvoyxZGxi2xicC0F6ngg)

        - ISMS\-2\-CL\-012 Access Control Policy sections 5\.7\-5\.8 covering remote access security requirements and multi\-factor authentication procedures

24. **Do you apply data protection measures \(e\.g\., encryption, anonymization, segregation\) for sensitive data? **\(Evidence required: Data protection policy, technical configuration sample, DPO report\.\)

    Yes, sensitive data is protected through AES\-256 encryption at rest, TLS 1\.2\+ encryption in transit, encrypted backup storage, strict tenant isolation in multi\-tenant SaaS, and hashed/salted passwords using private encryption algorithms\.

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section II: Data Encryption \- AES\-256 for sensitive data, TLS 1\.2\+ for transmission, encrypted backup storage; Section II: Multi\-tenant Data Management with tenant isolation, resource quotas, access boundaries; Section III: Data Transmission Security with TLS 1\.2\+ encryption, real\-time monitoring, integrity verification

25. **Do you enforce secure retention and destruction of data and media?** \(Evidence required: Data retention policy, data destruction certificates\.\)

    Yes, we enforce secure retention and destruction through a 6\-month retention period after contract termination, 7\-day encrypted local backups with automatic cleanup, 3\-month remote DR retention with physical destruction afterward, and CEO\-authorized data deletion procedures\.

    Supporting Materials:

    - [《Information Security Management Policy Handbook》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-BcoLdeTEvoyxZGxi2xicC0F6ngg)

        - Section III: Data Backup Strategy \- Section 8: Local Backup Management with 7\-day retention, AES\-256 encryption, automatic cleanup; Section 9: Remote Disaster Recovery Backup Management with 3\-month retention, physical destruction after 3 months

26. **Is your environment segmented \(internal, DMZ, external\)?** \(Evidence required: Network diagrams, firewall rules\)

    Yes, there is comprehensive network segmentation across cloud and on\-prem environments using AWS VPCs with Network ACLs, internal core services on private IPs without external exposure, zone\-based firewall policies \(Trust/Untrust/DMZ/Local\), and VLAN segmentation for office\-network isolation\.

    Supporting Materials:

    - [《AWS Network Security Configuration》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CGaOd54iUo5qsPxwL3Fc4OW0nab)\(Screenshots\)

    - [《On\-Premises Network Security Infrastructure \(Huawei \& H3C\)》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-BqOPdmh9xo42eAxjtx8cMQyBnig)

    - [《Internal Core Services \& Network Segmentation》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CgWad3EYpoA3MmxsTfUcx9imnKh)

27. **Do you have a lifecycle process for encryption keys \(generation, rotation, revocation\)?** \(Evidence required: Key management policy, HSM usage proof\.\)

    Yes, AES\-256 with 256\-bit keys is implemented along with user\-managed access and encryption keys and customer control over backup encryption, although a fully documented HSM\-backed key lifecycle \(generation/rotation/revocation\) is only partially defined\. For SSL certificates, we follow annual renewal cycles as part of our online security policy\.

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section II: Complete Autonomous Control of Data Access Permissions \- User\-managed access keys, encryption keys, permission configuration; Complete Autonomous Control of Backup Encryption \- User\-selected algorithms, key generation, encryption strength 

28. **Do you operate a SOC or equivalent detection tools? **\(Evidence required: SOC charter, SIEM screenshot, EDR deployment report\.\)

    Yes, security operations capabilities through AWS GuardDuty for intrusion detection, AWS WAF for application protection, real\-time monitoring with Grafana Loki and AWS CloudWatch, H3C SecPath Intrusion Prevention System with thousands of active detection signatures, and continuous network traffic monitoring\.

    Supporting Materials:

    - [《On\-Premises Network Security Infrastructure \(Huawei \& H3C\)》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-RzXWdDQ7CotKszx767DcNoxUnle)

        - H3C SecPath F1000\-E\-XI Intrusion Prevention System \(IPS\) Signature Library with CVE\-related exploit signatures, attack categorization, severity levels; H3C SecPath Firewall Operation Monitor Dashboard showing real\-time system resource usage and session statistics

    - 《AWS Network Security Configuration》

29. **Do you use threat intelligence feeds to improve monitoring?** \(Evidence required: TI subscription proof, SOC reports\.\)

    Yes, we subscribe to up\-to\-date threat intelligence feeds for malware and exploit activity and integrate real\-time CVE vulnerability repositories into Trivy container scanning for proactive security posture management\. 

    Supporting Materials:

    - [《Container Vulnerability Management》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EajmdX9ZdoXeKWxpxoOcFdMXnNe)

        - Harbor Vulnerability Scanner using latest real\-time CVE vulnerability repository through Trivy automation tool; Component\-Level Vulnerability Scan showing integration with current vulnerability databases and threat intelligence for container security

30. **Do you run independent penetration tests at least annually?** \(Evidence required:  Pentest report \(redacted\), remediation plan\.\)

    Yes, independent penetration tests are conducted at least annually \(in practice bi\-annual\) by third\-party security experts following OWASP standards, and all identified vulnerabilities are remediated during the testing period\.

    Supporting Materials:

    - [《ChemAIRS Penetration Test Report》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-RYn1dB9yMoWkVqx8prCcrCWvnhr)

        - Independent penetration testing by Zhiwang Anyun \(third\-party security firm\), OWASP\-Based Framework covering authentication, session management, data validation, denial of service, comprehensive coverage of 11 major test categories including XSS and SQL injection, 3 vulnerabilities found \(all marked as "Fixed" and "Good" risk level\), overall assessment of "Strong security protection measures"

31. **Do you enforce secure baseline configurations \(CIS, NIST\)?** \(Evidence required:  Baseline config doc, hardening checklist\.\) Note \(CIS = Center for Internet Security, NIST = National Institute of Standards and Technology\)

    No, we do not maintain explicit CIS/NIST baseline documents, but we implement security hardening through ISO 27001 controls, non\-privileged container execution \(nobody user\), endpoint security with audit software, and internal secure coding standards\.

    Supporting Materials:

    - [《Container Vulnerability Management》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EajmdX9ZdoXeKWxpxoOcFdMXnNe)

        - 17\.4: Application Pod Running with Non\-Privileged User \(nobody\) confirming containers run as restricted, non\-privileged system users instead of root

    - [《Information Security Management Policy Handbook》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EvOAdgUvuogCQsxIXmsc9yP0nBd)

        - ISO 27001 compliance framework with comprehensive security policies covering access control, backup, privileged access management, and mobile device management

32. **Are privileged accounts controlled with MFA, session logging, vaulting?** \(Evidence required: PAM policy, tool screenshot, audit logs\.\)

    Yes, privileged accounts are individually approved with minimum\-rights principles, subject to comprehensive session logging and audit trails, governed by privileged access policies and quarterly reviews, and will be protected by MFA capabilities under our access\-control roadmap\. 

    Supporting Materials:

    - [《Information Security Management Policy Handbook》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-BcoLdeTEvoyxZGxi2xicC0F6ngg)

        - ISMS\-2\-CL\-003 Privileged Access Management Policy with rules for creating, using, controlling, and removing accounts with special access privileges; quarterly reviews for privileged users

    - [《ChemAIRS Admin Audit Log》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-XNr7d7P8aoDyExxl75CcHRTmn7e)

        - Comprehensive administrative audit trail capturing all privileged actions with username, timestamp, operation type, API request URL, parameters, and execution duration with downloadable records

33. **Have you adopted Zero Trust principles **\(least privilege, continuous verification\)? \(Evidence required: Zero Trust roadmap, implemented controls\.\)

    Yes, we partially implement Zero Trust principles through least\-privilege and minimum\-user policies, continuous monitoring with real\-time alerts, strict network segmentation and internal\-only access for core services, and tenant\-isolated RBAC for SaaS\. 

    Supporting Materials:

    - [《Information Security Management Policy Handbook》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-BcoLdeTEvoyxZGxi2xicC0F6ngg)

        - ISMS\-2\-CL\-012 Access Control Policy implementing minimum privilege and minimum user principles with quarterly reviews for privileged users

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section II: Multi\-tenant isolation, privilege separation, continuous monitoring with multi\-level alerts, and session\-based identity verification

    - [《H3C SecPath Firewall Security Policy Table Showing Zone\-Based Access Rules》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-JjR1dhibkoqK6nxA2MrcgLL7n3e)

    - [《PostgreSQL Role Privilege Configuration \(Read\-Only Access Controls\)》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-LTsJdrHFWoFjJmxHgUocZXK1nNc)

    - [《JumpServer User Account Management and Access Governance》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-C2MOddeUBo8ZZdxpMBacW7tin2c)

34. **Do you embed security in SDLC \(SAST, DAST, secure code review\)? **\(Evidence required: SDLC policy, SAST/DAST report, code review logs\.\)

    Yes, we embed security in the SDLC using SonarQube SAST in CI/CD, Trivy container scanning, OWASP\-aligned testing, mandatory peer reviews, and quality\-gate enforcement that blocks merges/releases until security criteria are met\.

    Supporting Materials:

    - [《Development Security Pipeline》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-LviPdBwOYobntJxJfHtcoWfpnYb)

        - 18\.1: GitLab CI Pipeline Log showing SonarQube Static Code Analysis execution with quality gate status PASSED, scanning \~1389 source files with secret detection and code quality checks

    - [《Chemical\.AI Security Development Principles and Coding Standards》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-MtcmdGTcboF6bsxp9AgcS4J6nAd)

        - Software Security Development Lifecycle \(SDL\) integrating security into every development phase: requirements, design, coding, testing, and maintenance

35. **Do you secure APIs with authentication, authorization, and monitoring?** \(Evidence required: API gateway config, API security test results\.\)

    Yes, APIs are secured via mandatory X\-Api\-Key authentication, server\-side validation with HTTP 401 responses for invalid credentials, parameterized queries, RBAC\-based authorization, and detailed logging of API activity for monitoring and auditing\. 

    Supporting Materials:

    - [《Postman Request ‒ Timeout / 401 / 200》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CoxGdI2QaoyMdCxcJnOcFVz2nxh)

        - API authentication testing showing ChemAIRS API requires valid X\-Api\-Key for access, timeout due to missing/invalid API key, HTTP 401 Unauthorized response for invalid credentials proving API\-level access control

    - [《ChemAIRS Admin Audit Log》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-XNr7d7P8aoDyExxl75CcHRTmn7e)

        - Audit log capturing API request URLs, parameters, and execution duration for all administrative activities with comprehensive monitoring

36. **Do you apply security controls for cloud services \(CSPM, CASB\)?** \(Evidence required: Cloud security policy, CSPM report\.\)

    Yes, cloud security controls through AWS native services including AWS GuardDuty for threat detection, AWS WAF for application protection, AWS CloudWatch for monitoring, VPC Network ACLs for traffic control, and security group configurations, though explicit CSPM/CASB tools not documented\.

    Supporting Materials:

    - [《AWS Network Security Configuration》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CGaOd54iUo5qsPxwL3Fc4OW0nab)\(Screenshots\)

        - 16\.2: AWS VPC Network ACL Configuration providing mandatory network\-level protection with inbound and outbound traffic rules enforcing organizational policies for allowed or restricted communication

37. **Are mobile devices managed with security controls \(encryption, remote wipe\)?** \(Evidence required: MDM policy, screenshot of enrolled devices\.\)

    Yes, mobile devices are governed via mobile\-device and endpoint policies requiring password protection, restricting storage of important data, and limiting wireless communications to approved protocols, complemented by network segmentation that restricts personal device access, though full MDM with encryption and remote wipe is only partially documented\. 

    Supporting Materials:

    - [《Information Security Management Policy Handbook》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-Ecr3daWVro4X0axe3pNcTLLTnfc)

        - ISMS\-2\-CL\-011 Mobile Device Management Policy establishing rules for mobile device use including password protection requirements, prohibition on storing important data on mobile devices, and wireless data transmission restrictions to approved protocols only

    - [《User Endpoint Policy Enforcement Overview》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-QksXdpURFoiESlxgWNHc2gXPnQx)

38. **Are backups encrypted, segregated, immutable, and regularly tested?** \(Evidence required: Backup policy, test restoration report\.\)

    Yes, backups are protected with AES\-256 encryption for local backups, TLS 1\.2\+ with AES\-256 for remote DR, dual\-layer retention \(7\-day local and 3\-month remote\), physical destruction after retention, and quarterly/bi\-annual restoration testing\.

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section III: Data Backup Strategy \- Section 8: Local Backup Management with AES\-256 encryption and automatic cleanup; Section 9: Remote Disaster Recovery with TLS 1\.2 \+ AES\-256 and physical destruction after 3 months; Section VI: Regular Assessment with quarterly backup testing

39. **Do you implement ransomware detection and recovery measures? **\(Evidence required: Anti\-ransomware policy, test evidence\.\)

    Yes, ransomware risk is mitigated via advanced hardware firewalls, AWS GuardDuty, continuous anomaly monitoring, antivirus and malware controls, encrypted multi\-copy backups across isolated availability zones, and DR procedures with defined RTO/RPO for rapid recovery\.

    Supporting Materials:

    - [《Information Security Management Policy Handbook》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-BcoLdeTEvoyxZGxi2xicC0F6ngg)

        - ISMS\-2\-CL\-006 Virus Management Policy with malware protection and continuous surveillance requirements

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section III: Dual\-layer backup protection with encrypted storage in multiple physically isolated availability zones; Section V: Business Continuity with RTO ≤4 hours and RPO ≤1 hour for rapid recovery from security incidents

40. **Do you have a tested cyber crisis response plan?** \(Evidence required: Crisis management playbook, simulation report\.\)

    Yes, we maintain a cyber crisis response plan with a professional incident response team, a defined emergency process \(incident categorization, assessment, isolation, mitigation\), bi\-annual emergency drills, regular plan updates, and explicit RTO/RPO objectives\.

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section V: Data Recovery and Emergency Response \- Section 16: Business Continuity with bi\-annual drills, regular plan updates; Emergency response process including steps for incident categorization, initial assessment, threat isolation and impact mitigation

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-25: Emergency Preparedness and Response Control Procedure establishing emergency response planning and preparedness procedures; ZHKJ\-QESP\-16: Communication Control Procedure covering crisis communication and emergency notification procedures

41. **Are systems configured for digital forensics investigations?** \(Evidence required: Forensics policy, log retention proof\.\)

    Yes, systems are configured to support digital forensics via encrypted log storage, ≥1\-year retention of system/application/security logs, restricted audit\-admin access, and detailed audit trails capturing user, timestamp, operation, API, and parameters\. 

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-GORudywdXoIN28xJKRqcVhlWnkc)

        - Section IV: Log Management \- Section 13: System/application/security logs with encrypted storage, 1\+ year retention, compliance requirements supporting forensic analysis

    - [《ChemAIRS Admin Audit Log》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-XNr7d7P8aoDyExxl75CcHRTmn7e)

        - Comprehensive administrative audit trail with downloadable records capturing all privileged actions including username, timestamp, operation type, API request URL, parameters, and execution duration

42. **Do you enforce access control for offices and datacenters?** \(Evidence required: Physical access policy, access logs\.\)

    Yes, physical access is controlled via role\-based access cards with multi\-level approvals, segregated access to sensitive areas, centralized card lifecycle management and logging, visitor restrictions, and AWS datacenter physical security for cloud workloads\.

    Supporting Materials:

    - [《Company Physical Access Control Security Management Procedures》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-Gi85dl6rfoBrYExBxyYc4SUcnVc)

        - Role\-based default permissions by department \(R\&D, Chemistry, Project Management, Business\), multi\-level approval workflow via Feishu for additional access requests, segregated access to sensitive areas \(labs, server rooms, executive offices\), granular zone\-based permissions with audit trail through card usage logging, immediate revocation upon termination or role changes

43. **Do you secure connected devices and industrial systems?** \(Evidence required: IoT/OT security policy, risk assessment\.\)

    Yes, although IoT/OT is limited, we secure endpoints and mobile devices with mobile\-device policies, password requirements, restrictions against storing important data, network segmentation, and endpoint audit software on company computers\. 

    Supporting Materials:

    - [《Information Security Management Policy Handbook》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-BcoLdeTEvoyxZGxi2xicC0F6ngg)

        - ISMS\-2\-CL\-011 Mobile Device Management Policy establishing rules for mobile device use including approved device requirements and wireless data transmission restrictions

    - 《User Endpoint Policy Enforcement Overview》

        - Centralized endpoint security system monitoring software usage, website access, USB and peripheral device access, file transfer risks, and time\-based workstation policy enforcement

44. **Do you track lessons learned from incidents and update security controls? **\(Evidence required: Post\-incident reports, improvement logs\.\)

    Yes, we track lessons learned via formal post\-incident investigation and improvement processes that analyze causes, define corrective and preventive actions, verify effectiveness, and feed results into continuous improvement\.

    Supporting Materials:

    - [《Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-24: Accident and Incident Investigation and Handling Control Procedure with post\-incident investigation and corrective action procedures; ZHKJ\-QESP\-14: Improvement Control Procedure defining systematic approach for continual improvement with metrics for measuring improvement effectiveness and sustainable implementation; ZHKJ\-QESP\-26: Corrective and Preventive Action Control Procedure with root cause analysis and effectiveness verification

45. **Do you report security KPIs and metrics to management? **\(Evidence required: Governance dashboard, KPI report\.\)

    Yes, we track and report security KPIs such as incident response times, vulnerability remediation rates, code vulnerabilities/security hotspots, and quality gate status using SonarQube dashboards, CloudWatch metrics, and internal reporting to management\. 

    Supporting Materials:

    - [《Development Security Pipeline》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-LviPdBwOYobntJxJfHtcoWfpnYb)

        - 18\.3: SonarQube Dashboard showing OWASP\-aligned code quality and security metrics with new bugs, vulnerabilities, security hotspots tracking and quality gate indicators demonstrating mature security governance

    - [《AWS Network Security Configuration》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CGaOd54iUo5qsPxwL3Fc4OW0nab)\(Screenshots\)

        - 16\.3\.2: AWS CloudWatch Container Insights Dashboard aggregating operational telemetry with metrics, events, and anomaly detection across all workloads providing comprehensive monitoring and reporting capabilities for management oversight

---

# IT Quality Questionnaire

### Organisation / Quality and Safety Management

46. **Is there a quality structure?  What are its roles and responsibilities?  How many people?**

    Yes, Chemical\.AI has an established quality management structure with defined roles and responsibilities:

    - Assessment Team: CEO/Data Security Administrator \(Risk Owner\), DevOps Manager and Development Leaders \(Technical Assessors\), Operations and customer\-facing staff \(Business Stakeholders\), plus External Validation through third\-party assessors \(annual\)

    - Quality Management Team: Dedicated team performing regular security vulnerability scans and testing, separate from development team

    - Code Security Team: Reviews daily vulnerability reports and submits issues to code owners for repair

    - Information Security Team: Data Protection Officer \(DPO\) and security management team

    Supporting Materials:

    - [《ChemAIRS Information Security Risk Assessment Methodology》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-DH1rdd1dDoqHOuxfaZqcohXhnKd)[\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-DH1rdd1dDoqHOuxfaZqcohXhnKd)

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-Anh3d5Qvgo2TqpxWqoMcZngvnPf)[\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-Anh3d5Qvgo2TqpxWqoMcZngvnPf)

47. **What method or guideline do you use for quality management? What is the specific procedure you follow?**

    Chemical\.AI follows multiple quality management frameworks:

    - ISO Standards: ISO 9001 and ISO 27001:2022 certified \(valid through December 21, 2027\)

    - Quality Management System: 29 documented procedures \(ZHKJ\-QESP\-01 through ZHKJ\-QESP\-29\) covering core quality processes

    - Software Development: Software Security Development Lifecycle \(SDL\) integrating security into every development phase \(requirements, design, coding, testing, maintenance\)

    - OWASP Standards: Following OWASP Top 10, OWASP ASVS for secure coding recommendations

    Supporting Materials:

    - 《Chemical\.AI ISO27001 EXP2027》

    - 《Chemical\.AI Security Development Principles and Coding Standards》

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-Anh3d5Qvgo2TqpxWqoMcZngvnPf)[\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-Anh3d5Qvgo2TqpxWqoMcZngvnPf)

48. **How long has your quality management guideline been in place?**

    Current ISO 27001:2022 certification was issued on December 16, 2024, with previous certifications showing ongoing quality management since at least 2022\.

49. **Have you set specific quality goals? If so, how are they specified and tracked internally? Do you use internal quality standards? What processes are covered by these standards?**

    Yes, Chemical\.AI has established specific quality goals and tracking mechanisms:

    Quality Metrics Tracked:

    - New vulnerabilities: 0 \(SonarQube dashboard\)

    - Security Hotspots: 0

    - Quality Gate: PASSED status

    - Code coverage, reliability, and maintainability ratings

    - Performance metrics including incident response times and vulnerability remediation rates

    Internal Quality Standards Cover:

    - Document Control \(ZHKJ\-QESP\-01\)

    - Risk Management \(ZHKJ\-QESP\-15\)

    - Data Analysis and KPI measurement \(ZHKJ\-QESP\-13, ZHKJ\-QESP\-22\)

    - Continuous Improvement \(ZHKJ\-QESP\-14\)

    - Customer Satisfaction Measurement \(ZHKJ\-QESP\-10\)

    Supporting Materials:

    - [《Quality Management System Procedures Compilation》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-YWhpdKTj5oJx53xloZZc1PfWnGc)

    - [《Development Security Pipeline》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-RpB0dF5ssoYPNKxLx9CcSRZjnZc)

50. **How are your activities documented? Please provide examples\.**

    Comprehensive documentation system with multiple levels:

    Examples of Documentation:

    - Vulnerability Reports: Daily vulnerability reports reviewed by code security team

    - Audit Logs: All testing and deployment activities logged and retained for auditing

    - Code Analysis Reports: Static code analysis with SonarQube \(27,694 lines analyzed\)

    - Test Reports: ChemAIRS System Test Report \(Version 3\.5\.0\) with 44 major functional tests, 100% pass rate

    - Penetration Test Reports: Annual third\-party assessment \(ZWAY\-PET\-202508\-01\)

    - Quality Records: Document control with version management, retention schedules, and master lists

    Supporting Materials:

    - [《ChemAIRS\-backend Code Analysis Report》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-ToQxdQOV1oklODxoezBcCX98nGe)

    - [《ChemAIRS Penetration Test Report》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NkCYdDu1soNpUIxLyPwcmHdXnDd)

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-OIcjdcR2hotYqlxyiLQcyfzYnme)[\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-OIcjdcR2hotYqlxyiLQcyfzYnme)

        - ZHKJ\-QESP\-01 \(Document Control Procedure\), ZHKJ\-QESP\-02 \(Record Control Procedure\)

51. **How does the document workflow \(writing, review, approval\) work?**

    Structured document workflow with multiple approval levels:

    Document Control Process \(ZHKJ\-QESP\-01\):

    - Systematic approach for document creation, approval, distribution, and maintenance

    - Document identification and version control

    - Obsolete document management

    - Master lists and distribution records

    Code Review Workflow:

    - Dual approval requirement: Development lead AND Data security lead review

    - Only current, approved documents used throughout organization

    - External documents control \(standards, regulations, customer specifications\)

    - Configuration changes require internal modification approval process

    Supporting Materials:

    - [《ChemAIRS\-backend Code Analysis Report》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-ToQxdQOV1oklODxoezBcCX98nGe)

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-OIcjdcR2hotYqlxyiLQcyfzYnme)

        - ZHKJ\-QESP\-01 \(Document Control Procedure\)

52. **How are staff trained \(general training, training in best practices, quality, safety, traceability, review\)?**

    Comprehensive training program with multiple components:

    Training Management \(ZHKJ\-QESP\-29\):

    - Systematic approach for training planning, delivery, and evaluation

    - Competency\-based training programs and certification requirements

    - Training record maintenance and competency verification

    - Orientation, technical skills, safety training, and ongoing professional development

    Specific Training Areas:

    - Security Awareness: Bi\-annual mandatory training for all employees

    - Technical Skills: Specialized training for key positions

    - Emergency Preparedness: Emergency drills and response training

    - Quality Training: Regular security bulletins and best practices

    - Training Effectiveness: Evaluation and continuous improvement

    Supporting Materials:

    - [《ChemAIRS SaaS Environment Data Security Management Regulations》\(Doc\)](https://chemical-ai.feishu.cn/wiki/HBgBwwBPwiutYLkfn7hcbbqbnHz)

        - Section VI Section 19 \(Training and Education\)

    - [《Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-29 \(Training Management Control Procedure\)

53. **How do you verify that your subcontractors meet your quality standards \(e\.g\., through audits or periodic reviews\)?**

No subcontractors used \- all software developed in\-house\. However, supplier management procedures exist\.

54. **Do you have a validation process in place that identifies and manages risks associated with the critical functions of your products or services?**

    Yes, comprehensive risk management and validation processes:

    Risk Management Framework \(ZHKJ\-QESP\-15\):

    - Risk identification, assessment, and management processes

    - Risk criteria, evaluation methods, and treatment strategies

    - Risk monitoring, review, and communication activities

    - Risk registers with historical scores and year\-over\-year trend analysis

    - Control effectiveness measurements

    Validation Processes:

    - Design and Development Control \(ZHKJ\-QESP\-06\): Design input requirements, review stages, verification activities, validation requirements

    - Risk Assessment: Annual comprehensive assessment \(mandatory\), plus assessments for major system changes, security incidents, and regulatory changes

    - Quality Controls: Independent review by Data Security Administrator, cross\-validation with automated tools, stakeholder review sessions

    Critical Functions Covered:

    - Authentication and session management

    - Data validation and integrity

    - Network security and access controls

    - Backup and disaster recovery

    - Compliance with pharmaceutical industry standards

    Supporting Materials:

    - [《ChemAIRS Information Security Risk Assessment Methodology》](https://chemical-ai.feishu.cn/docx/EXHKdKe7Jof8DCxBTn6cEZ6gnVg)\(Doc\)

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-06 \(Design and Development Control Procedure\), ZHKJ\-QESP\-15 \(Risk Control Procedure\)

### Project Planning / Management

55. **Is the project management methodology referenced in a procedure?**

    Yes, project management methodology is referenced in multiple quality management procedures

    Project Management Components:

    - Design and Development Control Procedure \(ZHKJ\-QESP\-06\) \- Controls design and development of new products and services

    - Product Realization Control Procedure \(ZHKJ\-QESP\-08\) \- Controls overall product realization process from planning to delivery

    - Risk Control Procedure \(ZHKJ\-QESP\-15\) \- Controls improvement project planning, implementation, and monitoring

    - Communication Control Procedure \(ZHKJ\-QESP\-16\) \- Establishes internal and external communication processes

56. **How are projects managed \(definition of activity, processes, documentation, responsibilities\)? Provide quality and project plan templates if not attached to the business proposal\.**

    Systematic project management through multiple control procedures

    Project Management Elements:

    - Process planning, resource allocation, and workflow management

    - Design input requirements, review stages, and verification activities

    - Project planning, implementation, and monitoring with defined metrics

    - Stakeholder communication and expectation management

    - Document identification, version control, and approval processes

    Supporting Materials:

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-06, ZHKJ\-QESP\-08, ZHKJ\-QESP\-14, ZHKJ\-QESP\-16

57. **How is the planning and monitoring of the project carried out \(tools, reports\)?**

    Comprehensive monitoring and reporting framework

    Planning and Monitoring Tools:

    - GitLab CI/CD pipeline for development workflow tracking

    - SonarQube for code quality monitoring and reporting

    - AWS CloudWatch for infrastructure monitoring

    - Risk Assessment Worksheet and Asset Inventory Template

    - Quarterly reports to internal stakeholders

    - Annual comprehensive reviews for customers

    Supporting Materials:

    - [《ChemAIRS Information Security Risk Assessment Methodology》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-DH1rdd1dDoqHOuxfaZqcohXhnKd)

    - [《Development Security Pipeline》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CfwEdDqTsoSkNhxNEoFcFXdnndh)

### Software Development

58. **Who reviews the program code and how?**

    Multi\-layered code review process with defined roles and responsibilities

    Code Review Team Structure:

    - Code Security Team \- Reviews daily vulnerability reports

    - Development Lead \- Required approval for all changes

    - Data Security Lead \- Required approval for all changes \(dual approval system\)

    - Quality Management Team \- Performs independent security vulnerability scans

    Review Process:

    - SonarQube integrated into CI/CD for automated code analysis

    - Mandatory peer review before merge approval

    - Vulnerabilities identified in daily reports reviewed by code security team

    - Only after repair completion will merge\-in request be approved

    Supporting Materials:

    - [《Development Security Pipeline》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CfwEdDqTsoSkNhxNEoFcFXdnndh)

    - [《Chemical\.AI Security Development Principles and Coding Standards》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-MtcmdGTcboF6bsxp9AgcS4J6nAd)

59. **For each stage of development, what is the testing strategy?**

    Comprehensive testing strategy across all development phases

    Development Testing Stages:

    - Structure Test \(White Box\): Static code analysis, mandatory peer review, unit testing, security testing verification

    - Module Testing: Database layer validation, middleware component testing, API endpoint validation

    - Integration Testing: End\-to\-end workflow testing, system integration validation

    - Security Testing: SonarQube SAST, Trivy container scanning, penetration testing

    - Pre\-release Testing: Deployed in test clusters replicating production settings

    Testing Tools and Methods:

    - SonarQube for static application security testing \(SAST\)

    - Trivy for container vulnerability scanning with real\-time CVE database

    - Annual third\-party penetration testing

    - Quality management team performs regular security vulnerability scans

    Supporting Materials:

    - [《Development Security Pipeline》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CfwEdDqTsoSkNhxNEoFcFXdnndh)

    - [《Container Vulnerability Management》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EajmdX9ZdoXeKWxpxoOcFdMXnNe)

    - [《ChemAIRS Penetration Test Report》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CLJAdko8Wo1BtXxFkUxcgwUWnzg)  

60. **Which project documents vary depending on the project concerned \(general design, functional specifications, etc\.\)? Give examples\.**

    Project documentation varies based on scope and requirements

    Variable Project Documents:

    - Design input requirements and specifications \(project\-specific\)

    - Risk Assessment Worksheet \(tailored to project scope\)

    - Asset Inventory Template \(project\-specific assets\)

    - Design output documentation and validation requirements

    - Design history files \(maintained per project\)

61. **How are software components managed \(identification, version, author\)?**

    Comprehensive software component management through version control and documentation

    Component Management System:

    - GitLab CI/CD pipeline with version tracking

    - Document identification and version control procedures

    - Container image management with Harbor repository

    - Admin audit log capturing all component changes with timestamps and user identification

    Version Control Features:

    - Systematic document creation, approval, distribution, and maintenance

    - Version control with obsolete document management

    - Master lists and distribution records for all controlled documents

    - Container images tagged and tracked through CI/CD pipeline

    Supporting Materials:

    - [《Development Security Pipeline》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CfwEdDqTsoSkNhxNEoFcFXdnndh)GitLab CI Pipeline

    - [《ChemAIRS Admin Audit Log》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-XNr7d7P8aoDyExxl75CcHRTmn7e)\(Screenshots\)

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-01 Document Control Procedure

62. **How are components of an application release identified and tracked?**

Systematic release tracking through automated pipeline and audit logging

Release Component Tracking:

- GitLab CI/CD pipeline tracks all release components

- Container images built and versioned for each release

- Trivy scanning performed on all release images

- Admin audit log records all release activities with full traceability

Release Management Process:

- Code artifacts built as container images

- Pre\-release deployment in test clusters

- Harbor repository management for container versioning

- Quality management team validation before production release

Supporting Materials:

- [《Development Security Pipeline》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-CfwEdDqTsoSkNhxNEoFcFXdnndh)GitLab CI Pipeline

- [《ChemAIRS Admin Audit Log》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-XNr7d7P8aoDyExxl75CcHRTmn7e)\(Screenshots\)

- [《Container Vulnerability Management》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EajmdX9ZdoXeKWxpxoOcFdMXnNe)

63. **How are your products designed and configured to comply with pharmaceutical agency regulatory requirements for electronic registrations and signatures?**

    Pharmaceutical regulatory compliance through comprehensive governance and validation frameworks

    Regulatory Compliance Framework:

    - ISO 27001:2022 certification covering pharmaceutical industry standards

    - GDPR\-compliant data processing agreement template

    - Comprehensive audit trail with electronic signature capabilities

    - Data sovereignty and complete customer control options

    Electronic Records and Signatures Support:

    - Admin audit log with complete traceability \(username, timestamp, operation type\)

    - Document control procedures ensuring regulatory compliance

    - Legal and regulatory identification and update control procedures

    - Compliance evaluation control procedures with systematic monitoring

    Pharmaceutical\-Specific Features:

    - Local deployment option providing complete customer control

    - Data Processing Agreement addressing pharmaceutical data protection requirements

    - Risk assessment methodology aligned with pharmaceutical industry standards

    - Quality management procedures designed for regulatory environments

### Project Delivery  / Completion 

64. **How are the software and documents related to the delivered version archived?**

Comprehensive archiving system through document control and record management procedures

Software and Document Archiving Components:

- Document Control Procedure \(ZHKJ\-QESP\-01\) \- Systematic approach for document creation, approval, distribution, and maintenance

- Record Control Procedure \(ZHKJ\-QESP\-02\) \- Creation, identification, storage, and retention of quality records

- GitLab CI/CD pipeline maintaining version history and build artifacts

- Harbor repository for container image archiving with versioning

- Admin audit log providing downloadable records with full traceability

Supporting Materials:

- [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

- [《ChemAIRS Admin Audit Log》](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-XNr7d7P8aoDyExxl75CcHRTmn7e)\(Screenshots\)

65. **Is the archiving methodology recorded in a procedure \(process, functional control, traceability of the actions implemented\)?**

    Yes, archiving methodology is formally documented in multiple procedures with comprehensive traceability

    Documented Archiving Procedures:

    - Document identification, version control, and obsolete document management

    - Master lists and distribution records for all controlled documents

    - Record legibility, retrievability, and protection requirements with retention periods

    - Electronic and physical record storage systems with disposal procedures

    - Comprehensive administrative audit trail capturing all actions with timestamps

    Supporting Materials:

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-01, ZHKJ\-QESP\-02

66. **What is the method of delivery of a product \(methodology, control, documentation to be given to the customer for the delivery of qualified components in a qualified environment, proof of adequate functional tests\)?**

    Systematic product delivery methodology with comprehensive documentation and testing validation

    Product Delivery Methodology:

    - Product Realization Control Procedure \(ZHKJ\-QESP\-08\) \- Controls overall product realization process from planning to delivery

    - Production and Service Control Procedure \(ZHKJ\-QESP\-09\) \- Controls production operations and service delivery processes

    - Customer Communication Control Procedure \(ZHKJ\-QESP\-05\) \- Manages contract review, order processing, and delivery coordination

    Quality and Testing Documentation:

    - Pre\-release environments deployed in test clusters replicating production settings

    - Comprehensive functional testing with documented test results and validation

    - Container vulnerability scanning and security validation before release

    Supporting Materials:

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-05, ZHKJ\-QESP\-08, ZHKJ\-QESP\-09

    - [《Container Vulnerability Management》\(Screenshots\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-EajmdX9ZdoXeKWxpxoOcFdMXnNe)

### Support / Maintenance 

67. **What is the process for handling anomalies and customer requests \(identification, traceability, resolution, delivery\)?**

    Comprehensive anomaly and customer request handling process with systematic identification and resolution

    Anomaly and Request Handling Process:

    - Customer Communication Control Procedure \(ZHKJ\-QESP\-05\) \- Systematic approach for customer interaction and handling inquiries, feedback, and complaints

    - Nonconforming Product Control Procedure \(ZHKJ\-QESP\-12\) \- Controls identification, segregation, and disposition of nonconforming products

    - Vulnerability management process with daily reports reviewed by code security team

    Traceability and Resolution:

    - All ChemAIRS application level vulnerabilities notified to administrators via email

    - Hotfix and new releases provided by administrators via email

    - Complete audit trail with username, timestamp, operation type, and resolution tracking

    Supporting Materials:

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-05, ZHKJ\-QESP\-12

68. **How are support calls handled \(process, time slot\)?**

    Structured support call handling process with defined communication procedures

    Support Call Handling:

    - Customer Communication Control Procedure \(ZHKJ\-QESP\-05\) \- Establishes systematic approach for customer interaction and communication

    - Effective two\-way communication channels with customers

    - Email notification system for vulnerability and support issues

    - Dedicated business manager contact for individual client communication

    Supporting Materials:

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-05

69. **How are customer complaints handled?**

    Systematic customer complaint handling with comprehensive tracking and resolution procedures

    Customer Complaint Handling Process:

    - Customer Communication Control Procedure \(ZHKJ\-QESP\-05\) \- Defines processes for handling customer inquiries, feedback, and complaints

    - Customer Satisfaction Measurement Control Procedure \(ZHKJ\-QESP\-10\) \- Customer feedback collection, analysis, and reporting processes

    - Customer surveys, complaint analysis, and satisfaction metrics tracking

    - Trending analysis and improvement action planning based on complaints

    - Systematic approach to understanding customer perceptions and resolving issues

    Supporting Materials:

    - [《程序文件\(汇编\) \- Quality Management System Procedures Compilation》\(Doc\)](https://chemical-ai.feishu.cn/docx/GB5ZdqRBMoTyKbxwzhncw5MEnee#share-NktHd8JRGoiYlGxGwWlczxkYnJe)

        - ZHKJ\-QESP\-05, ZHKJ\-QESP\-10



