#!/usr/bin/env python3

"""
Supplying functions as arguments to other functions.
"""

def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep="\n" # '\n' is a newline character - it starts a new line.
)
#print("")



"""
Passing in a function using the optional keyword 'key=' argument, when doing
a function call.
"""

def mod_5(x):
    """Return the remainder of x afrer dividing by 5"""
    return x % 5


print(
    "Which number is biggest?",
    max(100, 51, 14),
    "Which number is the biggest modulo 5?",
    max(100, 51, 14, key=mod_5), # Passing in the func 'mod_5()' as an optional arg.
    sep="\n"
)
print("")
