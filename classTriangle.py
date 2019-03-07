#!/usr/bin/env python3

# Create a Triangle class with a method called area that calculates and
# returns its area.
class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

# Create a function method called 'area' that calculates the area
# of a triangle and returns the answer to the method 'area'.
    def area(self):
        areaTriangle = self.base * self.height / 2
        return areaTriangle

# Assign the var my_Triangle with the Triangle() class and params of 5 and 10.
my_Triangle = Triangle(5, 10)   # Triangle() class with base 5 and height 10.
print(my_Triangle.area())       # Print out the area of var my_Triangle with
                                # the area() method.

