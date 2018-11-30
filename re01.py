#!/usr/bin/env python3

# Search for lines that contains 'From'

import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From", line):
        print(line)
