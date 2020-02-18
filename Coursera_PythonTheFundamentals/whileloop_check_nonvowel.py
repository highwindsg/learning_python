#!/usr/bin/env python3

s = "there"

i = 0   # Setting the first index of the string initially to 0.

while not (s[i]) in "aeiouAEIOU":
    print(s[i])
    i += 1

""" Therefore while the index of the string does not have any vowels in it,
it will print out the non-vowel index and carry on to the next index by
increasing the index by 1. The result will print out 't' and 'h' and stop. """

