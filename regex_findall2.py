#!/usr/bin/env python3

# Import the regular expression module named 're'.
import re

l = "Beautiful is better than ugly."

"""
From 're' module, uses the 'findall' method and passes
in a param of a word, then a string and it returns a
list with all the items in the string that the pattern
matches.
You can ignore case-sensitive in the 'findall' method by
passing in 're.IGNORECASE' to the 'findall' method as
the third param.
"""
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

