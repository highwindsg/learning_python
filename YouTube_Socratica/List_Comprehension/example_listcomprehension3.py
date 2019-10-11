#!/usr/bin/env python3

v = [3, -3, 1]  # Create a list of 3 numbers and assign to var 'v'.
w = [4*num for num in v]    # for every number in var list 'v', multiply by 4 and assign each answer to var 'w'.
print(w)
print("")

# Cartesian product calculation.
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]  # Using list comprehension to calculate cartesian product.
print(cartesian_product)
print("")
