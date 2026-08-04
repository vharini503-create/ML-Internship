import numpy as np

print("----- DAY 11 NUMPY PRACTICE -----")

# 1. Create Arrays

arr1 = np.array([10, 20, 30, 40, 50])

print("\n1D Array:")
print(arr1)

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\n2D Array:")
print(arr2)

# 2. Array Information

print("\nShape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

# 3. Indexing

print("\nFirst Element:", arr1[0])
print("Last Element:", arr1[-1])

# 4. Slicing

print("\nSliced Array:", arr1[1:4])

# 5. Array Operations

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nAddition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# 6. Mathematical Functions

numbers = np.array([5, 10, 15, 20])

print("\nSum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# 7. Reshape

array = np.array([1, 2, 3, 4, 5, 6])

print("\nReshaped Array:")
print(array.reshape(2, 3))

# 8. User Input Array

nums = input("\nEnter numbers separated by space: ")

arr = np.array(nums.split(), dtype=int)

print("Array:", arr)
print("Square of Elements:", arr ** 2)

print("\n----- DAY 11 COMPLETED -----")