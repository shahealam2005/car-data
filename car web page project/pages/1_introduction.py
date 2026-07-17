import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Introduction | Car Sales Analytics",
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
            rgba(5, 10, 16, 0.35) 100%
        ),
        url("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1600&q=85");

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
    max-width: 700px;
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
    font-size: 52px;
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
    max-width: 650px;
}

/* SECTION */

.section-header {
    margin-top: 60px;
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
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 12px;
}

.section-description {
    color: #929daa;
    font-size: 16px;
    line-height: 1.8;
    max-width: 900px;
}

/* CONTENT CARD */

.content-card {
    background: linear-gradient(
        145deg,
        #111821,
        #0e141c
    );
    border: 1px solid #222c38;
    border-radius: 16px;
    padding: 32px;
    min-height: 250px;
}

.content-card-title {
    color: #ffffff;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 16px;
}

.content-card-text {
    color: #929daa;
    font-size: 15px;
    line-height: 1.8;
}

/* OBJECTIVE CARDS */

.objective-card {
    background: #0f161f;
    border: 1px solid #222c38;
    border-radius: 15px;
    padding: 28px;
    min-height: 230px;
    transition: all 0.3s ease;
}

.objective-card:hover {
    transform: translateY(-5px);
    border-color: #3b82c4;
    box-shadow: 0px 15px 35px rgba(0, 0, 0, 0.25);
}

.objective-number {
    color: #4da3ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 22px;
}

.objective-title {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 12px;
}

.objective-text {
    color: #929daa;
    font-size: 14px;
    line-height: 1.7;
}

/* WORKFLOW */

.workflow-card {
    background:
        linear-gradient(
            135deg,
            rgba(77, 163, 255, 0.09),
            rgba(77, 163, 255, 0.02)
        );
    border: 1px solid rgba(77, 163, 255, 0.25);
    border-radius: 16px;
    padding: 32px;
    margin-top: 25px;
}

.workflow-title {
    color: #ffffff;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 12px;
}

.workflow-text {
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

/* RESPONSIVE */

@media (max-width: 768px) {

    .page-header {
        padding: 40px 25px;
    }

    .page-title {
        font-size: 38px;
    }
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------
header_html = """
<div class="page-header">
<div class="page-header-content">
<div class="page-label">01 / Introduction</div>
<div class="page-title">Understanding the <span>Project</span></div>
<div class="page-description">
A structured introduction to the Car Sales Analytics project, its purpose,
analytical objectives and the role of data analysis in understanding the
automotive sales market.
</div>
</div>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)


# --------------------------------------------------
# ABOUT THE PROJECT
# --------------------------------------------------
about_heading = """
<div class="section-header">
<div class="section-label">Project Background</div>
<div class="section-title">About the Car Sales Analytics Project</div>
<div class="section-description">
The automotive industry generates large amounts of sales data that can be
used to understand market performance, customer preferences and sales
patterns. This project uses exploratory data analysis and interactive
visualization to transform raw car sales data into meaningful information.
</div>
</div>
"""

st.markdown(about_heading, unsafe_allow_html=True)


# --------------------------------------------------
# ABOUT CARDS
# --------------------------------------------------
col1, col2 = st.columns(2, gap="large")

with col1:

    project_card = """
<div class="content-card">
<div class="content-card-title">Project Purpose</div>
<div class="content-card-text">
The primary purpose of this project is to analyze a car sales dataset and
identify useful patterns hidden within the data. The analysis focuses on
understanding the structure of the dataset, comparing different variables
and presenting important findings through clear visualizations.
<br><br>
The final result is an interactive Streamlit dashboard that provides a
simple and structured way to explore automotive sales information.
</div>
</div>
"""

    st.markdown(project_card, unsafe_allow_html=True)


with col2:

    importance_card = """
<div class="content-card">
<div class="content-card-title">Why Car Sales Analysis Matters</div>
<div class="content-card-text">
Car sales analysis helps in understanding how different factors influence
the automotive market. By studying sales data, analysts can identify
popular vehicle categories, compare market performance and observe
important trends.
<br><br>
These insights can support better decision-making and provide a clearer
understanding of customer demand and overall market behaviour.
</div>
</div>
"""

    st.markdown(importance_card, unsafe_allow_html=True)


# --------------------------------------------------
# OBJECTIVES SECTION
# --------------------------------------------------
objective_heading = """
<div class="section-header">
<div class="section-label">Analytical Goals</div>
<div class="section-title">Project Objectives</div>
<div class="section-description">
The project follows a set of clear analytical objectives to ensure that
the dataset is explored systematically and the final findings are easy
to understand.
</div>
</div>
"""

st.markdown(objective_heading, unsafe_allow_html=True)


# --------------------------------------------------
# OBJECTIVE CARDS
# --------------------------------------------------
obj1, obj2, obj3, obj4 = st.columns(4, gap="medium")

with obj1:

    objective1 = """
<div class="objective-card">
<div class="objective-number">OBJECTIVE 01</div>
<div class="objective-title">Understand the Data</div>
<div class="objective-text">
Study the structure, columns, data types and overall characteristics of
the car sales dataset.
</div>
</div>
"""

    st.markdown(objective1, unsafe_allow_html=True)


with obj2:

    objective2 = """
<div class="objective-card">
<div class="objective-number">OBJECTIVE 02</div>
<div class="objective-title">Explore Patterns</div>
<div class="objective-text">
Use exploratory data analysis to identify trends, relationships and
important patterns within the dataset.
</div>
</div>
"""

    st.markdown(objective2, unsafe_allow_html=True)


with obj3:

    objective3 = """
<div class="objective-card">
<div class="objective-number">OBJECTIVE 03</div>
<div class="objective-title">Visualize Insights</div>
<div class="objective-text">
Present analytical results using clear and interactive charts that make
complex information easier to understand.
</div>
</div>
"""

    st.markdown(objective3, unsafe_allow_html=True)


with obj4:

    objective4 = """
<div class="objective-card">
<div class="objective-number">OBJECTIVE 04</div>
<div class="objective-title">Generate Findings</div>
<div class="objective-text">
Summarize the most important observations and conclusions obtained from
the complete data analysis process.
</div>
</div>
"""

    st.markdown(objective4, unsafe_allow_html=True)


# --------------------------------------------------
# PROJECT WORKFLOW
# --------------------------------------------------
workflow_heading = """
<div class="section-header">
<div class="section-label">Analysis Process</div>
<div class="section-title">Project Workflow</div>
<div class="section-description">
The complete project is divided into multiple stages. Each stage contributes
to transforming raw data into understandable and meaningful analytical insights.
</div>
</div>
"""

st.markdown(workflow_heading, unsafe_allow_html=True)


workflow_html = """
<div class="workflow-card">
<div class="workflow-title">Introduction → Dataset Overview → EDA Analysis → Sales Insights → Conclusion</div>
<div class="workflow-text">
The analysis begins with an introduction to the project and an overview of
the dataset. The next stage focuses on exploratory data analysis using
statistical methods and visualizations. Important observations are then
converted into meaningful sales insights, followed by a final conclusion
that summarizes the overall findings of the project.
</div>
</div>
"""

st.markdown(workflow_html, unsafe_allow_html=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
footer_html = """
<div class="custom-footer">
Car Sales Analytics Dashboard | Introduction
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)