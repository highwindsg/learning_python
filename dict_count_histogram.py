#!/usr/bin/env python3

counts = dict()
#line = input("Enter a line of text: ") # Request user to enter a long line of text.
fname = input("Enter the file name: ")  # Or just request user to open a text filename,
                                        # and assign to var 'fname'.
fhand = open(fname)     # Use open() method on var 'fhand'.
line = fhand.read()     # Use the read() method on var 'fhand' and assign to new var 'line'.
words = line.split()    # Use the split() method on 'line' and assign to new var 'words'.

# Then check how many repetitions for each word are there in all the words.
for word in words:
    counts[word] = counts.get(word, 0) + 1  # The pattern of checking to see if a key is
                                            # already in a dict and assuming a default
                                            # value (0) if the key is not there is so
                                            # common that there is a method called .get()
                                            # that does this for us.
print("Counts", counts) # Then print out the counts dict of the histograms of word count.