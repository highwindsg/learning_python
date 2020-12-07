#!/usr/bin/env python3

"""
'schedule' is a dictionary where a class name is a key and its value is how many
credits it was worth. Go through and accumulate the number of credits that
have been earned so far and assign that to the variable 'total_credits'.
Do not hardcode.
"""

schedule = {
            "UARTS 150": 3,
            "SPANISH 103": 4,
            "ENGLISH 125": 4,
            "SI 110": 4,
            "ENS 356": 2,
            "WOMENSTD 240": 4,
            "SI 106": 4,
}

total_credits = 0   # Initialize accumulator var.
for course in schedule:
    total_credits = total_credits + schedule[course]
print("Total number of credits earned so far:", total_credits)
print("")


"""
The dictionary Junior shows a schedule for a junior year semester.
The key is the course name and the value is the number of credits.
Find the total number of credits taken this semester and assign it
to the variable credits.
"""

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

credits = 0
for course in Junior:
    credits = credits + Junior[course]
print(credits)
print("")


"""
Create the dictionary characters that shows each character from the 
string sally and its frequency. Then, find the most frequent letter 
based on the dictionary. Assign this letter to the variable best_char.
"""

sally = "sally sells sea shells by the sea shore"
characters = {}

# First create the dict 'characters'.
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1
print(characters)
print("")


# Then convert the dict into a list with the keys only.
# Duplicated letters will only be listed once.
char_lst = list(characters.keys())
print(char_lst)
print("")


# Assume the first letter in the list as the best character first.
best_char = char_lst[0]

# Comparing if the item value in characters dict is greater than the 
# value in best_char var. If yes, then the value in var item will replace
# value of var best_char.
for item in char_lst:
    if characters[item] > characters[best_char]:
        best_char = item
print(best_char)
print("")
