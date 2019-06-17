#!/usr/bin/env python3

message = input("> ")   # Request user input and assign it to var 'message'.
words = message.split(" ")  # Use the .split method to separate the message
                            # and then assign it to the var 'words'.
emojis = {          # Create the dict of emojis.
    ":)": "😀",     # On MacOS, press Ctrl+Cmd+Space to see emojis selection.
    ":(": "😔"
}

output = ""     # First set the output to empty string.
for word in words:
    output += emojis.get(word, word) + " "     # See comment below.

"""
The .get method have two params.
First param will get the word, and
if the word is not there then will
accept the second param's word.
"""

print(output)

