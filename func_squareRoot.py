#!/usr/bin/env python3

def squareRoot(x):
    """
    Below line will parse in
    whatever number is for x, and
    will calculate the square root
    and finally return the answer
    back to the function squareRoot.
    """
    return x**(1/2)

num = int(input("Enter an integer number: "))
print(num, "after square root is", squareRoot(num))

