#!/usr/bin/env python3

counts = dict()
names = ["cserv", "cwen", "xserv", "zqian", "cwen"]

for name in names:
    if name not in counts:
        counts[name] = 1    # Insert into dict 'counts' with index key var obj and value of 1,
                            # if the var obj name is not found in a given names list.
    else:
        counts[name] += 1   # But if already found, then add 1 to increment the counts dict.

print(counts)
