#!/usr/bin/env python3

# To find the smallest number from a given list of numbers.

smallest = None

print("Before")

for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)

print("After", smallest)
