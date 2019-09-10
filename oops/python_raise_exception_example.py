#!/usr/bin/env python3

# Python allows the programmer to use a keyword 'raise' to force a specific exception to occur.

# Creating a custom exception class.
class CoffeeTooHotException(Exception):     # The custom class inherits from the 'Exception' superclass.
    def __init__(self, msg):    # Define a init start func method with params 'self' and 'msg'(message).
        super().__init__(msg)   # Using the super() func, call the init method from the 'Exception' class,
                                # pass the 'msg' param to the constructor of the 'Exception' class in line 23.

class CoffeeTooColdException(Exception):    # The custom class inherits from the 'Exception' superclass.
    def __init__(self, msg):    # Define a init start func method with params 'self' and 'msg'(message).
        super().__init__(msg)   # Using the super() func, call the init method from the 'Exception' class,
                                # pass the 'msg' param to the constructor of the 'Exception' class in line 26.

class CoffeeCup:    # Create a class named 'CoffeeCup'.
    def __init__(self, temperature):        # Define the init start func with param 'self' and 'temperature'.
        self.__temperature = temperature    # From self, initialise the private attrib '__temperature' to 'temperature'.

    def drink_coffee(self):     # Define the func 'drink_coffee' with param 'self'.
        if self.__temperature > 85:     # From 'self', if the private attrib of '__temperature' > 85, print statemt.
            print("Coffee Too Hot ")
            # Raise the custom exception with param of the temperature being entered in client call from line 33.
            raise CoffeeTooHotException("Coffee Temperature: " + str(self.__temperature))
        elif self.__temperature < 65:   # From 'self', if the private attrib of '__temperature' < 65, print statemt.
            # Raise the custom exception with param of the temperature being entered in client call from line 33.
            print("Coffee Too Cold ")
            raise CoffeeTooColdException("Coffee Temperature: " + str(self.__temperature))
        else:                           # And if the temp is between 65 and 85, print statemt.
            print("Coffee Ok to Drink")


cup = CoffeeCup(99)     # Set var 'cup' to an instance of 'CoffeeCup' class with param 75.
cup.drink_coffee()      # Client call var 'cup' with the attribs of drink_coffee() func.
"""
So we can also explicitly raise an exception in line 10 and 13 as well.
"""