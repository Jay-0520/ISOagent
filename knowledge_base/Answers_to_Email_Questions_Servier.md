# Answers\_to\_Email\_Questions\_Servier

#### As part of our security policies, we require the use of Single Sign\-On \(SSO\) for accessing our systems \(including SaaS applications\)\. Could you please confirm if your solution supports SSO integration?

Yes, ChemAIRS supports Single Sign\-On \(SSO\) integration with production\-ready Azure AD, support for SAML 2\.0 and OAuth 2\.0, manual user pre\-creation with SSO credential validation, LDAP\-based federated identity, and evaluation of other SSO providers on a case\-by\-case basis\. 

#### Do you work with any third parties? For data hosting, software development, or software support…

Yes, but with limited and clearly defined third\-party relationships: no subcontractors \(all software is developed in\-house\), AWS cloud infrastructure is used for hosting in SaaS deployments, independent third\-party penetration testing is conducted regularly, and the local\-deployment option eliminates third\-party data concerns\.

#### In which countries are your servers located and where will our data be hosted?

For SaaS, all customer data is hosted in the United States, specifically in the AWS North California \(us\-west\-1\) region, stored on AWS database servers with multi\-copy instances across different availability zones, and no SaaS data is stored outside the U\.S\.; customers needing data localization can instead select local deployment\. 

#### Could you please transfer the technical and functional documentation to us, including user manuals, technical architecture documents, and operational maintenance plans?

Yes, we provide technical and functional documentation as follows:

- ChemAIRS\_Local\_Deployment\_Instructions\.pdf

- System\_and\_Hardware\_Standards\_and\_Specifications\_for\_ChemAIRS\_Local\_Deployment\.pdf

### Access Management

#### Who is responsible of access management and access controls?

Yes, we operate a multi\-level access management structure where the CEO/Data Security Administrator provides overall governance, the Tenant Administrator manages customer\-side accounts and password resets, the Business Manager coordinates account creation and communication, the DevOps Manager implements technical access, and the Account Management Team assists with credential resets and verification\. 

#### How do you manage access controls?

Comprehensive access control is enforced through tenant\-level RBAC, individual account assignment with the minimum\-rights principle, privileged access requiring formal approval, multi\-factor authentication \(in development\), an account lockout policy after 5 failed attempts, and prohibition of shared accounts, with each account limited to one device\. 

#### Do you perform user accounts and access reviews, and if so, how frequently?

Yes, user accounts are subject to systematic and periodic reviews as defined in account management rules, ensuring individual IDs follow minimum\-rights principles, account usage and access patterns are regularly monitored, and tenant administrators oversee user lifecycle management\. 

#### Do you perform administrator accounts and access reviews, and if so, how frequently? With recertification?

Yes, administrator accounts undergo enhanced oversight, with privileged access individually assigned and approved, separated from regular users via tenants and RBAC, fully traceable to specific individuals through comprehensive audit logging, and governed by emergency access procedures requiring documented justifications and reviews\. 

#### If you manage several environments \(such as sandbox, training, etc\.\): is access review conducted for all available environments? Are test, training, or other accounts deleted if not used for more than a specific period, and are passwords reset regularly?

Yes, we manage DEV, Test, QA, and pre\-release environments on separate infrastructure with isolated test clusters, apply consistent access controls and periodic reviews across all environments, and enforce user account lockout and password complexity policies to manage dormant accounts and maintain security hygiene\. 



