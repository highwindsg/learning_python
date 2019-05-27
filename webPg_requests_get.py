#!/usr/bin/env python3

"""
The requests module lets you easily download files from the Web without
having to worry about complicated issues such as network errors,
connection problems, and data compression.
"""
import requests

# Create a var 'res' (eg. means response) and set it to use the
# .get method from the requests module, and parse in the URL params.
res = requests.get("http://automatetheboringstuff.com/files/rj.txt")

# Print out to see what is the data type of var 'res'.
print(type(res))

# Print out to see what is the total length of the entire text file
# without downloading the entire text file completely.
print(len(res.text))

# Print out the first 250 characters from the text in var 'res'.
print(res.text[:250])

