#!/usr/bin/env python3

import random

class Dice:     # Create class named Dice.
    def roll(self): # Define a new func method named roll.
        first = random.randint(1, 6)    # From random, get the randint method,
                                        # pass in the values of 1 to 6, simulating
                                        # the actual dice numbers. Then assign it
                                        # to the var first.
        second = random.randint(1, 6)   # Same comment as above.
        return first, second    # Return the values of 'first' and 'second' back
                                # to the roll() func method.


dice = Dice()   # Set var dice to an instance of class Dice().
print(dice.roll())  # From var dice, get the roll func method and print out the
                    # output.

