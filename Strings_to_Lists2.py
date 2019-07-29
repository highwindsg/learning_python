#!/usr/bin/env python3

line = "A lot            of spaces"
etc = line.split()
print(etc)
print("")

line = "first;second;third" # ';' is treated as part of the string.
thing = line.split()        # The split() method without any param will convert the string to a list,
print(thing)
print(len(thing))           # and the list has only 1 item.
print("")

thing = line.split(";")     # You can specify what delimiter char to use in the splitting.
print(thing)
print(len(thing))           # After using ';' as a param in the split() method, the list will
print("")                   # have 3 items.
