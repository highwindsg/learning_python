#!/usr/bin/env python3

""" Use a for statement to print 10 random numbers. """

import random

rnums = []

for i in range(0, 10):
    i = random.randint(0, 10)
    rnums.append(i)

print(rnums)
print("")


# Alternatively:

howmany = 10

for counter in range(howmany):
    rannumber = random.random()
    print(rannumber)

print("")



""" Repeat the above exercise but this time print 10 random numbers
between 25 and 35. """

howmanyagain = 10

for counter in range(howmanyagain):
    rannumber = random.randrange(25, 36)
    print(rannumber)

print("")
