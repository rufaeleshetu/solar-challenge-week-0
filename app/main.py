import sys
import os

# Add src to the system path so it can import eda_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import streamlit as st
from eda_utils import load_data, show_boxplot, show_top_regions

st.set_page_config(page_title="🌍 Solar Energy Dashboard", layout="wide")
st.title("🌍 Solar Farm Data Insights Dashboard")

# Sidebar widget to select country
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])

# Load the data
df = load_data(country)

if not df.empty:
    st.markdown(f"### Boxplot of GHI in {country}")
    show_boxplot(df)

    st.markdown(f"### Top Insights for {country}")
    show_top_regions(df)
