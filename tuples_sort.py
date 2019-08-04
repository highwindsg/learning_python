#!/usr/bin/env python3

print("Sorting dict items using tuples.")
d = {
    "a": 10,
    "b": 1,
    "c": 22
}
print(d.items())

# Sorting the dict items by the key, using the sorted() method.
print(sorted(d.items()))    # The sorted() method takes a list as input.

# Again using the sorted() method to sort the dict items, and assign to var 't'.
t = sorted(d.items())
print(t)

for k, v in sorted(d.items()):
    print(k, v)

print("")

print("Sort by values instead of keys.")
c = {
    "a": 10,
    "b": 1,
    "c": 22
}
tmp = list()    # First create an empty 'tmp' list.

for k, v in c.items():
    tmp.append( (v, k) )    # Using the .append method and pass (v, k) as one argument.
print(tmp)

tmp = sorted(tmp, reverse=True) # using the sorted() method on the 'tmp' list and reverse it.
print(tmp)                      # so the value numbers are sorted in a descending order.
