#!/usr/bin/env python3


document = "cat.txt"
file = open(document, "r")


def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.
    The lines should have the newline removed.

    Precondition: len(letter) == 1
    """

    matches = []

    # CODE MISSING HERE
#    document = "cat.txt"
#    file = open(document, "r")

    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))

# Or,
#    for line in file:
#        if line.startswith(letter):
#            matches.append(line.rstrip('\n'))

    return matches


ans = lines_startswith(file, "i")
print(ans)
