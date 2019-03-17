#!/usr/bin/env python3
"""
Create Rectangle and Square classes with a method called calculate_perimeter
that calculates the perimeter of the shapes they represent. Create
Rectangle and Square objects and call the method on both of them.
"""
class Rectangle():  # Create a class named Rectangle().
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calc_perimeter(self):   # Create a method named calc_perimeter that
                                # calculates the perimeter of the rectangle.
        return self.width + self.width + self.length + self.length


class Square(): # Create a class named Square().
    def __init__(self, s):
        self.side = s

    def calc_perimeter(self):   # Create a method named calc_perimeter that
                                # calculates the perimeter of the square.
        return self.side * 4


Rectangle = Rectangle(2, 5) # Create a Rectangle object and assign it with the
                            # Rectangle() class with param 2 and 5 respectively.
print(Rectangle.calc_perimeter())   # Print the output of Rectangle object by
                                    # calling the calc_perimeter method on it.

Square = Square(3)  # Create a Square object and assign it with the Square()
                    # class with param 3.
print(Square.calc_perimeter())  # Print the output of Square object by calling
                                # the calc_perimeter method on it.
