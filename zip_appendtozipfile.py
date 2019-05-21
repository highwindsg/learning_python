#!/usr/bin/env python3

# Import module 'zipfile' and 'os'.
import zipfile, os

# From 'os', use the .chdir() method and parse in the working dir param.
os.chdir("/Users/mac/Documents/GitHub/learning_python")

# Set var 'newZip' to using zipfile's module .ZipFile() method and parse
# in params of new zip filename and option to append ('a'). Append means to
# add another file to an existing zipped file.
newZip = zipfile.ZipFile("new.zip", "a")

# From newZip, use the write method and parse in the params of file to be
# zipped and the compression type.
newZip.write("fakenews.txt", compress_type = zipfile.ZIP_DEFLATED)
newZip.close()
