#!/usr/bin/env python3

import re

string = "Two too."

"""The regular expression matches a 't', followed by
an 'o' or a 'w', followed by an 'o'."""
m = re.findall("t[ow]o", string, re.IGNORECASE)

print(m)

