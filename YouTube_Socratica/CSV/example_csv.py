#!/usr/bin/env python3

path = "///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/CSV/google_stock_data.csv"
file = open(path)

for line in file:
    print(line)
print("")

# Using list comprehension to read a CSV file without using the CSV module.
lines = [line for line in open(path)]
print(lines[0])     # Each line is treated as a string with a \n at the end.
print(lines[1])
print(lines[0].strip())    # Can also use the .strip() method to remove any whitespace.
print(lines[0].strip().split(","))     # Can also use the strip func to divide the string into smaller pieces.
dataset = [line.strip().split(",") for line in open(path)]
print(dataset[0])
print(dataset[1])
"""Unfortunately the data are all still strings. And there are other CSV files that may contain words and numbers.
Therefore we should use the CSV module."""
