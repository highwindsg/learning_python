#!/usr/bin/env python3

total = 0
count = 0

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count += 1

average = total / count
print("Average: ", average)
