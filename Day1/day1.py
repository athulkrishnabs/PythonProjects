# Day 1: Combined Python Practice

# 1. Age Category & Adult Check
age = int(input("Enter your age: "))

if age >= 60:
    print("You are a Senior Citizen")
elif age >= 18:
    print("You are an Adult")
elif age >= 13:
    print("You are a Teenager")
else:
    print("You are a Minor")

# Adult check Yes/No
if age >= 18:
    print("Yes, you are an adult")
else:
    print("No, you are not an adult")

print()  # blank line for readability

# 2. Marks / Grades
marks = int(input("Enter your marks (0-100): "))
if marks >= 90:
    print("Grade: A - Excellent!")
elif marks >= 70:
    print("Grade: B - Good Job!")
elif marks >= 50:
    print("Grade: C - Needs Improvement")
else:
    print("Grade: Failed - Work Harder!")

print()

# 3. Even or Odd Number
num = int(input("Enter a number to check even or odd: "))
if num % 2 == 0:
    print(f"{num} is an Even Number")
else:
    print(f"{num} is an Odd Number")

print()

# 4. Password Check
password = input("Enter your password: ")
correct_password = "Drishyam123"

if password == correct_password:
    print("Access Granted! Welcome!")
else:
    print("Access Denied! Incorrect Password")
