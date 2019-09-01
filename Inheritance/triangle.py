#!/usr/bin/env python3

from polygon import Polygon     # From the polygon.py file/module, import the Polygon superclass.
from shape import Shape

# A subclass can inherit multiple super class.
# Create a subclass named Triangle, that inherits from the Polygon() superclass and Shape() superclass.
class Triangle(Polygon, Shape):   
    def area(self):         # Define a func named area() with param self.
        return self.get_width() * self.get_height() / 2     # Calculate the area of triangle and return the answer
                                                            # to the area() func in class Rectangle().