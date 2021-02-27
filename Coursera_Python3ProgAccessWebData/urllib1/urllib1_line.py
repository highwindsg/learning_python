#!/usr/env python3

# Import the functions from 'urllib module - request, parse, error'.
import urllib.request, urllib.parse, urllib.error

# From urllib module's request func, use the '.urlopen()' method to parse in the URL to the web content,
# and assign the values to var 'fhand'.
file = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in file:   # For every line in var 'file',
    print(line.decode())    # print out the line by decoding it using the '.decode()' method.

print("")

