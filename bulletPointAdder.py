#!/usr/bin/env python3
# bulletPointaAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
# 1. Paste text from the clipboard.
# 2. Do something to it, like add a star and a space at each line.
# 3. Copy the new text to the clipboard.

import pyperclip

# Step 1.
text = pyperclip.paste()

# TODO: Separate lines and add stars. This line is a reminder to
# complete the next part of the program eventually.

# Step 2.
# Separate lines and add stars.
# We split the 'text' along its newlines (eg. '\n') to get a list in which
# each item is one line of the text.
# And then we store the list in var 'lines'.
lines = text.split("\n")

for i in range(len(lines)):     # loop through all indexes in the 'lines' list.
    lines[i] = "* " + lines[i]  # Add a star & a space to each string in 'lines' list.

# The 'lines' list now contains modified lines that start with stars.
# But pyperclip.copy() is expecting a single string value, not a list of string values.
# To make this single string value, pass 'lines' into the join() method to get a
# single string joined from the list’s strings.”
text = "\n".join(lines)

# Step 3.
pyperclip.copy(text)
