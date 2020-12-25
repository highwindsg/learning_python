#!/usr/bin/env python3

"""
Use for loops to make a turtle draw these regular polygons
(regular means all sides the same lengths, all angles the same):

1. An equilateral triangle
2. A square
3. A hexagon (six sides)
4. An octagon (eight sides)
"""

import turtle


wn = turtle.Screen()
bob = turtle.Turtle()

# An octagon (eight sides)
for _ in range(8):
    bob.forward(60)
    bob.left(45)


# A hexagon (six sides)
for _ in range(6):
    bob.color("green")
    bob.forward(90)
    bob.left(300)


# A square
for _ in range(4):
    bob.color("blue")
    bob.right(90)
    bob.forward(90)


# An equilaterial triangle
for _ in range(3):
    bob.color("red")
    bob.forward(100)
    # the angle of each vertice of a regular polygon
    # is 360 divided by the number of sides.
    bob.left(360/3)


# A pentagon
for _ in range(5):
    bob.color("orange")
    bob.forward(100)
    bob.left(360/5)


wn.exitonclick()
