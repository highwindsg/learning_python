#!/usr/bin/env python3

fhand = open("mbox-short.txt")

# Use the .startswith() method to only print out lines that starts with 'From:'.
for line in fhand:
    line = line.rstrip()        # Strip away the empty white spaces on the right side.
    if not "@uct.ac.za" in line:    # This means that if the quoted string is not found in line,
        continue                    # then continue next line to find the quoted string.
    print(line)

