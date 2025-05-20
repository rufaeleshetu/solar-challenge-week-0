# app/main.py

import os
import sys

# Add project root to Python path so src/ can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from src.eda_utils import load_data, show_boxplot, show_top_regions

# Page settings
st.set_page_config(page_title="🌞 Solar Energy Dashboard", layout="wide")
st.title("🌍 Solar Farm Data Insights Dashboard")

# Sidebar for selecting country
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])

# Load the data
df = load_data(country)

if not df.empty:
    # Boxplot section
    st.markdown(f"### Boxplot of GHI in {country}")
    show_boxplot(df)

    # Top insights section
    st.markdown(f"### Top Insights for {country}")
    show_top_regions(df)
else:
    st.warning("No data found for the selected country.")
