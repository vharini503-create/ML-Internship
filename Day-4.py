print("----- DAY 4 PYTHON PRACTICE -----")

# 1. FOR LOOP

print("\nNumbers from 1 to 10")

for i in range(1, 11):
    print(i)

# 2. WHILE LOOP

print("\nNumbers from 1 to 5")

count = 1

while count <= 5:
    print(count)
    count += 1

# 3. SUM OF FIRST N NUMBERS

n = int(input("\nEnter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

# 4. MULTIPLICATION TABLE

num = int(input("\nEnter a number: "))

print("\nMultiplication Table")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 5. EVEN NUMBERS

print("\nEven Numbers from 1 to 20")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 6. BREAK

print("\nBreak Example")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

# 7. CONTINUE

print("\nContinue Example")

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

# 8. NESTED LOOP

print("\nStar Pattern")

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# 9. FACTORIAL

num = int(input("\nEnter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

# 10. COUNTDOWN

print("\nCountdown")

num = 5

while num > 0:
    print(num)
    num -= 1

print("Done!")

print("\n----- DAY 4 COMPLETED -----")