#!/usr/bin/env python3

# Another even faster way to use Fibonacci Sequence and Memoization to store cache values is to use a builtin tool.

# From the functools module, import the decorator lru_cache.
from functools import lru_cache     # 'lru_cache' means 'least recently used cache'.

# A one-line way to add memoization to your func.
@lru_cache(maxsize=1000)    # If not maxsize caching is set, then default will only be 128.
def fibonacci(n):
    # Check that the input is a positive integer.
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term.
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call to computer the Nth term.


for n in range(1, 501):
    print(n, ":", fibonacci(n))

print(fibonacci(-2))    # This client call will raise an ValueError.
print(fibonacci("Three"))   # This client call will raise an TypeError.

