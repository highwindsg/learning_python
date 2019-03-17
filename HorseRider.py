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

print(buff.owner.name)
print("The horse", buff.name, "is a", buff.breed, "breed and has-a rider named",
      buff.owner.name + ".")
