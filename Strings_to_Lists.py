#!/usr/bin/env python3

abc = "With three words"
stuff = abc.split()     # This will change the var string to a list.
print(stuff)            # This will print out a list of stuff.
print("")

print(len(stuff))
print("")

print(stuff[0])
print("")

for w in stuff:
    print(w)
