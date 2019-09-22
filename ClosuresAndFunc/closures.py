#!/usr/bin/env python3

# Using nested funcs and closures in Python.

# Defining a func in a func.
# Therefore the outerFunction() is an enclosing function.
def outerFunction(text):    # The 'outerFunction()' takes 'text' as an argument param.
    def innerFunction():    # Another local func of the 'outerFunction()' that prints the text param.
        print(text)
    innerFunction()

outerFunction("Hello")

""" Therefore if you define a function inside another function, it is called the nesting of function. """
