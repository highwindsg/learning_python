#!/usr/bin/env python3

import shutil, os

os.chdir("/Users/mac/Documents/GitHub/learning_python")

# Move filename 'bacon.txt' into existing folder named 'eggs/' and at the
# same time, rename that 'bacon.txt' to 'new_bacon.txt'.
# Note that if the folder named 'eggs/' is not found, then the file will
# be renamed to 'eggs' without file extension.
shutil.move("bacon.txt", "eggs/new_bacon.txt")

