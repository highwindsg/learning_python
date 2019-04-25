#!/usr/bin/env python3

# Below program shows how to display a fraction eg (3 / 5).

class Fraction:     # Create a class named Fraction.

    # Define a init start function with params self, top
    # and bottom.
    def __init__(self, top, bottom):
        # top is the numerator of a fraction.
        # From self, set the numerator attrib and assign to
        # var obj 'top'.
        self.numerator = top
        # bottom is the denominator of a fraction.
        # From self, set the denominator attrib and assign to
        # var obj 'bottom'.
        self.denominator = bottom

    # Define a show function method with param self.
    def show(self):
        # Print out the value param top (the numerator) and
        # bottom (the denominator).
        print(self.numerator, "/", self.denominator)

# Client call the var 'myf' is set to the class Fraction
# with params 3 and 5.
myf = Fraction(3, 5)

# The output by calling the print function on 'myf' var
# will show the object stored in memory only.
print(myf)

# Using the show method created in the class to print out
# the params of numerator and denominator as a fraction.
myf.show()

