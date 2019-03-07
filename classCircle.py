#!/usr/bin/env python3

import math

# Create a class named 'Circle' with a method called 'area' that calculates
# and returns its area.
class Circle():
    def __init__(self, r):  # Define a init start function with params self and r.
        self.radius = r     # From self get the attribute radius and assign to r.

    def area(self):     # Create a function method area with params self.
        areaCircle = math.pi * self.radius ** 2     # Area of a circle = pi*r^2
        return areaCircle

# Create a circle object, call 'area' on it, and print the result.
Circle = Circle(5)      # Parse 5 into the Circle class and assign to var obj Circle.
print(Circle.area())    # Print the area of the var obj Circle.

