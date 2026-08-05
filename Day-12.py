import pandas as pd

print("----- DAY 12 PANDAS PRACTICE -----")

# 1. Create Series

marks = pd.Series([85, 90, 78, 95])

print("\nSeries:")
print(marks)

# 2. Create DataFrame

student = {
    "Name": ["Harini", "Rahul", "Priya", "Arun"],
    "Age": [20, 21, 20, 22],
    "Marks": [85, 90, 78, 95]
}

df = pd.DataFrame(student)

print("\nDataFrame:")
print(df)

# 3. Display Information

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nLast 2 Rows:")
print(df.tail(2))

# 4. Select Column

print("\nNames:")
print(df["Name"])

# 5. Select Multiple Columns

print("\nName and Marks:")
print(df[["Name", "Marks"]])

# 6. Basic Statistics

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# 7. Filter Data

print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])

# 8. Save to CSV

df.to_csv("students.csv", index=False)

print("\nstudents.csv file created successfully.")

print("\n----- DAY 12 COMPLETED -----")