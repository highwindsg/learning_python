#!/usr/bin/env python3

"""
Now that you have seen and practiced a bit with opening and closing files,
there is another mechanism that Python provides for us that cleans up the
often forgotten close.
When we are done we simply stop indenting and let Python take care of closing
the file and cleaning up.
"""

with open("emotion_words.txt", "r") as ew:
    for line in ew:
        print(line)

print("")
print("")

"""
This is the same as the code below that specifically closes the file var
with the .close() function..
"""

ew = open("emotion_words.txt", "r")
for line in ew:
    print(line)
ew.close()

