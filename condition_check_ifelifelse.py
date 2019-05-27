#!/usr/bin/env python3

word = input("Please enter a four-letter word: ")
word_length = len(word)
if word_length == 4:
    print(word, "is a four-letter word. Well done.")
elif word_length == 3:
    print(word, "is a three-letter word. Try again.")
else:
    print("Sorry", word, "is not a four or three letter word.")

