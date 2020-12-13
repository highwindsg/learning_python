#!/usr/bin/env python3

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
jose = turtle.Turtle()
jose.shape("turtle")
jose.speed(1)
jose.penup()    # No line will be drawn.

# For loop below will make turtle footprints, without lines drawn.
for _ in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)   # Move backwards.
    jose.right(36)  # Turn right by 36 degrees.

wn.exitonclick()
