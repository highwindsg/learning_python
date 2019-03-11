#!/usr/bin/env python3

# Do not run this program. For illustration only. Errors are expected.

# Drawing shapes
# w/o polymorphism
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Square":
        a_shape.draw_square()
    if type(a_shape) == "Circle":
        a_shape.draw_circle()

# Drawing shapes
# with polymorphism
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    a_shape.draw()

""" If you wanted to add a new shape to the shapes list without polymorphism,
you would have to modify the code in the for-loop to test 'a_share' type and call
its draw method. With a uniform, polymorphism interface, you can add as many
shape classes to the 'shapes' list in the future as you want, and the shape will
be able to draw itself without any additional code."""

