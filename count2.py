#!/usr/bin/env python3

# This program request user to enter the filenname and then counts
# the words and how many times it occurs. And then presents in a sorted dictionary.

import string

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
#print(counts)
