#!/usr/bin/env python3
# Search for lines that have an at '@' sign between characters

import re

hand = open("mbox-short.txt")
#hand = open("mbox.txt")

for line in hand:
    line = line.rstrip()
    x = re.findall("\S+@\S+", line)
    if len(x) > 0:
        print(x)

hand.close()