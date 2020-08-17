#!/usr/bin/env python3

"""
Write a function, accum, that takes a list of integers as input
and returns the sum of those integers.
"""

def accum(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

list1 = accum([2, 4, 2])
print(list1)
