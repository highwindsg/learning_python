#!/usr/bin/env python3

# Current working dir:
# "/Users/cay1sgp/Documents/GitHub/learning_python/Coursera_PythonTheFundamentals"

flanders_filename = "In_Flanders_Fields.txt"
flanders_file = open(flanders_filename, "r")
flanders_poem = ""

line = flanders_file.readline()
while line != "":
    flanders_poem = flanders_poem + line
    line = flanders_file.readline()

print(flanders_poem)
flanders_file.close()

