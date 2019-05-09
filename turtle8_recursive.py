#!/usr/bin/env python3

from turtle import *

t = Turtle()    # Create a turtle 't' with the Turtle() func.
myWin = t.getscreen()   # Create a window fot 't' to draw in
                        # using the .getscreen() method.

def tree(branchLen, t): # Create a tree func with branch length,
                        # and the 't' turtle params.
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen -15, t)
        t.left(40)
        tree(branchLen -10, t)
        t.right(20)
        t.backward(branchLen)

t.color("green")    # To set the color of the turtle line.
t.left(90)
t.up
t.backward(300)
t.down()
tree(110, t)    # Call the tree func with params branch length
                # of 110 and the 't' turtle.)
myWin.exitonclick() # When the program finishes, click inside
                    # the window to close.

