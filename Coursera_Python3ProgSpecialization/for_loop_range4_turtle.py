#!/usr/bin/env python3

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
jose = turtle.Turtle()
jose.shape("turtle")
jose.fillcolor("green") # Changes the color of the turtle.
jose.speed(1)
jose.penup()    # No line will be drawn.

# For loop below will make turtle footprints, without lines drawn.
for _ in range(10):
    jose.dot()  # Leaves a dot at the current position.
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)   # Move backwards.
    jose.right(36)  # Turn right by 36 degrees.

wn.exitonclick()


"""
Summary of Turtle Methods

Method      Parameters      Description

Turtle      None            Creates and returns a new turtle object
forward     distance        Moves the turtle forward
backward    distance        Moves the turle backward
right       degree angle    Turns the turtle clockwise
left        angle           Turns the turtle counter clockwise
up          None            Picks up the turtles tail from drawing line
down        None            Puts down the turtles tail to draw line
color       color name      Changes the color of the turtle’s tail
fillcolor   color name      Changes the color of the turtle will use to fill a polygon
pensize     line width      Sets the thickness of the drawing line.
heading     None            Returns the current heading
position    None            Returns the current position
goto        x,y             Move the turtle to position x,y
begin_fill  None            Remember the starting point for a filled polygon
end_fill    None            Close the polygon and fill with the current fill color
dot         None            Leave a dot at the current position
stamp       None            Leaves an impression of a turtle shape at the current location
shape       shapename       Should be ‘arrow’, ‘triangle’, ‘classic’, ‘turtle’, ‘circle’, or ‘square’
speed       integer         0 = no animation, fastest; 1 = slowest; 10 = very fast

https://fopp.umsi.education/books/published/fopp/PythonTurtle/SummaryOfTurtleMethods.html
"""
