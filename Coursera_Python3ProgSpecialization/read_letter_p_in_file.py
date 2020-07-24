#!/usr/bin/env python3

""" Find the words in text file with a letter 'p' and print out as a list. """

f = open("school_prompt2.txt", "r")
text = f.readlines()
p_words = []
for lines in text:
    lines = lines.split()
    for words in lines:
        if "p" in words:
            p_words.append(words)
print(p_words)
