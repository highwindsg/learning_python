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
print("")

"""
Creating a closures func to calculate the power of a given base number.
"""
def nth_power(exponent):    # Define an outer func named 'nth_power()' with param 'exponent'.
    def pow_of(base):       # Define an inner func named 'pow_of()' with param 'base'.
        return pow(base, exponent)  # Use the built-in func of pow() to calculate with 'base' and
                                    # 'exponent' value, and return the answer to the inner func 'pow_of()'.
    return pow_of       # Then finally return the value of 'pow_of' without parenthesis to the outer func.

square = nth_power(2)   # Passing the exponent value of '2' into the func 'nth_power()', and assigning to var 'square'.
print(square(2))        # Print the answer of square 2 to the power of 2.
print(square(3))        # Print the answer of square 3 to the power of 2.
print(square(4))        # Print the answer of square 4 to the power of 2.
print(square(5))        # Print the answer of square 5 to the power of 2.

cube = nth_power(3)     # Passing the exponent value of '3' into the func 'nth_power()', and assigning to the var 'cube'.
print(cube(2))      # Print the answer of cube 2 to the power of 3.
print(cube(3))      # Print the answer of cube 3 to the power of 3.
print(cube(4))      # Print the answer of cube 4 to the power of 3.
print(cube(5))      # Print the answer of cube 5 to the power of 3.
