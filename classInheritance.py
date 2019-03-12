#!/usr/bin/env python3

""" You can define a child that inherits from a parent class by passing the name of the
parent class as a parameter to the child class when you create it. The following creates
a 'Square' class that inherits from the 'Shape' class:
"""

class Shape():  # Create a class named Shape().
    def __init__(self, w, l):   # Define a init start function with params self, w and l.
        self.width = w  # From self, get the width attribute and assign to w.
        self.len = l    # From self, get the len attribute and assign to l.

    def print_size(self):   # Create a 'print_size' function method with param self.
        print("""{} by {}""".format(self.width, self.len))  # Print the width and len in
                                                            # .format from the instance var
                                                            # from class Shape().

""" Because you passed the 'Shape' class to the 'Square' class as a param; the 'Square'
class inherits the 'Shape' class's var and methods.
And because of inheritance, you can create a 'Square' object, pass it a width and length,
and call the method 'print_size' on it without writing any code (aside from 'pass') in
the 'Square' class.
"""
class Square(Shape):    # Create a class 'Square' and pass it the 'Shape' class as a param.
    pass

a_square = Square(20, 20)   # Create a var 'a_square' and call the 'Square' class on it
                            # with params 20, 20.
a_square.print_size()
""" From 'a_square', call the 'print_size' function method. You can because var 'a_square'
has been assigned with the child 'Square' class that inherits the parent 'Shape' class. """
