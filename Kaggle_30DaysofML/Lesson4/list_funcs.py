#!/usr/bin/env python3

# Functions that works with lists.

# A list of things.
planets = ["Mercury",
           "Venus",
           "Earth",
           "Mars",
           "Jupiter",
           "Saturn",
           "Uranus",
           "Neptune"
           ]

# How many planets are there in the planet list? Use the len() func.
print(len(planets))
print("")

# To sort the planets in a alphanumeric order. Use the sorted() func.
print(sorted(planets))
print("")

# Sum up the numbers in the list. Use the sum() func.
primes = [2, 3, 5, 7]
print(sum(primes))
print("")

# Parse in single list as an argument in the max() or min() func.
print(max(primes))
print("")
print(min(primes))
print("")
