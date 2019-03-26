#!/usr/bin/env python3

import re

line = "123?34 hello?"

# The first param '\d' matches only digits in a string
# and output them to a list.
m = re.findall("\d", line, re.IGNORECASE)

print(m)

