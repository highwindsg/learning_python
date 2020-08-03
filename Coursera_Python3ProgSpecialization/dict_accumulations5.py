#!/usr/bin/env python3

f = open("scarlet.txt", "r")
txt = f.read()  # now 'txt' is a long string containing all the characters.
x = {}
for c in txt:
    if c not in x:
        # If we have not seen this character before, then initialize a counter for it.
        x[c] = 0

    # whether we've seen the character before or not, increment its counter.
    x[c] += 1


# Below is an example of a scrabble score of each letter to a score number.
# Starting with common letter 'a' with score of 1 and less common letter 'z'
# with score of 10.
letter_values = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 8,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10
}
print(letter_values)

scrabble_score = 0
# First check that only letters are looked at and not punctations.
for letter in x:
    # And to keep track of the letters being looked at, we use a 'scrabble_score' accumulator var.
    if letter in letter_values:
        # Therefore score is equals to the previous score plus the value of that letter,
        # and multiply by that letter in the 'x' dict.
        scrabble_score = scrabble_score + letter_values[letter] * x[letter]
print(scrabble_score)
