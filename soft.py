#!/usr/bin/env python3

# This program sort a list of words from longest to shortest
# and alphabetically in the reverse order.

# DECORATE a sequence by building a list of tuples with one or
# more sort keys preceding the elements from the sequence.
txt = "but soft what light in yonder window breaks"
words = txt.split()
t = list()
for word in words:      # The first loop builds a list of tuples,
    t.append((len(word), word))     # where each tuple is a word
                                    # preceded by its length.

# SORT the list of tuples using the Python built-in sort.
t.sort(reverse=True)    # 'reverse=True' tells sort to go in
                        # decreasing order.

# UNDECORATE by extracting the sorted elements of the sequence.
res = list()
for length, word in t:  # The second loop traverses the list of
    res.append(word)    # tuples and builds a list of words in
                        # descending order of length.

print(res)
