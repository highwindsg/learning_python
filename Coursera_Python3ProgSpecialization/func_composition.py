#!/usr/bin/env python3

def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a+b+c

a = -5
b = 2
c = 10
result = sum_of_squares(a, b, c)
print(result)
print("")



"""
What are the possible types of variable z?
"""

def cyu3(x, y, z):
   if x - y > 0:
      return y -2
   else:
      z.append(y)
      return x + 3

""" Ans: List. Because append can be performed on lists. """
