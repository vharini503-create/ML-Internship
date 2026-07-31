print("----- DAY 7 PYTHON PRACTICE -----")

# 1. TUPLES

print("\n1. Tuples")

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Tuple:", fruits)
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])
print("Length:", len(fruits))

# 2. SETS

print("\n2. Sets")

numbers = {10, 20, 30, 40, 20, 10}

print("Original Set:", numbers)

numbers.add(50)
print("After add():", numbers)

numbers.remove(30)
print("After remove():", numbers)

# 3. SET OPERATIONS

print("\n3. Set Operations")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference (A-B):", A.difference(B))

# 4. DICTIONARIES

print("\n4. Dictionaries")

student = {
    "Name": "Harini",
    "Age": 20,
    "Course": "AI & ML"
}

print(student)

print("Name:", student["Name"])

student["College"] = "B.S. Abdur Rahman Crescent Institute"

print("Updated Dictionary:")
print(student)

# 5. LOOP THROUGH DICTIONARY

print("\n5. Dictionary Items")

for key, value in student.items():
    print(key, ":", value)

# 6. USER INPUT DICTIONARY

print("\n6. Student Details")

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")

details = {
    "Name": name,
    "Age": age,
    "Course": course
}

print("\nStudent Details")
print(details)

# 7. COUNT FREQUENCY

print("\n7. Frequency Counter")

items = [1, 2, 2, 3, 4, 3, 2, 5]

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)

print("\n----- DAY 7 COMPLETED -----")