#!/usr/bin/env python3

"""
A 'constructor' in a class is a special block of statements called when an object is created.
"""



class PartyAnimal:
    x = 0
    
    def __init__(self): # Initiate the class with a param 'self', this func is known as the constructor.
        print("I am constructed")
        
    def party(self):
        self.x += 1
        print("So far", self.x)
        
    def __del__(self):  # 
        print("I am destucted", self.x)
        
        
        
an = PartyAnimal()  # 'an' is an instance of class PartyAnimal. Or 'an' is-a PartyAnimal.
an.party()
an.party()
an = 42     # So when 'an' is assigned a new value, 'an' will run the destructor func in the class.
print("an contains", an)
print("")

# So when you try to run this line again, obj would not be found as the destructor has deleted/destroyed
# the 'an' obj, which is no longer pointing to the class.
#an.party()

# Only by re-assigning var obj 'an' with the PartyAnimal class again ...
an = PartyAnimal()
an.party()  # ... then you can call the obj and it's func.
print("")
