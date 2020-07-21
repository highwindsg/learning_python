#!/usr/bin/env python3

filename = "squared_numbers.txt"    # This filename var will contain the txt and will be created.
outfile = open(filename, "w")   # The filename var obj is opened with write mode.

for num in range(1, 13):
    square = num * num
    outfile.write(str(square) + "\n")   # write the square in string to the outfile onj.

outfile.close() # Close the outfile obj.

infile = open(filename, "r")    # Now open the txt file with read mode and assign to var infile.
print(infile.read()[:10])   # Read the first 10 char of infile obj, and print out.
infile.close()  # Close the infile obj.

