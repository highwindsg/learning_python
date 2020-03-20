#!/usr/bin/env python3


def count_matches(s1, s2):
    """ (str, str) -> int

    Return the number of positions in s1 that contain the
    same character at the corresponding positions of s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches("ate", "ape")
    2
    >>> count_matches("head", "hard")
    2
    """

    # First create an accumulator that will contain the number of matches.
    num_matches = 0

    for i in range(len(s1)):
        # So if the character at index position of s1 is the same as s2,
        # add the number to the accumulator var of num_matches.
        if s1[i] == s2[i]:
            num_matches += 1

    return num_matches


Ans = count_matches("ate", "ape")
Ans2 = count_matches("head", "hard")

# So if put in list of numbers instead of characters, the func will still
# work as lists and strings are treated similarly in Python, known as
# 'polymorphism'. The ability of objects of different types to respond to
# the same func call.
Ans3 = count_matches([1, 2, 3], [5, 2, 3])
print(Ans)
print(Ans2)
print(Ans3)

