#!/usr/bin/env python3

fhand = open("mbox.txt")
count = 0

# To print out how many lines in all are there in the file.
for line in fhand:
    count += 1
print("Line Count:", count)
