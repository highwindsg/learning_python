#!/usr/bin/env python3

x = [1, 2, 3]

def add_to_each():
    for i in range(3):
        x[i] += 1   # For every item in x, increase by 1.
    return i

i = add_to_each()   # Print out the first instance of i, in this first func call.

print(x)
print(i)
