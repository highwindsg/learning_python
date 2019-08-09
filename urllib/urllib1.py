#!/usr/bin/env python3

# Run this program in its own sub-folder.

import urllib.request, urllib.parse, urllib.error

# Request to open a URL of 'http://data....' from the 'urllib' library, and assign it to var 'fhand'.
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

# For every line in var 'fhand' which is the URL content, print out the content line by line
# using the .decode() in case of any particular character set within, and .strip() method.
for line in fhand:
    print(line.decode().strip())
