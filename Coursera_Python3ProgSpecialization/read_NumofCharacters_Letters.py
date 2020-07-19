#!/usr/bin/env python3

# Using the file school_prompt2.txt, find the number of characters or letters 
# in the file and assign that value to the variable num_char.

f = open("school_prompt2.txt")
text = f.read()
num_char = len(text)
print(num_char)

# https://pythonexamples.org/python-count-number-of-characters-in-text-file/

