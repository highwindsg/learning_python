#!/usr/bin/env python3

"""
Write a Python program that assigns the principal amount of 10000 to 
variable P, assign to n the value 12, and assign to r the interest 
rate of 8% (0.08). Then have the program prompt the user for the 
number of years, t, that the money will be compounded for. 
Calculate and print the final amount after t years.
"""

# PIL is the Python Image Library & we are using the Image module.
from PIL import Image
myImage = Image.open("compoundInterest.png")
myImage.show()

P = 10000
n = 12
r = 0.08
t = int(input(
    "Enter the number of years the money will be compounded for: "
))
A = P * ( ((1 + (r / n)) ** (n * t)) )

print("The final amount after", t, "years is", A)
print("")
