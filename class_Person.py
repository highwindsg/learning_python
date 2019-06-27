#!/usr/bin/env python3

class Person:   # Create a Person class. 
    def __init__(self, name):   # Define a init start with param self and name.
        self.name = name        # From self, set the attrib name to var obj name.

    def talk(self):             # Define a method talk with param self.
        print(f"Hi, I am {self.name}")  # Print out the name of the person dynamically.


john = Person("John Smith")     # Set var john to an instance of class Person
                                # with param of string 'John Smith'.
#print(john.name)
john.talk()

bob = Person("Bob Smith")       # Set var bob to an instance of class Person
                                # with param of string 'Bob Smith'.
bob.talk()                      # From var bob, get the talk method.

