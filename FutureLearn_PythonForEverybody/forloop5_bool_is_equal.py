#!/usr/bin/env python3

# https://www.futurelearn.com/courses/programming-for-everybody-python/3/steps/723011

found = False
print("Before", found)
for value in [9, 413, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After", found)

