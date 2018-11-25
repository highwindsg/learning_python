#!/usr/bin/env python3

# This program request user to enter the filenname and then counts
# the words and how many times in occurs. And then presents in a dictionary.

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
