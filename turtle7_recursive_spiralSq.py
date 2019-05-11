#!/usr/bin/env python3

from turtle import *

# We create a 'myTurtle' with the 'Turtle()' function.
myTurtle = Turtle()

# We create a window for 'myTurtle' to draw in using the
# .getscreen() method.
myWin = myTurtle.getscreen()

def drawSpiral(myTurtle, lineLen):
    # So if the length of the line is longer then zero
    # we instruct the turtle to go forward by len units
    # and then turn right 90 degrees.
    if lineLen > 0:
        myTurtle.forward(lineLen)   # myTurtle uses .forward method
                                    # with the length of line param.
        myTurtle.right(90)  # myTurtle turn right 90 degrees.
        # The recursive step is when we call drawSpiral
        # again with a reduced length.
        drawSpiral(myTurtle, lineLen -5)


# So by giving a param lineLen of 100, myTurtle will draw
# from 100 and reducing every time by -5, until lineLen is 0.
drawSpiral(myTurtle, 100)

# The func below is a method of the window that puts the
# turtle into a wait mode until you click inside the
# window, after which the program cleans up and exits.
myWin.exitonclick()

