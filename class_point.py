#!/usr/bin/env python3

class Point:            # Create a class named Point.
    # Creating different types of methods in the class Point.
    def move(self):     # Define a func method named move with param self.
        print("move")   # Print the word 'move' in the func move().

    def draw(self):     # Define a func method named draw with param self.
        print("draw")   # Print the word 'draw' in the func draw().


point1 = Point()        # Set var point1 to an instance of class Point.
point1.draw()           # From point1, get the attrib of draw, which is to
                        # print out the word 'draw'.
point1.x = 10           # Set point1 with an attrib of x to a value of 10.
point1.y = 20           # Set point1 with another attrib of y to a value of 20.
print(point1.x)         # Print out the value of x from point1.
print(point1.y)         # Print out the value of y from point1.

point2 = Point()        # Set var point2 to an instance of class Point.
point2.x = 1            # Set point2 with an attrib of x to a value of 1.
print(point2.x)         # Print out the value of x from point2.

