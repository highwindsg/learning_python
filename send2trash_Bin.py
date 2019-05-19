#!/usr/bin/env python3

"""
Rather than deleting files and folders permanently, it is much
better to delete files and folders with the third-party send2trash module.
You can install this module by running 'pip install send2trash' from a
Terminal window.
It will send folders and files to your computer’s trash or recycle bin
instead of permanently deleting them.
However it does not free up diskspace like permanently deleting them does.
Also note that the 'send2trash()' function can only send files to the recycle
bin; it cannot pull files out of it.
"""

import send2trash   # Import module 'send2trash' and 'os'.

#os.chdir("/Users/mac/Documents/GitHub/learning_python")
baconFile = open("bacon.txt", "a")  # Set var 'baconFile' in open mode to
                                    # a text file with append mode.
baconFile.write("Bacon is not a vegetable.")
baconFile.close()
send2trash.send2trash("bacon.txt")

