#!/usr/bin/env python3

"""
Using the re .findall() method to find all digits.
"""

import re

x = "My 2 favourite numbers are 19 and 42"
y = re.findall("[0-9]+", x)     # To find all digits.
print(y)    # We will get back a list of digits as strings.
print("")



"""
The repeat characters (* and +) push outward in both directions
(greedy) to match the largest possible string.
"""

import re

x = "From: Using the : character"
y = re.findall("^F.+:", x)  # The '+' sign before ':' pushes out further to look for the last ':'.
print(y)
print("")



"""
To find one or more characters but not greedy.
"""

import re

x = "From: Using the : character"
y = re.findall("^F.+?:", x)
print(y)
print("")



"""
Using the re .findall() method in string extraction.
"""

import re

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("\S+@\S+", x)    # '\S+' means at least one non-whitespace character.
print(y)
print("")



"""
Using the .find() method to extract the host or domain name.
"""

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

atpos = data.find("@")
print(atpos)

sppos = data.find(" ", atpos)
print(sppos)

host = data[atpos+1 : sppos]    # To find out the host name by using slicing
print(host)
print("")



"""
Using the double split pattern to extract the host or domain name.
"""

words = data.split()
print(words)

email = words[1]    # 1 is the second index in the words list.
print(email)

pieces = email.split("@")   # Split the pieces without the '@'.
print(pieces)   # Print out the email without the '@' in a list.
print(pieces[1])
print("")



"""
Now using regex to extract the host of domain name.
"""

import re

lin = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y2 = re.findall("@([^ ]*)", lin)
print(y2)
print("")
