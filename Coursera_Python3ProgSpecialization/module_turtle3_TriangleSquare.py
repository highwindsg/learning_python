#!/usr/bin/env python3

import turtle


wn = turtle.Screen()    # Set up the window and its attribs.
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # Create tess and set his pen width.
tess.pensize(5)

alex = turtle.Turtle()  # Create alex.
alex.color("hotpink")   # Set his color.

tess.forward(80)    # Let tess draw an equilateral triangle.
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)  # Complete the triangle.

tess.right(180) # Turn tess around.
tess.forward(80)    # move her away from the origin so we can see alex.

alex.forward(50)    # Make alex draw a square.
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
