#!/usr/bin/env python3

"""
Swapping Values between Variables.
This feature is used to enable swapping the values of two
variables. With conventional assignment statements, we have to
use a temporary variable. For example, to swap a and b:
"""

a = 1
b = 2
temp = a
print(temp)
a = b
print(a)
b = temp
print(b)
print(a, b, temp)

print("")

""" Tuple assignment solves this problem neatly: """

a = 1
b = 2
(a, b) = (b, a)
print(a, b)

print("")
