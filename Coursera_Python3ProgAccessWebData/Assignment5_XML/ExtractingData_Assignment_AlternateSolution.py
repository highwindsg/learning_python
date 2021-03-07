#!/usr/bin/env python3

"""
Alternate solution.

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


import urllib.request as ur
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
print("Retrieving ...", url)
xml = ur.urlopen(url).read()
print("Retrieved", len(xml), "characters")

tree = ET.fromstring(xml)
counts = tree.findall(".//count")

total_number = 0    # Initialize a counting total number accumulator to 0 first.
sum = 0 # Initialize the sum to accumulator to 0 first.

for item in counts:
    print(type(item.text), item.text)
    sum += int(item.text)   # To add/sum up the text, needs to convert it into integer first.
    total_number += 1
    
print("Count: ", total_number)
print("Sum: ", sum)
print("")
