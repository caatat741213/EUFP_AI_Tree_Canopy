# Ethical Considerations and Prototype Planning in AI: Canopy Decision Support System (DSS)

## Analyzing AI from Multiple Lenses

- Accessibility
- Ethics
- Equity
- Privacy & Security
- Sustainability
- Well-being

---

## Accessibility in AI

### 1. Accessibility

**Definition:** Ensuring AI systems can be used by people with diverse abilities and conditions.

**In Urban Forestry (Canopy DSS):**

- Simple mobile interfaces for field crews (arborists) using large buttons, high-contrast text, and voice-to-text logging for hands-on, outdoor field environments.
- Public web portals with screen reader compatibility and keyboard navigation so all citizens can access neighborhood canopy maps and heat island data.
- Multi-language support to accommodate diverse municipal workforces and residents.
- **Prototype Planning Tip:** During prototyping, involve older workers and field crew members in testing the arborist mobile view under outdoor lighting conditions (glare).

---

## Ethical Implications

### 2. Ethics

**Definition:** Moral principles that govern the development and application of AI.

**In Urban Forestry (Canopy DSS):**

- Do not let the AI prioritize cost savings so much that it neglects high-risk trees in low-priority zones, causing safety hazards.
- Explain the decisions of the AI clearly to build trust with municipal workers and the general public.

**Example:** A prototype for tree maintenance scheduling must not hide the reasoning behind why specific census tracts receive priority.

- **Prototype Planning Tip:** Conduct ethical risk assessments early to ensure that safety thresholds (e.g., critical tree trunk size DBH > 45cm) are never compromised for financial savings.

---

## Equity in AI Solutions

### 3. Equity

**Definition:** Fair access and outcomes across diverse user groups.

**In Urban Forestry (Canopy DSS):**

- Ensure that budget distribution doesn't favor wealthy areas just because they have more historical data or active citizens complaining about trees.
- Distribute new tree planting (sapling deployment) to low-income and low-canopy tracts to reduce the Urban Heat Island (UHI) effect.
- **Prototype Planning Tip:** Test the model with socio-economic indexes to verify that the budget allocation formula weights disadvantaged areas fairly.

---

## Privacy and Security

### Privacy

**Definition:** Protecting personal and operational data from unauthorized access.

**In Urban Forestry (Canopy DSS):**

- Census boundary files and socio-economic data must be aggregated to protect individual household privacy.
- Avoid tracking arborist locations outside of designated work hours or outside of specific tree maintenance locations.
- **Prototype Planning Tip:** Build the prototype using only aggregated tract-level data and design clear data minimization rules.

---

## Security

**Definition:** Protecting the AI system from cyberattacks, tampering, and data breaches.

**In Urban Forestry (Canopy DSS):**

- The system manages municipal assets, budgets ($3.3M canopy plan), and operational calendars, making it a target for unauthorized tampering.
- A hacked system could direct public works resources to private lands or manipulate cost estimations.
- **Prototype Planning Tip:** Implement Role-Based Access Control (RBAC) and Multi-Factor Authentication (MFA) in the early prototype flow.

---

## Sustainability

**Definition:** Minimizing environmental impacts and using resources efficiently.

**In Urban Forestry (Canopy DSS):**

- Running geospatial analysis, LiDAR canopy data processing, and training models (XGBoost) requires computational power and causes carbon emissions.
- AI must help reduce resource waste, like optimized truck routing for pruning crews to lower fuel consumption.
- **Prototype Planning Tip:** Use lightweight machine learning models (like optimized XGBoost or Random Forest) and deploy them on green-energy cloud servers.

---

## Well-being

**Definition:** Promoting physical, mental, and emotional health of users.

**In Urban Forestry (Canopy DSS):**

- Proactive tree pruning reduces storm damage, property damage, and power outages, which directly improves citizen safety and peace of mind.
- Do not overload field workers with tight, AI-generated schedules that ignore extreme heat warnings or physical fatigue.
- **Prototype Planning Tip:** Involve arborists in the prototype design phase so they can suggest maximum daily workload limits and schedule flexibility.

---

## Course Outcome 4.2: Prototype Justification

- Contributions in ideation, design, research, development, and enhancement.

---

## Ideation Phase

### Ideation Stage: Identifying Opportunities and Risks

**Objective:** Brainstorm potential AI solutions to a real-world municipal forestry budgeting and risk prioritization problem.

**Individual Contribution Examples:**

