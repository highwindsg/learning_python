#!/usr/bin/env python3

""" Encapsulation refers to two concepts. The first is that in OOP, objects group variables
(state) and methods (for altering state or doing calculations that use state) in a single
unit - the object:
"""
class Rectangle():  # Create a class named 'Rectangle()'.
    def __init__(self, w, l):   # Define a init start function method with params self, w and l.
        self.width = w  # From 'self', get the attribute 'width' and assign it to w.
        self.len = l    # From 'self', get the attribute 'len' and assign it to l.

    # Define a area function method with params self.
    def area(self):
        return self.width * self.len    # Return the area function with answer of width * len
                                        # from the params self.

rect = Rectangle(10, 20)    # Assign the var 'rect' with class 'Rectangle()' and params 10, 20.
print(rect.area())          # Print output of 'area()' function from var 'rect'.

""" In this case, the instance variables 'len' and 'width' hold the object's state. The object's
state is grouped in the same unit (the object) as the method 'area'. The method uses the
object's state to return the rectangle's area.
"""
