#!/usr/bin/env python3

"""
The basic outline of this problem is to read the file, look for integers using the 're.findall()' method, 
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers 
and summing up the integers.
"""

import re

file = open("regex_sum_1173582.txt")
numlist = list()

for line in file:
    # For every line in 'file' text, pick out the numbers using '.re.findall()' method,
    # and assign it to the var 'num' list.
    num = re.findall("[0-9]+", line)
    # Insert the 'num' list value to the 'numlist' var list.
    numlist = numlist + num
print(numlist)
    
sum = 0     # Initialize var sum total to 0 first.

for item in numlist:
    sum = sum + int(item)   # Converting the string item to integer as so to do addition.

print(sum)



"""
An alternate two-liner verson using list comprehension can also be done.
Hint below.
"""

#import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
