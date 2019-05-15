#!/usr/bin/env python3

import random
import turtle

def tree(size, myTurtle):   # Create a func tree with params size and myTurtle).
    myTurtle.pensize(size / 10) # From myTurtle use the .pensize method and
                                # parse in the size params).

    if size < random.randint(1, 2) * 20:    # If the size is less than 1 or 2
        myTurtle.color("green")             # multiply by 20, then draw in green.
    else:
        myTurtle.color("brown")     # If not, then draw in brown.

    if size > 5:
        myTurtle.forward(size)
        myTurtle.left(25)
        tree(size - random.randint(10, 20), myTurtle)
        myTurtle.right(50)
        tree(size - random.randint(10, 20), myTurtle)
        myTurtle.left(25)
        myTurtle.penup()
        myTurtle.backward(size)
        myTurtle.pendown()


window = turtle.Screen()    # Set var window with the turtle module using the
                            # screen() func.
window.bgcolor("black")     # From the window var obj, use the .bgcolor with
                            # param black color.

myTurtle = turtle.Turtle()  # Set var myTurtle with the turtle module using the
                            # Turtle() func.
myTurtle.color("brown", "blue") # From myTurtle, use the .color method with
                                # params brown and blue color.
myTurtle.left(90)   # From myTurtle, turn left by 90 degrees.
myTurtle.speed(0)   # From myTurtle, use the .speed method with param 0.
myTurtle.penup()    # Stops turtle from drawing.
myTurtle.setpos(0, -250)    # Set the tutle position at a location.
myTurtle.pendown()  # Pull the pen down and drawing when moving.

# Client call the tree() func with params 120 and myTurtle var.
tree(120, myTurtle)

# Click on the window to close when drawing is completed.
window.exitonclick()

