#!/usr/bin/env python3

# Using __del__ (a destructor) to destroy a local created var value.

class PartyAnimal:  # Create a class named 'PartyAnimal'.
    x = 0           # var 'x' to 0 first.

    def __init__(self):             # Create a init/constructor start func with param self.
        print("I am constructed")

    def party(self):                # Create a 'party' function with param self.
        self.x = self.x + 1         # From the 'party' function, set the param self with the attrib of var 'x',
                                    # and increase the value of var 'x' by 1 count.
        print("So far", self.x)     # Then print out the value of the latest count of var 'x' from param self.

    def __del__(self):              # Create a delete/destructor func with param self.
        print("I am destroyed", self.x)

an = PartyAnimal()          # an is-a PartyAnimal() class.
an.party()                  # Client call the 'party' function.
an.party()                  # Client call the 'party' function again.
an = 42                     # Set var 'an' to new value with 42. This will then cause the destructor func
                            # to delete whatever previous value of 'self.x' in line 14, since now there is a new
                            # manual assignment for var 'an'.
print("an contains", an)

'''
The constructor and destructor are optional.
The constructor is typically used to set up variables.
The destructor is seldom used.
'''
