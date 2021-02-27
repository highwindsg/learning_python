#!/usr/bin/env python3

# Import module 'urllib' with functions of .request, parse and error.
import urllib.request, urllib.parse, urllib.error

# From 'urllib' module, use the '.request' func and use the '.urlopen()' and
# parse in the URL to the webpage content.
file = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict() # Create and empty counts dictionary.
#print(counts)

for line in file:   # For every line in 'file',
    words = line.decode().split()   # decode it and split it, then assign the values to var 'words'.
    for word in words:  # For every word item in 'words',
        counts[word] = counts.get(word, 0) + 1  # use the '.get()' method and parse in the argument
        # of the word item if it has been counted before, and increase by 1. And assign that word item
        # top the counts dict.
        
print(counts)   # Print out the 'counts' dict.
print("")
