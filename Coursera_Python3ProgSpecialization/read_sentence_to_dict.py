#!/usr/bin/env python3

# Provided is a string saved to the variable name sentence.
# Split the string into a list of words, then create a dictionary
# that contains each word and the number of times it occurs.
# Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

listofwords = sentence.split()
print(listofwords)
word_dict = {}

for word in listofwords:    # For every word in the listofwords,
    if word not in word_dict:   # if that word is not in the listofwords,
        word_dict[word] = 0 # then initialize that word key with a new counter value.
    word_dict[word] += 1    # Otherwise if the word is already in the word_dict,
    # then add 1 value to the word key.
    
word_counts = word_dict
print(word_counts)
print("")
