#!/usr/bin/env python3

"""
When a child class inherits a method from a parent class, you can override
it by defining a new method with the same name as the inherited method.
A child class's ability to change the implementation of a method from its
parent class is called 'method overriding'.
"""

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))


class Square(Shape):    # A child class named 'Square' that has the
                        # parent class 'Shape' passed in as a param.
    def area(self):
        return self.width * self.len

    def print_size(self):   # A new 'print_size' method is defined, it
                            # overrides the parent method of the same
                            # name and prints a new message.
        print("I am {} by {}".format(self.width, self.len))


a_square = Square(20, 20)
a_square.print_size()

