#!/usr/bin/env python3

# Coin flip program

import random

nFlips = 0      # To count the number of flips
nTails = 0      # To count the number of flips that came up as tails
nHeads = 0      # To count the number of flips that came up as heads

maxFlips = int(input("How many flips do you want to do? "))

while nFlips < maxFlips:
    # Randomly choose 0 or 1, because a coin flip can only result in one of two answers
    # (heads or tails)
    zeroOrOne = random.randrange(0, 2)

    # If we get a zero, say that was a heads
    # If we get a one, say that was a tails
    if zeroOrOne == 0:
        nHeads = nHeads + 1
    else:
        nTails = nTails + 1

    nFlips = nFlips + 1

print()
print("Out of", nFlips, "coin tosses, we had:", nHeads, "heads, and", nTails, "tails.")
