#!/usr/bin/env python3

## Write a function that converts a string to a float and returns the result.
## Use exception handling to catch the exception that could occur.

def StrToFloat(x):
    """
    The line below converts whatever number
    entered in the x params and returns the
    answer to the StrToFloat function.
    """
    return float(x)

"""
Try to run the program and ask user
to input a number.
And if the user enters wrongly,
catch the error exception and inform
user to try again by creating a except
function to parse in the error word.
"""
try:
    number = str(input("Enter a number: "))
    print(float(number))

except(ValueError):     # The open and close parentheses/brackets are optional.
    print("Invalid, please try again.")

