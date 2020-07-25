#!/usr/bin/env python3

# For items in mydict that has more than 3 characters in the key,
# add up their total values.

total = 0
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}

for akey in mydict:
    if len(akey) > 3:
        total = total + mydict[akey]

print(total)
