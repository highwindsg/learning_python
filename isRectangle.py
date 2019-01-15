#!/usr/bin/env python3

# Write a program that contains a function called isRectangle.
# The function is passed four parameters representing the length of each of the four
# sides of a shape in the order of left, top, right, bottom.
# Asumme that all angles are 90-degrees angles.

def isRectangle(left, right, top, bottom):
    if left == right and top == bottom:
        rectangleSides = True
    else:
        rectangleSides = False
    return rectangleSides

def printRectangle(side1, side2, side3, side4):
    # Next line calls the 'isRectangle' function and parses in four sides of the
    # params each corresponding directly to the left, right, top and bottom.
    theResult = isRectangle(side1, side2, side3, side4)
    if theResult is True:       # 'is True' is redundant, but easier to read.
        print(side1, side2, side3, "and", side4, "represents a rectangle.")
    else:
        print(side1, side2, side3, "and", side4, "do not represents a rectangle.")

# Test cases.
printRectangle(4, 4, 8, 8)
printRectangle(4, 2, 8, 8)

# Alternatively, get user to input four of the sides assuming in cm.
user_left = float(input("Enter cm for left side: "))
user_right = float(input("Enter cm for right side: "))
user_top = float(input("Enter cm for top side: "))
user_bottom = float(input("Enter cm for bottom side: "))
printRectangle(user_left, user_right, user_top, user_bottom)
