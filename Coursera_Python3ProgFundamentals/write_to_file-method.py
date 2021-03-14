#!/usr/bin/env python3


def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE MISSING HERE
    for s in sentences:
        file.write(s)
        file.write('\n')

# Or,
#    for s in sentences:
#        file.write(s + '\n')


