# Enhancing Urban Forestry Planning with an AI-Powered Tree Canopy DSS
# Multi-Dimensional Tree Asset Risk Prioritization for Tri-City Forestry Management

## Introduction
The cities of Kitchener, Waterloo, and Cambridge continue to invest in urban forestry programs to improve environmental quality, reduce urban heat, and increase community well-being. However, municipal forestry teams often face limited budgets and staffing resources, making it difficult to prioritize where tree planting and maintenance efforts will have the greatest impact.
This system helps planners identify streets and neighborhoods where tree planting or maintenance would provide the highest environmental, social, and infrastructure benefit.

## Project Files

| File / Folder | Purpose |
| --- | --- |
| `Assignment_1.ipynb` | Main analysis notebook and DSS workflow for Assignment 1 |
| `Assignment_1EX.ipynb` | Extended analysis notebook that introduces a new real dataset and produces a different analysis result and report |
| `Assignment_2.ipynb` | Twin-track AI rapid prototyping and optimization pipeline for Assignment 2 |
| `Assignment_4.ipynb` | AI System Integration plan and Performance Management notebook for Assignment 4 |
| `document/` | Written reports, presentations, and extra artifacts for all assignments |
| `document/mdset/` | Markdown versions of the case studies, assignment reports, and slide decks |
| `datasets/` | Raw, supplemented, and processed spatial/tabular data used by the notebooks |
| `Result/` | Output folder containing model execution outputs, figures, database records, and logs |

## Repository Structure

```text
EUFP_AI_Tree_Canopy/
├── .agents/
│   └── AGENTS.md
├── Assignment_1.ipynb
├── Assignment_1EX.ipynb
├── Assignment_2.ipynb
├── Assignment_4.ipynb
├── README.md
├── requirements.txt
├── temporary.md
├── datasets/
│   ├── Census_of_Population2021_CSV.csv
│   ├── Street_Tree_Inventory.csv
│   ├── Tree_Canopy_2019.csv
│   ├── Tree_Inventory.csv
│   └── Planning_Communities_Kitchener.geojson
├── document/
│   ├── Assignment_1.docx
│   ├── Assignment_1.pdf
│   ├── Assignment_2.docx
│   ├── Assignment2.pdf
│   ├── Assignment2.pptx
│   ├── Assignment3_ AI Adoption and Change Management.docx
│   ├── Assignment3_ AI Adoption and Change Management.pdf
│   ├── CanopyIQ_AI_Adoption_Tracker_Link.pdf
│   ├── Canopy_DSS_Change_Management_Plan.docx
│   ├── Case_Study_Canopy.docx
│   ├── Enhancing-Urban-Forestry-Planning-with-an-AI-Powered-Tree-Canopy-DSS.pptx
│   ├── problem statement Case Studies.docx
│   ├── References.txt
│   └── mdset/
└── Result/
    ├── document/
    │   ├── canopyiq_index.csv
    │   ├── canopyiq_index.gpkg
    │   ├── df2.pkl
    │   └── res2.json
    └── img/
        ├── Ex_ai_regression_model.png
        ├── Ex_critical_trees_by_neighborhood.png
        ├── Social_Vulnerability_vs_Environmental_Metrics_Perfect.png
        ├── ai_model_residuals.png
        ├── ai_regression_model_fit.png
        └── canopy_and_equity_distributions.png
```

## Project Highlights

### Assignment_1
* Assignment 1 focuses on the macro-level urban forestry decision support workflow, including canopy coverage analysis, heat-risk interpretation, socio-economic equity mapping, and a simple regression-based budget forecasting model.

### Assignment_1EX
* Assignment_1EX extends the original work by introducing a new real dataset and producing a different analytical result and report.
* The notebook integrates real land surface temperature data from Landsat/Google Earth Engine, combines it with census income information, and applies spatial imputation to build a richer socio-economic and climate-aware analysis.
* It compares linear regression, Random Forest, and XGBoost models for maintenance-cost forecasting, with the tree-based models showing the strongest predictive performance.

### Assignment_2
* Assignment 2 expands the framework into a micro-level asset risk prioritization engine across the full tri-city region, comparing a traditional manual modeling path with a GenAI-assisted pipeline and neural network approach.

### Assignment_4
* Assignment 4 covers the integration plan, cloud deployment architecture, and model performance management system for the Tree Canopy DSS (CanopyIQ).
* The notebook calculates a multi-criteria **CanopyIQ Index** at the community level (validated with Spearman Correlation and weight-perturbed Monte Carlo simulations) to direct regional planting resources.
* It harmonizes Kitchener and Waterloo inventories into a unified model training set of over 145,000 active/removed records and tests the transferability, baseline performance, and pest-feature dependencies of Random Forest classifiers.
* The section outlines system SLAs/KPIs, drift triggers, and annual retraining schedules.

