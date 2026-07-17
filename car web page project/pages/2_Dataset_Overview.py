import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Dataset Overview | Car Sales Analytics",
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
            rgba(5, 10, 16, 0.90) 55%,
            rgba(5, 10, 16, 0.40) 100%
        ),
        url("https://images.unsplash.com/photo-1493238792000-8113da705763?auto=format&fit=crop&w=1600&q=85");

    background-size: cover;
    background-position: center;
    border-radius: 20px;
    padding: 55px 50px;
    min-height: 300px;
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
    max-width: 650px;
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
    font-size: 35px;
    font-weight: 800;
}

.metric-note {
    color: #4da3ff;
    font-size: 13px;
    margin-top: 8px;
}

/* INFO CARD */

.info-card {
    background:
        linear-gradient(
            135deg,
            rgba(77, 163, 255, 0.09),
            rgba(77, 163, 255, 0.02)
        );
    border: 1px solid rgba(77, 163, 255, 0.25);
    border-radius: 16px;
    padding: 28px 32px;
    margin-top: 30px;
}

.info-title {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.info-text {
    color: #9da8b5;
    font-size: 15px;
    line-height: 1.8;
}

/* TABLE */

[data-testid="stDataFrame"] {
    border: 1px solid #222c38;
    border-radius: 12px;
    overflow: hidden;
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

    # Try loading as old Excel format
    try:
        df = pd.read_excel(
            file_path,
            engine="xlrd"
        )
        return df

    except Exception:
        pass

    # Try loading as CSV
    try:
        df = pd.read_csv(
            file_path
        )
        return df

    except Exception:
        pass

    # Try CSV with latin1 encoding
    try:
        df = pd.read_csv(
            file_path,
            encoding="latin1"
        )
        return df

    except Exception as error:
        raise error


# --------------------------------------------------
# LOAD THE DATA
# --------------------------------------------------
try:

    df = load_data()

except Exception as e:

    st.error("Unable to load the dataset.")

    st.write(
        "Make sure the file 'cars_clean.xls' is placed "
        "in the main project folder with app.py."
    )

    st.write("Error details:")

    st.code(str(e))

    st.stop()


# --------------------------------------------------
# DATASET INFORMATION
# --------------------------------------------------
total_rows = df.shape[0]

total_columns = df.shape[1]

missing_values = int(
    df.isnull().sum().sum()
)

duplicate_rows = int(
    df.duplicated().sum()
)

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
02 / Dataset Overview
</div>

<div class="page-title">
Explore the <span>Dataset</span>
</div>

<div class="page-description">
A complete overview of the car sales dataset, including its size,
structure, data types, missing values and statistical characteristics.
</div>

</div>
</div>
"""

st.markdown(
    header_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# DATASET SUMMARY
# --------------------------------------------------
summary_heading = """
<div class="section-header">

<div class="section-label">
Dataset Summary
</div>

<div class="section-title">
Understanding the Data Structure
</div>

<div class="section-description">
Before performing exploratory data analysis, it is important to
understand the basic structure and quality of the dataset. The following
metrics provide a quick overview of the available data.
</div>

</div>
"""

st.markdown(
    summary_heading,
    unsafe_allow_html=True
)


# --------------------------------------------------
# METRIC CARDS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(
    4,
    gap="medium"
)


with col1:

    card = f"""
<div class="metric-card">

<div class="metric-label">
Total Records
</div>

<div class="metric-value">
{total_rows:,}
</div>

<div class="metric-note">
Rows in the dataset
</div>

</div>
"""

    st.markdown(
        card,
        unsafe_allow_html=True
    )


with col2:

    card = f"""
<div class="metric-card">

<div class="metric-label">
Total Features
</div>

<div class="metric-value">
{total_columns}
</div>

<div class="metric-note">
Columns available
</div>

</div>
"""

    st.markdown(
        card,
        unsafe_allow_html=True
    )


with col3:

    card = f"""
<div class="metric-card">

<div class="metric-label">
Missing Values
</div>

<div class="metric-value">
{missing_values:,}
</div>

<div class="metric-note">
Empty values detected
</div>

</div>
"""

    st.markdown(
        card,
        unsafe_allow_html=True
    )


with col4:

    card = f"""
<div class="metric-card">

<div class="metric-label">
Duplicate Records
</div>

<div class="metric-value">
{duplicate_rows:,}
</div>

<div class="metric-note">
Repeated rows detected
</div>

</div>
"""

    st.markdown(
        card,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# DATASET PREVIEW
# --------------------------------------------------
preview_heading = """
<div class="section-header">

<div class="section-label">
Data Preview
</div>

<div class="section-title">
Explore the Raw Dataset
</div>

<div class="section-description">
The table below displays records from the dataset. Use the slider
to control how many rows you want to preview.
</div>

</div>
"""

st.markdown(
    preview_heading,
    unsafe_allow_html=True
)


# Prevent slider error if dataset is very small
if len(df) >= 5:

    rows_to_show = st.slider(
        "Number of rows to display",
        min_value=5,
        max_value=min(50, len(df)),
        value=min(10, len(df))
    )

else:

    rows_to_show = len(df)


st.dataframe(
    df.head(rows_to_show),
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# COLUMN INFORMATION
# --------------------------------------------------
column_heading = """
<div class="section-header">

<div class="section-label">
Feature Information
</div>

<div class="section-title">
Column and Data Type Analysis
</div>

<div class="section-description">
This section provides information about every feature in the dataset,
including its data type, number of missing values and number of unique values.
</div>

</div>
"""

st.markdown(
    column_heading,
    unsafe_allow_html=True
)


column_info = pd.DataFrame({

    "Column Name":
        df.columns,

    "Data Type":
        [
            str(df[column].dtype)
            for column in df.columns
        ],

    "Non-Null Values":
        [
            df[column].notnull().sum()
            for column in df.columns
        ],

    "Missing Values":
        [
            df[column].isnull().sum()
            for column in df.columns
        ],

    "Unique Values":
        [
            df[column].nunique()
            for column in df.columns
        ]

})


st.dataframe(
    column_info,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# FEATURE CLASSIFICATION
# --------------------------------------------------
classification_heading = """
<div class="section-header">

<div class="section-label">
Feature Classification
</div>

<div class="section-title">
Numerical and Categorical Features
</div>

<div class="section-description">
The dataset features are automatically classified based on their data
types. This classification will be useful during exploratory data analysis.
</div>

</div>
"""

st.markdown(
    classification_heading,
    unsafe_allow_html=True
)


tab1, tab2 = st.tabs(
    [
        "Numerical Features",
        "Categorical Features"
    ]
)


with tab1:

    if numerical_columns:

        numerical_df = pd.DataFrame({

            "Numerical Columns":
                numerical_columns

        })

        st.dataframe(
            numerical_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No numerical columns were detected."
        )


with tab2:

    if categorical_columns:

        categorical_df = pd.DataFrame({

            "Categorical Columns":
                categorical_columns

        })

        st.dataframe(
            categorical_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No categorical columns were detected."
        )


# --------------------------------------------------
# STATISTICAL SUMMARY
# --------------------------------------------------
statistics_heading = """
<div class="section-header">

<div class="section-label">
Descriptive Statistics
</div>

<div class="section-title">
Statistical Summary
</div>

<div class="section-description">
Descriptive statistics summarize the numerical features of the dataset,
including average values, minimum values, maximum values and variation.
</div>

</div>
"""

st.markdown(
    statistics_heading,
    unsafe_allow_html=True
)


if numerical_columns:

    statistical_summary = (
        df[numerical_columns]
        .describe()
        .T
        .reset_index()
    )

    statistical_summary = (
        statistical_summary.rename(
            columns={
                "index": "Feature"
            }
        )
    )

    st.dataframe(
        statistical_summary,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No numerical features are available "
        "for statistical analysis."
    )


# --------------------------------------------------
# DATA QUALITY
# --------------------------------------------------
quality_heading = """
<div class="section-header">

<div class="section-label">
Data Quality
</div>

<div class="section-title">
Missing and Duplicate Data
</div>

<div class="section-description">
Data quality analysis helps identify potential issues that may affect
the accuracy of further analysis and visualizations.
</div>

</div>
"""

st.markdown(
    quality_heading,
    unsafe_allow_html=True
)


quality_col1, quality_col2 = st.columns(
    2,
    gap="large"
)


with quality_col1:

    st.subheader(
        "Missing Values by Column"
    )

    missing_by_column = (
        df.isnull()
        .sum()
    )

    missing_by_column = (
        missing_by_column[
            missing_by_column > 0
        ]
        .sort_values(
            ascending=False
        )
    )

    if len(missing_by_column) > 0:

        missing_table = pd.DataFrame({

            "Column":
                missing_by_column.index,

            "Missing Values":
                missing_by_column.values

        })

        st.dataframe(
            missing_table,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success(
            "No missing values were detected "
            "in the dataset."
        )


with quality_col2:

    st.subheader(
        "Duplicate Record Analysis"
    )

    if duplicate_rows == 0:

        st.success(
            "No duplicate records were detected "
            "in the dataset."
        )

    else:

        st.warning(
            f"{duplicate_rows} duplicate records "
            "were detected."
        )


# --------------------------------------------------
# FINAL DATASET SUMMARY
# --------------------------------------------------
info_html = f"""
<div class="info-card">

<div class="info-title">
Dataset Overview Complete
</div>

<div class="info-text">
The dataset contains <strong>{total_rows:,} records</strong> and
<strong>{total_columns} features</strong>. It includes
<strong>{len(numerical_columns)} numerical features</strong> and
<strong>{len(categorical_columns)} categorical features</strong>.
This overview provides the foundation for the exploratory data analysis
performed in the next section of the project.
</div>

</div>
"""

st.markdown(
    info_html,
    unsafe_allow_html=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
footer_html = """
<div class="custom-footer">
Car Sales Analytics Dashboard | Dataset Overview
</div>
"""

st.markdown(
    footer_html,
    unsafe_allow_html=True
)