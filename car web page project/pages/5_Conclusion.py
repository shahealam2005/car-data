import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Conclusion | Car Sales Analytics",
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
            rgba(5, 10, 16, 0.88) 50%,
            rgba(5, 10, 16, 0.32) 100%
        ),
        url("https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?auto=format&fit=crop&w=1600&q=85");

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
    max-width: 950px;
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
    font-size: 32px;
    font-weight: 800;
}

.metric-note {
    color: #4da3ff;
    font-size: 13px;
    margin-top: 8px;
}

/* FINDING CARDS */

.finding-card {
    background: linear-gradient(
        145deg,
        #111821,
        #0e141c
    );
    border: 1px solid #222c38;
    border-radius: 16px;
    padding: 30px;
    min-height: 235px;
    transition: all 0.3s ease;
}

.finding-card:hover {
    transform: translateY(-5px);
    border-color: #3b82c4;
    box-shadow: 0px 15px 35px rgba(0, 0, 0, 0.25);
}

.finding-number {
    color: #4da3ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 22px;
}

.finding-title {
    color: #ffffff;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 13px;
}

.finding-text {
    color: #929daa;
    font-size: 15px;
    line-height: 1.8;
}

/* CONCLUSION CARD */

.conclusion-card {
    background:
        linear-gradient(
            135deg,
            rgba(77, 163, 255, 0.10),
            rgba(77, 163, 255, 0.025)
        );
    border: 1px solid rgba(77, 163, 255, 0.28);
    border-radius: 18px;
    padding: 38px;
    margin-top: 25px;
}

.conclusion-title {
    color: #ffffff;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 16px;
}

.conclusion-text {
    color: #a7b1bd;
    font-size: 16px;
    line-height: 1.9;
}

/* PROCESS CARD */

.process-card {
    background: #0f161f;
    border: 1px solid #222c38;
    border-radius: 15px;
    padding: 28px;
    min-height: 190px;
}

.process-number {
    color: #4da3ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 18px;
}

.process-title {
    color: #ffffff;
    font-size: 19px;
    font-weight: 700;
    margin-bottom: 10px;
}

.process-text {
    color: #929daa;
    font-size: 14px;
    line-height: 1.7;
}

/* FINAL BANNER */

.final-banner {
    margin-top: 55px;
    padding: 45px;
    text-align: center;
    border-radius: 18px;
    background:
        linear-gradient(
            135deg,
            rgba(77, 163, 255, 0.14),
            rgba(77, 163, 255, 0.03)
        );
    border: 1px solid rgba(77, 163, 255, 0.30);
}

.final-banner-title {
    color: #ffffff;
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 15px;
}

