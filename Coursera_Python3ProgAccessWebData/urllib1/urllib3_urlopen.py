#!/usr/bin/env python3

"""
To print out the content of a non https webpage.
"""

# Import the module 'urllib' and functions '.request', '.parse', '.error'.
import urllib.request, urllib.parse, urllib.error

# Using the '.urlopen()' method from module func of 'urllib.request', parse in
# the URL webpage address. Then assign the values to var 'file'.
file = urllib.request.urlopen("http://www.dr-chuck.com/page1.html")

for line in file:   # For every line item in var 'file',
    print(line.decode().strip())    # use the .decode() and .strip() methods on
    # every line and print them out.
    
print("")
