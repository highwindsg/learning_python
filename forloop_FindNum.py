#!/usr/bin/env python3

# To find the number 3 from a given list, and setting the value from False to True after 3 is found.

found = False

print("Before", found)

for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found, value)

print("After", value, found)
