#!/usr/bin/env python3

"""
Create a dictionary called 'lett_d' that keeps track of all the characters in
the string 'product' and note how many times each character was seen. Then
find the key with the highest value in this dictionary and assign that key
to 'max_value' variable. Likewise there are two parts to this question.
"""
product = "iphone and andriod phones"

lett_d = {}

# The first part is to find how many times each character was seen.
for c in product:   # For every character in the 'product' string,
    if c not in lett_d: # if a character is not seen in dict 'lett_d',
        lett_d[c] = 0   # then initialize that character key with value 0.
    lett_d[c] += 1  # Then increase the counter of that character by 1,
print(lett_d)       # regardless whether it is seen before or not.

print("")

# The second part is to find the character that occurs the most.
keys = list(lett_d.keys())  # Use the .keys() method on dict 'lett_d' to
                            # create a list and assign to var 'keys'.
print(keys)
max_value = keys[0] # Suppose we set the first key's value as the higher value.
for key in keys:    # For every key in the keys list,
    if lett_d[key] > lett_d[max_value]: # if the value 'lett_d[key]' is greater
                                        # than the value of 'lett_d[max_value],
        max_value = key # then assign this 'key' value the latest 'max_value'.
print(max_value)

print("")


"""
Create the dictionary characters that shows each character from the
string sally and its frequency. Then, find the most frequent letter
based on the dictionary. Assign this letter to the variable best_char.
"""

sally = "sally sells sea shells by the sea shore"

characters = {}

for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1
print(characters)

keys = list(characters.keys())
print(keys)
best_char = keys[0]

for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key
print(best_char)

print("")
