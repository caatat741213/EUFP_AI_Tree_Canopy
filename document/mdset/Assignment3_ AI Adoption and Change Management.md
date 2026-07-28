AI Adoption and Change Management
Objective:
The goal of this assignment is to assess your ability to:
•	Analyze stakeholder feedback and propose AI solution improvements.
•	Identify barriers to AI adoption and suggest mitigation strategies.
•	Develop a change management plan for AI deployment.
•	Build a prototype tool to track AI adoption and stakeholder feedback.
 
Part 1: Case Study Analysis (40 Marks)
Scenario:
Yu Bank recently implemented an AI-powered fraud detection system. However, after deployment, employees reported difficulties in trusting the system due to false positives. Additionally, customers raised concerns about incorrect fraud alerts on their accounts.
Tasks:
1.	Identify three key stakeholders affected by this issue and describe their concerns. (10 Marks)
2.	Suggest two methods for collecting feedback to improve the AI system. (10 Marks)
3.	Propose two technical improvements to enhance fraud detection accuracy. (10 Marks)
4.	Recommend one strategy to improve user trust and adoption of the AI system. (10 Marks)
 
Task 1: Identify three key stakeholders affected by this issue and describe their concerns. (10 Marks)
1. Bank Customers
•	Frustration with Erroneous Declines: The primary concern for customers involves "incorrect fraud alerts" that lead to the rejection of valid transactions. Wedge et al. (2017) estimated that approximately one in every six customers has experienced a legitimate transaction being declined within the past year, causing significant personal inconvenience.
•	Loss of Brand Loyalty: High false positive rates can permanently damage the relationship between a customer and the bank. Research indicates that after a false decline, 26% of shoppers reduce their spending at that merchant, while 32% stop shopping there entirely; similarly, customers may lose faith in their card issuer and switch to a competitor (Wedge et al., 2017).
•	Demand for Human Oversight: Customers generally do not trust AI to operate with total autonomy in high-stakes financial environments. TD Bank (2026) found that only 18% of consumers are comfortable allowing AI to make important financial decisions independently, while nearly half state that human review of AI guidance would increase their confidence.
2. Bank Employees and Fraud Analysts
•	Crisis of System Trust: Analysts find it "difficult to trust the system" because the high volume of false positives makes the AI's output seem unreliable. If the system lacks explainability, analysts cannot understand the "why" behind a flagged transaction, leading to a reluctance to use the AI's recommendations for high-stakes decisions (Financial Services Sector Coordinating Council [FSSCC], 2026).
•	Operational Inefficiency and Alert Fatigue: The industry struggles with an imbalance where only one in five transactions declared as fraud is actually fraudulent (Wedge et al., 2017). This forces analysts to waste time investigating meaningless alerts in 24/7 monitoring centers, which reduces overall operational effectiveness and causes "alert fatigue".
•	Preference for Human-Led Models: Employees are concerned about being replaced by black-box automation and prefer a "human-led, AI-enhanced" approach. TD Bank (2026) noted that most employees want AI to handle repetitive data processing while leaving final, critical decision-making authority in human hands.
3. Bank Management and the Organization
•	Financial and Revenue Impacts: Management is concerned about the tangible financial damage caused by "incorrect alerts". For every blocked sale, the bank loses out on interchange fees, which are typically assessed at 1.75% of the transaction value (Wedge et al., 2017). In many cases, the total value of falsely declined orders exceeds the actual cost of fraud itself.
•	Compliance and Regulatory Risks: Selvam (2025) argued that financial institutions are facing strict global requirements—such as the EU AI Act and U.S. fair lending laws—that mandate banks be able to justify automated decisions and prove they are non-discriminatory. If Yu Bank's system cannot provide clear explanations for alerts, the organization faces potential legal penalties and reputational harm.
•	Organizational Readiness Gap: There is often a "tension between capability and confidence," as technology typically advances faster than the organizational readiness required to manage it (TD Bank, 2026). Management must balance the drive for innovation with responsible implementation to ensure that AI projects achieve durable, mission-aligned results rather than stalling in the pilot phase (Ali et al., 2025).
 
