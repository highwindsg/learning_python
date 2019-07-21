#!/usr/bin/env

while True:
    line = input("> ")
    if line[0] == "#":  # If the first character, first slice is a #, then continue to next input line.
        continue
    if line == "done":
        break
    print(line)
print("Done!")
