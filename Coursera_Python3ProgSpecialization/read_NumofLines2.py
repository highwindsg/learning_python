#!/usr/bin/env python3

"""
Write code to find out how many lines are in the file
'emotion_words.txt'.
Save this value to the variable 'num_lines'.
Do not use the 'len' method.
"""

emotionfile = open("emotion_words.txt")
num_lines = 0

for aline in emotionfile:
    num_lines += 1


print("Number of lines in the file:", num_lines)

