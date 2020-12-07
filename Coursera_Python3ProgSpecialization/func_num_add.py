#!/usr/bin/env python3

"""
Write a function called add that takes any number as its input
and returns that sum with 2 added.
"""

def add(num):
    return num + 2



"""
Write a function named total that takes a list of integers as input, 
and returns the total value of all those integers added together.
"""

def total(lst):
    sum = 0
    for num in lst:
        sum = sum + num
    return sum

lst = [1, 2, 3, 4]
print(total(lst))
print("")



# Write a function that adds three numbers.
def addNum(x, y, z):
    return (x + y + z)

print(addNum(3, 5, 4))
print("")
