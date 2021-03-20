#!/usr/bin/env python3

"""
We can create lots of objs, and the class is the template for the objs.
We can store each different obj in its own var.
This is called multiple instances of the same class.
Therefore each instance has its own copy of the 'instance var'.
"""



class PartyAnimal:
    x = 0   # Set class var 'x' to 0.
    name = ""   # Set class vae 'name' to an empty string.
    
    """ To initiate the class, or known as the constructor.
    Constructors can have additional params. eg. 'z'.
    These can be used to set up 'instance vars' for the particular instance
    of the class. (eg. for the particular obj).
    """
    def __init__(self, z):  # Initiate the class with params self and z.
        self.name = z   # From obj self, set the class var of name to z.
        print(self.name, "constructed")
        
    def party(self):
        self.x += 1     # Increase the value of obj self.x by 1.
        print(self.name, "party count", self.x) # Print out the name and the attrib value of x.
        
    # In this example there are no destructor func '__del__()' as it is optional and rarely used.
        

        
s = PartyAnimal("Sally")    # 's' is an independent instance and is-a PartyAnimal class with param Sally.
s.party()   # Calling the obj 's' and its party() func.
#s = 99
print("")

j = PartyAnimal("Jim")      # Create another independent instance of 'j' is-a PartyAnimal class with param Jim.
j.party()   # Calling the obj 'j' and its party() func.
print("")

s.party()   # Calling the obj 's' and its party() func. We can still call the obj 's' because it
# still is-a PartyAnimal class and is not destroyed yet. Unless you assigns var 's' with another value.
# The attrib value of 'x' will also be printed out as 's' is using the same class var of 'x'.
print("")
