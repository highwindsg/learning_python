#!/usr/bin/env python3

"""
Try to enter the age in integer value, and if a value error occurs, except the
value error and change it to some other better message for the user.
"""

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0, pls try again.")
except ValueError:
    print("Invalid value, pls try again")

