#!/usr/bin/env python3

# https://www.py4e.com/html3/05-iterations

largest = None  # Declare largest as None first.
print("Before:", largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print("Loop", itervar, largest)
print("Largest number is:", largest)
print("")

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest :
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest number is:", smallest)

