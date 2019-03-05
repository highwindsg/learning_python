#!/usr/bin/env python3

class Rectangle():  # Create a class named 'Rectangle()'.
    def __init__(self, w, l):   # Define a init start function method with params self, w and l.
        self.width = w  # From 'self', get the attribute 'width' and assign it to w.
        self.len = l    # From 'self', get the attribute 'len' and assign it to l.

    # Define a area function method with params self.
    def area(self):
        return self.width * self.len    # Return the area function with answer of width * len
                                        # from the params self.

    # Define a change_size function method with params self, w and l.
    def change_size(self, w, l):
        self.width = w  # From self, get the attribute 'width' and assign it to w.
        self.len = l    # From self, get the attribute 'len' and assign it to l.

rect = Rectangle(10, 20)    # Assign the var 'rect' with class 'Rectangle()' and params 10, 20.
print(rect.area())          # Print output of 'area()' function from var 'rect'.
rect.change_size(20, 40)    # From 'rect' var, the function method of 'change_size()' with 20, 40.
print(rect.area())          # Print output of 'area()' function from var 'rect'.

