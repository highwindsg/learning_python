#!/usr/bin/env python3

# Execute the following in Python interactive mode.

"""
# The tkinter module and func will bring up a explorer dialog box.
>>> import tkinter.filedialog

# Using the tkinter module askopenfile func to choose a existing
# filename in a selected directory.
>>> from_filename = tkinter.filedialog.askopenfile()

# Using the tkinter module asksaveasfilename func to choose the
# filename you want to create and a directory location.
>>> to_filename = tkinter.filedialog.asksaveasfilename()

# Open the existing filename in read mode and assign to var
# file_file.
>>> from_file = open(from_filename, 'r')

# From the var obj from_file, use the .read() method to read the file
# and assign the whole line to var contents.
>>> contents = from_file.read()

# Then close the existing filename var using the .close() method.
>>> from_file.close()

# Open the to_filename obj (which is the destination new filename) with
# write mode, and assign it to var to_file.
>>> to_file = open(to_filename, 'w')

# Using the .write() method on var to_file, write a word 'Copy\n'
# with new line.
>>> to_file.write('Copy\n')

# Using the .write() method on var to_file, write the contents into
# the var obj of to_file, which is the destination new filename).
>>> to_file.write(contents)

# Then close the var obj to_file using the .close() method.
>>> to_file.close()
"""
# Then check the destination dir for the new copied file.
#
