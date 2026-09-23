# Jazz\_questionnaires

## Can you please outline how this search is completed / what is the technical basis for the search and retrieval? Also is the literature sourced from Chemical AI curated sources? … or from external sources? … or both?

We search literature references based on molecular similarity and reaction similarity\. The literature source is curated by [Chemical\.ai](http://chemical.ai/)\. It is a collection of patents, peer\-reviewed journals, and some other databases we have purchased and have the right to include in our reaction data\. Together, it's close to a hundred million reaction data, and all of them are transferred to Jazz's server during the installation phase, so it stays on your server\. We update our databases to capture the latest reactions twice a year, and we will put the new data in your server when we do the annual update\. 

## Will the Jazz data/corpora be used to further train or improve the proprietary machine learning models in CHEMAIRS and how can this be verified?

No\. You do not share any data with us, because Jazz's version of CHEMAIRS is hosted in your own server\. We have zero access to your data\. 



## Do you use metadata or telemetry for model improvement?

No\. Our algorithm improvement is independent from any client engagement\. 



## Describe the technology components and applications of the proposed solution \(e\.g\. Bedrock, Dataiku, Redshift, Veeva, LLMs\)

ChemAIRS is a self\-contained chemistry R\&D platform\. It is not built on Bedrock, Dataiku, Redshift, or Veeva, and does not require integration with any of them\. All models are proprietary to [Chemical\.AI](http://chemical.ai/) and are packaged with the application\. No LLM is used at this moment\. 

**Components \(not all applicable to Jazz, depending on the licensed modules\):**

- **Retrosynthetic analysis engine\.** Proprietary machine learning models \(reaction template extraction plus neural ranking\) trained on curated public and licensed reaction corpora, generating multiple synthetic routes per target with scoring on route viability, cost, and step count\.

- **Forward synthesis prediction and synthesizability \(SA\) scoring\.** Predicts likely products and rates how readily a proposed structure can be made\.

- **Impurity prediction\.** Flags probable side products ahead of analytical work\.

- **Process chemistry module\.** Cost accounting, solvent and reagent assessment, and scale\-up considerations at the route level\.

- **Bayesian optimization\.** Reduces the number of experimental rounds required to reach target reaction conditions\.

**Deployment and security:** ChemAIRS is available as a local \(on\-premise or private VPC\) deployment behind the customer's firewall, which is how the majority of our pharma customers run it\. AES\-256 encryption at rest and in transit\. Role\-based access control\. ELN integration via API\. In a local deployment, no structures, routes, or usage data are transmitted to [Chemical\.AI](http://chemical.ai/)\.

**Applications:** route scouting and feasibility assessment before lab commitment, COGS and process optimization for scale\-up, impurity troubleshooting, building block sourcing strategy, and CRO quoting\.

**Model transparency:** the core prediction engine does not depend on generative LLMs\. Outputs are traceable to reaction precedent, and each proposed step can be inspected against the literature or patent reaction it derives from\. This matters for validation: the system is auditable rather than opaque\.

## Does any of the following apply to the AI use case:

## a\. Involves employment and worker management, e\.g\. CV/Resume review, Annual Employee Review, Promotion/Bonus assessment

## b\.           Uses biometric identification or information, e\.g\. race, political opinions, trade union membership, emotional state, social scoring, religious or philosophical beliefs, sex life or sexual orientation

## c\.            Confidential, proprietary or personal data entered into the system\. This applies to Jazz information or third\-party information, including clinical trial data\.

## d\.           Diagnostic programs used to determine disease and treatment

## e\.            Algorithm design with risk of bias in development

## f\.             Automated decision making

## g\.            If “No” to the statements above, is there a risk that the AI use case could otherwise be viewed as posing a risk of harm to the health, safety, or rights of individuals, including by materially influencing the outcome of human decision making?

## h\.           If a vendor will be providing the AI tool, does the contract address who owns the data that is input into the system, the vendor's rights to / limitations on re\-use of such data, and whether Company's data can be used to further develop the vendor's algorithms for use with other customers?

## i\.             If a vendor will be providing the AI tool, are Company’s rights with respect to ownership, use, and disclosure of the AI tool outputs clear?

**No\.** ChemAIRS has no application to hiring, performance, promotion, or compensation decisions\. It does not process employee data of any kind\.

**b\. Biometric identification or protected\-category information: No\.** The system operates exclusively on chemical structures, reaction data, and supplier catalog information\. It does not ingest, infer, or process biometric data or any protected personal characteristic\.

**c\. Confidential, proprietary, or personal data entered into the system: Yes, confidential and proprietary data stored on Jazz's own server\. No personal data, and no clinical trial data\.** Users input molecular structures, which for a pharma customer are typically proprietary and pre\-disclosure\. In a local deployment, all input structures, generated routes, and project data remain entirely within Jazz's environment\. [Chemical\.AI](http://chemical.ai/) has no access to them, no telemetry is transmitted, and no customer data is available to us for any purpose, including model training\. Data at rest and in transit is AES\-256 encrypted, with access governed by the customer's own controls\. ChemAIRS is not designed for and does not require patient data, clinical data, or any personal information\.

**d\. Diagnostic programs to determine disease or treatment: No\.** ChemAIRS is a synthesis planning and process chemistry tool\. It has no diagnostic, clinical, or treatment\-related function, makes no claims about efficacy or safety in patients, and is not a medical device\.

**e\. Algorithm design with risk of bias in development: Limited, and not in the protected\-class sense\.** **No**\. 

**f\. Automated decision making: No\.** ChemAIRS is decision support\. It generates ranked options with supporting evidence; a chemist selects, modifies, or rejects them\. No experiment is initiated, no material is purchased, and no decision is executed by the system\. There is no autonomous action path and no automated decision affecting any individual\.

**g\. Other risk of harm to health, safety, or rights of individuals: No\.** The system does not touch individuals at any point\. It operates upstream of clinical work, on chemistry rather than people, and every output passes through qualified human judgment before it influences anything\. 

**h\. Contractual treatment of data ownership and vendor re\-use: No\. **Under our standard agreement, the customer retains full ownership of all data input into the system\. [Chemical\.AI](http://chemical.ai/) acquires no rights to that data, may not re\-use it for any purpose, and expressly may not use it to train, tune, or otherwise develop our models for use with other customers\. In a local deployment this is enforced architecturally as well as contractually, since the data never reaches us\.

**i\. Customer rights to AI tool outputs: Yes\.** The customer owns all outputs generated from its inputs, including routes, conditions, predictions, and reports, and is free to use, modify, and disclose them\.