Task 2: Suggest two methods for collecting feedback to improve the AI system. (10 Marks)
To address the "tension between capability and confidence" currently facing Yu Bank, the organization must implement structured feedback mechanisms that involve both technical validation and human expertise (TD Bank, 2026). Drawing from the provided sources, the following two methods are suggested to collect feedback and improve the AI fraud detection system:
1. Human-in-the-Loop (HITL) Expert Annotation and Propagation
The most effective way to improve the model's accuracy and restore employee trust is to integrate a Human-in-the-Loop (HITL) framework. This method leverages the domain knowledge of fraud analysts—referred to as Subject Matter Experts (SMEs)—to refine the AI's decision-making logic (Kadam, n.d.).
•	The Process: Analysts manually review transactions flagged as "fraudulent" by the AI. They provide a feedback signal, such as a "isFraud" label scaled from 0 to 100, based on their investigation (Kadam, n.d.). This feedback is not only used to correct individual errors but is also run through a feedback propagation algorithm that updates related transaction nodes in the bank’s data graph (Kadam, n.d.).
•	The Benefit: Research shows that even small amounts of expert feedback can significantly boost model performance, particularly in reducing false positives and helping the model adapt to evolving fraud patterns (Kadam, n.d.). By allowing analysts to "coach" the system, Yu Bank can transition from a "black-box" model to a "human-led, AI-enhanced" model, which is the preferred standard for both employees and consumers (TD Bank, 2026).
2. Implementation of Customer Explanation and Contestation Interfaces
Since Yu Bank's customers are concerned about incorrect alerts, the bank should implement customer-centric feedback channels coupled with Explainable AI (XAI). This method ensures that fairness is not just measured statistically but is experienced subjectively by the users (Selvam, 2025).
•	The Process: When a transaction is flagged or denied, the bank should provide a "reason code" or a natural language explanation (e.g., "Transaction blocked due to unusual device location") generated by tools like SHAP or LIME (Financial Services Sector Coordinating Council [FSSCC], 2026; Selvam, 2025). Alongside this explanation, the bank should provide an interface for customers to contest the decision or provide instant feedback (e.g., "This was me; approve future transactions from this location").
•	The Benefit: Analyzing real-time customer feedback and "user complaints" allows the bank to spot model drift or systemic biases that quantitative metrics might miss (FSSCC, 2026). Furthermore, providing customers with a way to resolve issues through human interaction—which 81% of consumers prefer in high-stakes situations—helps maintain brand loyalty and prevents the erosion of trust caused by "erroneous declines" (TD Bank, 2026; Wedge et al., 2017).
 
