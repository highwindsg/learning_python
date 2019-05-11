#!/usr/bin/env python3

"""
Turtle graphics is a popular way for introducing programming to kids.
Reference to https://docs.python.org/3.6/library/turtle and
help("turtle") for more information.
Imagine a robotic turtle starting at (0, 0) in the x-y plane.
"""
from turtle import *

forward(200)

# The for loop makes a diameter 200 semicircle, curving down.
for i in range(100):
    forward(3.416)
    right(1.8)

forward(200)
bye()

