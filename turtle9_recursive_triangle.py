#!/usr/bin/env python3

# To try drawing a spiral triangle bigger and bigger.
from turtle import *

t = Turtle()
myWin = t.getscreen()

def triangle(lineLen, t):
    if lineLen > 5:
        t.forward(lineLen)
        t.left(120)
        triangle(lineLen +5, t)
        t.left(120)
        t.forward(lineLen)
        t.left(120)

