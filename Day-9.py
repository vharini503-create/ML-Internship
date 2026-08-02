print("----- DAY 9 PYTHON PRACTICE -----")

# 1. Create and Write to a File

with open("student.txt", "w") as file:
    file.write("Name: Harini\n")
    file.write("Course: AI & ML\n")
    file.write("College: B.S. Abdur Rahman Crescent Institute\n")

print("File created and data written successfully.")

# 2. Read the File

print("\nReading File:")

with open("student.txt", "r") as file:
    content = file.read()

print(content)

# 3. Append Data

with open("student.txt", "a") as file:
    file.write("Year: 3rd Year\n")

print("Data appended successfully.")

# 4. Read File Line by Line

print("\nReading Line by Line:")

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())

# 5. Count Number of Lines

with open("student.txt", "r") as file:
    lines = file.readlines()

print("\nTotal Lines:", len(lines))

# 6. Count Number of Words

with open("student.txt", "r") as file:
    text = file.read()

words = text.split()

print("Total Words:", len(words))

# 7. User Input and Save

name = input("\nEnter your name: ")
age = input("Enter your age: ")

with open("user.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age)

print("User details saved successfully.")

# 8. Read User File

print("\nUser Details:")

with open("user.txt", "r") as file:
    print(file.read())

print("\n----- DAY 9 COMPLETED -----")