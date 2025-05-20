import streamlit as st
import pandas as pd


from utils import load_data, show_boxplot, show_top_regions

st.set_page_config(page_title="🌞 Solar Energy Dashboard", layout="wide")
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
else:
    st.warning("Data not found or failed to load.")
