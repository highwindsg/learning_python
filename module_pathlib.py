#!/usr/bin/env python3

from pathlib import Path

# If no param is passed in, then path() will use the current working dir.
path = Path("ecommerce")
print(path.exists())    # This will print out if the folder 'ecommerce' exist or not.
print("")

# Using glob to find files and dir in the current path.
for file in path.glob("*.py"):
    print(file) # Print out all the *.py filenames only.

