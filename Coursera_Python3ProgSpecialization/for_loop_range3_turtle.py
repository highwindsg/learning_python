#!/usr/bin/env python3

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()   # Start with pen up.

# Therefore below for loop will only make footprints, and not draw lines.
for _ in range(30):
    tess.stamp()
    tess.forward(dist)
    tess.right(24)
    dist = dist + 2

wn.exitonclick()
