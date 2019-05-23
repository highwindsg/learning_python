#!/usr/bin/env python3

# Import module 'zipfile' and 'os'.
import zipfile, os

# From 'os' use the .chdir() method and parse in the working dir as param.
# Have to provide the absolute path to the working dir.
os.chdir("/Users/mac/Documents/GitHub/learning_python")

# Set var 'exampleZip' with the zipfile module's .ZipFile() method and
# parse in the actual zipped filename as param.
exampleZip = zipfile.ZipFile("example1.zip")

# From var obj 'exampleZip', use the extractall() method. The extractall()
# method is from the zipfile module and it will return the absolute path
# to the file.
exampleZip.extractall()
exampleZip.close()
