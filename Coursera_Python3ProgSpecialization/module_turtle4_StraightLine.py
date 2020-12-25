#!/usr/bin/env python3

import turtle

wn = turtle.Screen()

alex = turtle.Turtle()

alex.shape("turtle")
""" Every turtle can have its own shape.
The ones available “out of the box” are arrow, blank, circle, classic,
square, triangle, turtle. """

alex.speed(1)
""" Every turtle can have its own speed. (1 - 10, slowest to fastest, 0 is
same as 10).
And if a decimal is set, eg. 1.0 of 0.9 then the speed param will only
take into account the whole number, and disregard whatever comes after the
decimal place. """

alex.up()   # Same as .penup(), will not draw line.
alex.stamp()    # Leaving a turtle foorptint, even when the pen is up.
alex.forward(100)
alex.down() # Same as .pendown(), will draw line.
alex.stamp()    # Leaving a turtle footprint.
alex.forward(80)
alex.up()
alex.forward(50)


wn.exitonclick()
