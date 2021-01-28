#!/usr/bin/env python3

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0   # initializing

for item in nums:   # iterating
    accum = accum + item    # updating

print(accum)
print("")



"""
Write code to create a list of integers from 0 through 52 and assign that list 
to the variable numbers. You should use a special Python function – do not type 
out the whole list yourself. HINT: You can do this in one line of code!
"""

numbers = list(range(0, 53))
print(numbers)
print("")
