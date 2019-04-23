#!/usr/bin/env python3

"""
Any sequence that supports iteration can be used within a list comprehension
to construct a new list.
"""
list = [letter.upper() for letter in 'comprehension' if letter not in 'aeiou']
print(list)

