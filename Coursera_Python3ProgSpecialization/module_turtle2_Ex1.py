#!/usr/bin/env python3

"""
Modify the program file 'module_turtle.py' so that before it creates
the window, it prompts the user to enter the desired background color.
It should store the user’s responses in a variable, and modify the
color of the window according to the user’s wishes.
(Hint: you can find a list of permitted color names at
https://www.w3schools.com/colors/colors_names.asp. 
It includes some quite unusual ones, like “PeachPuff” and “HotPink”.)

Do similar changes to allow the user, at runtime, to set alex’s color.

Do the same for the width of alex's pen. Hint: your dialog with the user
will return a string, but alex’s pensize method expects its argument to
be an int. That means you need to convert the string to an int before
you pass it to pensize.

Then finally run the program which draws a rectangle.
"""

import turtle


wn = turtle.Screen()
bgcolor = input("Please enter the background color: ")
wn.bgcolor(bgcolor)

alex = turtle.Turtle()
color = input("Please enter the color of turtle alex: ")
alex.color(color)

width = int(input("Please enter the thickness of the line (>= 0 interger number): "))
alex.pensize(width)

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
