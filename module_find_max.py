#!/usr/bin/env python3

# Ensure that the file 'utils.py' is in the same working dir.
import utils    # Import the utils module without the .py file extension.
#from utils import find_max     # Or import only the find_max() method from the
                                # utils module.

numbers = [10, 3, 6, 2]         # Assign the var numbers with a list of numbers.
maximum = utils.find_max(numbers)   # From utils, get the attrib of the find_max()
                                    # method, pass in the numbers param and assign
                                    # it to var max.
print(maximum)  # Print out the var max.

