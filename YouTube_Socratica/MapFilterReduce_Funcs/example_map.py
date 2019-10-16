#!/usr/bin/env python3

import math


def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)
print("")

# Method 2: Use 'map' function.

print(map(area, radii))
print(list
      (map
       (area, radii)
       )
      )
