# Ethical Considerations and Prototype Planning in AI: CanopyIQ

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

**In CanopyIQ (Tree Canopy DSS):**

- The system uses a map-first design where priority tiers are shown via color-shaded polygons, which excludes users with color vision deficiency and screen readers.
- Communities that were never fully digitized can appear as low-density due to lack of public tree inventories.
- Tabular data equivalents (like exporting `canopyiq_index.csv`) should be provided alongside map canvases to make the data readable.
- **Prototype Planning Tip:** During prototyping, test the dashboard interfaces using accessibility tools (like screen readers and color-blind filters) and design text-based fallback tables for geospatial data.

---

## Ethical Implications

### 2. Ethics

**Definition:** Moral principles that govern the development and application of AI.

**In CanopyIQ (Tree Canopy DSS):**

- Avoid model overreliance where a Random Forest classifier trained on a specific pest signature (*Fraxinus* and Emerald Ash Borer epidemic) is mistaken for a general tree mortality predictor.
- Prevent scope creep where risk scores meant for planning proactive maintenance are used to automate tree removals without human validation.
- **Example:** A prototype predicting tree removal probabilities must clearly state its dependencies and route predictions to certified arborist inspections.
- **Prototype Planning Tip:** Conduct ethical risk assessments during model design, and create a model card specifying that the system acts strictly as an advisory support tool.

---

## Equity in AI Solutions

### 3. Equity

**Definition:** Fair access and outcomes across diverse user groups.

**In CanopyIQ (Tree Canopy DSS):**

- Ensure that equal weightings (0.25 for deficit, attrition, monoculture, and backlog) do not inadvertently neglect historically under-inventoried areas.
- Prioritize neighborhoods based on both ecological risk and socioeconomic factors to promote urban canopy equity.
- **Prototype Planning Tip:** Build inclusive datasets and simulate scenario outcomes under different weight configurations to evaluate fairness. Enforce a Green Equity KPI during prototyping.

---

## Privacy and Security

### Privacy

**Definition:** Protecting personal and operational data from unauthorized access.

**In CanopyIQ (Tree Canopy DSS):**

- Street tree records carry exact GPS coordinates adjacent to private residential frontages, making individual trees identifiable.
- Linking public tree records with census income data creates a risk of socioeconomic profiling of neighborhoods.
- **Prototype Planning Tip:** Keep all socioeconomic joins restricted to the census tract level with minimum population counts, and separate public community-level metrics from internal tree-level removal probability outputs.

---

## Security

**Definition:** Protecting the AI system from cyberattacks, tampering, and data breaches.

**In CanopyIQ (Tree Canopy DSS):**

- The DSS integrates directly with Cityworks schedules and shapes municipal budgets, making it vulnerable to unauthorized modifications.
- Malformed or malicious CSV/shapefile data uploads from Kitchener, Waterloo, or Cambridge could poison the model's training data.
- **Prototype Planning Tip:** Implement Role-Based Access Control (RBAC) over TLS, log all user overrides, and build a schema-enforcer layer to isolate and quarantine invalid records.

---

## Sustainability

**Definition:** Minimizing environmental impacts and using resources efficiently.

**In CanopyIQ (Tree Canopy DSS):**

- Random Forest model training over 145,326 tree records and geospatial processing of Landsat LST rasters consume significant computing power.
- Recommending tree removals without scheduling replanting causes a short-term loss of canopy coverage.
- **Prototype Planning Tip:** Use lightweight machine learning models (like optimized XGBoost or Random Forest) and deploy them on green-energy cloud servers.

---

## Well-being

**Definition:** Promoting physical, mental, and emotional health of users.

**In CanopyIQ (Tree Canopy DSS):**

- AI-generated schedules must not make field crews feel micromanaged, ignoring their local forestry knowledge and safety concerns.
- Labeling communities as "low priority" or "neglected" can harm community trust and resident well-being.
- **Prototype Planning Tip:** Involve field crews in design feedback to allow manual overrides, and reframe public vocabulary to focus on "highest need" and "currently well served."

---

## Course Outcome 4.2: Prototype Justification

