import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="France Top 50 Playlist Analysis",
    page_icon="🎵",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("data/Atlantic_France_cleaned.csv")

df["date"] = pd.to_datetime(df["date"])

# Duration in minutes
df["duration_min"] = df["duration_ms"] / 60000

# --------------------------------------------------
# DURATION BUCKETS
# --------------------------------------------------

def duration_bucket(duration):

    if duration < 2.5:
        return "Short"

    elif duration < 4:
        return "Medium"

    else:
        return "Long"


df["duration_bucket"] = df["duration_min"].apply(duration_bucket)

# --------------------------------------------------
# RANK TIERS
# --------------------------------------------------

def rank_tier(position):

    if position <= 10:
        return "Top 10"

    elif position <= 25:
        return "Top 25"

    else:
        return "Top 50"


df["rank_tier"] = df["position"].apply(rank_tier)

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Filters")

# Date Filter

min_date = df["date"].min()
max_date = df["date"].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

# Album Type Filter

album_filter = st.sidebar.multiselect(
    "Album Type",
    options=df["album_type"].unique(),
    default=df["album_type"].unique()
)

# Explicit Filter

explicit_filter = st.sidebar.multiselect(
    "Explicit Content",
    options=df["is_explicit"].unique(),
    default=df["is_explicit"].unique()
)

# Rank Tier Filter

rank_filter = st.sidebar.multiselect(
    "Rank Tier",
    options=df["rank_tier"].unique(),
    default=df["rank_tier"].unique()
)

# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[1])

filtered_df = df[
    (df["date"] >= start_date)
    &
    (df["date"] <= end_date)
    &
    (df["album_type"].isin(album_filter))
    &
    (df["is_explicit"].isin(explicit_filter))
    &
    (df["rank_tier"].isin(rank_filter))
]

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎵 France Top 50 Playlist Analysis")

st.markdown(
    """
    Audience Sensitivity, Content Compliance &
    Format Preference Analysis Dashboard
    """
)

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

total_records = len(filtered_df)

explicit_percentage = (
    filtered_df["is_explicit"].mean() * 100
)

avg_duration = (
    filtered_df["duration_min"].mean()
)

album_percentage = (
    (filtered_df["album_type"] == "album").mean() * 100
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Records",
    f"{total_records:,}"
)

col2.metric(
    "Explicit %",
    f"{explicit_percentage:.2f}%"
)

col3.metric(
    "Avg Duration",
    f"{avg_duration:.2f} min"
)

col4.metric(
    "Album %",
    f"{album_percentage:.2f}%"
)

# --------------------------------------------------
# EXPLICIT VS CLEAN
# --------------------------------------------------

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

# --------------------------------------------------
# ALBUM TYPE DISTRIBUTION
# --------------------------------------------------

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

# --------------------------------------------------
# DURATION HISTOGRAM
# --------------------------------------------------

st.subheader("Song Duration Distribution")

fig3 = px.histogram(
    filtered_df,
    x="duration_min",
    nbins=30,
    title="Distribution of Song Duration (Minutes)"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------------------------------
# DURATION CATEGORY ANALYSIS
# --------------------------------------------------

st.subheader("Duration Category Analysis")

duration_counts = (
    filtered_df["duration_bucket"]
    .value_counts()
    .reset_index()
)

duration_counts.columns = [
    "Duration Category",
    "Count"
]

fig4 = px.bar(
    duration_counts,
    x="Duration Category",
    y="Count",
    title="Short vs Medium vs Long Songs"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# --------------------------------------------------
# ALBUM SIZE DISTRIBUTION
# --------------------------------------------------

st.subheader("Album Size Distribution")

fig5 = px.histogram(
    filtered_df,
    x="total_tracks",
    nbins=30,
    title="Album Size Distribution"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# --------------------------------------------------
# ALBUM SIZE VS POPULARITY
# --------------------------------------------------

st.subheader("Album Size vs Popularity")

fig6 = px.scatter(
    filtered_df,
    x="total_tracks",
    y="popularity",
    title="Album Size Impact on Popularity"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

# --------------------------------------------------
# INSIGHTS PANEL
# --------------------------------------------------

st.subheader("France Market Insights")

explicit_pct = (
    filtered_df["is_explicit"].mean() * 100
)

album_pct = (
    (filtered_df["album_type"] == "album").mean() * 100
)

st.info(
    f"""
    • Explicit content represents {explicit_pct:.1f}% of chart entries.

    • Album tracks represent {album_pct:.1f}% of chart entries.

    • Average song duration is {avg_duration:.2f} minutes.

    • These insights help Atlantic Records understand
      content acceptance, format preference, and audience
      behavior in the French music market.
    """
)

# --------------------------------------------------
# DATASET PREVIEW
# --------------------------------------------------

st.subheader("Filtered Dataset")

st.dataframe(
    filtered_df.head(100),
    width="stretch"
)