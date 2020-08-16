#!/usr/bin/env python3

"""
Write two functions, one called addit and one called mult.
addit takes one number as an input and adds 5.
mult takes one number as an input, and multiplies that input
by whatever is returned by addit, and then returns the result.
"""

def addit(num):
    result = num + 5
    return result


def mult(num):
    result = num * addit(num)
    return result


print(addit(5))
print(mult(2))

print("")

""" What does this function print out? """

def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)

print("")
