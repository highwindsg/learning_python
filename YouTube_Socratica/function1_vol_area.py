#!/usr/bin/env python3

import math

print(dir(math))  # To see what classes are available from the math module.


def volume(r):  # Create a func named volume() with a param argument of 'r'.
    """" Returns the volume of a sphere with radius r.
    Formula: 4 divide by 3, multiply by pi, multiply by radius to the power of 3. """
    v = (4.0 / 3.0) * math.pi * r ** 3
    return v  # Return the value of 'r' to the volume.


# Calculate the volume of a sphere with radius of 2 and print out the answer.
print(volume(2))

# Can use the help() function to read about the doc string of the func.
help(volume)

print("")


def triangle_area(b, h):
    """ To calculate the area of a triangle.
    Formula: half base multiply by height.
    Returns the area of a triangle with base b and height h. """
    return 0.5 * b * h


print(triangle_area(3, 6))  # Area of the triangle with base 3 and height 6.
