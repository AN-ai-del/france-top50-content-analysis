import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="France Top 50 Playlist Analysis",
    page_icon="🎵",
    layout="wide"
)

df = pd.read_csv("data/Atlantic_France_cleaned.csv")
df["date"] = pd.to_datetime(df["date"])
df["duration_min"] = df["duration_ms"] / 60000


def duration_bucket(duration):
    if duration < 2.5:
        return "Short"
    elif duration < 4:
        return "Medium"
    else:
        return "Long"


def rank_tier(position):
    if position <= 10:
        return "Top 10"
    elif position <= 25:
        return "Top 25"
    else:
        return "Top 50"


df["duration_bucket"] = df["duration_min"].apply(duration_bucket)
df["rank_tier"] = df["position"].apply(rank_tier)

st.sidebar.header("Filters")

min_date = df["date"].min()
max_date = df["date"].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

album_filter = st.sidebar.multiselect(
    "Album Type",
    options=df["album_type"].unique(),
    default=df["album_type"].unique()
)

explicit_filter = st.sidebar.multiselect(
    "Explicit Content",
    options=df["is_explicit"].unique(),
    default=df["is_explicit"].unique()
)

rank_filter = st.sidebar.multiselect(
    "Rank Tier",
    options=df["rank_tier"].unique(),
    default=df["rank_tier"].unique()
)

start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[1])

filtered_df = df[
    (df["date"] >= start_date)
    & (df["date"] <= end_date)
    & (df["album_type"].isin(album_filter))
    & (df["is_explicit"].isin(explicit_filter))
    & (df["rank_tier"].isin(rank_filter))
]

st.title("🎵 France Top 50 Playlist Analysis")

st.markdown(
    """
    Audience Sensitivity, Content Compliance &
    Format Preference Analysis Dashboard
    """
)

total_records = len(filtered_df)

explicit_percentage = filtered_df["is_explicit"].mean() * 100
avg_duration = filtered_df["duration_min"].mean()
album_percentage = (filtered_df["album_type"] == "album").mean() * 100

acceptance_score = (
    filtered_df["popularity"].mean()
    * (51 - filtered_df["position"].mean())
    / 50
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Records", f"{total_records:,}")
col2.metric("Explicit %", f"{explicit_percentage:.2f}%")
col3.metric("Avg Duration", f"{avg_duration:.2f} min")
col4.metric("Album %", f"{album_percentage:.2f}%")
col5.metric("Acceptance Score", f"{acceptance_score:.1f}")

st.subheader("Explicit vs Clean Content")

explicit_counts = filtered_df["is_explicit"].value_counts().reset_index()
explicit_counts.columns = ["Content Type", "Count"]

fig1 = px.pie(
    explicit_counts,
    names="Content Type",
    values="Count",
    title="Explicit vs Clean Distribution"
)

st.plotly_chart(fig1, width="stretch")

st.subheader("Album Type Distribution")

album_counts = filtered_df["album_type"].value_counts().reset_index()
album_counts.columns = ["Album Type", "Count"]

fig2 = px.bar(
    album_counts,
    x="Album Type",
    y="Count",
    title="Album vs Single Tracks"
)

st.plotly_chart(fig2, width="stretch")

st.subheader("Song Duration Distribution")

fig3 = px.histogram(
    filtered_df,
    x="duration_min",
    nbins=30,
    title="Distribution of Song Duration (Minutes)"
)

st.plotly_chart(fig3, width="stretch")

st.subheader("Duration Category Analysis")

duration_counts = filtered_df["duration_bucket"].value_counts().reset_index()
duration_counts.columns = ["Duration Category", "Count"]

fig4 = px.bar(
    duration_counts,
    x="Duration Category",
    y="Count",
    title="Short vs Medium vs Long Songs"
)

st.plotly_chart(fig4, width="stretch")

st.subheader("Album Size Distribution")

fig5 = px.histogram(
    filtered_df,
    x="total_tracks",
    nbins=30,
    title="Album Size Distribution"
)

st.plotly_chart(fig5, width="stretch")

st.subheader("Album Size vs Popularity")

fig6 = px.scatter(
    filtered_df,
    x="total_tracks",
    y="popularity",
    title="Album Size Impact on Popularity"
)

st.plotly_chart(fig6, width="stretch")

st.subheader("Rank Tier Comparison")

rank_summary = (
    filtered_df
    .groupby("rank_tier")["popularity"]
    .mean()
    .reset_index()
)

fig7 = px.bar(
    rank_summary,
    x="rank_tier",
    y="popularity",
    title="Average Popularity by Rank Tier"
)

st.plotly_chart(fig7, width="stretch")

st.subheader("Explicit Content by Rank Tier")

explicit_rank = pd.crosstab(
    filtered_df["rank_tier"],
    filtered_df["is_explicit"]
)

fig8 = px.bar(
    explicit_rank,
    barmode="group",
    title="Explicit vs Clean Songs Across Rank Tiers"
)

st.plotly_chart(fig8, width="stretch")

st.subheader("Most Frequent Artists")

top_artists = (
    filtered_df["artist"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_artists.columns = ["Artist", "Appearances"]

fig9 = px.bar(
    top_artists,
    x="Artist",
    y="Appearances",
    title="Top Artists in France Top 50"
)

st.plotly_chart(fig9, width="stretch")

st.subheader("France Market Insights")

st.info(
    f"""
    • Explicit content represents {explicit_percentage:.1f}% of chart entries.

    • Album tracks represent {album_percentage:.1f}% of chart entries.

    • Average song duration is {avg_duration:.2f} minutes.

    • Content Acceptance Score is {acceptance_score:.1f}.

    • These insights help Atlantic Records understand content acceptance,
      format preference, and audience behavior in the French music market.
    """
)

st.subheader("Executive Summary")

st.success(
    f"""
    Key Findings:

    • Explicit content accounts for {explicit_percentage:.1f}% of chart entries.

    • Album tracks account for {album_percentage:.1f}% of chart entries.

    • Average song duration is {avg_duration:.2f} minutes.

    • Content Acceptance Score is {acceptance_score:.1f}.

    • The France Top 50 demonstrates strong acceptance of explicit content
      and balanced representation of album and single releases.
    """
)

st.subheader("Filtered Dataset")

st.dataframe(
    filtered_df.head(100),
    width="stretch"
)