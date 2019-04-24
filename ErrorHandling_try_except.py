#!/usr/bin/env python3

import math

num = int(input("Please enter an integer: "))

try:
    print(math.sqrt(num))
except:
    print("Bad value for square root.")
    print("Changing num to a absolute value instead.")
    print(math.sqrt(abs(num)))

"""
If user enters a negative integer, line 12 calculation will
raise an error exception.
We can handle this error exception by calling the print
function within a 'try' block.
A corresponding 'except' block catches the exception and
prints a message back to the user in the event that an
exception occurs.
"""
