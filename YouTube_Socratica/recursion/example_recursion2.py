#!/usr/bin/env python3

# Recursion, the Fibonacci Sequence and Memoization.
# Using memoization to cache values and using a Python builtin tool.

# Firstly, create a empty dict named fibonacci_cache to store recent func calls.
fibonacci_cache = {}

def fibonacci(n):
    # If we have cached the value, then return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)     # Recursive call to computer the Nth term.

    # Cache the value in fibonacci_cache dict, and then return it to the func.
    fibonacci_cache[n] = value
    return value


for n in range(1, 1001):
    print(n, ":", fibonacci(n))
