#!/usr/bin/env python3

# To print the ten most common words from the text 'romeo-full.txt',
# and display the word used most to the word least used.

import string

fhand = open("romeo-full.txt")
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

