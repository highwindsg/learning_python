#!/usr/bin/env python3

"""
Write a program that asks the user for the number of sides, the length of the side, 
the color, and the fill color of a regular polygon. The program should draw the 
polygon and then fill it in.
"""

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

num_sides = int(input("Enter the number of sides of the polygon: "))
length_sides = float(input("Enter the length of the side(cm): "))
colorname = input("Line color of polygon? ")
fcolor = input("Color fill-in of polygon? ")

alex.color(colorname)
alex.fillcolor(fcolor)
alex.begin_fill()

for i in range(int(num_sides)):
    alex.forward(float(length_sides))
    alex.left(int(360 / num_sides))

alex.end_fill()
wn.exitonclick()
