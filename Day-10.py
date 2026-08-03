print("----- DAY 10 PYTHON PRACTICE -----")

# 1. Basic try-except

print("\n1. Division Program")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

# 2. try-except-else

print("\n2. try-except-else")

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)

# 3. try-except-finally

print("\n3. try-except-finally")

try:
    file = open("sample.txt", "w")
    file.write("Hello, Python!")
    print("Data written successfully.")
except Exception as e:
    print("Error:", e)
finally:
    file.close()
    print("File closed.")

# 4. Multiple Exceptions

print("\n4. Multiple Exceptions")

try:
    numbers = [10, 20, 30]
    index = int(input("Enter index (0-2): "))
    print("Value =", numbers[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Please enter a valid integer.")

# 5. Raise Exception

print("\n5. Raise Exception")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age =", age)

except ValueError as e:
    print("Error:", e)

# 6. Password Validation

print("\n6. Password Validation")

try:
    password = input("Enter password: ")

    if len(password) < 6:
        raise ValueError("Password must contain at least 6 characters.")

    print("Password accepted.")

except ValueError as e:
    print("Error:", e)

print("\n----- DAY 10 COMPLETED -----")