- Contributions in ideation, design, research, development, and enhancement.

---

## Ideation Phase

### Ideation Stage: Identifying Opportunities and Risks

**Objective:** Brainstorm potential AI solutions to a real-world municipal forestry budgeting and risk prioritization problem.

**Individual Contribution Examples:**

- **Product Manager / Business Analyst:**
  - Identifies operational inefficiency in reactive budgeting across Kitchener, Waterloo, and Cambridge.
  - Ensures social and environmental risks are mapped early.
- **UX Researcher / Human-Centered Designer:**
  - Brings arborist and citizen perspectives on public tree priority labeling to the table.
  - Focuses on accessibility issues (like screen readers and map accessibility).

**Key Ethics Touchpoints:**

- How does the initial system concept handle under-digitized areas without biasing the model against them?
- **Case Example:** Ideating the multi-criteria index where the team decided to weight backlog and monoculture equally to avoid favoring wealthy tracts.

---

## Design Phase

### Design Stage: Prototyping User Interface and System Flow

**Objective:** Visualize how users interact with the AI system and what the system will do.

**Individual Contribution Examples:**

- **UX/UI Designer:**
  - Designs WCAG-compliant dashboards showing tabular data beside map canvases.
  - Rewrites public-facing language to avoid negative priority labels.
- **System Architect:**
  - Designs the data flow from CSV/shapefiles through the schema-enforcer to Cityworks.

**Key Ethics Touchpoints:**

- Does the system design enforce that tree-level risk probabilities are kept behind authenticated login?
- **Case Example:** The dashboard design includes an auditable override panel for planners to manually adjust maintenance schedules.

---

## Research Phase

### Research Stage: Data Collection and Model Selection

**Objective:** Gather relevant datasets, study existing solutions, and select appropriate AI models.

**Individual Contribution Examples:**

- **Data Scientist / AI Researcher:**
  - Analyzes the 145,326 tree records and discovers the high model dependency on the *Fraxinus* genus.
  - Runs Monte Carlo simulations (1,000 runs) to check the stability of the ranking index.
- **Privacy Analyst:**
  - Reviews census tract joins to ensure no individual residential income data is leaked.

**Key Ethics Touchpoints:**

- Is the training dataset representative of all planning communities, or does it suffer from inventory gaps?
- **Case Example:** The researcher includes a "data-coverage confidence flag" in the dataset to highlight areas with incomplete tree counts.

---

## Development Phase

### Development Stage: Building the AI Prototype

**Objective:** Code and integrate the AI model, interface, and infrastructure.

**Individual Contribution Examples:**

- **ML Engineer / Software Developer:**
  - Trains the Random Forest classifier to predict tree removals and implements the index calculation.
  - Implements the schema-enforcer layer to validate incoming CSV shapefiles.
- **Security Specialist:**
  - Sets up Role-Based Access Control (RBAC) and data encryption over TLS.

**Key Ethics Touchpoints:**

- Does the code support explainability (e.g., documenting feature importance in the Random Forest)?
- **Case Example:** The development team packages the prototype as a seasonal batch job rather than a high-energy, real-time web API.

---

## Enhancement Phase

### Enhancement Stage: Iterative Testing and Improvement

**Objective:** Continuously refine the AI prototype based on real-world feedback.

**Individual Contribution Examples:**

- **Test Engineer / QA Analyst:**
  - Verifies system behavior when non-conforming data is uploaded and checks WCAG compliance.
- **Operations Specialist:**
  - Gathers feedback from arborist crews during pilot runs about schedule overrides.

**Key Ethics Touchpoints:**

- Are the manual overrides logged correctly and used to retrain and improve the model over time?
- **Case Example:** Early tests showed that excluding *Fraxinus* caused model performance to collapse, prompting the team to add clear warning banners to the model card.

---

## Conclusion

- Ethical lens analysis is crucial to ensure that CanopyIQ remains a decision support tool rather than an automated decision maker.
- Highlight individual roles shows how data science, security, and operations collaborate to build a robust municipal AI.
- Future AI with ethical grounding will allow Kitchener, Waterloo, and Cambridge to build a more resilient and equitable urban forest.
