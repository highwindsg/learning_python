#!/usr/bin/env python3

class Hello:
    def __init__(self, name):
        self.name = name
        self.age = 10       # Even though '.age' is not parsed in line 4 __init__() func param as an argument,
                            # this default '.age' attrib can still be assigned here this way.
"""
Therefore it is not necessary to define all the arguments params in the init func.
The attrib can still be initialize/assign within the suite body using the 'self' param. eg. 'self.age = 10'.
"""


hello = Hello("Max")        # Func call the Hello() class with param 'Max' as the name, and assign to var 'hello'.
print(hello.name)           # Print out the attrib of '.name' from var obj 'hello'.
