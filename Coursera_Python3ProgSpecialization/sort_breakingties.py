#!/usr/bin/env python3

# Sorting tuples.

tups = [
    ("A", 3, 2),
    ("C", 1, 4),
    ("B", 3, 1),
    ("A", 2, 4),
    ("C", 1, 2)
]

# Sorting tuples by its first element.
for tup in sorted(tups):
    print(tup)
print("")



"""
Sorting a list of fruits by the length of the fruit name.
"""

fruits = ["peach", 
"kiwi", 
"apple",
"blueberry",
"papaya",
"mango",
"pear"
]
print(fruits)

# Sort a list of fruit words first by their length, smallest to
# largest, and then alphabetically to break ties among words of the
# same length.
# Using the sorted func with one required param and another optional
# lambda func param.
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))

for fruit in new_order:
    print(fruit)
print("")

# Sort it by largest to smallest, and then by alphabetical order.
# Using the sorted func with one required param, a second optional
# lambda func param, and a third optional param.
new_order_reverse = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)

for fruit in new_order_reverse:
    print(fruit)
print("")

# Sort the longest elements to be first and the shortest elements to
# be last.
new_order_reverse2 = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))

for fruit in new_order_reverse2:
    print(fruit)
print("")

""" Note that the above methods can be used for any numerical value 
that we want to sort, however this will not work for strings. """
