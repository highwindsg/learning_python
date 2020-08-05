#!/usr/bin/env python3

"""
Create a dictionary called 'd' that keeps track of all the characters in the
string 'placement' and note how many times each character was seen. Then find
the key with the lowest value in this dictionary and assign that key to
'min_value' variable. Therefore there are two parts to this question.
"""

placement = "Beaches are cool places to visit in spring however the Mackinow bridge is near. Most people visit Mackinow later."

d = {}  # First create a empty dict 'd'.

# This is the first part to find how many times each character was seen.
for c in placement: # 'c' stands for character.
    if c not in d:  # So if a character is not in dict 'd',
        d[c] = 0    # the initialize that character key with value 0.
    d[c] += 1   # Then increase the counter of that character if seen before by 1.
print(d)

print("")

# This is the second part to find the key with the lowest value.
keys = list(d.keys())   # To first get a list of keys, using the .keys() method
                        # on the dict 'd' and put then in a list and assign
                        # to var 'keys'.
print(keys)
min_value = keys[0] # Suppose we set the first key as the lowest value for now.

for key in keys:    # Then search for every key that has the next lower value.
    if d[key] < d[min_value]:
        min_value = key # And set the lower value key as the 'min_value'.

print(min_value)
