#!/usr/bin/env python3

"""
Functions can call other functions (Composition).
Take a large problem and break it down into a group of smaller
problems. This process of breaking a problem into smaller
subproblems is called 'functional decomposition'.
"""

def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)


def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d


def best_key(dictionary):
    ks = dictionary.keys()  # Have to turn ks into a list first.
    best_key_so_far = list(ks)[0]
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far


print(most_common_letter("aaabbbbbcccccccccccccccdddd"))
print("")
