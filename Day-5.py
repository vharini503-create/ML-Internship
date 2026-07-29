print("----- DAY 5 PYTHON PRACTICE -----")

# 1. Simple Function

def welcome():
    print("Welcome to Python Functions!")

welcome()

# 2. Function with Parameters

def greet(name):
    print("Hello,", name)

greet("Harini")

# 3. Addition Function

def add(a, b):
    print("Sum =", a + b)

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

add(num1, num2)

# 4. Function with Return Value

def square(number):
    return number * number

n = int(input("\nEnter a number: "))
result = square(n)

print("Square =", result)

# 5. Even or Odd Function

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("\nEnter a number: "))
print(number, "is", even_or_odd(number))

# 6. Largest Number Function

def largest(a, b, c):
    return max(a, b, c)

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest =", largest(a, b, c))

# 7. Factorial Function

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

num = int(input("\nEnter a number: "))
print("Factorial =", factorial(num))


# 8. Multiplication Table Function

def table(num):
    print("\nMultiplication Table")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

number = int(input("\nEnter a number: "))
table(number)

print("\n----- DAY 5 COMPLETED -----")