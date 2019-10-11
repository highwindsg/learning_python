#!/urs/bin/env python3

"""
Prime Number:
Only divisible by itself and 1
(2, 3, 5, 7, 11, 13, 17, 19, ...)

Composite number:
Can be factored into smaller integers
(4 = 2 x 2, 6 = 2 x 3, 8 = 2 x 2 x 2, 9 = 3 x 3, ...)

Unit: 1
(1 is neither called a prime nor composite, it is called a unit)
"""

import time
import math

def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False, if not a prime number."""
    if n == 1:
        return False  # 1 is not a prime number.

    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False, if not a prime number."""
    if n == 1:
        return False    # 1 is jot a prime

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# ===== Test Function =====
# Below will show which numbers within the range is truly a prime number.
t0 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t1 = time.time()
print("Time required: ", t1 - t0)

