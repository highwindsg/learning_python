#!/usr/bin/env python3

"""
To list out all the email addresses using the .find() method and using 'From:' as
criteria.
"""

print("Using .find() method:")
file1 = open("mbox-short.txt")

for line in file1:
    line = line.rstrip()
    if line.find("From:") >= 0:
        print(line)
        
print("")
        


"""
Now using regex by importing re. and using the .search() method from re module.
"""

import re

print("Using re .search() method:")
file2 = open("mbox-short.txt")

for line in file2:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
        
print("")



"""
Using the .startswith() method.
"""

print("Using .startswith() method:")
file3 = open("mbox-short.txt")

for line in file3:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
        
print("")



"""
Now using regex ny importing re. and using .search() method from re module.
"""

import re

print("Now again using re .search() method.")
file4 = open("mbox-short.txt")

for line in file4:
    line = line.rstrip()
    if re.search("^From:", line):   # '^' means matches the beginning of the line.
        print(line)
        
print("")



"""
Using regex and find numbers with decicals.
"""

import re

file = open("mbox-short.txt")
numlist = list()

for line in file:
    line = line.rstrip()
    stuff = re.findall("X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print("Maximum:", max(numlist))
print("")



"""
If you want a special regular expression character to just behave normally, use a back slash '\'.
"""

import re

x3 = "We just received $10.00 for cookies."
y3 = re.findall("\$[0-9.]+", x3)
print(y3)
print("")

