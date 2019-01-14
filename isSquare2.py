#!/usr/bin/env python3

# First function to determine if length and width represent a square.
def isSquare(length, width):
    if length == width:
        itsASquare = True
    else:
        itsASquare = False
    return itsASquare

# Second intermediate function that checks for a square and prints the result.
def printSquare(aLength, aWidth):   # Create second new function with two new params.
    theResult = isSquare(aLength, aWidth)   # Calling the first function and pass in
                                            # two params & assign to var 'theResult'.
    if theResult is True:   # 'is True' is redundant, but makes easy to understand.
        print(aLength, "and", aWidth, "represent a square.")
    else:
        print(aLength, "and", aWidth, "do not represent a square.")

# Test cases.
printSquare(5, 5)
printSquare(7.5, 8.5)

# Alternatively, get user input.
userLength = float(input("Enter a length: "))
userWidth = float(input("Enter a width: "))
printSquare(userLength, userWidth)
