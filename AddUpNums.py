#!/usr/bin/env python3

# Add up numbers from 1 to a target number.

target = int(input("Enter a target number: "))
total = 0
nextNumberToAddIn = 1
while nextNumberToAddIn <= target:
    # add in the next value
    total = total + nextNumberToAddIn   # add in the next number
    print("Added in:", nextNumberToAddIn, "Total so far is:", total)
    nextNumberToAddIn = nextNumberToAddIn + 1

print("The sum of the numbers from 1 to", target, "is:", total)
