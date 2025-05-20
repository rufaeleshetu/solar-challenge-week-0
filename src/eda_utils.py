import pandas as pd
import streamlit as st
import os


def load_data(country):
    filename = f"{country.lower().replace(' ', '_')}_clean.csv"
    filepath = os.path.join("data", filename)

    st.write("Trying to load:", filepath)  # debug
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        st.error(f"File not found: {filepath}")
        return pd.DataFrame()


def show_boxplot(df):
    st.write("📊 Boxplot would go here")
    # optional: add actual plotting logic


def show_top_regions(df):
    st.write("🌍 Top insights go here")
