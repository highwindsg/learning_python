#!/usr/bin/env python3

txt = "MICHIGAN"
x = {}
for c in txt:
    if c not in x:  # Iterate through every character in dict 'x'.
        x[c] = 0    # And if character is not encountered in dict 'x',
    x[c] += 1   # create a new character counter by increasing the counter of that new character.
                # Or increase the count by 1 if character seen before.
print(x)    # Print out the dict 'x' to show how many characters and its re-occurences.
print("")


"""
Create a dictionary called char_d from the string stri, so that the 
key is a character and the value is how many times it occurs.
"""

stri = "what can I do for you this good day"

char_d = {}
for c in stri:
    if c not in char_d:
        char_d[c] = 0
    char_d[c] += 1

print(char_d)
print("")
