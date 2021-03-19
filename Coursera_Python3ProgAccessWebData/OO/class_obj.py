#!/usr/bin/env python3

class PartyAnimal:  # Create a PartyAnimal class, with attrib x with value 0.
    x = 0   # x = 0 can be viewed as a accumulator.
    y = 0
    
    def party(self):    # In the class, define a func named party with param self.
        self.x += 1     # From self, get the attrib value of x and increase by 1.
        print("So far", self.x) # Then print out the txt and with the accumulated value of x.
        
    def crying(self):
        self.y -= 1
        print("This is a sad party", self.y)
        
        
an = PartyAnimal()  # an is-a PartyAnimal() class.


# Calling the obj 'an' and executing its func method of .party().
an.party()
an.party()
an.party()
# Calling the obj 'an' and executing its func method of .crying().
an.crying()
an.party()
# Or calling the PartyAnimal() class and executing its func method of .party() with param 'an' obj.
PartyAnimal.party(an)
an.party()
an.crying()
an.crying()
an.crying()
print("")
print(type(an)) # To show the data type opf the 'an' obj.
print(dir(PartyAnimal))  # Use dir() func to see the capabilities and what is inside the created class.
print("")
# or,
print(dir(an))
print("")
# Therefore 'dir()' func can be used to see what is inside of an obj.
