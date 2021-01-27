#!/usr/bin/env python3

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

# This for loop will loop through four times to draw a square.
for i in [0, 1, 2, 3]:
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
