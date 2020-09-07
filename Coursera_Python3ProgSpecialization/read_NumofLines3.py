#!/usr/bin/env python3

""" Find the number of lines in the file, travel_plans2.txt,
and assign it to the variable num_lines. """

f = open("travel_plans2.txt", "r")
text = f.readlines()    # .readlines() method converts text to a list with new lines.
print(text)
print("")

num_lines = len(text)
print(num_lines)
print("")
