#!/usr/bin/env python3

"""
We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1173586.xml (Sum ends with 10)

You do not need to save these files to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

Task: You are to look through all the <comment> tags and find the <count> values sum the numbers. 

To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML 
for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')

Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. 
You could also work from the top of the XML down to the comments node and then loop through the child nodes of 
the comments node.
"""


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL to the xml file: ")
# From the urllib.request module, use the .urlopen() method and parse in var obj url with the ctx context.
uh = urllib.request.urlopen(url, context = ctx)
# Read the entire 'uh' content and assign it to var 'data'.
data = uh.read()
print(data)
print("")
# From the xml elementtree, use the .fromstring() method and parse in the var obj 'data',
# and assign the values to 'tree'.
tree = ET.fromstring(data)
results = tree.findall("comments/comment")

count = 0
sum = 0

for item in results:
    x = int(item.find("count").text)
    sum = sum + x
    count += 1
    
print("Count: ", count)
print("Sum: ", sum)
print("")
