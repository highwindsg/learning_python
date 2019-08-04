#!/usr/bin/env python3

import re   # Importing the regular express 're' module.

hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From:", line):    # From 're' module, use the .search() method to search for 'From:' from 'line'.
        print(line)
