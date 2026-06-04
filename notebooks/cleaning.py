import pandas as pd

# Load data
df = pd.read_csv("data/Atlantic_France.csv")

print("\n================ ORIGINAL SHAPE ================")
print(df.shape)

# -----------------------------
# 1. Handle Missing Values
# -----------------------------

df['song'] = df['song'].fillna("Unknown")

print("\nMissing values after fix:")
print(df.isnull().sum())

# -----------------------------
# 2. Remove Duplicates
# -----------------------------

df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)

# -----------------------------
# 3. Convert Date
# -----------------------------

df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)

# -----------------------------
# 4. Convert duration
# -----------------------------

df['duration_min'] = df['duration_ms'] / 60000

# -----------------------------
# 5. Clean text columns
# -----------------------------

df['album_type'] = df['album_type'].str.lower().str.strip()
df['artist'] = df['artist'].str.strip()
df['song'] = df['song'].str.strip()

# -----------------------------
# 6. Explicit standardization
# -----------------------------

df['is_explicit'] = df['is_explicit'].astype(str).str.lower()

# -----------------------------
# 7. Save cleaned dataset
# -----------------------------

df.to_csv("data/Atlantic_France_cleaned.csv", index=False)

print("\nCLEANING COMPLETE ✅")
print("Saved as: Atlantic_France_cleaned.csv")