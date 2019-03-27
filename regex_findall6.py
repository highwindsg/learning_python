#!/usr/bin/env python3

# import the regular expression module 're'.
import re

# assign the string to a var 't'.
t = "__one__ __two__ __three__"

"""
Use the findall() method in regular expression and pass in
the first param to match on the first double underscore
and the last underscore with .*? in between, and then to
match them in the second param of 't'.
"""
found = re.findall("__.*?__", t)

for match in found:
    print(match)

