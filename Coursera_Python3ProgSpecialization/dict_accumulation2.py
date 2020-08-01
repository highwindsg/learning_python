#!/usr/bin/env python3

txt = "MICHIGAN"
x = {}
for c in txt:
    if c not in x:  # Iterate through every character in dict 'x'.
        x[c] = 0    # And if character is not encountered in dict 'x',
    x[c] += 1   # create a new character counter by increasing the counter of that new character.
print(x)    # Print out the dict 'x' to show how many characters and its re-occurences.
