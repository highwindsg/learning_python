#!/usr/bin/env python3

"""
Write a function called change that takes any string, adds
“Nice to meet you!” to the end of the argument given, and returns
that new string.
"""

def change(str):
    newstr = str + "Nice to meet you!"
    return newstr


intro = "Hi my name is Jon. "
print(change(intro))
