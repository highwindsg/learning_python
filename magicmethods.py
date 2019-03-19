#!/usr/bin/env python3

class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Dilbert")
print(lion)
"""
Every class in Python inherits from a parent class called Object.
Python utilizes the methods inherited from Object in different situations
-- like when you print an object in eg. line 8 above, which will give the
output of the Lion object at some memory location.
"""
