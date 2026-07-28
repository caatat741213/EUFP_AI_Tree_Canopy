AI Solution Adoption & Change Management Report: Canopy Decision Support System (DSS)
Project Overview
This project is about an AI Tree Management System (Canopy DSS) for three cities in Ontario, Canada: Kitchener, Waterloo, and Cambridge. 
In the past, the cities shared the tree budget equally without checking real needs. The new AI system uses tree records, satellite temperature data, and maps to check tree risks. It helps the cities spend money wisely by giving more budget to areas that need it most. 
 
Task 1: Change Management Challenges
When we introduce the Canopy DSS, we will face four main challenges:
	Manager and Staff Worry About Losing Control (Organizational):
	Operations managers and field workers are used to paper records and their own experience. 
	When AI reorders work priorities, managers worry about losing decision-making power and being blamed if the AI makes a mistake. 
	They requested an explanation screen and an "override button" to change AI decisions manually. 
	Data Integration Problems (Technical):
	The AI needs data from different sources, such as GPS locations, map boundaries, and temperature records. 
	In reality, some tree sizes or GPS locations are missing, and data format between Kitchener and Waterloo is different. This can make the AI predictions wrong. 
	Financial Uncertainty for Leadership (Economic):
	The system costs $45,000 CAD upfront for development and cloud setup. 
	The Chief Financial Officer (CFO) manages the overall $125,000 CAD budget and needs clear evidence of cost savings before approving the money. 
	Public Fairness and Trust Concerns (Social & Political):
	The AI gives more budget to low-income areas with fewer trees. 
	Richer neighborhoods with many trees might complain that this is unfair. Also, local residents worry that tree trimming work will cause daily noise and disruption. 
 
Task 2: System Requirements
1. Functional Requirements
	AI Cost Prediction Engine:
	The system uses an XGBoost machine learning model ($R^2 = 0.9985$ accuracy) to calculate future tree costs. 
	It calculates costs step-by-step: small trees ($450 CAD), medium/critical trees ($1,200 CAD), maintenance rates (5% small, 10% medium, 20% critical), plus a 36% storm emergency fee. 
	Human-in-the-Loop & Override Panel:
	The screen must show clear reason codes for AI choices. Managers have an "override button" to change AI decisions. The rule is "System advises, people decide". 
	Automatic Data Quality Check:
	The system automatically checks for missing tree size or GPS data. It requires over 95% complete data before running the AI. 
	Dashboards and Mobile Views:
	Managers get an executive dashboard showing budget savings. Field workers get a simple mobile screen to view daily work orders. 
2. Non-Functional Requirements
	Accuracy and Fallback Protocol:
	The model must stay over 99% accurate. If input data quality is bad, the system stops automatically and alerts IT staff. 
	IT Support and Security:
	The system uses secure cloud logins and role permissions. IT support promises a 24-hour response time for help tickets. 
	Algorithmic Transparency:
	The system clearly shows how factors affect cost (e.g., critical trees add +$4.76 CAD, protected environmental zones add +$583.74 CAD). This proves budget decisions are fair and objective. 
3. Training and Communication Plan
The project includes 5 basic training sessions before go-live: 
	AI Overview: Teach managers and IT the main goals and human oversight rules. 
	AI Ethics & Fairness: Teach managers and PR staff how the AI protects community equity. 
	Manager Workshop (2 Days): Day 1 covers dashboard navigation; Day 2 teaches how to interpret risk scores and use the override button. 
	Field Crew Orientation (3 Hours): Simple 3-hour practical training for arborists and field workers. 
	Data Quality Training: Teach data engineers how to clean data and hit the 95% completeness target. 
 
Task 3: Findings, Transition Plan & Impact Analysis
1. Key Benefits (Findings)
	Better Work Efficiency: The city stops sharing money blindly. The AI calculates real needs per neighborhood, saving hours of budget meeting time. 
	Risk Reduction: By finding high-risk trees early and doing proactive pruning, the cities can avoid 36% of emergency storm cleanup fees. 
2. Four-Phase Transition Timeline
To make the change smooth, the project follows four simple phases: 
	Phase 1: Assessment (July 16 – July 31): Check data availability, project goals, and main worries. 
	Phase 2: Planning (August 01 – August 21): Approve the AI roadmap, training plan, and data rules. 
	Phase 3: Implementation & Pilot (August 24 – November 15):
	Train staff and field crews. 
	Run a 3-month trial in the highest-risk neighborhood, Forest Heights (Census tract 0008.01). 
	Phase 4: Evaluation (November 16 – November 20): Review pilot results and decide whether to launch across all three cities. 
3. Financial Impact & Payback Period
	Upfront Setup Cost: $45,000 CAD. 
	Expected Annual Savings: $115,000 CAD per year by preventing tree emergencies. 
	Payback Period: It takes only 4.7 months to earn back the investment (\frac{$45,000}{$115,000/year}=4.7months)! 

