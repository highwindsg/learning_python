#!/usr/bin/env python3

fhand = open("mbox-short.txt")

# Use the .startswith() method to only print out lines that starts with 'From:'.
for line in fhand:
    line = line.rstrip()        # Strip away the empty white spaces on the right side.
    if line.startswith("From:"):
        print(line)
