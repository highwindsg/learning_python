#!/bin/env python3

from turtle import *


color("red", "pink")    # red outline, pink fill-in color.
begin_fill()

left(50)
forward(100)

circle(40, 180) # radius 40 and 180 for semi circle.
left(260)
circle(40, 180) # radius 40 and 180 for semi circle.
forward(100)

end_fill()
done()
