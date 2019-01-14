#!/usr/bin/env python3

# Write a program code to call the function with test values for the length and
# width of the sides and print the results if they two values entered results
# in a square.

def isSquare(length, width):    # Pass in two params for length and width.
    if length == width:         # '==' means 'is equal equal' or 'is the same'.
        answer = "represent a square."
    else:
        answer = "do not represent a square."
    return answer

enter_length = float(input("Enter the cm of length: "))
enter_width = float(input("Enter the cm of width: "))
FinalAns = isSquare(enter_length, enter_width)
print(enter_length, "and", enter_width, FinalAns)
