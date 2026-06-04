import pandas as pd

df = pd.read_csv("data/Atlantic_France.csv")

print("\n==================== DATA OVERVIEW ====================")
print("Shape:", df.shape)

print("\n==================== COLUMNS ====================")
print(df.columns.tolist())

print("\n==================== DATA INFO ====================")
print(df.info())

print("\n==================== FIRST 5 ROWS ====================")
print(df.head())

print("\n==================== MISSING VALUES ====================")
print(df.isnull().sum())

print("\n==================== DUPLICATES ====================")
print(df.duplicated().sum())