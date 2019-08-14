#!/usr/bin/env python3

# Creating two different instance vars from a single class.

class PartyAnimal:      # Create a class named 'PartyAnimal.
    x = 0               # Set var 'x' with 0 first.
    name = ""           # Set var 'name' with empty string first.

    def __init__(self, z):  # Define a init start func with params self and z.
        self.name = z       # Set param 'self' with attrib var 'name' and assign to param 'z'.
        print(self.name, "constructed") # Print out the 'name' attrib from param 'self' which points to 'z'.

    def party(self):        # Define a party func with param self.
        self.x = self.x + 1 # Set param 'self' with an attrib of var 'x' and increase count by 1,
                            # and then assign it back to var obj 'self.x'.
        print(self.name, "party count", self.x) # Print out the var obj of 'self.name' and 'self.x'.

s = PartyAnimal("Sally")    # Var 's' is-a PartyAnimal class with param 'Sally'.
s.party()                   # Client call the func 'party' from class 'PartyAnimal()'.

j = PartyAnimal("Jim")      # Var 'j' is-a PartyAnimal class with param 'Jim'.
j.party()                   # Client call the func 'party' from class 'PartyAnimal().

s.party()                   # Client call again the func 'party' from class 'PartyAnimal().
