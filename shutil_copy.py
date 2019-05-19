#!/usr/bin/env python3

import shutil, os   # Importing the 'shutil' module library that supports the
                    # operations of copying an removal of file.
                    # Importing the 'os' module library that portable way of
                    # using operating system dependent functionality.

# From 'os' module, use the 'chdir' func method to change to a working dir.
os.chdir("/Users/mac/Documents/GitHub/learning_python")

# From 'shutil' module, use the copy func method to copy a filename 'spam.txt'
# to a existing folder named 'delicious/'.
shutil.copy("spam.txt", "delicious")
shutil.copy("eggs.txt", "delicious")

