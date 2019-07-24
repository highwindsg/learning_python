#!/usr/bin/env python3

s = "Monty Python"

print(s[0:4])   # Slicing from index 0 up to but not including 4.

print(s[6:7])   # Slicing from index 6 up to but not including 7.

print(s[6:20])  # Slicing from index 6 up to but not including 20,
                # although there are no index position 20,
                # python will still print out the remaining characters.

print("")

print(s[:2])    # Slicing from index 0 up to but not including 2.

print(s[8:])    # Slicing from index 8 up to the end of the word.

print(s[:])     # Slicing from beginning to the end, which is the whole word.

