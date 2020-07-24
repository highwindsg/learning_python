#!/usr/bin/env python3

# Using the file school_prompt2.txt, find the number of characters or letters 
# in the file and assign that value to the variable num_char.

f = open("school_prompt2.txt", "r")
text = f.read()
num_char = len(text)
print(num_char)

# https://pythonexamples.org/python-count-number-of-characters-in-text-file/

print("")

# Using the file school_prompt2.txt, find the number of words 
# in the file and assign that value to the variable num_char.

file = open("school_prompt2.txt", "r")
data = file.read()
words = data.split()
num_words = len(words)
print(num_words)

print("")
