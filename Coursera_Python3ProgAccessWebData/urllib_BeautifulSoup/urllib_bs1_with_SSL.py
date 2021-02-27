#!/usr/bin/env python3

"""
To print out the anchor tags of a https SSL secured site.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificates errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
