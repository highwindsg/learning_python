#!/usr/bin/env python3

course = "Python for Beginners"

# Replace the word 'Beginners' with 'Absolute Beginners'.
print(course.replace("Beginners", "Absolute Beginners"))

# Find the index position of the first letter 'o'.
print(course.find("o"))

# Check if the word 'Python' is in the var course. If yes, then it will return
# a boolean True. The 'in' operator produces a boolean value.
print("Python" in course)

# Check if the word 'python' is in the var course. If no, then it will return
# a boolean False. The 'in' operator produces a boolean value.
print("python" in course)

# Prints the output where the first character of every word for capitalized.
print(course.title())

# Prints the output in all upper case.
print(course.upper())

# Prints the output in all lower case.
print(course.lower())

