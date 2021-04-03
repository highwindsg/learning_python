#!/usr/bin/env python3

"""
Homework:
=========
Get a number from the user and tell the user whether his number is
even or odd.
"""


myNumber = float(input("Please enter your number: "))

if myNumber % 2 == 0:   # any number mod by 2 gives 0, so is a number is an even number.
    print("You entered an even number.")
else:
    print("You entered an odd number.")
print("")
