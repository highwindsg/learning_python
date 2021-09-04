#!/usr/bin/env python3

# a list of prime numbers.
primes = [2, 3, 5, 7]

# a list of things.
planets = ["Mercury",
           "Venus",
           "Earth",
           "Mars",
           "Jupiter",
           "Saturn",
           "Uranus",
           "Neptune"
           ]

# a list of lists, or multiple lists in a list.
alphanumeric = [
    ["J", "Q", "K"],
    ["2", "2", "2"],
    ["6", "A", "K"], # the comman after the last line here is optional.
]
# Could also write on one line, but difficult to read.
alphanumeric2 = [["J", "Q", "K"], ["2", "2", "2"], ["6", "A", "K"]]

# a list can contain a mix of different types of variables.
my_fav_things = [32, "raindrops of roses", help]

print(planets[0]) # zero-based indexing, so the first element has an index of 0.
print("")

print(planets[1])
print("")

print(planets[-1])
print("")

print(planets[-2])
print("")

# using slicing to print the first three planets.
print(planets[0:3]) # up to 3 but does not include 3.
print("")

# leaving out the end index means print out the remaining length of the list.
print(planets[3:])
print("")

# print out all the planets except the first and the last.
print(planets[1:-1])
print("")

# print out the last 3 planets.
print(planets[-3:])
print("")

# to change an item in a list.
planets[3] = "Malacandra"
print(planets)
print("")

# to shorten the names of the first 3 planets of the list.
planets[:3] = ["Mur", "Ve", "Ea"]
print(planets)
# renaming them back to the orginal full name.
planets[:4] = ["Mercury", "Venus", "Earth", "Mars",]
print(planets)
print("")
