#!/usr/bin/env python3

"""
format:= (name, radius, density, distance from sun)

Radius: Radius at equator in kilometers.
Density: Average density in g/cm^3.
Distance from sun: Avg distance to sun in AUs.

1 Astronomical unit is est. avg distance of earth to sun.
"""

planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 9.551),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]


# Sort the planets by their size, with the largest planet first, so we look at the radius.

# Using lambda anonymous func at index 1 as the second slice which is the radius, and assign to var obj 'size'.
size = lambda planet: planet[1]

# Sort the 'planets' list with params key value set to var obj 'size', and reverse set to True since we want to sort
# from largest to smallest.
planets.sort(key=size, reverse=True)

print(planets)
print("")


# Sort the planets by the least density first.

# Using lambda anonymous func to create the sorting function at index 2 as the third slice which is the density,
# and assign to the var obj 'density'.
density = lambda planet: planet[2]

# Sort the 'planets' list with param key value set to var obj 'density'.
planets.sort(key=density)

print(planets)
print("")
