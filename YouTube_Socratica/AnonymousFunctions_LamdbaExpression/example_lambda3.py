#!/usr/bin/env python3

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a * x ** 2 + b * x + c


f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))
print("")

print(build_quadratic_function(3, 0, 1)(2))    # 3x^2 + 1 evaluated for x = 2
