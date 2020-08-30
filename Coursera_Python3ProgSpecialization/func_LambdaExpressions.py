#!/usr/bin/env python3

def f(x):
    return x - 1

print(f)
print(type(f))
print(f(3))
print("")

# To re-write the func f(x) in lambda expression:
print(lambda x: x-1)    # No return statemt is needs as it is implicit.
                        # Whatever is placed after the colon ':', will be returned.
lf = lambda x: x-1  # Assign the lambda func 'x' into var 'lf'.
print(type(lf))
print(lf(3))
print("")


"""
Convert the 'last_char()' func into a lambda func.
"""

def last_char(s):
    return s[-1]

last_char = lambda s: s[-1]
print(type(last_char))
print("")


"""
If the input to the lambda func below is a number (either positive
or negative), what is returned?
"""

f1 = (lambda x: -x)
print(f1(5))
print(f1(-5))
print("")

print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(6))   # lambda func call with param vallue 6.
print("")


"""
Create a lambda function that takes a string and returns the last
character in that string.
"""

last_char1 = (lambda s: s[-1])  # Assign lambda func to a var.
print(
    (last_char1)("Hello there everyone")    # Lambda func var call with a str.
    )
print("")
