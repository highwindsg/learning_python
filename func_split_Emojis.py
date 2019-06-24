#!/usr/bin/env python3

# Create a func named 'emoji_converter' and param message.
def emoji_converter(message):
    words = message.split(" ")  # Use the .split method to separate the message
                                # and then assign it to the var 'words'.
    emojis = {          # Create the dict of emojis.
        ":)": "😀",     # On MacOS, press Ctrl+Cmd+Space to see emojis selection.
        ":(": "😔"
    }

    output = ""     # First set the output var to an empty string.
    for word in words:
        output += emojis.get(word, word) + " "     # See comment below.
    return output   # Return the value of var 'output' to the 'emoji_converter'
                    # function.

"""
The .get method have two params.
First param will get the word, and
if the word is not there, then the
second param means that it will
accept the word as the default
value..
"""

message = input("> ")   # Request user input and assign it to var 'message'.
print(emoji_converter(message))

