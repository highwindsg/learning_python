#!/usr/bin/env python3

"""
Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.
"""

str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
c = list(str1)
# print(c)

numbs = 0   # initializing accumulator
for item in c:  # iterating
    numbs = numbs + 1   # updating accumulator

print(numbs)
print("")
