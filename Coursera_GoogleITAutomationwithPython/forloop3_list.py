#!/usr/bin/env python3

values = [23, 52, 59, 37, 48]
sum = 0 # Initialize a accumulator var of 'sum'.
length = 0  # Initialize a accumulator var of 'length'.

for value in values:
    sum += value
    length += 1
    
print("Total sum: " + str(sum) + " - Average: " + str(sum / length))
print("")



"""
Note: A for loop works well when you want to iterate over a sequence of elements.
"""
