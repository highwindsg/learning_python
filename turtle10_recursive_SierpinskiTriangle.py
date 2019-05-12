#!/usr/bin/env python3

from turtle import *

# Create a func named drawTriangle() with three params of points, color and
# the myTurtle.
def drawTriangle(points, color, myTurtle):  # To draw the outer big triangle.
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()       # The func draws a filled triangle using the
    myTurtle.goto(points[1])    # begin_fill and end_fill methods at each
    myTurtle.goto(points[2])    # degree so that the triangle is drawn in a
    myTurtle.goto(points[0])    # different color.
    myTurtle.end_fill()

# sierpinski() func relies heavily on the getMid() func. getMid() takes
# two endpoints arg and returns the point at halfway between them by dividing
# by 2.
def getMid(p1, p2):
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 )

# Create a func named sierpinski() with three params of points, degree and
# myTurtle.
def sierpinski(points, degree, myTurtle):   # To draw the outer most triangle.
    # Set var colormap to a list of different colors not limited by how many.
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        # The first recursive call.
        sierpinski([points[0],  # To draw the first inner lower left most triangle.
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree -1, myTurtle)
        # The second recursive call.
        sierpinski([points[1],  # To draw the second inner top most triangle.
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree -1, myTurtle)
        # The third recursive call.
        sierpinski([points[2],  # To draw the third inner lower right most triangle.
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree -1, myTurtle)


myTurtle = Turtle()
myWin = myTurtle.getscreen()

# Setting var myPoints with three index of starting locations.
myPoints = [(-500, -250), (0, 500), (500, -250)]

# Client call func sierpinski() to start drawing with params of defined myPoints;
# index 5 of violet color from var colormap; and the myTurtle function.
sierpinski(myPoints, 5, myTurtle)

# Click inside the window to close after drawing ends.
myWin.exitonclick()

