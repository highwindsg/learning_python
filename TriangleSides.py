#!/usr/bin/env python3

# To calculate the longest side of two different sets of triangles.
# Assumes that values passed in could be values representing strings.
def calculateHypotenuse(side1, side2):
    side1 = float(side1)
    side2 = float(side2)
    hypot = ((side1 ** 2) + (side2 ** 2)) ** 0.5
    return hypot

firstTriangleSide1 = input("Enter side 1: ")
firstTriangleSide2 = input("Enter side 2: ")
# Call function to calculate hypotenuse of first triangle.
hypot1 = calculateHypotenuse(firstTriangleSide1, firstTriangleSide2)

secondTriangleSide1 = input("Enter the first side: ")
secondTriangleSide2 = input("Enter second side: ")
# Call function to calculate hypotenuse of second triangle.
hypot2 = calculateHypotenuse(secondTriangleSide1, secondTriangleSide2)

print("The hypotenuse of the first triangle is: ", hypot1)
print("The hypotenuse of the second triangle is: ", hypot2)
