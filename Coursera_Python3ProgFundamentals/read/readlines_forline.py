#!/usr/bin/env python3

# Current working dir:
# "/Users/cay1sgp/Documents/GitHub/learning_python/Coursera_PythonTheFundamentals"

flanders_filename = "In_Flanders_Fields.txt"
flanders_file = open(flanders_filename, "r")
flanders_poem = ""

flanders_list = flanders_file.readlines()
for line in flanders_list:
    flanders_poem = flanders_poem + line

print(flanders_poem)
flanders_file.close()
