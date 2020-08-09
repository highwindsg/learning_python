#!/usr/bin/env python3

def add(a, b):  # 'a' and 'b' are formal params.
    total = a + b
    return total

my_var = 11

sum = add(11, 3)    # '11' and '3' are actual params.
print(sum)

print("")

sum2 = add(my_var, 3)
print(sum2)

print("")

def print_many(x, y):
    """Print out strings x, y times."""
    for i in range(y):
        print(x)

z = 3
print_many("Greetings", z)

print("")
