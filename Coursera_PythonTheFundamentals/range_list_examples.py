#!/usr/bin/env python3

"""
Because len returns the number of items in a list, it can be used
with range to iterate over all the indices. This loop prints all
the values in a list:

for i in range(len(lst)):
    print(lst[i])
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(lst)):
    print(lst[i])
print("")


""" This also gives us flexibility to process only part of a list.
For example, We can print only the first half of the list:"""

for i in range(len(lst) // 2):
    print(lst[i])
print("")


""" Or every other elements."""

for i in range(0, len(lst), 2):
    print(lst[i])
print("")

