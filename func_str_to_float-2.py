#!/usr/bin/env python3

## Optional textbook answer.
## Write a function that converts a string to a float and returns the result.
## Use exception handling to catch the exception that could occur.

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)

