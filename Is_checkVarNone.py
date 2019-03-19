#!/usr/bin/env python3

# Use the 'is' keyword to check if a variable is None.

x = 10
if x is None:
    print("x is None :( ")
else:
    print("x is not None")
print(type(x))

x = None
if x is None:
    print("x is None :( ")
else:
    print("x is not None")
print(type(x))
