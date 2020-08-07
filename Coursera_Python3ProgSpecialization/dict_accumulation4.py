#!/usr/bin/env python3

"""
Create a dictionary called 'char_d' from the string 'stri', so that the
key is character and the value is how many times it occurs.
"""

stri = "what can I do"
char_d = {}

for c in stri:
    if c not in char_d:
        char_d[c] = 0
    char_d[c] += 1
print(char_d)

print("")

"""
Create a dictionary, freq, that displays each character in string
str1 as the key and its frequency as the value.
"""

str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for c in str1:
    if c not in freq:
        freq[c] = 0
    freq[c] += 1
print(freq)

"""
Provided is a string saved to the variable name s1.
Create a dictionary named counts that contains each letter in
s1 and the number of times it occurs.
"""

s1 = "hello"
counts = {}

for letter in s1:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] += 1
print(counts)
