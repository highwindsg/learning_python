#!/usr/bin/env python3

"""
Earlier on we created a python file 'useful_tools.py' and saved it in the same
working dir. Now for the new program below that is in the same dir, we can import
the useful_tools.py as a module. This is so that we can use the variables and
functions that are already created in it.
"""

# Import var and func created in useful_tools.py as module 'useful_tools'.
# Module name must be the same name as the python file, without the extention.
import useful_tools

# From module 'useful_tools', get the roll_dice() func and parse in param 10.
print(useful_tools.roll_dice(10))

