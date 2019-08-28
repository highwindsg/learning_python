#!/usr/bin/env python3

class Rectangle:        # Create a class named 'Rectangle()'.
    def __init__(self, height, width):  # Define a init start func with param self, height and width).
        self.height = height            # From self, get the attrib of height and set it to height.
        self.width = width              # From self, get the attrib of width and set it to width.

#    pass                # Insert the pass statement here to denote that this is a empty class.

rect1 = Rectangle(20, 60)     # 'rect1' obj is-a 'Rectangle()' with params 20 and 60.
rect2 = Rectangle(50, 40)     # 'rect2' obj is-a 'Rectangle()' with params 50 and 40.

# rect1.height = 20       # For 'rect1', set the 'height' attrib to 20.
# rect2.height = 30       # For 'rect2', set the 'height' attrib to 30.
#
# rect1.width = 40        # For 'rect1', set the 'width' attrib to 40.
# rect2.width = 10        # For 'rect2', set the 'width' attrib to 10.
"""
Since the attrib of 'height' and 'width' are set in the init start func from param 'self' in line 4 to line 6,
therefore it is not necessary to explicitly assign the '.height' and '.width' in line 13 to line 17 again.
"""

# Client call to calculate the area of 'rect1' and 'rect2' and print out.
print("Area of 'rect1': ", (rect1.height * rect1.width))
print("Area of 'rect2': ", (rect2.height * rect2.width))
