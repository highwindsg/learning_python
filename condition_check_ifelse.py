#!/usr/bin/env python3

word = input("Please enter a four-letter word: ")
word_length = len(word)
if word_length == 4:
    print(word, "is a four-letter word. Well done.")
else:
    print("Sorry", word, "is not a four-letter word.")

