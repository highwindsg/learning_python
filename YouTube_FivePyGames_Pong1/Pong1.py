#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=XGf2GcyHPhc&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=158&t=126s
Simple Pong game in Python 3 for beginners.
By @TokyoEdTech
Part 1: Getting started
"""

import turtle
from turtle import *

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)    # The turtle.tracer() method stops the game window from updating and therefore allow manual updating.


# Main game loop
while True:
    wn.update()     # Every time the while loop runs, it updates the game.

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)     # Want the paddle A to go to coordinates (X, Y) location.

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)     # Want the paddle B to go to coordinates (X, Y) location.

# Ball
