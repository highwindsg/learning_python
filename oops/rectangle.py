#!/usr/bin/env python3

class Rectangle:        # Create a class named 'Rectangle()'.
    pass                # Insert the pass statement here to denote that this is a empty class.

rect1 = Rectangle()     # 'rect1' obj is-a 'Rectangle()'.
rect2 = Rectangle()     # 'rect2' obj is-a 'Rectangle()'.

rect1.height = 20       # For 'rect1', set the 'height' attrib to 20.
rect2.height = 30       # For 'rect2', set the 'height' attrib to 30.

rect1.width = 40        # For 'rect1', set the 'width' attrib to 40.
rect2.width = 10        # For 'rect2', set the 'width' attrib to 10.


# Client call to calculate the area or 'rect1' and 'rect2' and print out.
print("Area of 'rect1': ", (rect1.height * rect1.width))
print("Area of 'rect2': ", (rect2.height * rect2.width))
