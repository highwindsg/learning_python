#!/usr/bin/env python3

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)
"""
The first loop iterates through every integer in 'list1'.
For each item in it, the second loop iterates through
each integer in its own iterable, adds it to the integer
from 'list1' and appends the result to the list 'added'.
"""

