#!/usr/bin/env python3

"""
An anagram is a word created by re-arranging the letters of another word.
eg. the word 'iceman' is an anagram of the word 'cinema'.
"""

def anagram(w1, w2):    # Create a function named 'anagram' with two params.
    w1 = w1.lower()     # Set var 'w1' to non-case sensitive.
    w2 = w2.lower()     # Set var 'w2' to non-case sensitive.
    return sorted(w1) == sorted(w2)

"""Use Python in-build sort() function to sort alphabetically and check
if they are equally the same, including case-sensitive.
If the same, return True to the function.
If not the same, then return False to the function."""


print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))
