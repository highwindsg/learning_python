#!/usr/bin/env python3

fhand = open("mbox-short.txt")

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
print(words)
print(words[2])
