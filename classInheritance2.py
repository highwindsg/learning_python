#!/usr/bin/env python3

""" A child class is like any other class; you can define methods and var in it without
affecting the parent class: """

class Shape():  # Create a class named 'Shape()'.
    def __init__(self, w, l):   # Create a init start function with params self, w and l.
        self.width = w  # From self, get the attribute width and assign to w.
        self.len = l    # From self, get the atribute len and assign to l.

    def print_size(self):   # Create a function method named 'print_size' with param self.
        print("""{} by {}""".format(self.width, self.len))


class Square(Shape):    # Create a class named 'Square' that inherits the parent 'Shape'
                        # class as a param.
    def area(self): # Define a area function method named 'area' with param self.
        return self.width * self.len    # Calculate the area by multiplying width and len,
                                        # and return the answer to 'area' method.

a_square = Square(20, 20)   # Create a var 'a_square', assign it with class 'Square' and
                            # params of 20, 20.
print(a_square.area())  # Then print the area of 'a_square' by calling the function method
                        # area(), which belongs to the class 'Square'.

