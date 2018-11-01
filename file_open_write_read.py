#!/usr/bin/env python3

# Open a new file named 'bacon.txt' in 'write' mode.
baconFile = open("bacon.txt", "w")

# Writes a line and ends with a '\n' new line.
baconFile.write("Hello world!\n")

# Then close the file.
baconFile.close()

# Open the file again in 'append' mode.
baconFile = open("bacon.txt", "a")

# Add a second new line of text while in appending mode.
baconFile.write("Bacon is not a vegetable.")

# Then close the file again.
baconFile.close()

# Open the file again.
baconFile = open("bacon.txt")

# Read the content of the file and pass it to var 'content'.
content = baconFile.read()

# Then close the file.
baconFile.close()

# Print out the text in var content.
print(content)
