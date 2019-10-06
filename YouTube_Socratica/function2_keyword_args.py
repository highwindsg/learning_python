#!/usr/bin/env python3

# To calculate a person's height from American units (feet and inches) to centimeters.
# 1 inch = 2.54 cm
# 1 foot = 12 inches

# Create a func named 'cm()' and parse in two keyword arguments with default values of 0.
def cm(feet=0, inches=0):
    """ Converts a length from feet and inches to centimeters. """
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


print(cm(feet=5))  # Converts 5 feet to centimeters.
print(cm(inches=70))  # Converts 70 inches to centimeters.
print(cm(feet=5, inches=8))  # Converts 5 feet and 8 inches to centimeters.
print(cm(inches=8, feet=5))  # Also can put the keyword inches first and the followed by feet.

print("")

""" There are two types of arguments in a function.
A 'keyword (aka default) argument' which requires an equal sign, and a 'required argument' which does not requires an
equal sign. When writing arguments in a function, you can use both types of arguments. But the 'keyword argument' with
equal sign must be the last one. """


def g(y, x=0):  # Create a func named 'g()' with non-default keyword arg first, then followed by required arg.
    return x + y


print(g(5))  # Client call the func 'g()' with required arg 'y' of value 5, whereas the keyword arg 'x=' is optional.

print(g(7, x=3))  # If need to parse in the keyword arg, must specify it's name.
# Therefore required arg are not given a name, they are determined by their position.
