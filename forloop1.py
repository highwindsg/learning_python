#!/usr/bin/env python3

A = [0, 1, 2, 3, 4, 5]  # A list
B = (0, 1, 2, 3, 4, 5)  # A tuple
C = {0, 1, 2, 3, 4, 5}  # A set
D = "012345"            # A string
E = {                   # A dictionary
    "name": "Max",
    "age": "20"
    }


for x in A:
    print(x)
print("")

for key, value in E.items():
    print(key, "", value)
print("")

for x in range(2,5):    # From 2 until 5, but not inclusive of 5.
    print(x)
print("")

for x in range(2,30,3): # From 2 until 30, but not inclusive of 30, and by step of 3.
    print(x)
else:
    print("Finished.")
print("")

