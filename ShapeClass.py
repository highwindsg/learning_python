#!/usr/bin/env python3
"""
Create a class called Shape. Define a method in it called what_am_i that prints
"I am a shape" when called. Change your Square and Rectangle classes from the
previous challenges (eg. RectSqClass.py) to inherit from Shape, create Square
and Rectangle objects, and call the new method on both of them.
"""
class Shape():   # new Shape class that has-a method called what_am_i.
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):    # The Square class inherits from Shape class.
    def __init__(self, s):
        self.side = s

    def calc_perimeter(self):
        return self.side * 4


class Rectangle(Shape): # The Rectangle class inherits from Shape class.
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calc_perimeter(self):
        return self.width * 2 + self.length * 2


Square = Square(5)
print("The perimeter of square is", Square.calc_perimeter())
Rectangle = Rectangle(3, 6)
print("The perimeter of rectangle is", Rectangle.calc_perimeter())

Square.what_am_i()
Rectangle.what_am_i()

