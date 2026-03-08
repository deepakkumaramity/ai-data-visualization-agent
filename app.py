
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI Data Visualization Agent")

file = st.file_uploader("Upload Dataset", type=["csv","xlsx"])

if file:
    if file.name.endswith("xlsx"):
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)

    st.write("Dataset Preview")
    st.dataframe(df.head())

    st.write("Basic Statistics")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) >= 2:
        col = st.selectbox("Select column for chart", numeric_cols)

        fig = plt.figure()
        df[col].hist()
        st.pyplot(fig)
