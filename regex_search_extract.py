#!/usr/bin/env python3

import re

x = "My 2 favourite numbers are 19 and 42"
y = re.findall("[0-9]+", x)     # the template '[0-9]+' will find all numbers ranging
                                # from 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9, '+' one or more.
print(y)

y2 = re.findall("[AEIOU]+", x)  # now the template '[AEIOU]+' will only search all
                                # upper case letters that matches, '+' one or more.
print(y2)   # The output will be an empty list as none of the search criteria matches.

