import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config("AI Data Analysis Agent", layout="wide")
st.title("🤖 AI Data Analysis Agent")

# ======================
# 🚀 FAST CSV LOAD (CACHE)
# ======================
@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = load_csv(uploaded_file)

    # ======================
    # 1️⃣ SUMMARY
    # ======================
    st.subheader("📌 Dataset Summary")

    summary = {
        "Rows": int(df.shape[0]),
        "Columns": int(df.shape[1]),
        "Column Names": df.columns.tolist(),
        "Missing Values": df.isnull().sum().to_dict(),
        "Duplicate Rows": int(df.duplicated().sum())
    }

    st.json(summary)

    # ======================
    # 2️⃣ DATA PREVIEW
    # ======================
    with st.expander("🔍 View Data"):
        st.dataframe(df.head())

    # ======================
    # 3️⃣ VISUALIZATION (FAST)
    # ======================
    st.subheader("📊 Visualizations")

    num_cols = df.select_dtypes(include=np.number).columns

    selected_col = st.selectbox("Select column", num_cols)

    # ⚡ SAMPLE DATA FOR SPEED
    data = df[selected_col].dropna()
    if len(data) > 50000:
        data = data.sample(50000, random_state=42)

    if st.button("📈 Generate Plot"):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(data, bins=30)
        ax.set_title(f"Distribution of {selected_col}")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
        plt.close(fig)

else:
    st.info("⬆️ CSV upload kara")
