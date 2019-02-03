#!/usr/bin/env python3

def squared(x):
    """
    The line below will
    calculate the square of
    whatever that is parsed
    into x.
    And then it will return
    the answer to the
    square function.
    """
    return x**2 

num = int(input("Enter an integer number: "))
print(num, "after squared is", squared(num))

