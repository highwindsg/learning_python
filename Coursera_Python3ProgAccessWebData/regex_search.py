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
