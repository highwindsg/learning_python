#!/usr/bin/env python3

""" Can also import the pdb as a module so as no need to manually type in the console to start the debugging."""

import pdb

def add(x, y):
    sum = x + y
    return sum

if __name__ == "__main__":
    x = input("Num 1 : ")       # The int() method is purposely omitted out in order to show how to use debugging.
    y = input("Num 2 : ")       # The int() method is purposely omitted out in order to show how to use debugging.
    pdb.set_trace()     # From pdb, get the 'set_trace()' method, which will set a break point for the next line.
    z = add(x, y)
    print(z)

"""
The 'pdb.set_trace()' method will set a break point for the next line.
Then run the program and enter the two inputs, and then the program will break/stop at line 16.
And after the debugging is done, remove the 'pdb.set_trace()' line to end the debugging.
"""
