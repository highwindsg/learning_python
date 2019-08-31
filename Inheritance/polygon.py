#!/usr/bin/env python3

class Polygon:          # Create a superclass named Polygon.
    __width = None      # Set a private __width var to None.
    __height = None     # Set a private __height var to None.

    def set_values(self, width, height):    # Define a set_values() func with param self, width and height).
        self.__width = width        # From self, set the private var __width to width.
        self.__height = height      # From self, set the private var __height to height.
    
    # Because the private vars in the superclass cannot be used outside of its own class, we need to create
    # separate new public funcs or methods in the superclass to get the values of the private member vars.
    def get_width(self):        # Create a public get_width() func with param self.
        return self.__width     # Get the private value of __width from self and return it to the get_width() func.
    def get_height(self):       # Create a public get_height() func with param self.
        return self.__height    # Get the private value of __height from self and return it to the get_height() func.


class Rectangle(Polygon):   # Create a subclass named Rectangle, that inherits from the Polygon() superclass.
    def area(self):         # Define a func named area() with param self.
        return self.get_width() * self.get_height()     # Calculate the area of rectangle and return the answer
                                                        # to the area() func in class Rectangle().


class Triangle(Polygon):    # Create a subclass named Triangle, that inherits from the Polygon() superclass.
    def area(self):         # Define a func named area() with param self.
        return self.get_width() * self.get_height() / 2     # Calculate the area of triangle and return the answer
                                                            # to the area() func in class Rectangle().

"""
So when a subclass inherits from a superclass, the parameters and member vars (except for private vars) from the
superclass can then be used by the other subclass also.
"""

rect = Rectangle()          # rect is-a Rectangle() class.
tri = Triangle()            # tri is-a Triangle() class.
rect.set_values(50, 40)     # From rect var obj, set the attrib of .set_values with param 50 and 40)
tri.set_values(50, 40)      # From tri var obj, set the attrib of .set_values with param 50 and 40)

print(rect.area())
print(tri.area())
