#!/usr/bin/env python3

# Below script will convert European lift numbers to US lift numbers.
# For exmaple, level 0 in Europe in level 1 in US.

inp = input("Europe floor?")
usf = int(inp) + 1          # Converting the input str value to int value, as input will always be in a string.
print("US floor", usf)
