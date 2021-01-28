#!/usr/bin/env python3

"""
Create a list of numbers 0 through 40 and assign this list to the variable numbers. 
Then, accumulate the total of the list’s values and assign that sum to the variable sum1.
"""

numbers = list(range(0, 41))
# print(numbers)

sum1 = 0
for item in numbers:
    sum1 = sum1 + item

print(sum1)
print("")