Task 3: Propose two technical improvements to enhance fraud detection accuracy. (10 Marks)
To address the high rate of false positives and restore organizational trust at Yu Bank, the following refined technical improvements are proposed. These suggestions integrate technical mechanisms with cross-departmental collaboration strategies to ensure effective change management and operational readiness.
1. Implementation of Automated Behavioral Feature Engineering (Deep Feature Synthesis)
The current system’s high false positive rate likely stems from analyzing transactions in isolation. Wedge et al. (2017) noted that false positives often occur when models fail to recognize unique, legitimate customer patterns.
•	Mechanism: Yu Bank should adopt Deep Feature Synthesis (DFS), an algorithm that automatically derives hundreds of behavioral features (e.g., cards.Mean(Hour(transactions.date))) from historical data to capture intricate "patterns of use" for each account.
•	Cross-Departmental Collaboration: This implementation requires a tight synergy between Data Engineers and Risk/Fraud Analysts (Subject Matter Experts). While engineers manage the data pipelines, analysts must provide the domain expertise to validate which auto-generated "deep features" actually reflect suspicious behavior versus harmless consumer habits.
•	Change Management Impact: By involving analysts in the feature-validation process, the bank addresses the "implementation gap" where staff feel disconnected from the technology. This collaborative "situated enablement" helps analysts understand the "why" behind the scores, transforming the AI from an opaque monitor into a transparent tool that mirrors their own professional logic.
2. Adoption of an Attention-Based Ensemble with a Confidence-Aware Gating Mechanism
Single models often fail to leverage complementary signals, leading to "uncertainty" that triggers incorrect alerts in imbalanced banking data. Chagahi et al. (n.d.) proposed a stacking architecture to mitigate this by fusing diverse neural networks.
•	Mechanism: The bank should implement an Attention-Based Ensemble (integrating GNNs and RNNs) with a Confidence-Aware Combination (CAC) Layer. This layer estimates model uncertainty for each transaction and only passes the most reliable, "confident" results to the final decision engine.
•	Cross-Departmental Collaboration: This requires ongoing coordination between ML Engineers, Risk Analysts, and Compliance/Legal Officers. As the CAC layer identifies "low-confidence" transactions, these must be routed for Human-in-the-Loop (HITL) review. Risk analysts provide the necessary "expert annotation" to resolve these ambiguous cases, while Compliance ensures the gating criteria meet regulatory standards for transparency and fairness.
•	Change Management Impact: Transitioning to a "Human-Led, AI-Enhanced" model is critical for adoption. When employees have the authority to overrule or confirm low-confidence AI predictions, their trust in the system increases. This strategy treats fairness and human oversight as "infrastructural requirements" rather than obstacles, ensuring that the technology matures alongside the organization's readiness to manage it.
 
Task 4: Recommend one strategy to improve user trust and adoption of the AI system. (10 Marks)
To improve user trust and ensure the durable adoption of the AI system at Yu Bank, the bank should implement a Human-Led, AI-Enhanced Governance Strategy centered on transparency and active oversight. According to TD Bank (2026), trust in financial AI is situational and must be earned, particularly when adoption outpaces the organizational readiness required to manage it.
This strategy consists of the following three core components:
1. Transitioning to a "Human-in-the-Loop" Operational Model
Yu Bank must move away from fully autonomous AI decision-making, as only 18% of consumers feel comfortable with AI making independent financial decisions. Instead, the bank should adopt a model where AI serves as a decision-support tool while humans maintain ultimate accountability for high-stakes outcomes like fraud alerts. FSSCC (2026) recommends "human-in-the-loop" reviews for ambiguous decisions to ensure that the system supports, rather than replaces, professional judgment. Providing employees with the ability to escalate or overrule AI-generated scores is the single most influential factor in increasing their confidence in the technology.
2. Deploying Explainable AI (XAI) Justifications
To resolve the "difficulties in trusting the system", the bank must eliminate the "black-box" nature of its fraud detection logic. Appani (2024) argues that high predictive accuracy (such as a 0.99 AUC-ROC) is insufficient if it lacks commensurate justification schemes for stakeholders.
•	For Employees: The system should provide "interpretability," allowing analysts to inspect the internal logic and feature weights that drive a fraud score.
•	For Customers: When an alert is triggered, the bank should provide "explainability" via natural language "reason codes" (e.g., "Transaction flagged due to unusual device location") rather than generic denials. This clarity fosters trust by demystifying the bank's decision-making process.
3. Establishing a "Fairness and Contestation" Interface
Selvam (2025) emphasizes that trust is built when customers have the opportunity to contest AI-driven decisions. Yu Bank should implement a user-centric feedback loop where customers can instantly verify legitimate transactions that were falsely flagged. By treating fairness as an "infrastructural requirement" rather than a mere constraint, the bank can transform its AI from an intrusive monitor into a transparent collaborator that protects both the institution’s assets and the customer’s autonomy.
 
Part 2: Barriers to AI Adoption (20 Marks)
This case is connected to the finance industry because the Canopy DSS supports municipal budget planning, cost control, ROI evaluation, and resource allocation. The system helps Kitchener, Waterloo, and Cambridge decide where tree planting and maintenance budgets should be spent to create the greatest environmental, social, and financial benefit. It also responds to limited municipal budgets and staffing resources, which make it difficult for forestry teams to prioritize maintenance work effectively.
1.	Identify three barriers (organizational, technical, economic, or social) that could slow AI adoption in that industry. (10 Marks)
2.	Propose one practical solution for each barrier to encourage AI adoption. (10 Marks)
 
