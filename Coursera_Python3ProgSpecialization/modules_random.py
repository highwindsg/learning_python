#!/usr/bin/env python3

import random

prob = random.random()
print(prob)
print("")

diceThrow = random.randrange(1, 20)  # return an int, one of 1-19.
print(diceThrow)
print("")

diceThrowAgain = random.randrange(10)   # if you omit the first param (eg. 1, 10) then it is
# assumed to be 0, and will give you numbers 0-9.
print(diceThrowAgain)
print("")
