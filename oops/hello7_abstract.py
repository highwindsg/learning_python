#!/usr/bin/env python3

# Python abstract classes.

# Import the 'Abstract Base Classes' module and 'abstractmethod' module from library 'abc'.
from abc import ABC, abstractmethod

# Create a 'Shape' class that is a superclass that inherits from the ABC module.
class Shape(ABC):
    @abstractmethod     # Add a declarator.
    def area(self):     # Define a func named 'area' with param 'self'.
        pass

    @abstractmethod     # Add a declarator.
    def perimeter(self):    # Define a func named 'perimeter' with param 'self'.
        pass

# Create a subclass named 'Square' with param of the superclass 'Shape'.
# Therefore 'Square' class is inheriting from the 'Shape' superclass as well as inheriting
# the abstract methods.
class Square(Shape):
    def __init__(self, side):   # Define a init start with param 'self' and 'side'.
        self.__side = side      # From 'self', set the private attrib of '__side' is to 'side'.

    def area(self):     # Define a 'area' func with param 'self' that already inherits the abstract method.
        return self.__side * self.__side    # Calc the area and return the ans to the func.

    def perimeter(self):    # Define a 'perimeter' func with param 'self' that already inherits the abstract method.
        return 4 * self.__side      # Calc the perimeter and return the ans to the func.


square = Square(5)      # var 'square' is-a Square class with param value of 5.
print(square.area())    # Client call to print the area of square.
print(square.perimeter())   # Client call to print the perimeter of square.