---

## What The Notebooks Do

### Assignment 1: Macro-Level DSS Baseline
The workflow in `Assignment_1.ipynb` builds the foundational decision-support system by:
1. Combining Waterloo and Kitchener street tree inventories into a unified geospatial dataset.
2. Converting tree records into point geometries and joining them with census tract boundaries.
3. Aggregating tract-level indicators such as total trees, critical trees (`DBH > 45 cm`), canopy area, and ESPA proximity.
4. Generating visuals for canopy equity, heat mitigation, and budget planning.

### Assignment_1EX: Extension with New Real Data
The extension notebook in `Assignment_1EX.ipynb` broadens the analysis by introducing a new real-data layer and producing a revised analytical report:
1. Incorporating real land surface temperature data from Landsat and Google Earth Engine, with an offline cache fallback.
2. Integrating census income profiles and applying spatial imputation to construct a richer socio-economic index.
3. Re-running the spatial analysis to identify tracts with the highest concentration of critical trees and maintenance urgency.
4. Comparing multiple predictive models—linear regression, Random Forest, and XGBoost—for maintenance-cost forecasting.
5. Producing updated outputs such as hotspot plots, residual diagnostics, and feature-importance charts.

### Assignment 2: Micro-Level Risk Prioritization
The workflow in `Assignment_2.ipynb` shifts the project from regional planning to operational prioritization by:
1. Comparing a traditional manual pipeline with a GenAI-assisted modeling approach.
2. Creating a deterministic baseline risk score and a more advanced predictive framework.
3. Identifying the top 5 high-density risk zones and linking them to the budget logic from Assignment 1.

### Assignment 4: AI Integration & Performance Management
The workflow in `Assignment_4.ipynb` defines the system engineering and validation baseline by:
1. Planning the cloud deployment framework using AWS ECS, PostGIS databases, and Cityworks workforce integrations.
2. Calculating the CanopyIQ community priority index using normalized deficits, attrition rates, diversity, and backlog.
3. Conducting Spearman rank redundancy and Monte Carlo stability tests on the prioritized rankings.
4. Harmonizing street inventories to run cross-city transfer experiments (T1: Kitchener -> Waterloo; T2: Waterloo -> Kitchener).
5. Establishing a non-Fraxinus baseline to analyze model vulnerability after removing pest-damaged Ash tree profiles.
6. Defining KPIs (accuracy, latency, and green equity) alongside model drift monitoring and retraining pipelines.

## Key Findings and Outputs

* Assignment 1 establishes the spatial baseline for canopy planning and budget estimation.
* Assignment_1EX strengthens the analysis with real temperature and income data, leading to a more evidence-based maintenance prioritization framework.
* Assignment 2 demonstrates how operational risk scoring can be connected to budget allocation and how the GenAI-assisted path improves development efficiency.
* Assignment 4 delivers an end-to-end integration roadmap, demonstrates that cross-city model transfers are feasible, and proves that Random Forest models heavily rely on pest-infestation indicators, suggesting the need for annual retraining.

## Model and Analysis Notes

* Assignment 1 uses a regression-based approach for regional budget forecasting.
* Assignment_1EX evaluates the relationship between tree structure, canopy coverage, temperature, and socio-economic conditions, while reporting strong predictive performance from tree-based models (XGBoost $R^2 = 0.9985$).
* Assignment 2 compares a deterministic baseline with a GenAI-supported workflow to assess both analytical quality and operational feasibility.
* Assignment 4 demonstrates that Random Forest classifiers achieve high ROC-AUC (~0.835) under class-balanced pipelines, but their predictive accuracy drops when pest-damaged species profiles are excluded from feature vectors.

## How To Run
1. Clone the repository:

```bash
git clone https://github.com/caatat741213/EUFP_AI_Tree_Canopy.git
```

2. Create and activate a virtual environment:
```bash
# Windows:
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```
4. Verify all raw source files are correctly placed within the `./datasets/` root directory.

5. Open and run `Assignment_1.ipynb` first to execute the baseline geospatial joins and generate the macro regression parameters.
6. Run `Assignment_1EX.ipynb` next to introduce the new real dataset and examine the updated analytical results and report.
7. Execute `Assignment_2.ipynb` to run the double-track simulation, train the PyTorch MLP deep learning network, and output the efficiency comparison graphics directly to the `./Result/img/` folder.
8. Run `Assignment_4.ipynb` to execute the community prioritization engine, model the cross-city attrition classifier experiments, and export metric statistics to the `./Result/document/` directory.
