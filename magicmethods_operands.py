#!/usr/bin/env python3

"""
Operands in an expression must have a magic method the operator can use
to evaluate the expressions. For example, in the expression 2 + 2, each
integer object has a magic method called __add__ that Python calls when
it evaluates the expression. If you define an __add__ method in a class,
you can use the object it creates as operands in an expression with the
addition operator.

In computer programming, an operand is a term used to describe any
object that is capable of being manipulated. For example, in "1 + 2"
the "1" and "2" are the operands and the plus symbol is the operator.
"""
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        # Returns the absolute value of a number as positive always.
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)
