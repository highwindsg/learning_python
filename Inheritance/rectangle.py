#!/usr/bin/env python3

from polygon import Polygon     # From the polygon.py file/module, import the Polygon superclass.
from shape import Shape         # From the shape.py file/module, import the Shape superclass.

# A subclass can inherit multiple superclass.
# Create a subclass named Rectangle, that inherits from the Polygon() superclass and the Shape() superclass.
class Rectangle(Polygon, Shape):
    def area(self):         # Define a func named area() with param self.
        return self.get_width() * self.get_height()     # Calculate the area of rectangle and return the answer
                                                        # to the area() func in class Rectangle().