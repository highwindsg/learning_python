#!/usr/bin/env python3

class CoffeeCup:    # Create a class named 'CoffeeCup'.
    def __init__(self, temperature):        # Define the init start func with param 'self' and 'temperature'.
        self.__temperature = temperature    # From self, initialise the private attrib '__temperature' to 'temperature'.

    def drink_coffee(self):     # Define the func 'drink_coffee' with param 'self'.
        if self.__temperature > 85:     # From 'self', if the private attrib of '__temperature' > 85, print statemt.
            print("Coffee Too Hot ")
            raise Exception("Coffee too hot")
        elif self.__temperature < 65:   # From 'self', if the private attrib of '__temperature' < 65, print statemt.
            print("Coffee Too Cold ")
            raise Exception("Coffee too cold")
        else:                           # And if the temp is between 65 and 85, print statemt.
            print("Coffee Ok to Drink")


cup = CoffeeCup(16)     # Set var 'cup' to an instance of 'CoffeeCup' class with param 75.
cup.drink_coffee()      # Client call var 'cup' with the attribs of drink_coffee() func.
"""
So we can also explicitly raise an exception in line 10 and 13 as well.
"""