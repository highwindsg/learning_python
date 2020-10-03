#!/usr/bin/env python3

txt = "MICHIGAN"
x = {}
for c in txt:
    if c not in x:  # Iterate through every character in dict 'x'.
        x[c] = 0    # And if character is not encountered in dict 'x',
    x[c] += 1   # create a new character counter by increasing the counter of that new character.
                # Or increase the count by 1 if character seen before.
print(x)    # Print out the dict 'x' to show how many characters and its re-occurences.
print("")


"""
Create a dictionary called char_d from the string stri, so that the 
key is a character and the value is how many times it occurs.
"""

stri = "what can I do for you this good day"

char_d = {}
for c in stri:
    if c not in char_d:
        char_d[c] = 0
    char_d[c] += 1

print(char_d)
print("")



"""
Create a dictionary named letter_counts that contains each letter and 
the number of times it occurs in string1. Challenge: Letters should 
not be counted separately as upper-case and lower-case. Instead, all 
of them should be counted as lower-case.
"""

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}

for c in string1.lower():   # To look at every char as lower case.
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] += 1

print(letter_counts)
print("")
