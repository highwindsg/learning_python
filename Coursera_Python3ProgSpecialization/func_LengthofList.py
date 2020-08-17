#!/usr/bin/env python3

"""
Write a function, length, that takes in a list as the input.
If the length of the list is greater than or equal to 5,
return “Longer than 5”. If the length is less than 5,
return “Less than 5”.
"""

def length(lst):
    if len(lst) >= 5:
        Ans = "Longer than 5"
    else:
        Ans = "Less than 5"
    return Ans


list1 = "Today is a godod day to win."
print(length(list1))
