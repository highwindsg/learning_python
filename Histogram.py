#!/usr/bin/env python3

# Get the name of the file and open it.
name = input("Enter the filename: ") # Enter the full txt filename with extension.
handle = open(name, "r")            # Open the file in read mode and assign to var 'handle')

# Count word frequency.
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# All done
print(bigword, bigcount)
