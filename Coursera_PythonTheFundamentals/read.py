#!/usr/bin/env python3

# Current working dir:
# "/Users/cay1sgp/Documents/GitHub/learning_python/Coursera_PythonTheFundamentals"

flanders_filename = "In_Flanders_Fields.txt"
flanders_file = open(flanders_filename, "r")
flanders_poem = flanders_file.read()

print(flanders_poem)
flanders_file.close()

