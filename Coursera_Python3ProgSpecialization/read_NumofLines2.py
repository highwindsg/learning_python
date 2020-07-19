#!/usr/bin/env python3

emotionfile = open("emotion_words.txt")
num_lines = 0

for aline in emotionfile:
    num_lines += 1


print("Number of lines in the file:", num_lines)

