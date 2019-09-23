#!/usr/bin/env python3

"""
A closures is a function whose return value depends on the value of one or more var which are declared
outside the function.
"""
# Example of a closure.
def outerFunction(text):    # The 'text' var param is declared outside of the innerFunction().
    def innerFunction():    # So the value of the innerFunction() depends on the value of 'text' var that
                            # is declared outside of the inner func. And that makes it a closure.
        print(text)
    return innerFunction    # Return the innerFunction without any parenthesis ().

# Because the outer func is returning the inner func, that means now 'a' contains the inner func.
a = outerFunction("Hello")

# We will try deleting the outerFunction.
del outerFunction

# Because we have created in line 15 the var 'a' that contains the inner func, we can still use 'a()'
# as the inner func.
a()      # Client call the 'a()' inner func that prints the text var param.

"""
This means var 'a' is storing the state of the inner function even if the outer function is deleted.
And that is the magic of the closures.
A closures function is able to remember the values (eg. text) which are declared outside the function.
"""