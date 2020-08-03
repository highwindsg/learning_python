#!/usr/bin/env python3

"""
Provided is a string saved to the variable name 'sentence'.
Split the string into a list of words, then create a dictionary
that contains each word and the number of times it occurs.
Then save the dictionary th the variable name 'word_counts'.
"""

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

# First split the sentence into every single word in a list.
words = sentence.split()
# print(words)
word_counts = {}    # Create a empty dict accumulator.

for word in words:  # Loop through every word in 'words'.
    if word not in word_counts:
        word_counts[word] = 0   # If word is not seen before, then initialize that word counter to 0.
    word_counts[word] += 1

print(word_counts)
