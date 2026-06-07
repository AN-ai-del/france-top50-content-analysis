import streamlit as st
import pandas as pd

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="France Top 50 Analysis",
    page_icon="🎵",
    layout="wide"
)

# -----------------------
# Load Data
# -----------------------
df = pd.read_csv("data/Atlantic_France_cleaned.csv")

# -----------------------
# Title
# -----------------------
st.title("🎵 France Top 50 Playlist Analysis")

st.markdown("""
Audience Sensitivity, Content Compliance &
Format Preference Analysis Dashboard
""")

# -----------------------
# KPI Calculations
# -----------------------
total_songs = len(df)

explicit_percentage = (
    df["is_explicit"].mean() * 100
)

avg_duration = (
    df["duration_ms"].mean() / 60000
)

album_percentage = (
    (df["album_type"] == "album").mean() * 100
)

# -----------------------
# KPI Cards
# -----------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Records",
    f"{total_songs:,}"
)

col2.metric(
    "Explicit Content %",
    f"{explicit_percentage:.2f}%"
)

col3.metric(
    "Average Duration",
    f"{avg_duration:.2f} min"
)

col4.metric(
    "Album Tracks %",
    f"{album_percentage:.2f}%"
)

# -----------------------
# Dataset Preview
# -----------------------
st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    width="stretch"
)