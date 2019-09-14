#!/usr/bin/env python3

fh = open("demo2.txt")  # Open the file 'demo.txt' in readonly mode, and assign to var 'fh' (file handler in short).

#print(fh.read())

print(fh.readline(4))   # Printout the first 4 char of the first line; slice 0 - 4.
print(fh.readline())    # Continues to printout the remaining of the first line.
print(fh.readline())    # Printout line 2.
print(fh.readline())    # Printout line 3.

print(fh.readlines())   # Printout all the lines into a list.

fh.close()      # Closes the opened file 'demo2.txt'.
