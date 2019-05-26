#!/usr/bin/env python3

# mapIt.py - Launches a map in the browser using an address from the command
# line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:   # The integer is greater than 1 so as to assure that
                        # the 'sys.argv' var list has more than just filename
                        # in it. eg. 202A Punggol Field
    # Get address from command line.
    address = " ".join(sys.argv[1:])    # '1:' is to chop off the first part
                                        # of the python filename if not it
                                        # will appear in browser as well.
else:
    # Get address from clipboard.
    address = pyperclip.paste() # If the python script is run without any
                                # cmd line arguments, then the program will
                                # assume that the address is stored on the
                                # clipboard memory already.


webbrowser.open("https://www.google.com/maps/place/" + address)
"""
From the cmd line, run the python script:
eg. $ python mapIt.py 202A Punggol Field
And your browser should open and navigate automatically to the address
on google maps.
"""
