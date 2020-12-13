#!/usr/bin/env python3

import turtle
wn = turtle.Screen()

alan = turtle.Turtle()

distance = 50
for _ in range(10):
    alan.forward(distance)
    alan.right(90)
    distance = distance + 10