1. Identify three barriers (organizational, technical, economic, or social) that could slow AI adoption in that industry. (10 Marks)

1. Organizational Barrier: Staff resistance and loss of control
Municipal forestry teams may resist the Canopy DSS because they are used to relying on separate spreadsheets, manual planning, and professional judgement to schedule tree pruning and allocate budgets. If the AI system automatically reorders funding priorities, the Operations Manager may feel that daily decision-making power is being reduced. Staff may also worry that they will be blamed if the DSS gives inaccurate budget or maintenance recommendations. This barrier is important because urban forestry adoption depends not only on model accuracy, but also on whether staff accept the DSS as a practical support tool rather than a replacement for human judgement (Vogt, Hauer, & Fischer, 2015).
2. Technical Barrier: Poor and fragmented data quality
The Canopy DSS depends on data from different municipal sources, including shapefiles, CSV files, DBH tree records, canopy coverage, and geolocation data. In a real production environment, missing DBH values, trees without valid coordinates, and different update schedules between municipalities could reduce model accuracy. Poor input data is a major technical barrier because it can make AI predictions less reliable. This is especially risky in urban forestry because tree asset risk is affected by both physical tree conditions and local environmental factors, such as canopy cover and urban heat exposure (Ziter, Pedersen, Kucharik, & Turner, 2019).
3. Economic Barrier: High upfront cost and unclear ROI
The DSS requires an upfront investment for cloud hosting, data engineering, staff training, and dashboard maintenance. For the CFO, approving new AI spending may be difficult if the financial benefit is not clear. This is especially important because the municipality is already managing a large canopy plan, so leadership needs strong evidence that the AI system will create measurable savings. The financial case depends on showing that proactive maintenance is cheaper than reactive emergency work, using tree trimming and removal cost benchmarks as part of the ROI calculation (Big Leaf Tree, n.d.).
2. Propose one practical solution for each barrier to encourage AI adoption. (10 Marks)
1. Solution for Organizational Barrier: Start with a small pilot project
The city should first deploy the DSS in one high-risk census tract before expanding it to Kitchener, Waterloo, and Cambridge. This reduces the risk of full deployment and allows staff to see real results before fully trusting the system. The Operations Manager should also be included in the pilot design so the DSS is seen as a support tool, not a replacement for human decision-making. The system should clearly communicate that the DSS recommends actions, but people still make the final decision.
2. Solution for Technical Barrier: Build an automated data-quality pipeline
Before data enters the AI model, the system should automatically check for missing DBH values, invalid GPS coordinates, and outdated records. The project should also set a measurable data-completeness KPI, such as requiring more than 95% of tree records to have valid DBH and GPS fields. This helps protect the model accuracy and prevents the system from producing misleading predictions. A fallback process should also be created so the system pauses or flags outputs when data quality drops below the required threshold.
3. Solution for Economic Barrier: Present a clear cost-benefit case
The DSS should be presented as a pilot investment with measurable financial benefits. The cost-benefit case should compare the upfront cost of the DSS with estimated annual savings from proactive pruning, fewer emergency removals, and reduced storm-response surcharges. The dashboard should also include quarterly ROI reports so the CFO can compare actual savings with projected savings over time. This makes the investment easier to approve because leadership can track financial performance using clear evidence.
Conclusion
In this municipal finance and budgeting case, the main barriers to AI adoption are organizational resistance, technical data-quality problems, and economic uncertainty. These barriers can be reduced through a controlled pilot project, automated data validation, and a clear ROI report. By using these strategies, the Canopy DSS can become easier for municipal staff, financial leaders, and community stakeholders to trust and adopt.
 
