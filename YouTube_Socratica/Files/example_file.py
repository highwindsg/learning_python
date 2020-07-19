#!/usr/bin/env python3

# Open the file using the open() func and assign it to var obj 'f'.
f = open("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/guido_bio.txt")

# Use the .read() method on var obj 'f' in read mode, and assign the state of the read mode to
# var obj 'text'.
text = f.read()

# Finally close the file.
# It is ok to close the file obj 'f' as the content has been read into 'text' var obj.
f.close()

print(text)
print("")

# In case the file is not closed and something happens to the file before it is opened,
# use the 'with open()' method. Python will automatically close the file for you.
with open("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/guido_bio.txt") as fobj:
    bio = fobj.read()

print(bio)
