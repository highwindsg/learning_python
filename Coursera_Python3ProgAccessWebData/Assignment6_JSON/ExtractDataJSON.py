#!/usr/bin/env python3

"""
The program will prompt for a URL, read the JSON data from that URL using urllib 
and then parse and extract the comment count from the JSON data, 
compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1173587.json (Sum ends with 67)

You do not need to save these files to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
"""

import urllib.request, urllib.parse, urllib.error
import json



url = input("Enter JSON URL: ")

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

info = json.loads(data)
Count = 0
Sum = 0

for item in info["comments"]:
    print(item["count"])
    number = int(item["count"])
    Sum = Sum + number


print("Sum: ", Sum)
print("")
