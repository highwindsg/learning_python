#!/usr/bin/env python3

"""
Global variables are another way to have side effects.
For example, we could make 'double' have a side effect on the
global variable y.
"""

def double(n):
    global y    # Taking the value of var y from global var.
    y = 2 * n


y = 5
double(y)
print(y)
print("")
