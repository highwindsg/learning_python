#!/usr/bin/env python3

# Turn a list of strings into a single string by calling the 'join' method on
# an empty string, and passing in the list as a parameter.

words = [
        "The",
        "fox",
        "jumped",
        "over",
        "the",
        "fence",
        "."
        ]

sentence = "".join(words)    # Joining the words on an empty string.
print(sentence)
