#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen("http://www.dr-chuck.com/page1.html")

for line in file:
    print(line.decode().strip())
    
print("")
