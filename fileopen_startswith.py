#!/usr/bin/env python3

fhand = open("mbox-short.txt")

# Use the .startswith() method to only print out lines that starts with 'From:'.
for line in fhand:
    if line.startswith("From:"):
        print(line)
