import pandas as pd
import matplotlib.pyplot as plt

print("----- DAY 16 - EDA -----")

# 1. Create Dataset

data = {
    "Name": ["Harini", "Anu", "Kavi", "Priya", "Arun",
             "Rahul", "Divya", "Meena", "Vijay", "Riya"],

    "Age": [20, 21, 20, 22, 21,
            23, 20, 22, 21, 20],

    "Study_Hours": [5, 6, 4, 8, 7,
                    3, 6, 9, 5, 7],

    "Marks": [75, 82, 68, 90, 85,
              60, 80, 95, 72, 88]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

# 2. First Five Rows

print("\nFirst 5 Rows:")
print(df.head())

# 3. Last Five Rows

print("\nLast 5 Rows:")
print(df.tail())

# 4. Dataset Shape

print("\nDataset Shape:")
print(df.shape)

# 5. Dataset Information

print("\nDataset Information:")
df.info()

# 6. Statistical Summary

print("\nStatistical Summary:")
print(df.describe())

# 7. Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# 8. Unique Values

print("\nUnique Ages:")
print(df["Age"].unique())

# 9. Average Marks

print("\nAverage Marks:")
print(df["Marks"].mean())

# 10. Highest Marks

print("\nHighest Marks:")
print(df["Marks"].max())

# 11. Students with Marks > 80

print("\nStudents with Marks above 80:")
print(df[df["Marks"] > 80])

# 12. Histogram

plt.figure(figsize=(6, 4))

plt.hist(df["Marks"], bins=5)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

# 13. Bar Chart

plt.figure(figsize=(7, 4))

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.show()

# 14. Scatter Plot

plt.figure(figsize=(6, 4))

plt.scatter(df["Study_Hours"], df["Marks"])

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

# 15. Correlation

print("\nCorrelation:")
print(df[["Age", "Study_Hours", "Marks"]].corr())

print("\n----- DAY 16 COMPLETED -----")