#!/usr/bin/env python3

# Find the number of lines in the file, travel_plans2.txt, and assign it to
# the variable num_lines.

f = open("travel_plans2.txt")
num_lines = len(f.readlines())
print(num_lines)

# Read more at https://pythonexamples.org/python-file-operations/

