# Answers to Gilead Email Questions

1. **You indicated that PI is systematically destroyed, erased, or anonymized when it is no longer required\. Could you please provide details on the process or controls in place to ensure PI is securely deleted or destroyed once there is no longer a business or legal need to retain it?**

Customer data exists in two forms with different deletion strategies: Production Environment Data \- customers can delete their own data directly through the platform interface \(GDPR compliant\), and when a user's account is deleted, their production data is automatically deleted; Backup Data \- automatically destroyed after 7 days for local backups and 3 months for off\-site disaster recovery backups, ensuring complete data sanitization across all storage locations\.



2. **Regarding explicit or affirmative consent:**

    1. **Are individuals provided with a mechanism to change their preferences regarding the use of their PI? Please describe how this mechanism functions, or explain why it is not applicable\.**

    Yes, individuals can change their personal information usage preferences through: direct account settings for optional profile information \(user name, company details\)\. 

    

    2. **Are individuals able to withdraw consent they previously provided? If not, please explain why withdrawal of consent is not applicable\.**

    No, consent is required to access the platform and a previous consent cannot be withdrawn\. However, users can directly delete their production environment data themselves, and all backup data is guaranteed to be completely deleted within the established retention periods \(7 days for local backups, 3 months for off\-site disaster recovery backups\)\.

    

    3. **Please share the consent form or provide a link to the webpage where consent is obtained, if applicable\.**

    Consent is obtained through ChemAIRS's Privacy Policy at: [https://chemairs\.chemical\.ai/compliance/universal/privacy\-policy\.html](https://chemairs.chemical.ai/compliance/universal/privacy-policy.html)\. 

    Users must review the privacy policy "prior to accessing our Services" and provide express acknowledgment: "By proceeding to use our Services, you expressly acknowledge that you have read, understood, and consented to the terms set forth in this policy\." This ensures consent is obtained before or at the time of data collection in full GDPR compliance\.

    

3. **You indicated that there is a defined procedure or mechanism to ensure PI is accurate and kept up to date\. Could you please describe the process or mechanism in place?**

Users can directly update their own optional profile information through platform operations, with all backend data operations being idempotent and data consistency guaranteed through transactional mechanisms\. For organizational accounts, tenant administrators handle account adjustments and email updates with proper authorization\.



4. **You confirmed that individuals have access to their PI and the ability to correct, amend, or erase it\. Could you please explain the procedure used to support these requests?**

Users manage their own PI and can update their personal information directly through the platform interface\. We ensure that all operations follow GDPR\-compliant procedures\.



5. **Are there controls in place to ensure that access to PI is restricted to the minimum number of authorized individuals necessary?**

Yes, ChemAIRS implements comprehensive least privilege access controls: Environment Isolation with strict physical separation of production, development, and test environments plus network isolation through firewalls and VPN; Role\-Based Access Control \(RBAC\) with minimum required permissions for different user roles\. 