Part 3: Change Management Plan (20 Marks)
You are hired as a consultant to help a municipality/company deploy an AI-Powered Tree Canopy Decision Support System (DSS). Develop a change management plan covering:
1.	Stakeholder Analysis: Identify at least three key stakeholders and their roles. (5 Marks)
2.	Communication Strategy: Describe how you will communicate the AI transition and data-driven changes to internal employees and the public/customers. (5 Marks)
3.	Training & Support Plan: Outline how employees (such as operations managers and forestry crews) will be trained to work alongside the AI system and interpret its outputs. (5 Marks)
4.	Pilot Testing & Evaluation: Explain how you will test, evaluate, and improve the DSS in a limited scope (pilot area) before implementing a full, multi-city deployment. (5 Marks)
 
1. Stakeholder Analysis: Identify at least three key stakeholders and their roles. (5 Marks)
The successful deployment of the Tree Canopy Decision Support System (DSS) depends on managing the expectations and concerns of key stakeholders. Three critical stakeholders include:
● Operations Manager (Kitchener/Waterloo/Cambridge):
•	Role: The primary daily user responsible for managing municipal forestry operations and acting on the DSS risk prioritization outputs. 
•	Concerns: Fears a loss of manual decision-making autonomy and worries about personal accountability if the AI-predicted budget or risk models prove inaccurate. 
● CFO / Finance Leadership:
•	Role: The financial gatekeeper responsible for approving the upfront $45,000 CAD investment for the system. 
•	Concerns: Heavily focused on return on investment (ROI) justification, clear payback timelines, and potential public or political backlash over uneven budget allocations between neighborhoods. 
● Municipal Forestry Staff (Field Crews):
•	Role: The front-line users who execute the actual tree pruning, removal, and maintenance based on work orders generated by the system. 
•	Concerns: Transitioning from an intuition-based, familiar workflow to a strictly data-driven scheduling model requires proper training to handle the change smoothly. 
 
2. Communication Strategy: Describe how you will communicate the AI transition and data-driven changes to internal employees and the public/customers. (5 Marks)
To reduce friction, mitigate political risks, and ensure transparency, a structured, multi-layered communication strategy is established for both internal staff and external public stakeholders: 
● Internal Management Alignment: Hold monthly steering committee meetings involving the Operations Manager, CFO, and IT leads to review implementation progress, share updates, and directly resolve operational blockers. 
● Executive Financial Briefings: Conduct quarterly executive briefings for the CFO and senior leadership to present actual financial savings versus the projected targets, directly demonstrating the system's ROI. 
● Public & Community Engagement: To handle the sensitive nature of allocating more budget to "Critical Need" (low-income, low-canopy) neighborhoods, a plain-language project page will be published on the Regional Municipality of Waterloo website. This will be paired with a public community engagement session to explain the environmental equity algorithm transparently and build public trust.

 
3. Training & Support Plan: Outline how employees (such as operations managers and forestry crews) will be trained to work alongside the AI system and interpret its outputs. (5 Marks)
To ensure the organization successfully transitions to working alongside the AI system, targeted training modules and robust support frameworks will be deployed:
● Operations Manager Workshop (2 Days): A facilitated intensive session covering DSS dashboard navigation, risk score interpretation, and the clear definition of human authority—specifically training managers on how and when to manually override or escalate AI recommendations. 
● Field Staff Orientation (3 Hours): A practical briefing for front-line forestry crews to explain how work orders generated by the DSS differ from previous manual spreadsheet scheduling, preparing them for data-driven workflows. 
● Dedicated Helpdesk Support: A dedicated technical support channel will be active throughout the 3-month pilot phase, guaranteeing a maximum 24-hour response time to resolve any system queries or glitches immediately.
 
