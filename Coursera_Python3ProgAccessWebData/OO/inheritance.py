#!/usr/bin/env python3

"""
When we make a new class, we can reuse an existing class and inherit all the
capabilities of an existing class and then add our own little bit to make our
own new class.

Another form of store and re-use.

Write once, re-use many times.

The new class (child) has all the capabilities of the old class (parent),
and then some more bits of its own.

Also known as 'subclasses', which are more specialized versions of a class,
which inherit attributes and behaviors from their parent classes, and can
introduce their own.
"""



class PartyAnimal:
    
    x = 0
    name = ""
    
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")
        
    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)
        

# Creates a new FootballFan class which inherits everything from the PartyAnimal class.
# Other than all the features of PartyAnimal class, this new class will also have its
# own additional features below, eg. 'points' var and 'touchdown()' func.
class FootballFan(PartyAnimal):
    
    points = 0      # class var 'points' which belongs to the FootballFan class.
    
    def touchdown(self):    # Create func 'touchdown()' with param self.
        self.points += 7    # Increase the points value by 7.
        self.party()        # From self, call the party() func from PartyAnimal class.
        print(self.name, "points", self.points) # From self, get the name value which
        # is the inherited PartyAnimal call, and also the points from its own
        # FootballFan's class var.
        
        
s = PartyAnimal("Sally")    # 's' is-a PartyAnimal class with param Sally.
s.party()   # From obj 's', call the party() func.
print("")

j = FootballFan("Jim")      # 'j' is-a FootballFan class with param Jim, which has
# inherited from the PartyAnimal class.
j.party()   # From obj 'j', call the party() func.
print("")

j.touchdown()   # From obj 'j', which is-a FootballFan class, call its own
# touchdown() func.
print("")
