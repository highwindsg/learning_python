#!/usr/bin/env python3

# Dictionaries have a method called get() that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; otherwise
# it returns the default value.
# Example: (in a interactive shell below)
# >>> counts = {"chuck" : 1, "annie" : 42, "jan" : 100}
# >>> print(counts.get("jan", 0))
# 100
# >>> print(counts.get("tim", 0))
# 0

# In order to count more concisely how many times each letter appears in a given string,
# we use the get() method to handle cases where a key is not in a dictionary.
# This way, we reduce a few lines to one statement and eliminate the 'if' statement.

#word = "brontosaurus"
word2 = "DeoxyriboNucleic Acid"

d = dict()
for c in word2:
    d[c] = d.get(c,0) + 1
print(d)
