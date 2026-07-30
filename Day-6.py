print("----- DAY 6 PYTHON PRACTICE -----")

# 1. Creating a List

fruits = ["Apple", "Banana", "Orange", "Mango"]

print("Original List:")
print(fruits)

# 2. Accessing Elements

print("\nFirst Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])


# 3. List Slicing

print("\nFirst Two Fruits:", fruits[:2])
print("Last Two Fruits:", fruits[2:])


# 4. Adding Elements

fruits.append("Grapes")
print("\nAfter append():")
print(fruits)

fruits.insert(1, "Pineapple")
print("\nAfter insert():")
print(fruits)


# 5. Removing Elements

fruits.remove("Orange")
print("\nAfter remove():")
print(fruits)

fruits.pop()
print("\nAfter pop():")
print(fruits)

# 6. Sorting

numbers = [45, 12, 89, 23, 5]

print("\nOriginal Numbers:")
print(numbers)

numbers.sort()

print("Sorted Numbers:")
print(numbers)

# 7. Length of List

print("\nLength of Fruits List:", len(fruits))

# 8. Loop Through List

print("\nFruits List:")

for fruit in fruits:
    print(fruit)

# 9. Sum of List Elements

marks = [80, 75, 90, 85, 88]

total = sum(marks)

print("\nMarks:", marks)
print("Total Marks:", total)
print("Average Marks:", total / len(marks))

# 10. Find Largest Number

print("\nLargest Number:", max(numbers))
print("Smallest Number:", min(numbers))

print("\n----- DAY 6 COMPLETED -----")