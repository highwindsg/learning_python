#!/usr/bin/env python3

"""
Provided is a string saved to the variable name 'sentence'.
Split the string into a list of words, then create a dictionary
that contains each word and the number of times it occurs.
Then save the dictionary to the variable name 'word_counts'.
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

print("")

"""
Create a dictionary, freq_words, that contains each word in string
str1 as the key and its frequency as the value.
"""

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

words = str1.split()
freq_words = {}

for word in words:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1
print(freq_words)

print("")

"""
Create a dictionary called wrd_d from the string sent, so that
the key is a word and the value is how many times you have seen
that word.
"""

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

words = sent.split()
wrd_d = {}

for word in words:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] += 1
print(wrd_d)

print("")
