#!/usr/bin/env python3

# To drawing a spiral triangle bigger and bigger indefinitely.

from turtle import *

t = Turtle()
myWin = t.getscreen()

t.color("red")

def triangle(lineLen, t):
    if lineLen > 5:
        t.forward(lineLen)
        t.left(120)
        triangle(lineLen +5, t)
        t.forward(lineLen)
        t.left(120)
        triangle(lineLen +5, t)
        t.forward(lineLen)
        t.left(120)
        triangle(lineLen +5, t)
        t.forward(lineLen)


triangle(100, t)
myWin.exitonclick()

