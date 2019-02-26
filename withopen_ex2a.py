#!/usr/bin/env python

"""
The 'with open' statement closes the file after accepting input.
So assigning the input to a 'sentence' var allows for later use in
the program.
"""

sentence = input("What do you want to say? ")
with open("withopen_ex2.txt", "w") as f:
    f.write(sentence)

print("This is what he or she said:", sentence)

