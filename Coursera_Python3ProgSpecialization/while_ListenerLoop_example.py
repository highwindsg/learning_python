#!/usr/bin/env python3

theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)
print("")
# Note that zero is a sentinel value used to signal the end of the loop.
