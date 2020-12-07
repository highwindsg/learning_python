#!/usr/bin/env python3

import turtle   # allows us to use the turtles library.


wn = turtle.Screen()    # creates a graphics window.
wn.bgcolor("lightgreen")    # set the window background color.

alex = turtle.Turtle()  # creates a turtle object named var alex.
alex.color("red")   # invoking the color attrib from the turtle module.
# For a list of permitted color names at
# https://www.w3schools.com/colors/colors_names.asp.
alex.pensize(6) # set the width thickness of the pen.

# To draw a rectangle.
alex.forward(150)   # tell alex to move forward by 150 units.
alex.left(90)   # turn on its left by 90 degrees.
alex.forward(75)    # complete the second side of a rectangle.
alex.left(90)   # turn on its left by 90 degrees.
alex.forward(150)   # complete the third side of a rectangle..
alex.left(90)   # turn on its left by 90 degrees.
alex.forward(75)    # complete the last side of a rectangle.

# turtle.Screen().exitonclick()   # close the window once clicked inside.
# Alternatively,
wn.exitonclick()    # close the window once clicked inside.
