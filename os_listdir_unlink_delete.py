#!/usr/bin/env python3

import os

# From 'os' module, use the chdir method to change working dir.
os.chdir("/Users/mac/Documents/GitHub/learning_python")

# Below lines are for permanent deletion of filenames with extension of
# '.rxt'.
for filename in os.listdir("/Users/mac/Documents/GitHub/learning_python"):
    if filename.endswith(".rxt"):
        # From 'os' module, use the unlink method for permanent files deletion.
        #os.unlink(filename)    # It is better to comment out this line first
        print(filename)         # and print out the 'filename' var to confirm
                                # the correct files are to be deleted/unlink.
