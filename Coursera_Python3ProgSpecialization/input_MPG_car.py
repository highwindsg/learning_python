#!/usr/bin/env python3

"""
Write a program that will compute MPG for a car. 
Prompt the user to enter the number of miles driven and the number of 
gallons used. Print a nice message with the answer.

Formula for calculating Miles per Gallon (MPG):
(end – start) = miles driven
Miles Driven / Gallons Used = MPG
"""

miles = float(input("Enter miles driven: "))
gallons = float(input("Number of gallons used: "))
MPG = miles // gallons
print("Your car uses", MPG, "gallons per mile.")
print("")

# Or create a function.
def mpg(miles, gallons):
    miles = float(miles) // gallons
    km = miles * 0.425
    print("Your car uses", miles, "mpg or in km/litre,", km)
    return miles

mpg(30, 12)
print("")
