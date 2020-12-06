#!/usr/bin/env python3

"""
Write code to find out how many lines are in the file
'emotion_words.txt'.
Save this value to the variable 'num_lines'.
Do not use the 'len' method.
"""

emotionfile = open("emotion_words.txt")
num_lines = 0   # Initialize a counter var with value zero first.

for aline in emotionfile:
    num_lines += 1


print("Number of lines in the file:", num_lines)
emotionfile.close()
print("")


# Alternatively using 'with open()', there is no need to use .close()
# method at the end to close the file.
num_lines = 0   # Initialize a counter var with value zero first.

with open("emotion_words.txt") as emotionfile:
    for aline in emotionfile:
        num_lines += 1

print("Number of lines in the file using with open() method:", num_lines)
print("")
