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
        return self.width * 2 + self.length * 2


class Square(): # Create a class named Square().
    def __init__(self, s):
        self.side = s

    def calc_perimeter(self):   # Create a method named calc_perimeter that
                                # calculates the perimeter of the square.
        return self.side * 4

    """
    Define a method in your Square class called change_size that allows you
    to pass in a number that increases or decreases (if the number is negative)
    each side of a Square object by that number.
    """
    def change_size(self, new_size):    # Create a new method named change_size
                                        # with params self and new_size.
        self.side += new_size   # From self, get the side attribute and assign
                                # it incrementally with the new_size param.


# Create a Rectangle object and assign it with the Rectangle() class with
# param 2 and 5 respectively.
Rectangle = Rectangle(2, 5)
# Print the output of Rectangle object by calling the calc_perimeter method on it.
print("The perimeter of the rectangle is", Rectangle.calc_perimeter())

# Create a Square object and assign it with the Square() class with param 3.
Square = Square(3)
# Print the output of Square object by calling the calc_perimeter method on it.
print("The perimeter of the square is", Square.calc_perimeter())

# Create a New_Square object and calling the new change_size method on it.
Square.change_size(6)
# Print out only the new change_size's side from the Square object.
print("The side of the new square is", Square.side)

