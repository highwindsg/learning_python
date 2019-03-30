#!/usr/bin/env python3

import re   # Import the regular expression module 're'.

objFile = open("zen.txt", "r")  # Open the file with read mode and assign to
                                # var objFile. Have not start reading yet.

contentfile = objFile.read()    # Then use the read() method to start reading
                                # the content of zen.txt in objFile, and assign
                                # to var contentfile.

matches = re.findall("Dutch", contentfile)  # Use the findall method in 're' to
                                            # search for instances of the word
                                            # 'Dutch' from var contentfile, and
                                            # then assign to var matches.

print(matches)  # Client call the print function to print out the searches in
                # var 'matches'.
"""
Or simply at the command line just type eg.
$ grep Dutch zen.txt
"""
