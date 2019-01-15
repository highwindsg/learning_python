#!/usr/bin/env python3

# Write a program that contains a function called isEven.
# The function is passed one numeric (integer) parameter.

# First function to determine if numeric is divisible by 2 so that it is even.
def isEven(num):
    if num % 2 == 0:    # mod 2 checks if num divisible by 2 gives remainder 0.
        num = True
    else:
        num = False
    return num

# Second intermediate function that checks for numeric is even, then prints result.
def printresult(aNum):
    theResult = isEven(aNum)    # Calling the 'isEven' function that checks if
                                # numeric is even or not. Then pass it to the
                                # 'printresult' function.
    if theResult is True:       # 'is True' is redundant. but easier to read.
        print(aNum, "is even.")
    else:
        print(aNum, "is odd.")

# Test cases.
printresult(8)
printresult(-9)

# Alternatively, get user input.
userinput = float(input("Enter a numeric: "))
printresult(userinput)
