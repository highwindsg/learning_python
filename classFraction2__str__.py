#!/usr/bin/env python3

# Below program shows how to display a fraction eg (3 / 5)
# by using the __str__ python string method.

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

    # Define a string function method with param self.
    def __str__(self):
        # Print out the value param top (the numerator) and
        # bottom (the denominator).
        return str(self.numerator)+"/"+str(self.denominator)

# Client call the var 'myf' is set to the class Fraction
# with params 3 and 5.
myf = Fraction(3, 5)

# The output by calling the print function on 'myf' var
# now will show the actual fraction.
print(myf)

# The output below will print out that you ate 3/5 of the pizza.
print("I ate", myf, "of the pizza.")

# The output below will print out just 3/5 as the print
# function calls the var 'myf' and get the attrib of the
# __str__ string method.
print(myf.__str__())

