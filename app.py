import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="France Top 50 Analysis",
    page_icon="🎵",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("data/Atlantic_France_cleaned.csv")

df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Filters")

# Date Filter
min_date = df['date'].min()
max_date = df['date'].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

# Album Type Filter
album_filter = st.sidebar.multiselect(
    "Album Type",
    options=df['album_type'].unique(),
    default=df['album_type'].unique()
)

# Explicit Filter
explicit_filter = st.sidebar.multiselect(
    "Explicit Content",
    options=df['is_explicit'].unique(),
    default=df['is_explicit'].unique()
)

# -----------------------------
# Rank Tier Creation
# -----------------------------
def rank_tier(position):
    if position <= 10:
        return "Top 10"
    elif position <= 25:
        return "Top 25"
    else:
        return "Top 50"

df["rank_tier"] = df["position"].apply(rank_tier)

rank_filter = st.sidebar.multiselect(
    "Rank Tier",
    options=df["rank_tier"].unique(),
    default=df["rank_tier"].unique()
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df[
    (df["album_type"].isin(album_filter))
    &
    (df["is_explicit"].isin(explicit_filter))
    &
    (df["rank_tier"].isin(rank_filter))
]

# -----------------------------
# Title
# -----------------------------
st.title("🎵 France Top 50 Playlist Analysis")

st.markdown(
    "Audience Sensitivity, Content Compliance & Format Preference Analysis Dashboard"
)

# -----------------------------
# KPIs
# -----------------------------
total_records = len(filtered_df)

explicit_percentage = (
    filtered_df["is_explicit"].mean() * 100
)

avg_duration = (
    filtered_df["duration_ms"].mean() / 60000
)

album_percentage = (
    (filtered_df["album_type"] == "album").mean() * 100
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Records", f"{total_records:,}")
col2.metric("Explicit %", f"{explicit_percentage:.2f}%")
col3.metric("Avg Duration", f"{avg_duration:.2f} min")
col4.metric("Album %", f"{album_percentage:.2f}%")

# -----------------------------
# Charts
# -----------------------------

st.subheader("Explicit vs Clean Content")

explicit_counts = (
    filtered_df["is_explicit"]
    .value_counts()
    .reset_index()
)

explicit_counts.columns = [
    "Content Type",
    "Count"
]

fig1 = px.pie(
    explicit_counts,
    names="Content Type",
    values="Count",
    title="Explicit vs Clean Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# -----------------------------

st.subheader("Album Type Distribution")

album_counts = (
    filtered_df["album_type"]
    .value_counts()
    .reset_index()
)

album_counts.columns = [
    "Album Type",
    "Count"
]

fig2 = px.bar(
    album_counts,
    x="Album Type",
    y="Count",
    title="Album vs Single Tracks"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------------
# Data Preview
# -----------------------------

st.subheader("Filtered Dataset")

st.dataframe(
    filtered_df.head(100),
    width="stretch"
)