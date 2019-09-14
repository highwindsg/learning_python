#!/usr/bin/env python3

fh = open("demo.txt", "r")  # Open the file 'demo.txt' in readonly mode and assign to var 'fh'.

# Printout the no. of chars in every line.
for line in fh:
    print(len(line))

fh.close()  # Close the opened file 'demo.txt'.
