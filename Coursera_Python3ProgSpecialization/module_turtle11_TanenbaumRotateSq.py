#!/usr/bin/env python3

import turtle

wn = turtle.Screen()

tanenbaum = turtle.Turtle()
tanenbaum.hideturtle()  # Do not show the shape of the turtle, hide it.
tanenbaum.speed(20)

for i in range(350):
    tanenbaum.forward(i)
    tanenbaum.right(98)


wn.exitonclick()
