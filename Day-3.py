print("----- DAY 3 PYTHON PRACTICE -----")

# 1. INPUT & OUTPUT

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello,", name)
print("Your age is", age)

# 2. ARITHMETIC OPERATORS

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("\nArithmetic Operations")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power =", a ** b)

# 3. COMPARISON OPERATORS

print("\nComparison Operations")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# 4. LOGICAL OPERATORS

x = True
y = False

print("\nLogical Operations")
print("x AND y =", x and y)
print("x OR y =", x or y)
print("NOT x =", not x)

# 5. EVEN OR ODD

num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# 6. POSITIVE / NEGATIVE / ZERO

num = int(input("\nEnter another number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# 7. LARGEST OF THREE NUMBERS

n1 = int(input("\nEnter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 >= n2 and n1 >= n3:
    print("Largest =", n1)
elif n2 >= n1 and n2 >= n3:
    print("Largest =", n2)
else:
    print("Largest =", n3)

# 8. VOTING ELIGIBILITY

age = int(input("\nEnter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# 9. GRADE CALCULATOR

marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# 10. SIMPLE CALCULATOR

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Enter operation (+, -, *, /): ")

if choice == "+":
    print("Result =", num1 + num2)
elif choice == "-":
    print("Result =", num1 - num2)
elif choice == "*":
    print("Result =", num1 * num2)
elif choice == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")

print("\n----- DAY 3 COMPLETED -----")