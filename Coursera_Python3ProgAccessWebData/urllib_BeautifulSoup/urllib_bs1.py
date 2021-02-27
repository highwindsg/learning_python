#!/usr/bin/env python3

"""
To print out the anchor tags of a non https webpage.
"""


# Import module 'urllib' and its functions. eg. '.request', '.parse', .'error'.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup   # From module 'bs4', import 'BeautifulSoup' function.

url = input("Enter URL: ")  # Enter the input for URL and assign in to the var 'url'.
html = urllib.request.urlopen(url).read()   # Using the .urlopen() method, parse in the
# url values, and read it using the .read() method.
soup = BeautifulSoup(html, "html.parser")   # Using the 'BeautifulSoup()

# Retrieve all of the anchor tags.
tags = soup("a")
print(tags)
print("")

for tag in tags:
    print(tag.get("href", None))
    
print("")

"""
When prompted to enter the URL, type in http://www.dr-chuck.com/page1.htm
You should get a return reply of http://www.dr-chuck.com/page2.htm
"""
