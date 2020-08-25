#!/usr/bin/env python3

"""
Program a turtle to wander around randomly inside the screen.
When we run the program we want the turtle and program to behave
in the following way:

The turtle begins in the center of the screen.
Flip a coin. If it’s heads then turn to the left 90 degrees.
If it’s tails then turn to the right 90 degrees.
Take 50 steps forward.
If the turtle has moved outside the screen then stop, otherwise
go back to step 2 and repeat.
"""

import random
import turtle


def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = - w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn


t = turtle.Turtle()
wn = turtle.Screen()

t.shape("turtle")
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:   # heads
        t.left(90)
    else:           # tails
        t.right(90)

    t.forward(50)

wn.exitonclick()
print("")
