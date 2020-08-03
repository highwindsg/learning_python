#!/usr/bin/env python3

"""
Create a dictionary called 'char_d' from the string 'stri', so that the
key is character and the value is how many times it occurs.
"""

stri = "what can I do"
char_d = {}

for c in stri:
    if c not in char_d:
        char_d[c] = 0
    char_d[c] += 1

print(char_d)
