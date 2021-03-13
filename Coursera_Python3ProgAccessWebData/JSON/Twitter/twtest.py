#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

print("* Calling Twitter...")
url = augment("https://api.twitter.com/1.1/statuses/user_timeline.json",
              {"screen_name": "drchuck",
               "count": "2"}
              )
print(url)

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context = ctx) # Shut off the SSL cert checking.
data = connection.read()
print(data)

headers = dict(connection.getheaders())
print(headers)
print("")
