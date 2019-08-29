#!/usr/bin/env python3

"""
To declare a private member var or private attrib, use a double underscore in front of the var name.
eg. 'self.__varName', so '.__varName' is a private member var of param 'self'.
This is to prevent the value of the private var to be wrongly re-assigned with another value later
on in the same program.
Therefore a private member var is private to the class and cannot be used or called outside of the class.
A private member var can also be used in different functions that is within the same class.
"""

class Rectangle:        # Create a class named 'Rectangle()'.
    def __init__(self, height, width):  # Define a init start func with params self, height and width).
        self.__height = height      # From self, set the private attrib of .__height and assign to height.
        self.__width = width        # From self, set the private attrib of .__width and assign to width.
        
    def set_height(self, height):   # Define a func named set_height with params self and height.
        self.__height = height      # From self, set the private attrib of .__height and assign to height.
    def get_height(self, height):   # Define a func named get_height with params self and height.
        return self.__height        # Return the value of the private var of self.__height to the get_height() func.
    
    def set_width(self, width):     # Define a func named set_width with params self and width.
        self.__width = width        # From self, set the private attrib of .__width and assign to width.
    def get_width(self, width):     # Define a func named get_width with params self and width.
        return self.__width         # Return the value of the private var of self.__width to the get_width() func.
    
    def area(self):                 # Define a func named area with param self.
        return self.__height * self.__width     # Calculate the area of the rectangle by multiplying
                                                # the private values of self.__height and self.__width,
                                                # return the value to the area() func.

#    pass                # Insert the pass statement here to denote that this is a empty class.

rect1 = Rectangle(20, 60)     # 'rect1' obj is-a 'Rectangle()' with params 20 and 60.
rect2 = Rectangle(50, 40)     # 'rect2' obj is-a 'Rectangle()' with params 50 and 40.

# rect1.height = 20       # For 'rect1', set the 'height' attrib to 20.
# rect2.height = 30       # For 'rect2', set the 'height' attrib to 30.
#
# rect1.width = 40        # For 'rect1', set the 'width' attrib to 40.
# rect2.width = 10        # For 'rect2', set the 'width' attrib to 10.

# Client call to calculate the area of 'rect1' and 'rect2' and print out.
print("Area of 'rect1': ", rect1.area())
print("Area of 'rect2': ", rect2.area())
