#!/usr/bin/env python3

"""
Write a function named total that takes a list of integers as input,
and returns the total value of all those integers added together.
"""

def total(lst):
    tot = 0 # Create a var 'tot' as accumualator first with 0 value.
    for num in lst:
        tot = tot + num
    return tot

y = total([1, 5, 7])
print(y)

print("")

"""
Write a function called count that takes a list of numbers or
characters elements as input and returns a count of the number
of elements in the list.
"""

def count(seq):
    c = 0   # Initialize count var to 0 first.
    for _ in seq:
        c += 1  # Increment the counter for each item in seq.
    return c

print(count("hello"))
print(count([1, 2, 7]))

print("")
