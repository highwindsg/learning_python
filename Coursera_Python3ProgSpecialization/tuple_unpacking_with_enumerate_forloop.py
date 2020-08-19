#!/usr/bin/env python3

"""
The pythonic way to consume the results of enumerate, is to unpack
the tuples while iterating through them, so that the code is easier
to understand.
"""

fruits = ["apple", "pear", "approcot", "cherry", "peach"]
print(fruits)
print("")

for idx, fruit in enumerate(fruits):
    print(idx, fruit)
print("")

# Or to enumerate and unpack into tuples:
for fruit in enumerate(fruits):
    print(fruit)
print("")

