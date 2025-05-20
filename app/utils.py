import pandas as pd
import os
import streamlit as st

def load_data(country):
    filename = f"{country.lower().replace(' ', '_')}_clean.csv"
    filepath = os.path.join("data", filename)

    st.write("Trying to load:", filepath)  # Debug print

    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        st.error(f"File not found: {filepath}")
        return pd.DataFrame()