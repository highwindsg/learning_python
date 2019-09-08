#!/usr/bin/env python3

# Python exceptions.
""" An exception is an unexpected event, which occurs during the execution of a program,
that disrupts the normal flow of the program.
"""

result = None   # Set var 'result' to 'None' first.
a = float(input("Number 1: "))
b = float(input("Number 2: "))

try:
    result = a / b
except Exception as e:      # Use the 'Exception' class to output error to var 'e'.
    print("Error = ", type(e))      # Print out the 'type' of error 'e'.
else:
    print("__else__")
finally:                    # The 'finally' statement will execute even if you think the error happens or not.
    print("__finally__")


print("Result = ", result)
print("End")
