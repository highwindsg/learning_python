#!/usr/bin/env python3

# Create a string called first_forty that is comprised of the first 40
# characters of emotion_words2.txt.

f = open("emotion_words2.txt", "r")
text = f.read()
first_forty = text[0:40]
print(first_forty)
print("")
