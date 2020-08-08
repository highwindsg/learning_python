#!/usr/bin/env python3

import turtle   # Importing the turtle module.

# Define a func named 'drawSquare' with params 't' and 'sz'.
def drawSquare(t, sz):
    """Make turtle t draw a square with side sz."""

    for i in range(4):  # to run 4 times.
        t.forward(sz)   # to move forward.
        t.left(90)  # to turn 90 degrees left.


# Set up the window and parse all the windows attributes and assign
# to var 'wn'.
wn = turtle.Screen()
# Call the windows .bgcolor method and assign the 'lightgreen' color.
wn.bgcolor("lightgreen")

alex = turtle.Turtle()  # Create var 'alex', so 'alex' is a turtle.
drawSquare(alex, 50)    # Func call to draw the square passing the actual
                        # turtle and the actual side size in pixels.
wn.exitonclick()    # Close the windows once clicked on it.
