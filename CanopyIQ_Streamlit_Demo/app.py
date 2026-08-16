from pathlib import Path
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
ASSETS = BASE / "assets"

st.set_page_config(
    page_title="CanopyIQ",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Data
# -----------------------------
@st.cache_data
def load_data():
    index_df = pd.read_csv(DATA / "canopyiq_index.csv")
    with open(DATA / "canopyiq_communities.geojson", encoding="utf-8") as f:
        geojson = json.load(f)
    with open(DATA / "model_results.json", encoding="utf-8") as f:
        model_results = pd.DataFrame(json.load(f))
    with open(DATA / "metadata.json", encoding="utf-8") as f:
        metadata = json.load(f)
    return index_df, geojson, model_results, metadata

index_df, geojson, model_results, meta = load_data()
index_df = index_df.sort_values("rank").reset_index(drop=True)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .block-container {padding-top: 1.3rem; padding-bottom: 2rem;}
    .hero {
        padding: 1.25rem 1.35rem;
        border: 1px solid rgba(128,128,128,.22);
        border-radius: 16px;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, rgba(38,110,76,.10), rgba(88,166,120,.035));
    }
    .hero h1 {margin: 0; font-size: 2.15rem; line-height: 1.1;}
    .hero p {margin: .45rem 0 0 0; opacity: .82; font-size: 1.02rem;}
    .callout {
        padding: 1rem 1.1rem;
        border-left: 5px solid #4a7c59;
        background: rgba(74,124,89,.08);
        border-radius: 8px;
        margin: .6rem 0 1rem 0;
    }
    .warningbox {
        padding: 1rem 1.1rem;
        border-left: 5px solid #a67c00;
        background: rgba(166,124,0,.08);
        border-radius: 8px;
        margin: .6rem 0 1rem 0;
    }
    .tiny {font-size: .84rem; opacity: .72;}
    div[data-testid="stMetric"] {border: 1px solid rgba(128,128,128,.18); padding: .65rem .8rem; border-radius: 12px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Helpers
# -----------------------------
INDICATOR_LABELS = {
    "I_deficit": "Tree density deficit",
    "I_attrition": "Tree attrition",
    "I_monoculture": "Monoculture risk",
    "I_backlog": "Inspection backlog",
}

RAW_LABELS = {
    "dens": "Alive tree density / ha",
    "attrition": "Historical attrition",
    "diversity": "Shannon genus diversity",
    "backlog": "Inspection backlog",
}

NEED_LABEL = {
    "High": "High need",
    "Medium": "Moderate need",
    "Low": "Currently better served",
}

def community_row(name):
    return index_df.loc[index_df["pc"] == name].iloc[0]


def explain(row, n=2):
    pairs = sorted(
        [(INDICATOR_LABELS[k], float(row[k])) for k in INDICATOR_LABELS],
        key=lambda x: x[1],
        reverse=True,
    )
    reasons = []
    for label, value in pairs[:n]:
        if label == "Tree density deficit":
            reasons.append("relatively low alive-tree density")
        elif label == "Tree attrition":
            reasons.append("a comparatively high share of historical removals")
        elif label == "Monoculture risk":
            reasons.append("lower genus diversity and therefore higher monoculture exposure")
        elif label == "Inspection backlog":
            reasons.append("a longer inspection backlog")
    return " and ".join(reasons)


def indicator_frame(row):
    return pd.DataFrame({
        "Indicator": [INDICATOR_LABELS[k] for k in INDICATOR_LABELS],
        "Normalized priority contribution": [float(row[k]) for k in INDICATOR_LABELS],
    })


def metric_record(prefix):
    return model_results[model_results["model"].str.startswith(prefix)].iloc[0]


def section_title(title, caption=None):
    st.subheader(title)
    if caption:
        st.caption(caption)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🌳 CanopyIQ")
st.sidebar.caption("Urban forestry decision-support prototype")
page = st.sidebar.radio(
    "Demo section",
    [
        "Overview",
        "Community Prioritization",
        "Compare Communities",
        "Model Evaluation",
        "Responsible AI",
    ],
)
st.sidebar.divider()
st.sidebar.markdown("**Research status**")
st.sidebar.write("Prototype for academic demonstration. Not a deployed municipal system.")
st.sidebar.caption("Current evidence snapshot: integrated notebook outputs and verified project data.")

# -----------------------------
# Header
# -----------------------------
st.markdown(
    f"""
    <div class="hero">
      <h1>CanopyIQ</h1>
      <p>{meta['project_title'].split(': ', 1)[1]}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Overview
# -----------------------------
if page == "Overview":
    section_title(
        "From tree records to defensible community priorities",
        "CanopyIQ combines a transparent community index with a separate tree-level attrition experiment.",
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Raw municipal records", f"{meta['raw_inventory_rows']['total']:,}", "Kitchener + Waterloo")
    c2.metric("Harmonized ML records", f"{meta['harmonized_classifier_rows']['total']:,}", "Active/removed records")
    c3.metric("Ranked communities", f"{meta['ranked_communities']}", "Kitchener")
    c4.metric("Index stability", f"ρ = {meta['stability']['median_spearman_rho']:.3f}", "Median, 1,000 perturbations")

    st.markdown(
        """
        <div class="callout"><b>Core idea:</b> municipal planners should be able to see not only <i>which</i>
        community ranks higher, but <i>why</i>. The community score therefore uses four explicit indicators rather
        than a black-box model.</div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.1, 1])
    with left:
        st.markdown("#### Community priority index")
        formula_df = pd.DataFrame(
            {
                "Indicator": [
                    "Tree density deficit",
                    "Tree attrition rate",
                    "Genus monoculture risk",
                    "Inspection backlog",
                ],
                "Weight": ["25%", "25%", "25%", "25%"],
                "Interpretation": [
                    "Fewer alive trees per hectare → higher need",
                    "More historical removals → higher need",
                    "Lower genus diversity → higher risk",
                    "Longer time since inspection → higher need",
                ],
            }
        )
        st.dataframe(formula_df, hide_index=True, use_container_width=True)
        st.caption(f"Current formula: {meta['index_formula']}")

    with right:
        top = index_df.nsmallest(7, "rank").copy()
        fig = px.bar(
            top.sort_values("score"),
            x="score",
            y="pc",
            orientation="h",
            text=top.sort_values("score")["score"].map(lambda x: f"{x:.2f}"),
            labels={"score": "CanopyIQ score", "pc": "Community"},
            title="Highest-need communities in the current index",
        )
        fig.update_layout(height=420, margin=dict(l=10, r=10, t=55, b=10), showlegend=False)
        fig.update_xaxes(range=[0, 1])
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("Data coverage note", expanded=False):
        st.write(
            f"Kitchener has {meta['planning_boundaries']} planning-community polygons. "
            f"The municipal inventory contains eligible tree records for {meta['communities_with_tree_records']} communities. "
            f"The current index ranks {meta['ranked_communities']} because South Plains has no valid inspection year, "
            "so its inspection-backlog indicator cannot currently be calculated."
        )
        st.write(
            "Planning polygons with no eligible municipal tree records in this workflow: "
            + ", ".join(meta["boundaries_without_tree_records"]).title()
            + "."
        )

