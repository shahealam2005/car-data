import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Car Sales Analytics",
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

/* HERO SECTION */

.hero-container {
    position: relative;
    padding: 65px 55px;
    border-radius: 22px;
    background:
        linear-gradient(
            90deg,
            rgba(5, 10, 16, 0.98) 0%,
            rgba(5, 10, 16, 0.90) 42%,
            rgba(5, 10, 16, 0.30) 100%
        ),
        url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1600&q=85");

    background-size: cover;
    background-position: center;
    min-height: 440px;
    display: flex;
    align-items: center;
    border: 1px solid #202833;
    box-shadow: 0px 20px 50px rgba(0, 0, 0, 0.35);
}

.hero-content {
    max-width: 680px;
}

.hero-label {
    color: #b8c1cc;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 18px;
}

.hero-title {
    color: #ffffff;
    font-size: 58px;
    font-weight: 800;
    line-height: 1.08;
    margin-bottom: 20px;
}

.hero-title span {
    color: #4da3ff;
}

.hero-description {
    color: #c2c9d1;
    font-size: 18px;
    line-height: 1.7;
    max-width: 620px;
    margin-bottom: 28px;
}

.hero-tag {
    display: inline-block;
    padding: 10px 18px;
    background-color: rgba(77, 163, 255, 0.12);
    color: #74b9ff;
    border: 1px solid rgba(77, 163, 255, 0.35);
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    margin-right: 8px;
    margin-top: 8px;
}

/* SECTION */

.section-header {
    margin-top: 65px;
    margin-bottom: 28px;
}

.section-small-title {
    color: #4da3ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.section-title {
    color: #ffffff;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 12px;
}

.section-description {
    color: #8f9aa7;
    font-size: 16px;
    line-height: 1.7;
    max-width: 850px;
}

/* PROJECT CARDS */

