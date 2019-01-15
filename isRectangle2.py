#!/usr/bin/env python3

# Write a program that contains a function called isRectangle.
# The function is passed four parameters representing the length of each of the four
# sides of a shape in the order of left, top, right, bottom.
# Asumme that all angles are 90-degrees angles.

def isRectangle(left, top, right, bottom):
    if left == right:
       # return True    # This line can be redundant.
        if top == bottom:
            return True
    else:
        return False

def printRectangle(someLeft, someTop, someRight, someBottom):
    if isRectangle(someLeft, someTop, someRight, someBottom):
        print(someLeft, someTop, someRight, someBottom, "represents a rectangle.")
    else:
        print(someLeft, someTop, someRight, someBottom, "do not represents a rectangle.")

# Test cases.
printRectangle(5, 6, 5, 6)
printRectangle(5, 6, 7, 8)

# Get user input and call the function.
userLeft = int(input("Enter the left: "))
userTop = int(input("Enter the top: "))
userRight = int(input("Enter the right: "))
userBottom = int(input("Enter the bottom: "))
printRectangle(userLeft, userTop, userRight, userBottom)
