#!/usr/bin/env python3

"""
The main.py file will act as the main project file and import the required module from the
other triangle.py and rectangle.py file, that contains the respective object class.
"""

from rectangle import Rectangle     # From the rectangle.py file/module, import the Rectangle class.
from triangle import Triangle       # From the triangle.py file/module, import the Triangle class.

rect = Rectangle()          # rect is-a Rectangle() class.
tri = Triangle()            # tri is-a Triangle() class.
rect.set_values(50, 40)     # From rect var obj, set the attrib of .set_values with param 50 and 40)
tri.set_values(50, 40)      # From tri var obj, set the attrib of .set_values with param 50 and 40)

"""
Because the triangle.py and rectangle.py inherited the super class of share.py,
the .set_color() and .get_color() funcs can also be called here.
"""

rect.set_color("red")
tri.set_color("blue")

# Print out the area of the rectangle and triangle and format as strings.
print("Area of rectangle is", str(rect.area()) + ".")
print("Area of triangle is", str(tri.area()) + ".")

# Because there are no integer output, so no need to format as strings.
print("Color of rectangle is", rect.get_color() + ".")
print("Color of triangle is", tri.get_color() + ".")
