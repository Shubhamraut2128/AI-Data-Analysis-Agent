import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="AI Data Analysis Agent",
    layout="centered",
    initial_sidebar_state="auto"
)

# --------------------------
# Sidebar Upload
# --------------------------
st.sidebar.title("Upload CSV & Navigation")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

st.title("🤖 AI Data Analysis Agent")
st.subheader("Explore your data with multiple steps and visualizations")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # --------------------------
    # Step 1: Dataset Summary
    # --------------------------
    st.header("Step 1: Dataset Summary")
    with st.expander("View Dataset Summary"):
        st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
        st.write("Column Names:", df.columns.tolist())
        st.write("Missing Values:")
        st.write(df.isnull().sum())
        st.write("Duplicate Rows:", df.duplicated().sum())
        st.write("Data Types:")
        st.write(df.dtypes)

    # --------------------------
    # Step 2: Data Preview
    # --------------------------
    st.header("Step 2: Preview Data")
    with st.expander("View First 5 Rows"):
        st.dataframe(df.head(5))

    # --------------------------
    # Step 3: Numeric Statistics
    # --------------------------
    st.header("Step 3: Numeric Statistics")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        with st.expander("View Numeric Statistics"):
            st.dataframe(df[numeric_cols].describe().round(2))
    else:
        st.info("No numeric columns for statistics.")

    # --------------------------
    # Step 4: Histograms
    # --------------------------
    st.header("Step 4: Histograms")
    if numeric_cols:
        selected_col = st.selectbox("Select numeric column for histogram", numeric_cols, key="hist")
        if st.button("📈 Generate Histogram", key="hist_btn"):
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.histplot(df[selected_col].dropna(), bins=20, kde=True, ax=ax)
            ax.set_title(f"Histogram of {selected_col}")
            st.pyplot(fig)
            plt.close(fig)

    # --------------------------
    # Step 5: Boxplots
    # --------------------------
    st.header("Step 5: Boxplots")
    if numeric_cols:
        selected_col_box = st.selectbox("Select numeric column for boxplot", numeric_cols, key="box")
        if st.button("📊 Generate Boxplot", key="box_btn"):
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.boxplot(x=df[selected_col_box], ax=ax)
            ax.set_title(f"Boxplot of {selected_col_box}")
            st.pyplot(fig)
            plt.close(fig)

    # --------------------------
    # Step 6: Correlation Heatmap
    # --------------------------
    st.header("Step 6: Correlation Heatmap")
    if len(numeric_cols) > 1:
        if st.button("🟢 Show Correlation Heatmap", key="corr_btn"):
            corr = df[numeric_cols].corr()
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
            st.pyplot(fig)
            plt.close(fig)
    else:
        st.info("Need at least 2 numeric columns for correlation.")

    # --------------------------
    # Step 7: Pairplot (Optional)
    # --------------------------
    if len(numeric_cols) > 1:
        if st.checkbox("Show Pairplot (may be slow)", key="pairplot_chk"):
            st.header("Step 7: Pairplot of Numeric Columns")
            pairplot_fig = sns.pairplot(df[numeric_cols])
            st.pyplot(pairplot_fig)
            plt.close('all')

    # --------------------------
    # Step 8: Categorical Column Analysis
    # --------------------------
    st.header("Step 8: Categorical Column Analysis")
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    if cat_cols:
        selected_cat = st.selectbox("Select categorical column", cat_cols, key="cat")
        if st.button("📊 Show Barplot", key="cat_btn"):
            fig, ax = plt.subplots(figsize=(4, 3))
            df[selected_cat].value_counts().plot(kind='bar', ax=ax)
            ax.set_title(f"Barplot of {selected_cat}")
            st.pyplot(fig)
            plt.close(fig)
        with st.expander("Top 10 Frequent Values"):
            st.write(df[selected_cat].value_counts().head(10))
    else:
        st.info("No categorical columns found.")

    # --------------------------
    # Step 9: Missing Value Heatmap
    # --------------------------
    st.header("Step 9: Missing Value Heatmap")
    if df.isnull().sum().sum() > 0:
        if st.button("🟠 Show Missing Heatmap", key="missing_btn"):
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap="viridis", ax=ax)
            st.pyplot(fig)
            plt.close(fig)
    else:
        st.info("No missing values found.")

    # --------------------------
    # Step 10: Outlier Detection
    # --------------------------
    st.header("Step 10: Outlier Detection (IQR method)")
    if numeric_cols:
        outlier_summary = {}
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
            outlier_summary[col] = len(outliers)
        with st.expander("Number of Outliers per Column"):
            st.write(outlier_summary)
    else:
        st.info("No numeric columns for outlier detection.")

else:
    st.info("⬆️ Upload a CSV file to start step-by-step EDA")
