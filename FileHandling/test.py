#!/usr/bin/env python3

fh = open("demo.txt", "w")

#fh.write("Use open() function to open the file.\nThe open() function takes two parameters; filename and mode.")

try:
    for i in range(10):
        fh.write("This is line no %d\n" %(i+1))
finally:    # The 'finally:' body will execute even if the 'try:' body encounters error.
    fh.close()

# Alternatively, the line 7-9 can be re-written as below.
with open("demo.txt", "a") as fh:
    for i in range(10):
        fh.write("This is line %d\n" %(i+1))
