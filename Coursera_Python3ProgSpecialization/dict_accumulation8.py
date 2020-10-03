#!/usr/bin/env python3

"""
Create a dictionary called 'd' that keeps track of all the characters in the
string 'placement' and note how many times each character was seen. Then find
the key with the lowest value in this dictionary and assign that key to
'min_value' variable. Therefore there are two parts to this question.
"""

placement = "Beaches are cool places to visit in spring however the Mackinow Bridge is near. Most people visit Mackinow later since the island is a cool place to explore."

d = {}  # First create a empty dict 'd'.

# This is the first part to find how many times each character was seen.
for c in placement: # 'c' stands for character.
    if c not in d:  # So if a character is not in dict 'd',
        d[c] = 0    # the initialize that character key with value 0.
    d[c] += 1   # Then increase the counter of that character if seen before by 1.
print(d)
print("")

# This is the second part to find the key with the lowest value.
keys = list(d.keys())   # To first get a list of keys, using the .keys() method
                        # on the dict 'd' and put then in a list and assign
                        # to var 'keys'.
print(keys)
min_value = keys[0] # Suppose we set the first key as the lowest value for now.

for key in keys:    # Then search for every key that has the next lower value.
    if d[key] < d[min_value]:
        min_value = key # And set the lower value key as the 'min_value'.

print(min_value)
print("")


"""
Find the least frequent letter. Create the dictionary characters
that shows each character from string sally and its frequency.
Then, find the least frequent letter in the string and assign the
letter to the variable worst_char.
"""

sally = "sally sells sea shells by the sea shore and by the road"

characters = {}

# First create the dict 'characters' with the characters as keys and
# the frequency of occurances as values.
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1
print(characters)
print("")

# Then convert dict 'characters' into a list by using the .keys() method.
char_lst = list(characters.keys())
print(char_lst)
worst_char = char_lst[0]    # Assuming first item in list is worst_char,
                            # so that can start to make comparison next.

for item in char_lst:
    if characters[item] < characters[worst_char]:
        worst_char = item
print(worst_char)
print("")



"""
Create a dictionary named letter_counts that contains each letter
and the number of times it occurs in string1.
Challenge: Letters should not be counted separately as upper-case
and lower-case. Instead, all of them should be counted as lower-case.
"""

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

letter_counts = {}

for c in string1.lower():   # Use the .lower() string method to convert whole string to lower cases.
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] += 1
print(letter_counts)
print("")


"""
Create a dictionary called low_d that keeps track of all the
characters in the string p and notes how many times each character
was seen. Make sure that there are no repeats of characters as keys,
such that “T” and “t” are both seen as a “t” for example.
"""

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

low_d = {}

for c in p.lower():
    if c not in low_d:
        low_d[c] = 0
    low_d[c] += 1
print(low_d)
print("")
