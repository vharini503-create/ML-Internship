print("----- DAY 8 PYTHON PRACTICE -----")

# 1. Creating Strings

name = "Harini"

print("Name:", name)

# 2. String Indexing

print("\nFirst Character:", name[0])
print("Last Character:", name[-1])

# 3. String Slicing

print("\nFirst 3 Characters:", name[:3])
print("Last 3 Characters:", name[-3:])

# 4. String Methods

text = "python programming"

print("\nOriginal:", text)
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Replace:", text.replace("python", "Java"))
print("Length:", len(text))

# 5. Check String

word = input("\nEnter a word: ")

print("Is Alphabet?", word.isalpha())
print("Is Digit?", word.isdigit())
print("Is Alphanumeric?", word.isalnum())

# 6. Reverse a String

string = input("\nEnter a string: ")

print("Reversed:", string[::-1])

# 7. Palindrome Check

text = input("\nEnter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# 8. Count Vowels

sentence = input("\nEnter a sentence: ")

count = 0

for ch in sentence.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

# 9. Count Words

sentence = input("\nEnter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))

# 10. String Concatenation

first = input("\nEnter First Name: ")
last = input("Enter Last Name: ")

full = first + " " + last

print("Full Name:", full)

print("\n----- DAY 8 COMPLETED -----")