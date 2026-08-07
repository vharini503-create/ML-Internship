import pandas as pd

print("------ DAY 14 : PANDAS BASICS ------")

# Create a Series
numbers = pd.Series([10, 20, 30, 40, 50])

print("\nSeries:")
print(numbers)

# Create a DataFrame
student = {
    "Name": ["Harini", "Anu", "Kavi"],
    "Age": [20, 21, 22],
    "Marks": [90, 85, 95]
}

df = pd.DataFrame(student)

print("\nDataFrame:")
print(df)

# Display first rows
print("\nFirst Rows:")
print(df.head())

# Display columns
print("\nColumns:")
print(df.columns)

# Display information
print("\nInformation:")
print(df.info())

# Display statistics
print("\nStatistics:")
print(df.describe())

# Select a column
print("\nNames:")
print(df["Name"])

# Select multiple columns
print("\nName and Marks:")
print(df[["Name", "Marks"]])

print("\n----- DAY 14 COMPLETED -----")