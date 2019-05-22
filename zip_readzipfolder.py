#!/usr/bin/env python3

# Import module 'zipfile' and 'os'.
import zipfile, os

# From 'os', use the .chdir() method to change working dir.
os.chdir("/Users/mac/Documents/GitHub/learning_python")

# Create a var 'exampleZip' and set it using the zipfile module's ZipFile() func
# with a param of an existing zip file name.
exampleZip = zipfile.ZipFile("example1.zip")

# Print the content of the var exampleZip using the namelist() method from the
# ZipFile() obj.
print(exampleZip.namelist())

# Create a var 'spamInfo' and set it to using the Zipfile() obj's .getinfo()
# method with param of a txt file. This is to get the details of the txt file.
spamInfo = exampleZip.getinfo("spam.txt")

# Then print out the file size from 'spamInfo' using the .file_size method.
print(spamInfo.file_size)

# And print out the compressed size from 'spamInfo' using the .compress_size
# method.
print(spamInfo.compress_size)

# Close the opened exampleZip var.
exampleZip.close()
