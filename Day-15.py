import pandas as pd

print("----- DAY 15 - DATA PREPROCESSING -----")

# 1. Create Sample Dataset

data = {
    "Name": ["Harini", "Anu", "Kavi", "Harini"],
    "Age": [20, 21, None, 20],
    "Marks": [90, 85, 95, 90]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# 2. Dataset Information

print("\nDataset Information:")
df.info()

# 3. Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# 4. Fill Missing Values

df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAfter Filling Missing Values:")
print(df)

# 5. Remove Duplicates

df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# 6. Summary Statistics

print("\nSummary Statistics:")
print(df.describe())

# 7. Save Cleaned Dataset

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_data.csv'")

print("\n----- DAY 15 COMPLETED -----")