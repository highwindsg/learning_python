#!/usr/bin/env python3

# Recursion, the Fibonacci Sequence and Memoization

# Create a func named 'fibonacci()' with a param n.
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call


for n in range(1, 101):
    print(n, ":", fibonacci(n))

"""The above range is still do-able as it is just 10 numbers. However if the range is for 100 or 1000 numbers,
then there will be performance issue. This is because the computer has to repeat the work of of adding all over again
for each function call. Check out the next script 'example_recursion2.py' on how to use memoization - a
caching values method."""
