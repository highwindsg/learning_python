#!/usr/bin/env python3

# 'recs' is a class var in the Rectangle() class, and is set to an empty list.
class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.width = w  # From self, get the width attribute, and set it to w.
        self.len = l    # From self, get the len attribute, and set it to l.
        # From self, get the attribute from class var of recs, and use the append
        # method to add in the params.
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))

r1 = Rectangle(10, 24)  # Set r1 to an instance of class Rectangle with params.
r2 = Rectangle(20, 40)  # Set r2 to an instance of class Rectangle with params.
r3 = Rectangle(100, 200)    # Set r3 to an instance of class Rectangle with params.

print(Rectangle.recs)   # Print the output of recs from the Rectangle class.
"""
You created the class variable 'recs' outside of the __init__ method because
Python only calls the __init__ method when you create an object, and you want to
be able to access the class variable using the class object (which does not call
the __init__ method). eg. line 12.
"""
