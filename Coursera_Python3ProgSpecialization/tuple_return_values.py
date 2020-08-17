#!/usr/bin/env python3

"""
Below is a exmaple for 'tuple packing' the return values into a
tuple and return back to the func.
"""

def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r # Calculating circumference.
    a = 3.14159 * r * r # Calculating area.
    return (c, a)   # Using tuples as a return value to the func.


print(circleInfo(10))
print("")
