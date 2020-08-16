#!/usr/bin/env python3

"""
If a function makes a change to a mutable object like a list or
a dictionary, that's called a side effect.
"""

def double(y):
    y = 2 * y


def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"


y = 5
double(y)
print(y)

mylst = ["our", "students", "are", "awesome"]
changeit(mylst)
print(mylst)

"""
Therefore running 'double(y)' does not change the global y.
But running 'changeit(mylst)' does change mylst.
"""
