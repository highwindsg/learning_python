#!/usr/bin/env python3

fhand = open("mbox-short.txt")  # Use the .open() method to open the txt file and assign it to var 'fhand'.
inp = fhand.read()  # From var obj 'fhand', use .read() method and assign it to new var 'inp'.
print(len(inp))     # Print out the length of the var 'inp', which is the -> fhand -> mbox-short.txt file.
print("")
print(inp[:20])     # Print out the first 20 index of var obj 'inp'.
