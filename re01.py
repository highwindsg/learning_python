#!/usr/bin/env python3

# Search for lines that contains 'From'

import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From", line):     # From 're' module, use the 'search' method to find
        print(line)                 # lines that starts with 'From' and print then out.

 # The above program doesn't use the real power of regular expressions, since it can also
 # be done easily by using the 'line.find()' to accomplish the same result.
