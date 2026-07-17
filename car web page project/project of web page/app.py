import streamlit as st

st.set_page_config(
    page_title="Household Power Consumption Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Household Power Consumption Dashboard")

st.markdown("---")

st.subheader("Overview")

st.write("""
This dashboard provides an interactive analysis of household power consumption data.
It includes multiple analytical modules that help explore power usage patterns,
voltage trends, daily and monthly consumption, and relationships between electrical variables.
""")

st.markdown("---")

st.subheader("Available Modules")

st.write("""
- Dataset
- Data Summary
- Correlation Analysis
- Daily Analysis
- Hourly Analysis
- Monthly Analysis
- Power Analysis
- Voltage Analysis
- About
""")

st.markdown("---")

st.info("Select a module from the sidebar to begin the analysis.")