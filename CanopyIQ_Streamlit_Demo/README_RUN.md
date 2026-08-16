# CanopyIQ Streamlit Demo

**Project:** CanopyIQ: An AI-Assisted Decision Support System for Urban Tree Management and Community Prioritization

This is a lightweight academic demonstration interface built around the project's current executed outputs. It is **not** a production municipal system and it does not connect to Cityworks, AWS, or a live City of Kitchener environment.

## What the demo includes

- Overview of the verified research snapshot
- Interactive Kitchener community-prioritization map
- Community-level explanation of the four CanopyIQ indicators
- Side-by-side comparison of two planning communities
- Current executed Random Forest vs. baseline metrics
- Cross-city transfer results
- Responsible-AI and data-coverage limitations

## Data bundled with the demo

The demo uses compact derived outputs rather than copying the full raw municipal datasets:

- `data/canopyiq_index.csv` — regenerated from the current `canopyiq_index.gpkg`
- `data/canopyiq_communities.geojson` — WGS84 polygon geometry plus index attributes
- `data/model_results.json` — current executed classifier results from `res2.json`
- `data/metadata.json` — verified record counts, coverage notes, and index-stability results

The current index contains **51 ranked communities**. The source tree inventory has eligible records for 52 Kitchener communities, but **South Plains** has no valid inspection year, so its inspection-backlog indicator cannot currently be calculated. Three planning-community polygons have no eligible municipal tree records in the workflow: Dundee, Pioneer Tower East, and Victoria North.

## Windows quick start

### Option A — use the included launcher

Double-click:

`RUN_WINDOWS.bat`

It installs the three small demo dependencies into the currently selected Python environment and starts Streamlit.

### Option B — run from the VS Code terminal

```powershell
cd path\to\CanopyIQ_Streamlit_Demo
python -m pip install -r requirements-demo.txt
python -m streamlit run app.py
```

Streamlit will print a local address, normally `http://localhost:8501`.

## Recommended presentation flow (about 2 minutes)

1. **Overview** — explain that the index is transparent and stable.
2. **Community Prioritization** — select `CIVIC CENTRE`; show its rank and four drivers.
3. **Compare Communities** — compare `CIVIC CENTRE` with `VICTORIA PARK`.
4. **Model Evaluation** — show Random Forest vs. Fraxinus baseline.
5. **Responsible AI** — close on “CanopyIQ advises. Arborists decide.”

## Important evidence note

The app uses the **current executed model outputs**:

- Pooled Random Forest: F1 = 0.589, ROC-AUC = 0.835, PR-AUC = 0.692
- Fraxinus baseline: F1 = 0.558, ROC-AUC = 0.696, PR-AUC = 0.484
- RF without Fraxinus: F1 = 0.364, ROC-AUC = 0.749, PR-AUC = 0.341
- Kitchener → Waterloo: ROC-AUC = 0.773, F1 = 0.575
- Waterloo → Kitchener: ROC-AUC = 0.664, F1 = 0.398

Older markdown commentary inside `Assignment_T.ipynb` contains superseded numbers. Those older narrative values should not be used in the final report or presentation.
