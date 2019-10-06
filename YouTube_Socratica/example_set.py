#!/usr/bin/env python3

example = set()

print(dir(example))

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)
print(len(example))
print(type(example))

example.discard(59)

print("")

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print(odds.union(evens))
print(evens.union(odds))
print(odds)
print(evens)
print(evens.union(odds))
print(evens.intersection(odds))
print(primes.union(composites))
