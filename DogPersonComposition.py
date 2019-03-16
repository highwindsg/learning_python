#!/usr/bin/env python3

"""
Important concept: composition
Composition models the "has-a" relationship by storing an object as a variable in another
object. For example, you can use composition to represent the relationship between a dog
and its owner (a dog has-an owner).
"""

class Dog():
    def __init__(self,
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")    # The 'mick' var is assigned the 'Person' object with a param.
stan = Dog("Stanley",   # The 'stan' var is assigned the 'Dog' object with params
           "Bulldog",   # 'name' -> "Stanley"; 'breed' -> "Bulldog"; and var 'mick' that is
           mick)        # assigned with the 'Person' object with the 'name' instance var.

print(stan.owner.name)  # Print the output from 'stan' var and get the attribute of 'owner'
                        # from the 'Dog' object that has-a owner param, that is a var 'mick'
                        # which is assigned to the 'Person' object with the 'name' instance var.
"""
Now the 'stan' object "Stanley" has-an 'owner' -- a 'Person' object named "Mick Jagger"
-- stored in the 'owner' instance var.
"""
