#!/usr/bin/env python3
"""
Create a class called Horse and a class called Rider. Use composition to model
a horse that has-a rider.
"""
class Horse():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Rider():
    def __init__(self, name):
        self.name = name


johnny = Rider("Johnny Julian")
buff = Horse("Buffie", "Mustang", johnny)

# Print out the horse's owner/rider name. From buff which has been assigned the
# Horse class of params, obtain the owner param which is the var johnny, that
# has been assigned the Rider class with param "Johnny Julian".
print(buff.owner.name)

# Print out the horse's name, its breed and the rider's name.
# From var buff, which has been assigned the Horse params, get the name.
# From var buff, which has been assigned the Horse params, get the breed.
print("The horse", buff.name, "is a", buff.breed, "breed and has-a rider named",
      buff.owner.name + ".")
