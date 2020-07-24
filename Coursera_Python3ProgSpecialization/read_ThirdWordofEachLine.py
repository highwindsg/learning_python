#!/usr/bin/env python3

""" Using the file school_prompt2.txt, assign the third word of every line to a list called three. """

file = open("school_prompt2.txt", "r")
line = file.readlines()
three = []

for words in line:
    word = words.split()
    three.append(word[2])

print(three)
file.close()

print("")

# Alternatively, using the 'with open(.....) as f' idiom, the no need to close the file at the end.
three2 = []
with open("school_prompt2.txt", "r") as f:
    for line in f:
        word = line.split()
        three2.append(word[2])

print(three2)