.final-banner-text {
    color: #9da8b5;
    font-size: 16px;
    line-height: 1.8;
    max-width: 850px;
    margin: auto;
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
# DATASET INFORMATION
# --------------------------------------------------
total_records = len(df)

total_features = len(df.columns)

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

missing_values = int(
    df.isnull().sum().sum()
)

duplicate_records = int(
    df.duplicated().sum()
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------
header_html = """
<div class="page-header">
<div class="page-header-content">

<div class="page-label">
05 / Conclusion
</div>

<div class="page-title">
Final Project <span>Conclusion</span>
</div>

<div class="page-description">
A final summary of the analytical process, major observations and the
overall value gained from exploring the car sales dataset through data
analysis and interactive visualization.
</div>

</div>
</div>
"""

st.markdown(
    header_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# PROJECT SUMMARY
# --------------------------------------------------
summary_heading = """
<div class="section-header">

<div class="section-label">
Project Summary
</div>

<div class="section-title">
Completing the Analytical Journey
</div>

<div class="section-description">
The Car Sales Analytics project followed a structured data analysis
workflow. The process began by understanding the dataset, continued
through exploratory data analysis and interactive visualization, and
finally transformed the observations into meaningful insights.
</div>

</div>
"""

st.markdown(
    summary_heading,
    unsafe_allow_html=True
)


# --------------------------------------------------
# PROJECT METRICS
# --------------------------------------------------
metric1, metric2, metric3, metric4 = st.columns(
    4,
    gap="medium"
)


with metric1:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Records Analyzed</div>
<div class="metric-value">{total_records:,}</div>
<div class="metric-note">Total observations</div>
</div>
""",
        unsafe_allow_html=True
    )


with metric2:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Features Explored</div>
<div class="metric-value">{total_features}</div>
<div class="metric-note">Dataset variables</div>
</div>
""",
        unsafe_allow_html=True
    )


with metric3:

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


with metric4:

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
# KEY FINDINGS
# --------------------------------------------------
findings_heading = """
<div class="section-header">

<div class="section-label">
Key Findings
</div>

<div class="section-title">
Major Outcomes of the Analysis
</div>

<div class="section-description">
The exploratory analysis revealed several important characteristics of
the dataset. These findings demonstrate how different analytical methods
can be used to understand automotive data from multiple perspectives.
</div>

</div>
"""

st.markdown(
    findings_heading,
    unsafe_allow_html=True
)


finding1, finding2, finding3 = st.columns(
    3,
    gap="large"
)


with finding1:

    st.markdown(
        """
<div class="finding-card">

<div class="finding-number">
FINDING 01
</div>

<div class="finding-title">
Dataset Structure
</div>

<div class="finding-text">
The dataset contains a combination of numerical and categorical
features. Understanding these different data types made it possible
to select appropriate analytical methods and visualizations for
different variables.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with finding2:

    st.markdown(
        """
<div class="finding-card">

<div class="finding-number">
FINDING 02
</div>

<div class="finding-title">
Patterns and Variation
</div>

<div class="finding-text">
Exploratory analysis revealed variation across numerical values and
differences in the frequency of categorical groups. Distribution
analysis helped identify common ranges, dominant categories and
potential unusual observations.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with finding3:

    st.markdown(
        """
<div class="finding-card">

<div class="finding-number">
FINDING 03
</div>

<div class="finding-title">
Feature Relationships
</div>

<div class="finding-text">
Comparative analysis, scatter plots and correlation analysis provided
a clearer understanding of how different variables relate to one
another and how numerical performance can vary across categories.
</div>

</div>
""",
        unsafe_allow_html=True
    )


# --------------------------------------------------
# DATA QUALITY SUMMARY
# --------------------------------------------------
quality_heading = """
<div class="section-header">

<div class="section-label">
Data Quality
</div>

<div class="section-title">
Quality of the Analyzed Dataset
</div>

<div class="section-description">
Evaluating missing values and duplicate records is an important part
of data analysis because data quality directly affects the reliability
of analytical results.
</div>

</div>
"""

st.markdown(
    quality_heading,
    unsafe_allow_html=True
)


quality1, quality2 = st.columns(
    2,
    gap="large"
)


with quality1:

    st.markdown(
        f"""
<div class="finding-card">

<div class="finding-number">
MISSING DATA
</div>

<div class="finding-title">
{missing_values:,} Missing Values
</div>

<div class="finding-text">
The complete dataset was checked for missing information. Identifying
missing values helps analysts understand whether additional cleaning
or preprocessing may be required before performing advanced analysis.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with quality2:

    st.markdown(
        f"""
<div class="finding-card">

<div class="finding-number">
DUPLICATE DATA
</div>

<div class="finding-title">
{duplicate_records:,} Duplicate Records
</div>

<div class="finding-text">
Duplicate record analysis was performed to identify repeated
observations. Detecting duplicates is important for maintaining data
quality and avoiding misleading analytical results.
</div>

</div>
""",
        unsafe_allow_html=True
    )


# --------------------------------------------------
# ANALYTICAL WORKFLOW
# --------------------------------------------------
workflow_heading = """
<div class="section-header">

<div class="section-label">
Project Workflow
</div>

<div class="section-title">
From Raw Data to Final Insights
</div>

<div class="section-description">
The project was completed through a structured sequence of analytical
stages. Each stage contributed to building a clearer understanding
of the automotive dataset.
</div>

</div>
"""

st.markdown(
    workflow_heading,
    unsafe_allow_html=True
)


step1, step2, step3, step4 = st.columns(
    4,
    gap="medium"
)


with step1:

    st.markdown(
        """
<div class="process-card">

<div class="process-number">
STEP 01
</div>

<div class="process-title">
Understand
</div>

<div class="process-text">
Define the project purpose, objectives and analytical direction.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with step2:

    st.markdown(
        """
<div class="process-card">

<div class="process-number">
STEP 02
</div>

<div class="process-title">
Explore
</div>

<div class="process-text">
Study dataset structure, data types, quality and statistical properties.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with step3:

    st.markdown(
        """
<div class="process-card">

<div class="process-number">
STEP 03
</div>

<div class="process-title">
Analyze
</div>

<div class="process-text">
Use interactive visualizations to discover patterns and relationships.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with step4:

    st.markdown(
        """
<div class="process-card">

<div class="process-number">
STEP 04
</div>

<div class="process-title">
Conclude
</div>

<div class="process-text">
Transform analytical observations into meaningful final conclusions.
</div>

</div>
""",
        unsafe_allow_html=True
    )


# --------------------------------------------------
# FINAL CONCLUSION
# --------------------------------------------------
conclusion_heading = """
<div class="section-header">

<div class="section-label">
Final Conclusion
</div>

<div class="section-title">
What This Project Demonstrates
</div>

</div>
"""

st.markdown(
    conclusion_heading,
    unsafe_allow_html=True
)


conclusion_html = """
<div class="conclusion-card">

<div class="conclusion-title">
Car Sales Data Can Be Transformed Into Meaningful Information
</div>

<div class="conclusion-text">
The Car Sales Analytics project demonstrates the importance of a
structured approach to data analysis. Raw automotive data alone can
be difficult to interpret, but through dataset exploration, descriptive
statistics, interactive visualizations and comparative analysis, useful
patterns can be identified and communicated clearly.
<br><br>
The project also demonstrates how Python, Pandas, Plotly and Streamlit
can work together to create an interactive analytical application.
Instead of presenting analysis only through static tables, the dashboard
allows users to explore different variables and generate visual insights
through interactive controls.
<br><br>
Overall, the project provides a practical example of the complete data
analysis workflow, beginning with raw data and ending with meaningful
observations and conclusions.
</div>

</div>
"""

st.markdown(
    conclusion_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# FINAL PROJECT MESSAGE
# --------------------------------------------------
final_html = """
<div class="final-banner">

<div class="final-banner-title">
Analysis Complete
</div>

<div class="final-banner-text">
The Car Sales Analytics Dashboard successfully combines data exploration,
statistical analysis and interactive visualization into a single
structured web application. The project demonstrates how data can be
converted into clear, accessible and meaningful analytical insights.
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
Car Sales Analytics Dashboard | Final Conclusion
</div>
"""

st.markdown(
    footer_html,
    unsafe_allow_html=True
)