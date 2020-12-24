#!/usr/bin/env python3

"""
Try drawing the rest of the house. Each time you draw something
new on the screen, run the program to see if it execute in the
way that you expected!
"""

import turtle


wn = turtle.Screen()
bob = turtle.Turtle()

bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(50)

# Add your code below!
bob.left(90)
bob.forward(50)
bob.right(90)
bob.forward(30)
bob.left(135)
bob.forward(80)
bob.left(90)
bob.forward(80)
bob.left(135)
bob.forward(35)


wn.exitonclick()
