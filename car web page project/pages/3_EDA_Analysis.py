import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="EDA Analysis | Car Sales Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #0b0f14;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #080c11;
    border-right: 1px solid #1c2530;
}

section[data-testid="stSidebar"] * {
    color: #d7dde5;
}

/* PAGE HEADER */

.page-header {
    background:
        linear-gradient(
            90deg,
            rgba(5, 10, 16, 0.98) 0%,
            rgba(5, 10, 16, 0.90) 50%,
            rgba(5, 10, 16, 0.35) 100%
        ),
        url("https://images.unsplash.com/photo-1504215680853-026ed2a45def?auto=format&fit=crop&w=1600&q=85");

    background-size: cover;
    background-position: center;
    border-radius: 20px;
    padding: 60px 50px;
    min-height: 330px;
    display: flex;
    align-items: center;
    border: 1px solid #202833;
    box-shadow: 0px 20px 50px rgba(0, 0, 0, 0.30);
}

.page-header-content {
    max-width: 720px;
}

.page-label {
    color: #4da3ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

.page-title {
    color: #ffffff;
    font-size: 50px;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 18px;
}

.page-title span {
    color: #4da3ff;
}

.page-description {
    color: #c2c9d1;
    font-size: 17px;
    line-height: 1.8;
    max-width: 680px;
}

/* SECTION */

.section-header {
    margin-top: 55px;
    margin-bottom: 25px;
}

.section-label {
    color: #4da3ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.section-title {
    color: #ffffff;
    font-size: 31px;
    font-weight: 700;
    margin-bottom: 12px;
}

.section-description {
    color: #929daa;
    font-size: 16px;
    line-height: 1.8;
    max-width: 900px;
}

/* METRIC CARDS */

.metric-card {
    background: linear-gradient(
        145deg,
        #111821,
        #0e141c
    );
    border: 1px solid #222c38;
    border-radius: 15px;
    padding: 25px;
    min-height: 140px;
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: #3b82c4;
}

.metric-label {
    color: #8f9aa7;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.metric-value {
    color: #ffffff;
    font-size: 32px;
    font-weight: 800;
}

.metric-note {
    color: #4da3ff;
    font-size: 13px;
    margin-top: 8px;
}

/* ANALYSIS CARD */

.analysis-card {
    background:
        linear-gradient(
            135deg,
            rgba(77, 163, 255, 0.09),
            rgba(77, 163, 255, 0.02)
        );
    border: 1px solid rgba(77, 163, 255, 0.25);
    border-radius: 16px;
    padding: 28px 32px;
    margin-top: 25px;
}

.analysis-title {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.analysis-text {
    color: #9da8b5;
    font-size: 15px;
    line-height: 1.8;
}

/* FOOTER */

.custom-footer {
    margin-top: 70px;
    padding-top: 25px;
    padding-bottom: 10px;
    border-top: 1px solid #202833;
    color: #66717e;
    text-align: center;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------
@st.cache_data
def load_data():

    file_path = "cars_clean.xls"

    try:
        return pd.read_excel(
            file_path,
            engine="xlrd"
        )

    except Exception:
        pass

    try:
        return pd.read_csv(
            file_path
        )

    except Exception:
        pass

    try:
        return pd.read_csv(
            file_path,
            encoding="latin1"
        )

    except Exception as error:
        raise error


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
try:

    df = load_data()

except Exception as e:

    st.error("Unable to load the dataset.")

    st.write(
        "Make sure 'cars_clean.xls' is placed "
        "in the main project folder."
    )

    st.code(str(e))

    st.stop()


# --------------------------------------------------
# DETECT COLUMN TYPES
# --------------------------------------------------
numerical_columns = (
    df.select_dtypes(include="number")
    .columns
    .tolist()
)

categorical_columns = (
    df.select_dtypes(exclude="number")
    .columns
    .tolist()
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------
header_html = """
<div class="page-header">
<div class="page-header-content">

<div class="page-label">
03 / Exploratory Data Analysis
</div>

<div class="page-title">
Discover Patterns Through <span>Data</span>
</div>

<div class="page-description">
Explore distributions, category patterns, numerical relationships and
correlations within the car sales dataset using interactive visualizations.
</div>

</div>
</div>
"""

st.markdown(
    header_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# EDA OVERVIEW
# --------------------------------------------------
overview_html = """
<div class="section-header">

<div class="section-label">
Analysis Overview
</div>

<div class="section-title">
Exploring the Dataset
</div>

<div class="section-description">
Exploratory Data Analysis helps identify patterns, distributions,
relationships and unusual observations within the dataset. The charts
below are interactive and automatically generated using the available
numerical and categorical features.
</div>

</div>
"""

st.markdown(
    overview_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# METRICS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(
    4,
    gap="medium"
)


with col1:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Total Records</div>
<div class="metric-value">{len(df):,}</div>
<div class="metric-note">Available observations</div>
</div>
""",
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Total Features</div>
<div class="metric-value">{len(df.columns)}</div>
<div class="metric-note">Dataset variables</div>
</div>
""",
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Numerical Features</div>
<div class="metric-value">{len(numerical_columns)}</div>
<div class="metric-note">Quantitative variables</div>
</div>
""",
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Categorical Features</div>
<div class="metric-value">{len(categorical_columns)}</div>
<div class="metric-note">Category-based variables</div>
</div>
""",
        unsafe_allow_html=True
    )


# --------------------------------------------------
# NUMERICAL DISTRIBUTION
# --------------------------------------------------
numerical_heading = """
<div class="section-header">

<div class="section-label">
Univariate Analysis
</div>

<div class="section-title">
Numerical Feature Distribution
</div>

<div class="section-description">
Select any numerical feature to study its distribution. The histogram
shows how frequently different ranges of values occur in the dataset.
</div>

</div>
"""

st.markdown(
    numerical_heading,
    unsafe_allow_html=True
)


if numerical_columns:

    selected_numeric = st.selectbox(
        "Select a numerical feature",
        numerical_columns,
        key="numeric_distribution"
    )

    fig_hist = px.histogram(
        df,
        x=selected_numeric,
        nbins=30,
        marginal="box",
        title=f"Distribution of {selected_numeric}",
        template="plotly_dark"
    )

    fig_hist.update_layout(
        height=520,
        paper_bgcolor="#0b0f14",
        plot_bgcolor="#0f161f",
        title_font_size=20,
        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        )
    )

    st.plotly_chart(
        fig_hist,
        use_container_width=True
    )

else:

    st.info(
        "No numerical features were detected."
    )


# --------------------------------------------------
# CATEGORICAL ANALYSIS
# --------------------------------------------------
categorical_heading = """
<div class="section-header">

<div class="section-label">
Category Analysis
</div>

<div class="section-title">
Most Common Categories
</div>

<div class="section-description">
Select a categorical feature to compare the most frequently occurring
categories in the dataset.
</div>

</div>
"""

st.markdown(
    categorical_heading,
    unsafe_allow_html=True
)


if categorical_columns:

    selected_category = st.selectbox(
        "Select a categorical feature",
        categorical_columns,
        key="category_analysis"
    )

    top_n = st.slider(
        "Number of categories to display",
        min_value=5,
        max_value=20,
        value=10
    )

    category_counts = (
        df[selected_category]
        .astype(str)
        .value_counts()
        .head(top_n)
        .reset_index()
    )

    category_counts.columns = [
        selected_category,
        "Count"
    ]

    fig_category = px.bar(
        category_counts,
        x="Count",
        y=selected_category,
        orientation="h",
        title=f"Top {top_n} Categories in {selected_category}",
        template="plotly_dark"
    )

    fig_category.update_layout(
        height=520,
        paper_bgcolor="#0b0f14",
        plot_bgcolor="#0f161f",
        title_font_size=20,
        yaxis=dict(
            categoryorder="total ascending"
        ),
        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        )
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

else:

    st.info(
        "No categorical features were detected."
    )


# --------------------------------------------------
# NUMERICAL RELATIONSHIP
# --------------------------------------------------
relationship_heading = """
<div class="section-header">

<div class="section-label">
Bivariate Analysis
</div>

<div class="section-title">
Relationship Between Numerical Features
</div>

<div class="section-description">
Compare two numerical variables to explore possible relationships,
patterns and clusters within the car sales dataset.
</div>

</div>
"""

st.markdown(
    relationship_heading,
    unsafe_allow_html=True
)


if len(numerical_columns) >= 2:

    relation_col1, relation_col2 = st.columns(2)

    with relation_col1:

        x_feature = st.selectbox(
            "Select X-axis feature",
            numerical_columns,
            index=0,
            key="x_feature"
        )

    with relation_col2:

        default_y_index = (
            1
            if len(numerical_columns) > 1
            else 0
        )

        y_feature = st.selectbox(
            "Select Y-axis feature",
            numerical_columns,
            index=default_y_index,
            key="y_feature"
        )


    fig_scatter = px.scatter(
        df,
        x=x_feature,
        y=y_feature,
        opacity=0.65,
        title=f"{y_feature} vs {x_feature}",
        template="plotly_dark"
    )

    fig_scatter.update_layout(
        height=550,
        paper_bgcolor="#0b0f14",
        plot_bgcolor="#0f161f",
        title_font_size=20,
        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        )
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

else:

    st.info(
        "At least two numerical features are required "
        "for relationship analysis."
    )


# --------------------------------------------------
# BOX PLOT ANALYSIS
# --------------------------------------------------
box_heading = """
<div class="section-header">

<div class="section-label">
Distribution Analysis
</div>

<div class="section-title">
Compare Numerical Values Across Categories
</div>

<div class="section-description">
A box plot helps compare the distribution of a numerical feature across
different categories and can also help identify potential outliers.
</div>

</div>
"""

st.markdown(
    box_heading,
    unsafe_allow_html=True
)


if numerical_columns and categorical_columns:

    box_col1, box_col2 = st.columns(2)

    with box_col1:

        box_category = st.selectbox(
            "Select category",
            categorical_columns,
            key="box_category"
        )

    with box_col2:

        box_numeric = st.selectbox(
            "Select numerical feature",
            numerical_columns,
            key="box_numeric"
        )


    top_categories = (
        df[box_category]
        .value_counts()
        .head(10)
        .index
    )

    box_data = df[
        df[box_category].isin(
            top_categories
        )
    ]


    fig_box = px.box(
        box_data,
        x=box_category,
        y=box_numeric,
        title=f"{box_numeric} by {box_category}",
        template="plotly_dark"
    )

    fig_box.update_layout(
        height=550,
        paper_bgcolor="#0b0f14",
        plot_bgcolor="#0f161f",
        title_font_size=20,
        xaxis_tickangle=-35,
        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        )
    )

    st.plotly_chart(
        fig_box,
        use_container_width=True
    )

else:

    st.info(
        "Numerical and categorical features are required "
        "for this analysis."
    )


# --------------------------------------------------
# CORRELATION ANALYSIS
# --------------------------------------------------
correlation_heading = """
<div class="section-header">

<div class="section-label">
Correlation Analysis
</div>

<div class="section-title">
Relationships Between Numerical Variables
</div>

<div class="section-description">
The correlation matrix measures the strength and direction of relationships
between numerical features. Values closer to 1 indicate a strong positive
relationship, while values closer to -1 indicate a strong negative relationship.
</div>

</div>
"""

st.markdown(
    correlation_heading,
    unsafe_allow_html=True
)


if len(numerical_columns) >= 2:

    correlation_matrix = (
        df[numerical_columns]
        .corr()
        .round(2)
    )


    fig_corr = go.Figure(
        data=go.Heatmap(
            z=correlation_matrix.values,
            x=correlation_matrix.columns,
            y=correlation_matrix.columns,
            colorscale="Blues",
            zmin=-1,
            zmax=1,
            text=correlation_matrix.values,
            texttemplate="%{text}",
            hovertemplate=(
                "%{x}<br>"
                "%{y}<br>"
                "Correlation: %{z}<extra></extra>"
            )
        )
    )


    fig_corr.update_layout(
        title="Correlation Matrix",
        height=650,
        paper_bgcolor="#0b0f14",
        plot_bgcolor="#0f161f",
        font=dict(
            color="#ffffff"
        ),
        margin=dict(
            l=30,
            r=30,
            t=80,
            b=30
        )
    )


    st.plotly_chart(
        fig_corr,
        use_container_width=True
    )

else:

    st.info(
        "At least two numerical features are required "
        "for correlation analysis."
    )


# --------------------------------------------------
# CUSTOM INTERACTIVE ANALYSIS
# --------------------------------------------------
custom_heading = """
<div class="section-header">

<div class="section-label">
Interactive Exploration
</div>

<div class="section-title">
Build Your Own Analysis
</div>

<div class="section-description">
Select a category and a numerical feature to calculate and compare
aggregated values across different groups in the dataset.
</div>

</div>
"""

st.markdown(
    custom_heading,
    unsafe_allow_html=True
)


if categorical_columns and numerical_columns:

    custom_col1, custom_col2, custom_col3 = st.columns(3)

    with custom_col1:

        group_column = st.selectbox(
            "Group data by",
            categorical_columns,
            key="custom_group"
        )

    with custom_col2:

        value_column = st.selectbox(
            "Select numerical value",
            numerical_columns,
            key="custom_value"
        )

    with custom_col3:

        aggregation = st.selectbox(
            "Select calculation",
            [
                "Mean",
                "Sum",
                "Median",
                "Maximum",
                "Minimum"
            ]
        )


    if aggregation == "Mean":

        grouped_data = (
            df.groupby(group_column)[value_column]
            .mean()
        )

    elif aggregation == "Sum":

        grouped_data = (
            df.groupby(group_column)[value_column]
            .sum()
        )

    elif aggregation == "Median":

        grouped_data = (
            df.groupby(group_column)[value_column]
            .median()
        )

    elif aggregation == "Maximum":

        grouped_data = (
            df.groupby(group_column)[value_column]
            .max()
        )

    else:

        grouped_data = (
            df.groupby(group_column)[value_column]
            .min()
        )


    grouped_data = (
        grouped_data
        .sort_values(
            ascending=False
        )
        .head(15)
        .reset_index()
    )


    fig_custom = px.bar(
        grouped_data,
        x=group_column,
        y=value_column,
        title=(
            f"{aggregation} of {value_column} "
            f"by {group_column}"
        ),
        template="plotly_dark"
    )


    fig_custom.update_layout(
        height=550,
        paper_bgcolor="#0b0f14",
        plot_bgcolor="#0f161f",
        title_font_size=20,
        xaxis_tickangle=-35,
        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        )
    )


    st.plotly_chart(
        fig_custom,
        use_container_width=True
    )


# --------------------------------------------------
# FINAL ANALYSIS NOTE
# --------------------------------------------------
final_html = """
<div class="analysis-card">

<div class="analysis-title">
Exploratory Analysis Complete
</div>

<div class="analysis-text">
The visualizations above provide an interactive way to explore the
distribution of individual variables, compare categories, study
relationships between numerical features and identify correlations.
These observations provide the analytical foundation for extracting
important sales insights in the next section of the project.
</div>

</div>
"""

st.markdown(
    final_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
footer_html = """
<div class="custom-footer">
Car Sales Analytics Dashboard | Exploratory Data Analysis
</div>
"""

st.markdown(
    footer_html,
    unsafe_allow_html=True
)