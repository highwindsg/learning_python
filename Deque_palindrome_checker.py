#!/usr/bin/env python3

"""
A palindrome is a string that reads the same no matter forward
or backward. eg. radar, toot and madam.
We construct an algorithm to input a string of characters and
check whether it is a palindrome.
"""

# From python data structure basic library,
# import the Deque module.
from pythonds.basic import Deque

# Define a func named palchecker() with a param 'astring'.
def palchecker(aString):
    chardeque = Deque() # Set var 'chardeque' to a instance
                        # of class Deque.

    # For the character in aString, use the Deque module
    # method of .addRear() to add in the character to the
    # left most.
    for ch in aString:
        chardeque.addRear(ch)

    # Set the var stillEqual to True so that the algorithm
    # can continue to run.
    stillEqual = True

    # While the deque size is still greater than 1 and
    # stillEqual is still True,
    while chardeque.size() > 1 and stillEqual:
        # Remove the extreme right and left character
        # and compare them. If they are not the same
        # then set var stillEqual to False.
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    # Return the state of var stillEqual.
    return stillEqual


# Client call the palchecker() function on a param string
# and print out the boolean result if the param string is
# a palindrome or not.
print(palchecker("lsdjjfskf"))
print(palchecker("toot"))
print(palchecker("madam"))

