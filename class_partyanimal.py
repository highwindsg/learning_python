#!/usr/bin/env python3

class PartyAnimal:      # Create a class named 'PartyAnimal'.
    x = 0               # Set a var 'x' to 0 first.

    def party(self):    # Define a 'party()' function with param self.
        self.x = self.x + 1     # From self, get the 'x' attrib, increase 1, and assign back to var obj 'self.x'.
        print("So far", self.x) # Print out the text 'So far' and value of 'self.x').

animal = PartyAnimal()  # Set var 'animal' to an instance of class PartyAnimal.
print("Type", type(animal))

# Client call, from 'animal' var, get the party function.
animal.party()
animal.party()
animal.party()
