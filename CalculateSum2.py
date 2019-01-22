#!/usr/bin/env python3

def calculateSum(target):
    total = 0
    nextNumberToAddIn = 1
    while nextNumberToAddIn <= target:
        # add in the next value
        total = total + nextNumberToAddIn
        # increment
        nextNumberToAddIn = nextNumberToAddIn + 1
    return total

nTimes = 0  # initialize a counter
while nTimes < 3:   # To run a certain number of times.
    usersTarget = int(input("Enter a target number: "))
    thisTotal = calculateSum(usersTarget)
    print("The sum of the numbers 1 to", usersTarget, "is:", thisTotal)
    nTimes = nTimes + 1     # increment the counter

print("OK Bye")
