# Esteve

### Physical access to DPCs granted only to minimum necessary personnel, and permits reviewed periodically?
Yes\. All data is stored in the US, in AWS data centres\. Physical access there is controlled entirely by AWS on a least\-privilege, business\-need basis with periodic review, attested in its SOC 2 Type II and ISO 27001 reports; no Chemical\.AI personnel have physical access\. Chemical\.AI staff access the environment only logically, via an internal private network \(VPC\) deployment with a limited set of authorised AWS management accounts\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are temperature, humidity, and other environmental factors monitored in real time?
Yes\. AWS continuously monitors environmental conditions in its data centres\. Chemical\.AI additionally monitors system\-level health in real time via AWS CloudWatch and self\-hosted Prometheus/Grafana\.

*Sources:* ESTEVE questionnaire, 2026-09

### Is there an early warning system in place?
Yes\. AWS operates automated environmental detection and alerting at the facility level\. On the Chemical\.AI side, CloudWatch and Prometheus/Grafana alerts route to our operations and incident response team, which follows a defined process for classification, assessment, isolation and mitigation\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are environmental protection systems subject to periodic tests and maintenance? How often?
Yes\. AWS tests and maintains data\-centre environmental and fire suppression systems on its documented schedule, verified annually by independent third\-party auditors \(SOC 2 Type II, ISO 27001\)\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are Uninterruptible Power Supply \(UPS\) and electric generators systems in place? How long can they operate?
Yes\. AWS data centres are equipped with UPS units for bridging power and backup generators for extended utility outages, with routine testing and preventive maintenance under AWS's audited operations\. Chemical\.AI does not operate this infrastructure; AWS's published data\-centre controls and SOC 2 Type II report are the authoritative source for specific runtime figures\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are the UPS systems and electric generators tested and maintained regularly? How often?
Yes\. AWS performs routine testing and preventive maintenance of UPS and generator systems as part of its data\-centre operations, verified annually by independent auditors under SOC 2 Type II and ISO 27001\. Chemical\.AI does not operate this infrastructure and defers to AWS's published control documentation for specific intervals\.

*Sources:* ESTEVE questionnaire, 2026-09

### Is access to DPCs limited to authorized personnel with dedicated access control methods? With two\-factor authentication?
Yes\. Physical access to AWS data centres is restricted to authorised personnel with a documented business need, using dedicated access control systems with multi\-factor authentication at controlled entry points\. No Chemical\.AI personnel have physical access to the facilities; our staff access the environment only logically, through an internal private network \(VPC\) deployment with a limited number of authorised AWS management accounts\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are physical access to DPCs granted only to minimum necessary personnel and are those access permits reviewed periodically?
Yes\. AWS grants data\-centre access on a least\-privilege, business\-need basis and reviews authorisations periodically, revoking them when no longer required\. This is covered by its SOC 2 Type II and ISO 27001 attestations\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are physical access to DPCs recorded at the employee entrance / exit and are those access logs reviewed periodically?
Yes\. AWS logs and monitors entry to and exit from its data centres, and those records are retained and reviewed as part of its audited physical security controls\.

*Sources:* ESTEVE questionnaire, 2026-09

### Is there a formal procedure for visitor access to the data centre?
Yes\. AWS operates a formal visitor procedure requiring prior authorisation, identification, sign\-in, and escort by authorised staff throughout the visit\. Chemical\.AI does not host or admit visitors to the production environment\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are physical access to DPCs monitored with video surveillance system \(CCTV\), alarms, or security guards?
Yes\. AWS data centres are monitored by professional security staff, CCTV surveillance, and intrusion detection and alarm systems at perimeter and interior access points, operating continuously\.

*Sources:* ESTEVE questionnaire, 2026-09

### Do you have in place infrastructure redundancy measures, such as: disk mirroring, RAID, internet redundancy connections, failover telecommunications systems, etc\.?
Yes\. ChemAIRS runs on managed high\-availability AWS services \(EKS, RDS\) with instance replicas distributed across multiple Availability Zones, providing automatic failover for compute, storage and database layers\. Storage redundancy, network path redundancy and telecommunications failover are provided at the platform level by AWS\. The distributed containerised architecture also allows the application to be rebuilt quickly in a new cluster if required\.

*Sources:* ESTEVE questionnaire, 2026-09

### Do you have a redundant DPC located at least 15km from the main one?
Yes in substance\. ChemAIRS is deployed across multiple AWS Availability Zones, which are discrete data centres in separate physical facilities with independent power, cooling and networking, separated by a meaningful physical distance within the region\. Off\-site disaster recovery backups are retained separately from the primary environment\. AWS does not publish exact inter\-AZ distances, so we can confirm physical separation but not a specific kilometre figure\.

*Sources:* ESTEVE questionnaire, 2026-09

### Is there a documented disaster recovery plan at the DPC?
Yes\. ChemAIRS maintains a documented disaster recovery approach based on multi\-AZ high\-availability services with rapid failover, backed by a two\-tier backup structure: a 7\-day rolling local backup plus a 3\-month off\-site disaster recovery copy\. In the event of a catastrophic failure, affected users are notified by email through the Ops system and the client's dedicated business manager makes individual contact with progress and resolution\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are recovery tests carried out in the DPC? How often are those drills performed? And are documented?
Yes\. According to AWS, emergency recovery and system rebuild exercises are performed periodically to verify backup recoverability and availability, with results recorded\.

*Sources:* ESTEVE questionnaire, 2026-09

### Are IT assets / hardware in the DPCs \(servers, disks, cabling, ports, racks, etc\.\) inventoried and labelled?
Physical hardware in AWS data centres is inventoried, tracked and managed by AWS throughout its lifecycle under its audited asset management controls; Chemical\.AI has no physical assets in those facilities\. Chemical\.AI maintains its own inventory of provisioned cloud resources managed as code through Terraform and Kubernetes manifests\.

*Sources:* ESTEVE questionnaire, 2026-09
