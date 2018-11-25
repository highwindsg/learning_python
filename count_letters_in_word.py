#!/usr/bin/env python3

# Count how many times each letter appears in a given string.

word = "brontosaurus"

# Create a empty dictionary and assign it to the variable 'd'.
d = dict()

# The 'for loop' traverse the string.
# If the character 'c' is not in the dictionary, we create a new item key with the initial
# value of 1 since we have seen this letter once.
# But if the character 'c' is already in the dictionary we increment d[c].
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

# Finally, print out the dictionary.
print(d)
