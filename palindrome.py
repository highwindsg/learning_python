#!/usr/bin/env python3

"""
A palindrome is a word spelled the same way forward and backward.
Write an algorithm that checks if a word is a palindrome by reversing
all the letters in the word and testing if the reversed word and the
original word are the same.
"""

def palindrome(word):   # Create a function named palindrome with a param.
    word = word.lower() # Set var 'word' to word with non-case sensitive.
    return word[::-1] == word   # Reverse the word and compares it to the
                                # original. If they are the same, then
                                # return True to the function, if not the
                                # same, then return False to the function.


print(palindrome("Mother"))
print(palindrome("Mom"))
