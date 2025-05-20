import pandas as pd
import streamlit as st
import os

def load_data(country):
    filename = f"{country.lower().replace(' ', '_')}_clean.csv"
    filepath = os.path.join("data", filename)

    st.write("Trying to load:", filepath)  # debug message

    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        st.error(f"File not found: {filepath}")
        return pd.DataFrame()

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_boxplot(df):
    if "GHI" in df.columns:
        plt.figure(figsize=(10, 4))
        sns.boxplot(x=df["GHI"])
        st.pyplot(plt)
    else:
        st.warning("GHI column not found in the dataset.")

def show_top_regions(df):
    if "GHI" in df.columns and "Timestamp" in df.columns:
        top_rows = df.sort_values("GHI", ascending=False).head(5)
        st.table(top_rows[["Timestamp", "GHI"]])
    else:
        st.warning("GHI or Timestamp column not found.")