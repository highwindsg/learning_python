#!/usr/bin/env python3

from functools import reduce

# Multiply all numbers in a list.

# Using the reduce() func method.
data = [2, 3, 4, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(
    reduce(multiplier, data)
)

# Using just a for loop method.
product = 1
for x in data:
    product = product * x

print(product)

""" Therefore it is better to use loop instead of reduce, as loop seems more direct
and more easily understood. """
