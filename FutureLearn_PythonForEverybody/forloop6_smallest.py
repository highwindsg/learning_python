#!/usr/bin/env python3

# https://www.futurelearn.com/courses/programming-for-everybody-python/3/steps/723011

smallest = None # None is a flag value.
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:    # is - a operator used in a logical expression.
        smallest = value    # Grab the first value as the smallest first.
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)

