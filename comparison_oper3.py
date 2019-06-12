#!/usr/bin/env python3

weight = int(input("Weight: ")) # To do maths calculation, the var must be
                                # in integer format. So int is use to convert it.
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45   # weight var as int can then be multiplied.
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

