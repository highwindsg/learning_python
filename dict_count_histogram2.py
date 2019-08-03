#!/usr/bin/env python3

name = input("Enter a filename: ")
handle = open(name)

# Building up the dictionary 'count'.
counts = dict()  # First create a empty dictionary.
for line in handle:  # For every line in the txt file,
    words = line.split()    # separate every word using .split() into a list and assign it to var 'words'.
    #    print(words)
    for word in words:      # Building a histogram for every word in every line.
        counts[word] = counts.get(word, 0) + 1
print(counts)       # Print out the 'counts' dictionary, which is a histogram.

# To find the largest value from the key-value pair in the dict 'counts'.
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)    # So 'bigword' is the word that is most common,
                            # 'bigcount' is the number of times it appears.
