#!/usr/bin/env python3

import math

num = int(input("Please enter an integer: "))

if num < 0:
    raise RuntimeError("You can't use a negative number.")
else:
    print(math.sqrt(num))

"""
It is also possible for a programmer to cause a runtime exception
by using the 'raise' statement.
For example, instead of calling the square root function with a
negative number, we could have checked the value first and then
raised our own exception.
Note that the program would still terminate but now the exception
that caused the termination is something explicitly created by
the programmer.
"""
