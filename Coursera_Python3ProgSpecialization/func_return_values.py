#!/usr/bin/env python3

def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
""" Using '.format()' method to print out the result with first
param var obj 'toSquare' and second var obj 'result'.
"""
print("The result of {} squared is {}.".format(toSquare, result))

print("")
