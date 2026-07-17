import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Sales Insights | Car Sales Analytics",
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
        url("https://images.unsplash.com/photo-1494976388531-d1058494cdd8?auto=format&fit=crop&w=1600&q=85");

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
    min-height: 145px;
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
    font-size: 30px;
    font-weight: 800;
    word-break: break-word;
}

.metric-note {
    color: #4da3ff;
    font-size: 13px;
    margin-top: 8px;
}

/* INSIGHT CARD */

.insight-card {
    background: linear-gradient(
        145deg,
        #111821,
        #0e141c
    );
    border: 1px solid #222c38;
    border-radius: 16px;
    padding: 30px;
    min-height: 220px;
    transition: all 0.3s ease;
}

.insight-card:hover {
    transform: translateY(-4px);
    border-color: #3b82c4;
}

.insight-number {
    color: #4da3ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 20px;
}

.insight-title {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 12px;
}

.insight-text {
    color: #929daa;
    font-size: 15px;
    line-height: 1.8;
}

/* FINAL BANNER */

.final-banner {
    margin-top: 50px;
    background:
        linear-gradient(
            135deg,
            rgba(77, 163, 255, 0.10),
            rgba(77, 163, 255, 0.03)
        );
    border: 1px solid rgba(77, 163, 255, 0.25);
    border-radius: 16px;
    padding: 32px;
}

.final-title {
    color: #ffffff;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 10px;
}

.final-text {
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
<div class="page-label">04 / Sales Insights</div>
<div class="page-title">Turning Data Into <span>Insights</span></div>
<div class="page-description">
Transform exploratory analysis into meaningful observations by identifying
dominant categories, numerical patterns and important relationships within
the automotive dataset.
</div>
</div>
</div>
"""

st.markdown(
    header_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# INSIGHT OVERVIEW
# --------------------------------------------------
overview_html = """
<div class="section-header">
<div class="section-label">Insight Summary</div>
<div class="section-title">Key Observations From the Dataset</div>
<div class="section-description">
This section summarizes important patterns discovered within the dataset.
The insights are generated dynamically from the available categorical and
numerical features.
</div>
</div>
"""

st.markdown(
    overview_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# CALCULATE QUICK INSIGHTS
# --------------------------------------------------
if categorical_columns:

    primary_category = categorical_columns[0]

    most_common_value = (
        df[primary_category]
        .dropna()
        .astype(str)
        .mode()
    )

    if len(most_common_value) > 0:
        most_common_value = most_common_value.iloc[0]
    else:
        most_common_value = "N/A"

else:

    primary_category = "Category"
    most_common_value = "N/A"


if numerical_columns:

    primary_numeric = numerical_columns[0]

    average_numeric = (
        df[primary_numeric]
        .mean()
    )

    maximum_numeric = (
        df[primary_numeric]
        .max()
    )

else:

    primary_numeric = "Numerical Feature"
    average_numeric = 0
    maximum_numeric = 0


# --------------------------------------------------
# QUICK METRIC CARDS
# --------------------------------------------------
metric1, metric2, metric3, metric4 = st.columns(
    4,
    gap="medium"
)


with metric1:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Total Records</div>
<div class="metric-value">{len(df):,}</div>
<div class="metric-note">Analyzed observations</div>
</div>
""",
        unsafe_allow_html=True
    )


with metric2:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Most Common {primary_category}</div>
<div class="metric-value">{most_common_value}</div>
<div class="metric-note">Most frequent category</div>
</div>
""",
        unsafe_allow_html=True
    )


with metric3:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Average {primary_numeric}</div>
<div class="metric-value">{average_numeric:,.2f}</div>
<div class="metric-note">Mean numerical value</div>
</div>
""",
        unsafe_allow_html=True
    )


with metric4:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Maximum {primary_numeric}</div>
<div class="metric-value">{maximum_numeric:,.2f}</div>
<div class="metric-note">Highest recorded value</div>
</div>
""",
        unsafe_allow_html=True
    )


# --------------------------------------------------
# CATEGORY INSIGHTS
# --------------------------------------------------
category_heading = """
<div class="section-header">
<div class="section-label">Market Composition</div>
<div class="section-title">Dominant Categories</div>
<div class="section-description">
Analyze which values appear most frequently within a selected categorical
feature. This helps identify dominant groups within the dataset.
</div>
</div>
"""

st.markdown(
    category_heading,
    unsafe_allow_html=True
)


if categorical_columns:

    selected_category = st.selectbox(
        "Select a category for analysis",
        categorical_columns,
        key="insight_category"
    )

    top_categories = (
        df[selected_category]
        .dropna()
        .astype(str)
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_categories.columns = [
        selected_category,
        "Count"
    ]


    fig_category = px.bar(
        top_categories,
        x="Count",
        y=selected_category,
        orientation="h",
        title=f"Top Categories in {selected_category}",
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


    if len(top_categories) > 0:

        leading_category = (
            top_categories.iloc[0][selected_category]
        )

        leading_count = int(
            top_categories.iloc[0]["Count"]
        )

        leading_percentage = (
            leading_count /
            len(df) *
            100
        )


        st.markdown(
            f"""
