#!/usr/bin/env python3

# In order to print the keys in sorted alphabetical order, first must make a list of the keys
# in the dictionary using the keys method available in the dictionary objects.

counts = {
        "chuck" : 1,
        "annie" : 42,
        "jan" : 100
}

lst = list(counts.keys())
print(lst)

# And then sort that list and loop through the sorted list, looking up each key and
# printing out key-value pairs in sorted order.

lst.sort()
for key in lst:
    print(key, counts[key])
