#!/usr/bin/env python3

s = "xyz"

i = 0   # Initially setting the index of the char in the string to 0.

while i < len(s) and not (s[i] in "aeiouAEIOU"):
    print(s[i])
    i += 1


""" Therefore, first check if the length of the string is 0, then check which
index of the string is not a vowel, then print out that index non-vowel char.
And then increase the index by 1 to do the next char check. """

