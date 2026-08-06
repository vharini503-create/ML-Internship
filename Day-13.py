import matplotlib.pyplot as plt

print("-----  DAY 13 - MATPLOTLIB BASICS -----")

# 1. Line Plot

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.figure(figsize=(5,3))
plt.plot(x, y, marker="o")
plt.title("Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

# 2. Bar Chart

subjects = ["Python", "Java", "C++", "ML"]
marks = [90, 80, 75, 95]

plt.figure(figsize=(5,3))
plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart

languages = ["Python", "Java", "C++"]
students = [50, 30, 20]

plt.figure(figsize=(5,5))
plt.pie(students, labels=languages, autopct="%1.1f%%")
plt.title("Programming Language Preference")
plt.show()

# 4. Scatter Plot

height = [150, 155, 160, 165, 170]
weight = [45, 50, 55, 60, 65]

plt.figure(figsize=(5,3))
plt.scatter(height, weight)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()

print("\n----- DAY 13 COMPLETED -----")