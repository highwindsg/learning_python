#!/usr/bin/env python3

def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """

    theSum = 0  # Accumulator to keep track of the sum so far.
    aNumber = 1 # Another accumulator to keep track of where we are.
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))
print(sumTo(1000))
print("")