# -----------------------------
# Community Prioritization
# -----------------------------
elif page == "Community Prioritization":
    section_title(
        "Explore a community priority",
        "Select a Kitchener planning community to inspect its rank, score, raw measures and four normalized index components.",
    )
    default_idx = int(index_df.index[index_df["pc"] == "CIVIC CENTRE"][0]) if "CIVIC CENTRE" in set(index_df.pc) else 0
    selected = st.selectbox("Planning community", index_df["pc"].tolist(), index=default_idx)
    row = community_row(selected)

    a, b, c, d = st.columns(4)
    a.metric("Rank", f"#{int(row['rank'])} of {len(index_df)}")
    b.metric("CanopyIQ score", f"{row['score']:.3f}")
    c.metric("Planning need", NEED_LABEL.get(row["priority"], row["priority"]))
    d.metric("Alive trees", f"{int(row['alive']):,}")

    st.markdown(
        f"<div class='callout'><b>Why this rank?</b> {selected.title()} is elevated mainly by "
        f"{explain(row)}. The score is advisory and should be interpreted with local inventory coverage and arborist judgment.</div>",
        unsafe_allow_html=True,
    )

    map_col, detail_col = st.columns([1.25, 1])
    with map_col:
        map_df = index_df.copy()
        fig = px.choropleth_mapbox(
            map_df,
            geojson=geojson,
            locations="pc",
            featureidkey="properties.pc",
            color="score",
            hover_name="pc",
            hover_data={
                "rank": True,
                "score": ":.3f",
                "priority": True,
                "dens": ":.2f",
                "attrition": ":.2f",
                "pc": False,
            },
            center={"lat": 43.43, "lon": -80.48},
            zoom=9.7,
            opacity=0.78,
            color_continuous_scale="YlGnBu",
            labels={"score": "CanopyIQ score"},
        )
        fig.update_layout(mapbox_style="white-bg", margin=dict(l=0, r=0, t=0, b=0), height=535)
        fig.update_traces(marker_line_width=0.8, marker_line_color="rgba(45,45,45,.55)")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Map colour is supplemented by rank, score and tabular values so the result is not colour-only.")

    with detail_col:
        ind = indicator_frame(row)
        fig = px.bar(
            ind.sort_values("Normalized priority contribution"),
            x="Normalized priority contribution",
            y="Indicator",
            orientation="h",
            text=ind.sort_values("Normalized priority contribution")["Normalized priority contribution"].map(lambda x: f"{x:.2f}"),
            range_x=[0, 1],
            title="What drives the score?",
        )
        fig.update_layout(height=310, margin=dict(l=0, r=0, t=48, b=0), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        raw = pd.DataFrame(
            {
                "Measure": [
                    RAW_LABELS["dens"],
                    RAW_LABELS["attrition"],
                    RAW_LABELS["diversity"],
                    RAW_LABELS["backlog"],
                ],
                "Value": [
                    f"{row['dens']:.2f}",
                    f"{row['attrition']:.2f}%",
                    f"{row['diversity']:.2f}",
                    f"{row['backlog']:.0f} years",
                ],
            }
        )
        st.dataframe(raw, hide_index=True, use_container_width=True)

# -----------------------------
# Compare Communities
# -----------------------------
elif page == "Compare Communities":
    section_title(
        "Compare two communities",
        "This view is designed for the municipal question: Why does one community rank above another?",
    )
    names = index_df["pc"].tolist()
    col_a, col_b = st.columns(2)
    with col_a:
        a_name = st.selectbox("Community A", names, index=names.index("CIVIC CENTRE") if "CIVIC CENTRE" in names else 0)
    with col_b:
        b_name = st.selectbox("Community B", names, index=names.index("VICTORIA PARK") if "VICTORIA PARK" in names else min(1, len(names)-1))

    a = community_row(a_name)
    b = community_row(b_name)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric(a_name.title(), f"#{int(a['rank'])}", f"Score {a['score']:.3f}")
    c2.metric("Need tier", NEED_LABEL.get(a["priority"], a["priority"]))
    c3.metric(b_name.title(), f"#{int(b['rank'])}", f"Score {b['score']:.3f}")
    c4.metric("Need tier", NEED_LABEL.get(b["priority"], b["priority"]))

    rows = []
    for key, label in INDICATOR_LABELS.items():
        rows.append({"Indicator": label, "Community": a_name.title(), "Value": float(a[key])})
        rows.append({"Indicator": label, "Community": b_name.title(), "Value": float(b[key])})
    comp = pd.DataFrame(rows)
    fig = px.bar(
        comp,
        x="Value",
        y="Indicator",
        color="Community",
        barmode="group",
        orientation="h",
        range_x=[0, 1],
        title="Normalized priority components",
    )
    fig.update_layout(height=430, margin=dict(l=0, r=0, t=55, b=0))
    st.plotly_chart(fig, use_container_width=True)

    table = pd.DataFrame(
        {
            "Measure": ["CanopyIQ score", "Tree density / ha", "Attrition", "Genus diversity", "Inspection backlog"],
            a_name.title(): [f"{a.score:.3f}", f"{a.dens:.2f}", f"{a.attrition:.2f}%", f"{a.diversity:.2f}", f"{a.backlog:.0f} years"],
            b_name.title(): [f"{b.score:.3f}", f"{b.dens:.2f}", f"{b.attrition:.2f}%", f"{b.diversity:.2f}", f"{b.backlog:.0f} years"],
        }
    )
    st.dataframe(table, hide_index=True, use_container_width=True)

    if a_name != b_name:
        higher, lower = (a, b) if a.score >= b.score else (b, a)
        st.info(
            f"{higher.pc.title()} ranks higher in the current index. Its largest priority drivers are {explain(higher)}. "
            "This comparison explains the ranking; it does not authorize a maintenance or removal action."
        )

# -----------------------------
# Model Evaluation
# -----------------------------
elif page == "Model Evaluation":
    section_title(
        "Tree attrition experiment",
        "A separate Random Forest experiment estimates removal probability from harmonized Kitchener and Waterloo records.",
    )

    baseline = metric_record("B1:")
    pooled = metric_record("P:")
    no_frax = metric_record("D:")
    k_to_w = metric_record("T1:")
    w_to_k = metric_record("T2:")

    c1, c2, c3 = st.columns(3)
    c1.metric("Pooled RF ROC-AUC", f"{pooled.roc_auc:.3f}", f"Baseline {baseline.roc_auc:.3f}")
    c2.metric("Pooled RF PR-AUC", f"{pooled.pr_auc:.3f}", f"Baseline {baseline.pr_auc:.3f}")
    c3.metric("Pooled RF F1", f"{pooled.f1:.3f}", f"Baseline {baseline.f1:.3f}")

    st.markdown(
        """
        <div class="callout"><b>Interpretation:</b> the pooled Random Forest improves on the simple
        “is this tree Fraxinus?” rule, especially on ranking metrics. However, the model remains sensitive
        to species/pest history and does not transfer equally well in both city directions.</div>
        """,
        unsafe_allow_html=True,
    )

    chart_models = model_results[model_results["model"].str.startswith(("B0:", "B1:", "P:", "D:"))].copy()
    display_names = {
        "B0: majority class (pooled)": "Majority baseline",
        "B1: single rule - is it Fraxinus?": "Fraxinus rule",
        "P: RF pooled, 2 cities": "Pooled Random Forest",
        "D: RF pooled, no Fraxinus": "RF without Fraxinus",
    }
    chart_models["Model"] = chart_models["model"].map(display_names)
    long = chart_models.melt(id_vars="Model", value_vars=["f1", "roc_auc", "pr_auc"], var_name="Metric", value_name="Score")
    long["Metric"] = long["Metric"].map({"f1": "F1", "roc_auc": "ROC-AUC", "pr_auc": "PR-AUC"})
    fig = px.bar(long, x="Model", y="Score", color="Metric", barmode="group", range_y=[0, 1], title="Baseline and model comparison")
    fig.update_layout(height=430, margin=dict(l=0, r=0, t=55, b=0))
    st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.markdown("#### Fraxinus sensitivity")
        st.write(
            f"When Fraxinus records are excluded, ROC-AUC changes from **{pooled.roc_auc:.3f}** to **{no_frax.roc_auc:.3f}**, "
            f"while PR-AUC changes from **{pooled.pr_auc:.3f}** to **{no_frax.pr_auc:.3f}**. "
            "The reduction is meaningful, especially for precision-recall performance, but the current experiment does not support describing the model as completely collapsing."
        )
    with right:
        st.markdown("#### Cross-city transfer")
        st.write(
            f"Kitchener → Waterloo: **ROC-AUC {k_to_w.roc_auc:.3f}**, F1 {k_to_w.f1:.3f}.  "
            f"Waterloo → Kitchener: **ROC-AUC {w_to_k.roc_auc:.3f}**, F1 {w_to_k.f1:.3f}."
        )
        st.write("The asymmetry is a warning that municipal context matters and performance should be revalidated before transfer.")

    display_cols = ["model", "n_test", "prevalence", "accuracy", "precision", "recall", "f1", "roc_auc", "pr_auc"]
    st.dataframe(model_results[display_cols], hide_index=True, use_container_width=True)

# -----------------------------
# Responsible AI
# -----------------------------
elif page == "Responsible AI":
    section_title(
        "CanopyIQ advises. Arborists decide.",
        "The prototype is intentionally framed as decision support, not an autonomous municipal decision maker.",
    )

    st.markdown(
        """
        <div class="callout"><b>Human authority:</b> no model score authorizes tree removal. Community rankings guide
        planning attention; individual-tree predictions require qualified arborist inspection and operational review.</div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)
    with left:
        st.markdown("#### Controls built into the proposed design")
        st.markdown(
            """
            - **Advisory-only use:** predictions support scheduling and inspection, not automated removal.
            - **Accessible alternatives:** ranked tables accompany map views rather than relying on colour alone.
            - **Aggregate socioeconomic analysis:** demographic context should remain at census/community level.
            - **Planner override:** professional judgment must remain available and auditable.
            - **Monitoring:** model drift and cross-city transfer performance require periodic review.
            - **Replanting linkage:** removal-related planning should be paired with canopy replacement planning.
            """
        )
    with right:
        st.markdown("#### Known limitations in the current evidence")
        st.markdown(
            f"""
            - **Coverage gap:** {meta['ranked_communities']} communities are currently rankable, not 52; South Plains lacks a valid inspection year for the backlog indicator.
            - **Inventory dependence:** places with incomplete municipal inventories can be underrepresented.
            - **Pest history:** removing Fraxinus reduces pooled-model PR-AUC from **0.692** to **0.341**.
            - **Transfer asymmetry:** the model performs better from Kitchener → Waterloo than in the reverse direction.
            - **Prototype status:** Cityworks, AWS deployment and municipal procurement controls are proposed architecture, not live integrations.
            """
        )

    st.markdown(
        """
        <div class="warningbox"><b>Not for field authorization:</b> this academic prototype should not be used to
        make safety-critical tree removal decisions, allocate real municipal budgets, or represent a live City of Kitchener system.</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Stability of the transparent index")
    s = meta["stability"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Median Spearman ρ", f"{s['median_spearman_rho']:.3f}")
    c2.metric("5th percentile ρ", f"{s['p5_spearman_rho']:.3f}")
    c3.metric("Median top-15 preserved", f"{s['median_top15_preserved_pct']:.0f}%")
    st.caption("Based on 1,000 random ±20% perturbations of the four equal starting weights.")
