#!/usr/bin/env python3

fh = open("demo.txt", "r")

try:
    for line in fh:
        print(len(line.split(" ")))

finally:
    fh.close()

# Alternatively, can run the script as below, which is the same as line 3-10.
with open("demo.txt", "r") as fh:
    for line in fh:
        print((line.split(" ")))
