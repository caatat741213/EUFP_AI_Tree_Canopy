# In-Class Activity: Ethical Audit of Your AI Solution

## Learning Outcome Covered

**4.1** Analyze AI solutions from multiple lenses: accessibility, ethics, equity, privacy, security, sustainability, and well-being.

## Activity Overview

Evaluate the CanopyIQ Tree Canopy Decision Support System (DSS) as if it were being reviewed for real-world municipal deployment.

## Step 1: Project Reframing

- **What problem does your AI solve?**
  CanopyIQ integrates municipal tree records, LiDAR canopy data, and Landsat temperature data to prioritize budget allocation across 52 planning communities and predict tree removal probability. This helps the cities of Kitchener, Waterloo, and Cambridge move from flat-budget sharing to data-driven proactive maintenance, saving money and reducing storm emergency surcharges.
- **Who are the real users affected?**
  - Municipal forestry planners and operations managers (scheduling and budget allocation).
  - Field crews and arborists (daily work orders and locations).
  - Local residents (neighborhood shade, cooling, and tree maintenance noise/disruption).
- **What decisions does your AI influence?**
  - Which planning communities are prioritized for tree pruning, planting, and inspections.
  - Which specific trees are flagged for removal risk.
  - How the municipal tree management budget is distributed.

## Step 2: Ethical Audit

Evaluate CanopyIQ using the seven lenses:

| Lens | Key Questions | Your Analysis | Risk Level (Low/Med/High) |
|---|---|---|---|
| **Accessibility** | Can people with disabilities use it? | The map-first interface is unreadable to screen readers and difficult for color-blind users. Also, under-inventoried communities appear as low priority due to data gaps. | **Medium** |
| **Ethics** | Is the decision-making transparent and fair? | The Random Forest model depends heavily on the *Fraxinus* (ash) genus/EAB epidemic, lacking general tree mortality intelligence. There is a risk of automated removal without human validation (scope creep). | **High** |
| **Equity** | Does it introduce bias or discrimination? | Equal 0.25 weights for index factors is a value judgment. Communities with sparse historical records score lower, reinforcing historical neglect. | **Medium** |
| **Privacy** | Is user data collected, stored, or misused? | Tree coordinates map directly to private residential frontages. Joining tree records to census income data creates a risk of household profiling. | **Medium** |
| **Security** | Can the system be attacked or manipulated? | DSS exports schedule work orders directly into Cityworks, meaning a breach could misdirect municipal budgets. Malformed data could poison model training. | **Medium** |
| **Sustainability** | Does it consume excessive resources? | Random Forest training on 145,326 records, Monte Carlo runs, and Landsat processing consume compute energy. Focus on removals could cause net canopy loss. | **Low** |
| **Well-being** | Does it impact mental/social health? | Rigorous algorithmically generated schedules can cause stress for field crews. Negative priority labeling ("Low priority") can alienate community residents. | **Medium** |

## Step 3: Red Flag Identification

- **1 Critical Risk:** Model Overreliance on the *Fraxinus* signature. If deployed as a general tree removal predictor, it will fail to accurately predict mortality for other species, leading to hazardous trees being missed.
- **1 Moderate Risk:** Map-First Accessibility Exclusion. VIS-impaired and color-blind users cannot access the map data, and under-inventoried neighborhoods get neglected due to data gaps.
- **1 Responsible Design Choice:** Enforcing a **Green Equity KPI** (allocating at least 40% of the proactive budget to census tracts in the bottom 30% of income) and keeping the final decision authority with human arborists ("system advises, human decides").

## Step 4: Ethical Redesign

- **What would you change in your prototype to reduce risks?**
  - Implement a **data-coverage confidence flag** to identify areas with sparse tree records and route them to fieldwork instead of scoring them as low priority.
  - Prohibit any join of census income data directly to individual tree coordinates in the data model, restricting joins strictly to the tract level.
  - Introduce a **schema-enforcer layer** to validate and quarantine incorrect municipal uploads before model training.
- **What additional features / controls would you introduce?**
  - **WCAG 2.1 AA Tabular View:** Display a text-based, accessible table export of `canopyiq_index.csv` for screen reader compatibility.
  - **Explainability Layer & Model Card:** Embed a model card explaining the *Fraxinus* limitation and showing feature importance charts.
  - **Override Audit Logs:** Record all user overrides in an immutable audit log to capture arborist feedback for retraining.
  - **Replanting Work-Order Pairing:** Automatically pair every removal recommendation with a replanting work order.

## Step 5: Final Verdict

**Deploy with Conditions**

**Justification:** The system offers significant environmental and financial benefits ($115,000 CAD annual savings), but cannot operate autonomously. Defer all removal actions to manual certified arborist inspections, publish the model card limits, enforce the Green Equity KPI, and provide accessible tabular exports.

## Step 6: Peer Critique Reflection

> **“Would I trust this system if I were the user?”**

Yes, because the system protects community safety while actively addressing green equity through the Green Equity KPI. Arborists can trust it because they maintain professional agency through overrides.

> **“Would you take legal responsibility for this AI system?”**

Only under the "Deploy with Conditions" advisory framework. The final legal responsibility remains with human operators and arborists who review and authorize all physical field actions.
