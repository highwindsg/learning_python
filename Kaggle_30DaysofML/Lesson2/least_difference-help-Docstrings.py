#!/usr/bin/env python3

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """

    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10), # Python allows trailing commas in argument lists.
    least_difference(5, 6, 7)
)
print("")



"""
Using the help() func to seek help to understand about a func you have forgotten.
help(function_name)
"""

#help(least_difference)
print("")



"""
Separating a print() func output with a 'sep=' param.
And ending a print() func output with a 'end=" "' by not going to a new line.
"""

print(1, 2, 3, sep=" < ")
print(4, 5, 6, end=" ")
#print("")
