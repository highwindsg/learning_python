#!/usr/bin/env python3

class Person:               # Create a class Person.
    def __init__(self):     # Define a start init function with param self.
        self.name = "Bob"   # From self, get the name attribute and set it to Bob.


bob = Person()              # Set bob to an instance of class Person.
same_bob = bob
print(bob is same_bob)

another_bob = Person()      # Set another_bob to an instance of class Person.
print(bob is another_bob)
"""
When you use the keyword 'is' in an expression with the objects bob and same_bob
as operators, the expression evaluates to True because both variables point to
the same Person object at the same memory location.
But when you create a new Person object (eg. another_bob) and compare it to the
original bob, the expression evaluates to False because the variables point to
different Person objects which has a different memory location respectively.
"""
