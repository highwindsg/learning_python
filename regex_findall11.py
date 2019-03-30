#!/usr/bin/env python3

# Import the regular expression 're' module.
import re

# Find the word that have 'oo' in it and pass it to the var 'matches'.
matches = re.findall(".oo", "The ghost that says boo haunts the loo.")

# Call the print function on var 'matches'.
print(matches)
