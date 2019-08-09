#!/usr/bin/env python3

# To find out how many repeated words in a file.

import urllib.request, urllib.parse, urllib.error

# Request to open a URL 'http://...' using the 'urllib' library and assign it to var 'fhand'.
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()     # Create a counts dictionary.

for line in fhand:                  # For every line in 'fhand',
    words = line.decode().split()   # use the .decode() method in case of any character set and .split() method,
                                    # and assign it to var 'word'.
    for word in words:                          # For every individual word in var 'words',
        counts[word] = counts.get(word, 0) + 1  # use the .get() method to get the repeated word count by adding 1,
                                                # and assign it to 'counts' index.
print(counts)   # Print the dictionary.
