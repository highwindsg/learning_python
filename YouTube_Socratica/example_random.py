#!/usr/bin/env python3

import random

print(dir(random))
print(help(random.random))
print("")

# Display 10 random numbers from interval [0, 1), means it will display 0, but will never display 1.
for i in range(10):
    print(random.random())
print("")

# Using a .uniform() method to print random numbers from a given range.
print(dir(random))

for i in range(10):
    print(random.uniform(3, 7))

