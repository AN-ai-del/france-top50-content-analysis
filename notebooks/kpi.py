import pandas as pd

# Load cleaned data
df = pd.read_csv("data/Atlantic_France_cleaned.csv")

print("\n================ KPI ANALYSIS ================\n")

# -----------------------------
# 1. Explicit Content Share
# -----------------------------
explicit_share = df['is_explicit'].value_counts(normalize=True) * 100
print("Explicit Content Share (%):")
print(explicit_share)

# -----------------------------
# 2. Single vs Album Ratio
# -----------------------------
album_ratio = df['album_type'].value_counts(normalize=True) * 100
print("\nAlbum Type Distribution (%):")
print(album_ratio)

# -----------------------------
# 3. Duration Analysis
# -----------------------------
df['duration_min'] = df['duration_ms'] / 60000
avg_duration = df['duration_min'].mean()

print("\nAverage Song Duration (min):", avg_duration)

# -----------------------------
# 4. Rank Tier Analysis
# -----------------------------
def rank_tier(pos):
    if pos <= 10:
        return "Top 10"
    elif pos <= 25:
        return "Top 25"
    else:
        return "Top 50"

df['rank_tier'] = df['position'].apply(rank_tier)

tier_analysis = pd.crosstab(df['rank_tier'], df['is_explicit'], normalize='index') * 100

print("\nExplicit Distribution by Rank Tier (%):")
print(tier_analysis)

# -----------------------------
# 5. Album Size Impact
# -----------------------------
album_impact = df.groupby('total_tracks')['popularity'].mean()

print("\nAlbum Size vs Popularity (sample):")
print(album_impact.head(10))