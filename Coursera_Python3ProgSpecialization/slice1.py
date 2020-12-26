#!/usr/bin/env python3

# A substring of a string is called a slice.
# Selecting a slice is similar to selecting a character:

singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])
print("")


# If you omit the first index (before the colon), the slice 
# starts at the beginning of the string. If you omit the 
# second index, the slice goes to the end of the string.

fruit = "banana"
print(fruit[:3])
print(fruit[3:])
print("")


# What is printed by the following statements?

alist = [3, 67, "cat", [56, 57, "dog"], [], 3.14, False]
print(alist[4:])
print("")


# What is printed by the following statements?

L = [0.34, "6", "SI106", "Python", -2]
print(len(L[1:-1]))
print("")


# Create a new list using the 9th through 12th elements 
# (four items in all) of new_lst and assign it to the variable 
# sub_lst.

new_lst = [
    "computer", 
    "luxurious", 
    "basket", 
    "crime", 
    0, 
    2.49, 
    "institution", 
    "slice", 
    "sun", 
    ["water", "air", "fire", "earth"], 
    "games", 
    2.7, 
    "code", 
    "java", 
    ["birthday", "celebration", 1817, "party", "cake", 5], 
    "rain", 
    "thunderstorm", 
    "top down"
    ]

sub_lst = new_lst[8:12]
print(sub_lst)
print("")
