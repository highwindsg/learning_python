#!/usr/bin/env python3

"""
Define a function called 'sign' which takes a numerical argument
and returns -1 if it's negative, 1 if it's positive, and 
0 if it's 0.
"""

def sign(num):
    if num == 0:
        return 0
    elif num < 0:
        return -1
    elif num > 0:
        return 1
    
    
print(sign(5))
print(sign(-3))
print(sign(0))
print("")
