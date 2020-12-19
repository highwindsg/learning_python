#!/usr/bin/env python3

import turtle


wn = turtle.Screen()
june = turtle.Turtle()

for _ in range(8):
    june.color("green", "yellow")
    june.forward(50)
    june.right(90)


wn.exitonclick()
