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
    lett_d[c] += 1  # Then increase the counter of that characrter by 1 if seen before.
print(lett_d)

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
