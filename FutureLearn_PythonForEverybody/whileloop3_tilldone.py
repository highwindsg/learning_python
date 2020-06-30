#!/usr/bin/env python3

# If the first char input is a '#' then it will not print out the '#'.
# Instead will ask the user to input again.

while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)

print("Done!")