.feature-card {
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

.feature-card:hover {
    transform: translateY(-5px);
    border-color: #3b82c4;
    box-shadow: 0px 15px 35px rgba(0, 0, 0, 0.30);
}

.card-number {
    color: #4da3ff;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 25px;
}

.card-title {
    color: #ffffff;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 14px;
}

.card-description {
    color: #929daa;
    font-size: 15px;
    line-height: 1.7;
}

/* INFORMATION BANNER */

.info-banner {
    margin-top: 55px;
    background:
        linear-gradient(
            135deg,
            rgba(77, 163, 255, 0.10),
            rgba(77, 163, 255, 0.03)
        );
    border: 1px solid rgba(77, 163, 255, 0.25);
    border-radius: 16px;
    padding: 30px 35px;
}

.info-title {
    color: #ffffff;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 10px;
}

.info-text {
    color: #9da8b5;
    font-size: 15px;
    line-height: 1.7;
}

/* TECHNOLOGY CARDS */

.tech-card {
    background: #0f161f;
    border: 1px solid #222c38;
    border-radius: 14px;
    padding: 25px;
    min-height: 190px;
    transition: all 0.3s ease;
}

.tech-card:hover {
    transform: translateY(-4px);
    border-color: #3b82c4;
}

.tech-name {
    color: #4da3ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 20px;
}

.tech-title {
    color: #ffffff;
    font-size: 19px;
    font-weight: 700;
    margin-bottom: 10px;
}

.tech-description {
    color: #929daa;
    font-size: 14px;
    line-height: 1.7;
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

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #080c11;
    border-right: 1px solid #1c2530;
}

section[data-testid="stSidebar"] * {
    color: #d7dde5;
}

/* RESPONSIVE */

@media (max-width: 768px) {

    .hero-container {
        padding: 40px 25px;
        min-height: 400px;
    }

    .hero-title {
        font-size: 40px;
    }

    .hero-description {
        font-size: 16px;
    }
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
hero_html = """
<div class="hero-container">
<div class="hero-content">
<div class="hero-label">Automotive Data Intelligence</div>
<div class="hero-title">Car Sales <span>Analytics</span></div>
<div class="hero-description">
An interactive data analysis project designed to explore vehicle sales
performance, market trends, customer preferences and key patterns hidden
within automotive sales data.
</div>
<div>
<span class="hero-tag">Data Analysis</span>
<span class="hero-tag">Exploratory Data Analysis</span>
<span class="hero-tag">Interactive Visualization</span>
</div>
</div>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)


# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------
overview_html = """
<div class="section-header">
<div class="section-small-title">Project Overview</div>
<div class="section-title">From Raw Data to Meaningful Insights</div>
<div class="section-description">
This project follows a structured analytical workflow to understand the
car sales dataset. Each section of the dashboard focuses on a different
stage of the analysis, from understanding the dataset to discovering
patterns and presenting final conclusions.
</div>
</div>
"""

st.markdown(overview_html, unsafe_allow_html=True)


# --------------------------------------------------
# PROJECT CARDS
# --------------------------------------------------
col1, col2, col3 = st.columns(3, gap="large")

with col1:

    card1 = """
<div class="feature-card">
<div class="card-number">01 / INTRODUCTION</div>
<div class="card-title">Understand the Project</div>
<div class="card-description">
Explore the purpose of the project, analytical objectives and the
importance of studying automotive sales data.
</div>
</div>
"""

    st.markdown(card1, unsafe_allow_html=True)


with col2:

    card2 = """
<div class="feature-card">
<div class="card-number">02 / EDA ANALYSIS</div>
<div class="card-title">Explore the Data</div>
<div class="card-description">
Perform exploratory data analysis using statistical summaries,
interactive charts and visual comparisons to discover important
sales patterns.
</div>
</div>
"""

    st.markdown(card2, unsafe_allow_html=True)


with col3:

    card3 = """
<div class="feature-card">
<div class="card-number">03 / CONCLUSION</div>
<div class="card-title">Discover Key Findings</div>
<div class="card-description">
Summarize the most important observations, business insights and
conclusions obtained from the complete analysis.
</div>
</div>
"""

    st.markdown(card3, unsafe_allow_html=True)


# --------------------------------------------------
# INFORMATION BANNER
# --------------------------------------------------
info_html = """
<div class="info-banner">
<div class="info-title">Interactive Analytics Dashboard</div>
<div class="info-text">
Use the navigation menu in the sidebar to move through different
sections of the project. The dashboard is designed to provide a clear
analytical journey from understanding the dataset to exploring visual
trends and extracting meaningful conclusions.
</div>
</div>
"""

st.markdown(info_html, unsafe_allow_html=True)


# --------------------------------------------------
# TECHNOLOGY SECTION
# --------------------------------------------------
technology_heading = """
<div class="section-header">
<div class="section-small-title">Technology Stack</div>
<div class="section-title">Tools Used in This Project</div>
<div class="section-description">
The project combines Python-based data analysis and interactive web
technologies to transform raw automotive data into an accessible
analytical dashboard.
</div>
</div>
"""

st.markdown(technology_heading, unsafe_allow_html=True)


# --------------------------------------------------
# TECHNOLOGY CARDS
# --------------------------------------------------
tech1, tech2, tech3, tech4 = st.columns(4, gap="medium")

with tech1:

    python_card = """
<div class="tech-card">
<div class="tech-name">PYTHON</div>
<div class="tech-title">Programming</div>
<div class="tech-description">
Core programming language used for data processing and analysis.
</div>
</div>
"""

    st.markdown(python_card, unsafe_allow_html=True)


with tech2:

    pandas_card = """
<div class="tech-card">
<div class="tech-name">PANDAS</div>
<div class="tech-title">Data Analysis</div>
<div class="tech-description">
Used for cleaning, transforming and analyzing structured data.
</div>
</div>
"""

    st.markdown(pandas_card, unsafe_allow_html=True)


with tech3:

    plotly_card = """
<div class="tech-card">
<div class="tech-name">PLOTLY</div>
<div class="tech-title">Visualization</div>
<div class="tech-description">
Creates interactive charts for exploring important data patterns.
</div>
</div>
"""

    st.markdown(plotly_card, unsafe_allow_html=True)


with tech4:

    streamlit_card = """
<div class="tech-card">
<div class="tech-name">STREAMLIT</div>
<div class="tech-title">Web Application</div>
<div class="tech-description">
Converts the complete analysis into an interactive web dashboard.
</div>
</div>
"""

    st.markdown(streamlit_card, unsafe_allow_html=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
footer_html = """
<div class="custom-footer">
Car Sales Analytics Dashboard | Built with Python and Streamlit
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)