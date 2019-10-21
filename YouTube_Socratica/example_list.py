#!/usr/bin/env python3

example = list()
example = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

print(primes)
print("")

# Extracting values in a list by indexing.
print(primes[0])
print(primes[1])
print(primes[2])
print(primes[-1])
print(primes[-2])
print("")

# Extracting values in a list by slicing.
print(primes)
print(primes[2:5])  # Prints the values from primes list starts from index 2 to up 5 but does not includes index 5.
print(primes[0:6])
print("")

# Can also concatenate two lists together.
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
numbers2 = [1, 2, 3]
print(numbers + letters)
print(letters + numbers)
print(numbers + numbers2)

