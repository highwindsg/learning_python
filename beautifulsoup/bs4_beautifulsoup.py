#!/usr/bin/env python3

# Using the BeautifulSoup module to do web URL scraping.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup   # Import BeautifulSoup module from bs4 library.

url = input("Enter URL - ")                 # Ask user to enter the full URL and pass it to var 'url'.
html = urllib.request.urlopen(url).read()   # Open the var 'url' and read the content, and pass it to var 'html'.
soup = BeautifulSoup(html, "html.parser")   # Using BeautifulSoup() method, pass in two params of 'html' var and
                                            # the 'html.parser' var.

# Retrieve all of the anchor tags.
tags = soup("a")    # From soup, get the 'a' which is the URL anchor tag, and assign it to var 'tags'.
for tag in tags:    # Loop through the 'a' anchor tag in var 'tags',
    print(tag.get("href", None))    # and print out the href hypertext reference.