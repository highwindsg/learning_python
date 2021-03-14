#!/usr/bin/env python3

# Using while loop.
i = 1523
total = 0

while i <= 10503:
    total += i
    i += 2
print(total)

print("")

# Using for loop.
total = 0
for i in range(1523, 10504, 2):
    total += i
print(total)

print("")

# Or simply by a one-liner command:
print(sum(range(1523, 10504, 2)))

