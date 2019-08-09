#!/usr/bin/env python

"""
The 'with open' statement closes the file after accepting input.
So assigning the input to a 'sentence' var allows for later use in
the program.
"""

SENTENCE = input("What do you want to say? ")
with open("withopen_ex2.txt", "w") as f:
    f.write(SENTENCE)

print("This is what he or she said:", SENTENCE)
