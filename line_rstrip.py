#!/usr/bin/env python3

fhand = open("mbox-short.txt")

for line in fhand:
    line = line.rstrip()
    wds = line.split()
    # Guardian line a bit stronger so we set to 3
    # Guardian in a compound statement
    if len(wds) < 3 or wds[0] != "From" :
        continue
    print(wds[2])