<div class="final-banner">
<div class="final-title">Category Insight</div>
<div class="final-text">
The most frequently occurring value in <strong>{selected_category}</strong>
is <strong>{leading_category}</strong>, appearing
<strong>{leading_count:,} times</strong>. This represents approximately
<strong>{leading_percentage:.2f}%</strong> of all records in the dataset.
</div>
</div>
""",
            unsafe_allow_html=True
        )


# --------------------------------------------------
# NUMERICAL INSIGHTS
# --------------------------------------------------
numeric_heading = """
<div class="section-header">
<div class="section-label">Performance Analysis</div>
<div class="section-title">Numerical Feature Insights</div>
<div class="section-description">
Select a numerical feature to examine its average, minimum, maximum and
median values. These statistics provide a quick understanding of the
feature's overall range and central tendency.
</div>
</div>
"""

st.markdown(
    numeric_heading,
    unsafe_allow_html=True
)


if numerical_columns:

    selected_numeric = st.selectbox(
        "Select a numerical feature",
        numerical_columns,
        key="insight_numeric"
    )


    numeric_series = (
        df[selected_numeric]
        .dropna()
    )


    num1, num2, num3, num4 = st.columns(
        4,
        gap="medium"
    )


    with num1:

        st.metric(
            "Average",
            f"{numeric_series.mean():,.2f}"
        )


    with num2:

        st.metric(
            "Median",
            f"{numeric_series.median():,.2f}"
        )


    with num3:

        st.metric(
            "Minimum",
            f"{numeric_series.min():,.2f}"
        )


    with num4:

        st.metric(
            "Maximum",
            f"{numeric_series.max():,.2f}"
        )


    fig_numeric = px.histogram(
        df,
        x=selected_numeric,
        nbins=30,
        title=f"Distribution of {selected_numeric}",
        template="plotly_dark"
    )


    fig_numeric.update_layout(
        height=500,
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
        fig_numeric,
        use_container_width=True
    )


# --------------------------------------------------
# CATEGORY VS NUMERICAL INSIGHT
# --------------------------------------------------
comparison_heading = """
<div class="section-header">
<div class="section-label">Comparative Analysis</div>
<div class="section-title">Compare Performance Across Categories</div>
<div class="section-description">
Compare the average value of a numerical feature across different
categories to identify high-performing and low-performing groups.
</div>
</div>
"""

st.markdown(
    comparison_heading,
    unsafe_allow_html=True
)


if categorical_columns and numerical_columns:

    compare_col1, compare_col2 = st.columns(2)


    with compare_col1:

        comparison_category = st.selectbox(
            "Select grouping category",
            categorical_columns,
            key="comparison_category"
        )


    with compare_col2:

        comparison_numeric = st.selectbox(
            "Select numerical feature",
            numerical_columns,
            key="comparison_numeric"
        )


    comparison_data = (
        df.groupby(
            comparison_category
        )[comparison_numeric]
        .mean()
        .sort_values(
            ascending=False
        )
        .head(15)
        .reset_index()
    )


    fig_comparison = px.bar(
        comparison_data,
        x=comparison_category,
        y=comparison_numeric,
        title=(
            f"Average {comparison_numeric} "
            f"by {comparison_category}"
        ),
        template="plotly_dark"
    )


    fig_comparison.update_layout(
        height=540,
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
        fig_comparison,
        use_container_width=True
    )


    if len(comparison_data) > 0:

        best_category = (
            comparison_data
            .iloc[0][comparison_category]
        )

        best_value = (
            comparison_data
            .iloc[0][comparison_numeric]
        )


        st.markdown(
            f"""
<div class="final-banner">
<div class="final-title">Performance Insight</div>
<div class="final-text">
Based on average <strong>{comparison_numeric}</strong>,
<strong>{best_category}</strong> ranks highest among the analyzed
<strong>{comparison_category}</strong> groups, with an average value of
<strong>{best_value:,.2f}</strong>.
</div>
</div>
""",
            unsafe_allow_html=True
        )


# --------------------------------------------------
# AUTOMATIC INSIGHT CARDS
# --------------------------------------------------
insight_heading = """
<div class="section-header">
<div class="section-label">Analytical Findings</div>
<div class="section-title">What the Analysis Reveals</div>
<div class="section-description">
The following observations summarize the major analytical themes explored
throughout the dashboard.
</div>
</div>
"""

st.markdown(
    insight_heading,
    unsafe_allow_html=True
)


insight1, insight2, insight3 = st.columns(
    3,
    gap="large"
)


with insight1:

    st.markdown(
        """
<div class="insight-card">
<div class="insight-number">INSIGHT 01</div>
<div class="insight-title">Category Concentration</div>
<div class="insight-text">
The dataset contains categories with different levels of representation.
Identifying the most frequent groups helps reveal dominant segments within
the available automotive data.
</div>
</div>
""",
        unsafe_allow_html=True
    )


with insight2:

    st.markdown(
        """
<div class="insight-card">
<div class="insight-number">INSIGHT 02</div>
<div class="insight-title">Value Variation</div>
<div class="insight-text">
Numerical features show different ranges and distributions. Comparing
average, median, minimum and maximum values helps identify variation and
potential unusual observations.
</div>
</div>
""",
        unsafe_allow_html=True
    )


with insight3:

    st.markdown(
        """
<div class="insight-card">
<div class="insight-number">INSIGHT 03</div>
<div class="insight-title">Comparative Performance</div>
<div class="insight-text">
Grouping numerical values by categories allows different segments to be
compared and helps identify which groups have higher or lower average
performance.
</div>
</div>
""",
        unsafe_allow_html=True
    )


# --------------------------------------------------
# FINAL SUMMARY
# --------------------------------------------------
final_summary = """
<div class="final-banner">
<div class="final-title">From Analysis to Understanding</div>
<div class="final-text">
The insights generated from the dataset demonstrate how exploratory data
analysis can transform raw automotive records into meaningful information.
By examining dominant categories, numerical distributions and comparative
performance, the dashboard provides a structured foundation for drawing
the final conclusions of the project.
</div>
</div>
"""

st.markdown(
    final_summary,
    unsafe_allow_html=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
footer_html = """
<div class="custom-footer">
Car Sales Analytics Dashboard | Sales Insights
</div>
"""

st.markdown(
    footer_html,
    unsafe_allow_html=True
)