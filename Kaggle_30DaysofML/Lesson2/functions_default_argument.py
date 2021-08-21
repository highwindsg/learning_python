#!/usr/bin/env python3

"""
Adding optional arguments with default values to the functions.
"""

# Creating a func named 'greet()' with at least one default mandatory argument.
def greet(who="Colin"):
    print("Hello, ", who)
    

greet()
greet(who="Kaggle")
# In this case next below, we don't need to spedify the name of the argument,
# because it's unambiguous.
greet("world")
print("")
