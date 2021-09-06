#!/usr/bin/env python3

# List methods.

# A list of things.
planets = ["Mercury",
           "Venus",
           "Earth",
           "Mars",
           "Jupiter",
           "Saturn",
           "Uranus",
           "Neptune"
           ]

# Adding the name 'Pluto' to the end of the 'planets' list by using the .append() method.
print(
    planets.append("Pluto")
    )
print(planets)
print("")

# The .pop() method will remove the last element in the list.
print(
    planets.pop()
    )
print(planets)
print("")

# Using the .index() method to get the index to see where does 'Earth' fall in the order
# of the 'planets' list. The answer index '2' means it comes third in the 'planets' list.
print(
    planets.index("Earth")
    )
print("")

# Can also use the 'in' operator to determine if a value is in a list.
print("Mars" in planets)
print("Pluto" in planets)
print("")

# If you want to learn more about all the methods and attributes of a obj (eg. planets),
# which is a list, then call help() on the obj.
print(
    type(planets)
    )
print(
    help(planets)
    )
print("")
