#!/usr/bin/env python3

"""
list.sort() changes the list.
Q1. But can you create a sorted copy?
Q2. And how to you sort a tuple, where a tuple is immutable.
Ans: Use the 'sorted()' function.
"""

# Check the help text for the sorted() function.
print(help(sorted))
print("")

# Create a list of earth metals.
earth_metals = ["Beryllium",
                "Magnesium",
                "Calcium",
                "Strontium",
                "Barium",
                "Radium"]


# Use the 'sorted()' func on the 'earth_metals' list, and assign to var obj 'sorted_earth_metals'.
sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)  # Print out the alphabetically sorted earth metals.
print("")

# Sort a tuple of integers that are in a random order.
data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
sorted_data = sorted(data)  # Use the 'sorted()' func with 'data' as param, and assign to 'sorted_data' var obj.
print(sorted_data)
print("")

# Sort a string as it is iterable.
print(sorted("Alphabetical"))
