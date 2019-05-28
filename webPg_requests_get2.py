#!/usr/bin/env python3

"""
To download a file from the URL and save it with another filename.
"""

import requests

# Create var 'res' (eg. means response) and set it to using the .get method
# from the 'requests' module, with param of URL to the file.
res = requests.get("http://automatetheboringstuff.com/files/rj.txt")

# To check if the download will be successful by calling the
# 'raise_for_status()' method of the 'res' var obj. The program will then
# stop if some unexpected error happens.
res.raise_for_status()

# Create a 'playFile' var and set it to use the 'open()' func and params
# of a new filename with 'wb' (write binary) mode.
playFile = open("RomeoAndJuliet.txt", "wb")

# Using the '.iter_content()' method, pass in 100000 bytes of data
# per chunk size on each iteration through the loop.
for chunk in res.iter_content(100000):
    playFile.write(chunk)   # Then call the 'playFile' var obj and use
                            # the .write() method and pass in the param of
                            # the chunk data.

playFile.close()

"""
To review, here’s the complete process for downloading and saving a file:

1. Call requests.get() to download the file.
2. Call open() with 'wb' to create a new file in write binary mode.
3. Loop over the Response object’s iter_content() method.
4. Call write() on each iteration to write the content to the file.
5. Call close() to close the file.”

You can learn about the requests module’s other features from
http://requests.readthedocs.org/.
"""

