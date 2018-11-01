#!/usr/bin/env python3

# Saving variables in python programs to a binary shelf file using the
# 'shelve' module.
# This way the program can restore data to variables from the hard drive.

import shelve

# Call the 'shelve.open()' method and pass it a filename 'mydata'.
# This will create a filename 'mydata.db' in file file system.
# And then store the returned shelf value in a variable.
shelfFile = shelve.open("mydata")

# You can then make changes to a shelf value as if it were a dict.
# We create a list 'cats',
cats = ["Zophie", "Pooka", "Simon"]

# and then store the list in the var 'shelfFile' associated with the key
# 'cats' in a dict.
shelfFile["cats"] = cats

# Then we close the 'shelfFile' var.
shelfFile.close()

