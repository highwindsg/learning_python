#!/usr/bin/env python3

"""
Write a program that finds the key in a dictionary that has the maximum value.
If two keys have the same maximum value, it’s OK to print out either one.
"""

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
print(ks)
best_key_so_far = list(ks)[0]   # Have to turn ks into a real list before
                                # using [] to select an item.
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))
