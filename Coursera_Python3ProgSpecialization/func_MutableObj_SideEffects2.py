#!/usr/bin/env python3

"""
Global variables are another way to have side effects.
For example, we could make 'double' have a side effect on the
global variable y.
"""

def double(n):
    global y    # Taking the value of var y from global var.
    y = 2 * n


y = 5
double(y)
print(y)
print("")


"""
Side effects are sometimes convenient.
However, programs that have side effects can be very difficult
to debug. Wherever it is practical to do so, it is best to avoid
side effects. The way to avoid using side effects is to use
return values instead.
"""

def double_2(n):
    return 2 * n


y = 5
y = double_2(y)
print(y)

