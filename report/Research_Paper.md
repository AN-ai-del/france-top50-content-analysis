Audience Sensitivity, Content Compliance & Format Preference Analysis of France Top 50 Playlist
Author

Anushka Das

Internship

Unified Mentor Programme

Organization

Atlantic Recording Corporation

Abstract

This project analyzes the France Top 50 Playlist dataset to understand audience sensitivity toward explicit content, content compliance preferences, release format acceptance, and structural music characteristics. The analysis focuses on explicit content performance, album versus single representation, song duration preferences, and album structure impact on popularity. Using Python, Pandas, Plotly, and Streamlit, exploratory data analysis (EDA) and business intelligence techniques were applied to generate actionable insights. The findings reveal strong acceptance of explicit content, balanced representation between album and single releases, and a preference for medium-duration songs.

Keywords: Music Analytics, France Top 50, Explicit Content, Album Analysis, Streamlit Dashboard, Data Analytics

Table of Contents
Introduction
Problem Statement
Dataset Description
Data Preparation
Methodology
Exploratory Data Analysis
Results and Insights
Recommendations
Dashboard Overview
Conclusion
References
1. Introduction

The modern music industry increasingly relies on data-driven decision-making to understand listener behavior and optimize content strategies. Different markets demonstrate varying levels of acceptance toward explicit content, release formats, and album structures.

France is one of Europe's most influential music markets, making it important for record labels to understand audience preferences. This project analyzes playlist data to identify patterns that can help Atlantic Recording Corporation improve release planning and content strategies.

2. Problem Statement

Atlantic Recording Corporation seeks answers to the following questions:

How well does explicit content perform compared to clean content?
Do album tracks outperform singles?
What song durations are most common among successful tracks?
Does album size influence popularity?
How does content distribution vary across ranking tiers?

Without these insights, release strategies may not align with audience expectations.

3. Dataset Description

The dataset contains daily France Top 50 playlist records.

Dataset Fields
Column Name	Description
date	Playlist snapshot date
position	Playlist ranking
song	Song title
artist	Artist name
popularity	Popularity score
duration_ms	Song duration in milliseconds
album_type	Album, Single, or Compilation
total_tracks	Number of tracks in album
is_explicit	Explicit content flag
album_cover_url	Album artwork URL
Dataset Statistics
Original Records: 27,800
Cleaned Records: 27,781
Missing Values Fixed: 1
Duplicate Records Removed: 19
4. Data Preparation

Data preparation was performed before analysis to ensure data quality.

Missing Value Handling

A missing song title entry was identified and replaced appropriately.

Duplicate Removal

Nineteen duplicate rows were removed from the dataset.

Data Standardization

The following transformations were applied:

Date conversion to datetime format
Album type standardization
Explicit flag normalization
Text cleaning
Feature Engineering

New features created:

Duration Categories
Short (< 2.5 minutes)
Medium (2.5 – 4 minutes)
Long (> 4 minutes)
Rank Tiers
Top 10
Top 25
Top 50
5. Methodology

The project followed the following workflow:

Data Collection
Data Cleaning
Feature Engineering
Exploratory Data Analysis
Dashboard Development
Business Insight Generation

The analysis was performed using:

Python
Pandas
Plotly
Streamlit
6. Exploratory Data Analysis
6.1 Explicit Content Analysis

The distribution of explicit and clean songs was examined.

Findings
Category	Percentage
Explicit	56.26%
Clean	43.74%

Explicit content represents the majority of playlist entries.

6.2 Album Type Analysis

The representation of album tracks and singles was analyzed.

Findings
Album Type	Percentage
Album	52.86%
Single	47.10%
Compilation	0.03%

Album tracks maintain a slight advantage over singles.

6.3 Duration Analysis

Song durations were converted from milliseconds to minutes.

Findings
Average Duration: 3.09 minutes
Medium-duration songs dominate the chart.

The majority of successful tracks fall within the 2.5–4 minute range.

6.4 Album Structure Analysis

Album size was analyzed using the total_tracks variable.

Findings

Most successful songs originate from albums containing between 1 and 20 tracks.

Very large albums appear less frequently within the France Top 50.

6.5 Rank Tier Analysis

Tracks were categorized into:

Top 10
Top 25
Top 50

Popularity and explicit content distribution were compared across tiers.

Findings

The Top 10 contains the highest concentration of explicit content, suggesting strong listener acceptance.

7. Results and Insights
Insight 1: Explicit Content Dominates

Explicit songs account for more than half of all playlist entries, indicating strong audience acceptance.

Insight 2: Albums Remain Important

Album tracks slightly outperform singles, suggesting listeners continue to engage with complete album releases.

Insight 3: Medium-Length Songs Perform Best

Songs between 2.5 and 4 minutes appear most frequently within successful chart entries.

Insight 4: Album Size Influences Visibility

Moderately sized albums demonstrate stronger chart representation than extremely large albums.

Insight 5: Popularity Remains Consistent Across Rank Tiers

Popularity scores remain relatively stable across Top 10, Top 25, and Top 50 tracks.

8. Recommendations

Based on the findings, the following recommendations are proposed:

Recommendation 1

Continue supporting explicit releases where appropriate, as audience acceptance remains high.

Recommendation 2

Maintain investment in album-based release strategies, as album tracks continue to perform strongly.

Recommendation 3

Prioritize songs within the 2.5–4 minute range to align with listener preferences.

Recommendation 4

Focus on moderately sized album projects rather than excessively large releases.

Recommendation 5

Use playlist analytics continuously to adapt release strategies to evolving audience behavior.

9. Dashboard Overview

An interactive Streamlit dashboard was developed to visualize and explore the data.

Dashboard Features
Date Range Filter
Album Type Filter
Explicit Content Filter
Rank Tier Filter
KPI Cards
Explicit Content Analysis
Album Type Analysis
Duration Analysis
Album Size Impact Analysis
Executive Summary Section

The dashboard enables dynamic exploration of audience behavior and content preferences.

10. Conclusion

The France Top 50 Playlist demonstrates strong acceptance of explicit content, balanced representation between albums and singles, and a preference for medium-duration songs. Album size also appears to influence track visibility, with moderately sized albums performing most consistently.

The insights generated through this project provide valuable guidance for Atlantic Recording Corporation in designing release strategies tailored to the French music market.

11. References
France Top 50 Playlist Dataset
Unified Mentor Programme Project Documentation
Atlantic Recording Corporation Project Brief
Python Documentation
Pandas Documentation
Plotly Documentation
Streamlit Documentation
Appendix
Tools Used
Python
Pandas
NumPy
Plotly
Streamlit
GitHub
VS Code
Deliverables
Data Cleaning Pipeline
KPI Analysis
Interactive Dashboard
Research Paper
Executive Summary
GitHub Repository