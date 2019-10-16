#!/usr/bin/env python3

"""
Lambda Expressions

e.g.
lambda : Expression
lambda x: 3*x + 1
lambda x, y: (x*y)**0.5     # Geometric Mean
lambda x, y, z: 3/(1/x + 1/y + 1/z)     # Harmonic Mean
lambda x1, x2, ..., xn: <expression>
and more ...

The expression is the return value, and in a lambda there can only be one expression, and not multiple expressions.
"""

# Write a func to compute 3x+1
def f(x):
    return 3 * x + 1


print(f(2))  # Func call with param 2.
print("")

# To write in a lambda or anonymous function.
f = lambda x: 3 * x + 1
print(f(2))
print("")

# To combine first name and last name into a single "Full Name" and using the .strip() and .title() method to remove
# empty white space and set first letter as uppercase.
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("  leohard", "FULLER"))
