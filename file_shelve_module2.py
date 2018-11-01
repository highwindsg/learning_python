#!/usr/bin/env python3

# We can use the 'shelve' module to later reopen and retrieve the data
# from these shelf files. Shelve values don't have to be opened in read
# or write mode, they can do both once opened.

# Enter the below lines into the interative shell to see the results.

import shelve

# Here we open the shelf file to check that our data was stored correctly
# in the previous file 'file_shelve_module.py'.
shelfFile = shelve.open("mydata")
type(shelfFile)     # This line will show the datatype of 'shelfFile'.
shelfFile['cats']   # This line will output the 'cats' dict.
# Entering line 14 above will return the same list we stored earlier.

shelfFile.close()   # Then we close the 'shelfFile' var.
