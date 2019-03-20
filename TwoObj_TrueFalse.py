#!/usr/bin/env python3

"""
Write a function that takes two objects as parameters and returns True
if they are the same object, and False if not.
"""
def compare_objs(obj1, obj2):
    return obj1 is obj2

print(compare_objs("1", "2"))
