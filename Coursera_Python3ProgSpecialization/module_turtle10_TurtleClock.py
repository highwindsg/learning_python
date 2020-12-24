#!/usr/bin/env python3

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.shape("turtle")
alex.pensize(3)
alex.color("blue")

for i in range(12):
    alex.up()
    alex.forward(80)
    alex.down()
    alex.forward(10)
    alex.up()
    alex.forward(20)
    alex.stamp()
    alex.left(180)
    alex.forward(110)
    alex.right(30)


wn.exitonclick()
print(type(alex))
