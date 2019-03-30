#!/usr/bin/env python3

# Come up with a regular expression that matches all the digits in the string
# 'Arizona 479, 501, 870. California 209, 213, 650'.

import re

string = "Arizona 479, 501, 870. California 209, 213, 650"

matches = re.findall("\d", string)  # '\d' is meant for numeric digits only.

print(matches)
"""
Or alternatively just enter the line below in command line eg.
$ echo Arizona: 479, 501, 870. California: 209, 213, 650. | grep [[:digit:]]
"""