- **Operations Manager (Municipal Forestry Department):**
  - Identifies the operational difficulties of reactive storm maintenance and high surcharges (50%-100%).
  - Highlights safety risks to field crews and calls for an override mechanism in the AI schedule.
- **City Financial Officer (CFO):**
  - Defines the budget limits ($125,000 reference budget and $3.3M overall canopy plan).
  - Keeps the team focused on achieving a clear Return on Investment (ROI) and saving emergency funds.
- **Data Scientist (AI Architect):**
  - Proposes integrating tree inventory datasets with LiDAR canopy cover layers to estimate costs and risk.

**Key Ethics Touchpoints:**

- Are we planning the system to serve all neighborhoods fairly, or will it only focus on complaint-heavy areas?
- **Case Example:** During ideation of the Canopy DSS, the team decided to include census socio-economic data specifically to address environmental justice and UHI mitigation.

---

## Design Phase

### Design Stage: Prototyping User Interface and System Flow

**Objective:** Visualize how forestry managers and field crews interact with the AI-driven budget and scheduling system.

**Individual Contribution Examples:**

- **UX/UI Designer:**
  - Designs a web dashboard for managers showing cost estimates and risk rankings per census tract.
  - Designs a simplified, mobile-friendly interface for field workers to log maintenance status.
- **System Architect:**
  - Outlines how the Python data pipeline will combine CSV files, GIS shapefiles, and temperature layers.

**Key Ethics Touchpoints:**

- Does the interface display explainable AI outputs (e.g., showing exact coefficients like +$4.76 CAD per critical tree)?
- **Case Example:** The design includes an explainable cost-breakdown screen and a prominent "Override" button for the Operations Manager, ensuring human oversight.

---

## Research Phase

### Research Stage: Data Collection and Model Selection

**Objective:** Gather geospatial datasets, clean data, and test appropriate AI models for cost estimation.

**Individual Contribution Examples:**

- **Data Scientist / GIS Researcher:**
  - Collects tree inventories from Kitchener and Waterloo, LiDAR canopy layers, and ESPA files.
  - Cleans data, handles missing tree sizes (DBH), and checks data quality against a 95% completeness target.
- **Policy Analyst / Equity Expert:**
  - Integrates the 2021 Canadian Census demographic statistics to calculate the Socio-Economic Index.

**Key Ethics Touchpoints:**

- Does the dataset exclude individual personal identifiers while retaining spatial coordinates for public tree assets?
- **Case Example:** The researcher discovered that Waterloo and Kitchener used different data formats for tree species, requiring standard mapping to prevent model bias against certain tree types.

---

## Development Phase

### Development Stage: Building the AI Prototype

**Objective:** Develop the data pipeline and train machine learning models to forecast annual costs.

**Individual Contribution Examples:**

- **ML Engineer / Developer:**
  - Trains Linear Regression, Random Forest, and XGBoost models.
  - Achieves $R^2 = 0.9985$ with XGBoost and integrates the predictive formula into the backend API.
- **Security Specialist:**
  - Configures user authentication, secure cloud database hosting, and encryption for GIS datasets.

**Key Ethics Touchpoints:**

- Is the XGBoost model overfitting to historical patterns, or does it generalize well to new areas like Cambridge?
- **Case Example:** The developer selected a lightweight XGBoost model with optimized parameters to run efficiently in the cloud, lowering energy consumption.

---

## Enhancement Phase

### Enhancement Stage: Iterative Testing and Improvement

**Objective:** Test the prototype with real users, gather feedback, and improve performance and usability.

**Individual Contribution Examples:**

- **QA Analyst / Test Engineer:**
  - Runs automated data quality checks and tests system behavior when tree size (DBH) data is missing.
- **Operations Specialist:**
  - Conducts a 3-month pilot test in the Forest Heights neighborhood (Census tract 0008.01) to evaluate the system.

**Key Ethics Touchpoints:**

- Does the system crash gracefully when input data is incomplete, or does it output wrong cost predictions?
- **Case Example:** Feedback from the pilot showed that arborists needed simplified data logging when wearing gloves; the team updated the mobile interface with larger touch buttons.

---

## Conclusion

- Ethical lens analysis is crucial to ensure the Canopy DSS is safe, fair, and accessible to all citizens and municipal staff.
- Highlight individual roles shows how cooperation between operations, finance, and engineering creates a better system.
- Future AI with ethical grounding will ensure the cities of Kitchener, Waterloo, and Cambridge manage public trees efficiently while keeping communities cooler and safer.