4. Pilot Testing & Evaluation: Explain how you will test, evaluate, and improve the DSS in a limited scope (pilot area) before implementing a full, multi-city deployment. (5 Marks)
Before launching a full, tri-city rollout across Kitchener, Waterloo, and Cambridge, the system will undergo a controlled pilot to mitigate risk and optimize performance:
● Controlled Scope (The Pilot Area): The DSS will first be deployed exclusively in census tract 0008.01 (Forest Heights), which is identified as the highest-ranked neighborhood in the risk matrix. This limits organizational exposure and allows the team to build real-world confidence. 
● Evaluation Metrics: The pilot will be evaluated across two primary benchmarks over a 3-month period: 
•	Technical: Monitoring the data validation pipeline to ensure tree records maintain a >95% data completeness KPI (valid DBH and GPS data) to safeguard the model's prototyping accuracy ($R^2 > 0.99$). 
•	Financial: Tracking initial savings indicators to confirm progress toward the projected $115,000 CAD annual savings target (proving the 4.7-month payback period). 
● Continuous Improvement: During months 2 and 3, operational feedback and real-world closed-loop invoice data will be captured to continuously retrain the PyTorch MLP model. Full tri-city deployment will only occur in Month 4+ after the pilot area successfully meets its evaluation baselines. 

 
Part 4: Prototype Tool Development (20 Marks)
Task:
Create a Google Sheet prototype to track AI adoption progress, stakeholder feedback, and training. Include the following tabs:
•	Project Overview: AI adoption phases, timelines, key milestones.
•	Stakeholder Feedback: Names, feedback, status, action items.
•	Training Schedule: Sessions, participants, completion status.
•	Progress Tracker: Tasks, responsible teams, deadlines, completion %.
Bonus (5 Marks): Use conditional formatting, dropdowns, and formulas to enhance usability.

 
Reference 
TD Bank. (2026, March). 2026 AI insights report: Artificial intelligence at the consumer inflection point. TD Stories. https://stories.td.com/us/en/article/2026-ai-insights-report-artificial-intelligence-at-the-consumer-inflection-point,
Hussain, A., & Rizwan, R. (2024). Strategic AI adoption in SMEs: A prescriptive framework (arXiv:2408.11825v1). arXiv. https://doi.org/10.48550/arXiv.2408.11825
Ali, D., Ahmed, M., Wang, H., Khan, A., Jordan, N. P. A., Kim, S. S. Y., Muchhala, M. D., Merkle, A. K., & Papakyriakopoulos, O. (2025). AI adoption across mission-driven organizations (arXiv:2510.03868v1). arXiv.
Weinberg, A. I. (2025, October 24). A framework for the adoption and integration of generative AI in midsize organizations and enterprises (FAIGMOE) (arXiv:2510.19997v1). arXiv. https://doi.org/10.48550/arXiv.2510.19997
Financial Services Sector Coordinating Council. (2026, January). AI and explainability in finance: Explainability challenges, practices and recommendations.
Lamria, G. (n.d.). AI-driven fraud detection in the financial sector: Architecture, impact, and challenges. Columbia Academic Commons.
CIBC. (n.d.). CIBC’s trustworthy AI commitment.
Kadam, P. (n.d.). Enhancing financial fraud detection with human-in-the-loop feedback and feedback propagation. arXiv.
Selvam, M. (2025). Ethical AI for personalized banking: Addressing bias and fairness challenges. LatIA, 3(361). https://doi.org/10.62486/latia2025361
Big Leaf Tree. (n.d.). Tree Removal and Trimming Price Guide. https://bigleaftree.ca/price-guide/
Nesbitt, L., Meitner, M. J., Girling, C., Sheppard, S. R., & Lu, Y. (2019). Who has access to urban vegetation? A spatial analysis of distributional green equity in US cities. Landscape and Urban Planning, 181, 51-79.
Vogt, J. M., Hauer, R. J., & Fischer, B. C. (2015). Explaining the urban forest: A need for proactive asset management. Arboriculture & Urban Forestry, 41(1), 25-43.
Ziter, C. D., Pedersen, E. J., Kucharik, C. J., & Turner, M. G. (2019). Scale-dependent interactions between tree canopy cover and impervious surfaces reduce urban air temperature. Proceedings of the National Academy of Sciences, 116(15), 7575-7580.

