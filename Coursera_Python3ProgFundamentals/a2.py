#!/usr/bin/env python3


def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if dna1 >= dna2:
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num = 0
    for char in dna:
        if char == nucleotide:
            num += 1
    return num


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    """ (str) -> bool

    Shows True if only the uppercase characters of "A", "T", "C", and "G"
    is returned.

    >>> is_valid_sequence("ATCG")
    True
    >>> is_valid_sequence("HURE")
    False
    """
#    for char in dna:
#        if char not in ("ATCG") and char in ("0123456789"):
#            return False
#        else:
#            return True

    for char in dna:
        if char not in ("ATCG"):
            return False
        else:
            return True


def insert_sequence(dna1, dna2, idx):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>> insert_sequence("CCGG", "AT", 2)
    "CCATGG"
    >>> insert_sequence("ATG", "GCG", 4)
    "ATGGCG"
    """
    return dna1[:idx] + dna2 + dna1[idx:]


def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement. "A" complementary part is "T", and
    "C" complementary part is "G".

    >>> get_complement("A")
    T
    >>> get_complement("G")
    C
    """
    for char in nucleotide:
        if char == "A":
            return "T"
        if char == "T":
            return "A"
        if char == "C":
            return "G"
        if char == "G":
            return "C"
        else:
            return None


def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.
    For example, if you call this function with 'AT' as the argument,
    it should return 'TA'.

    >>> get_complementary_sequence("AT"):
    "TA"
    >>> get_complementary_sequence("GCTA"):
    "CGAT"
    """
    sequence = ""   # Initially, set the sequence with nothing.
    for char in dna:
        sequence += get_complement(char)
    return sequence

