#!/usr/bin/env python3

# Converting numbers into words.

# Create a dict from numeric keys of 0 to 9 with pair values of the word.
Numbers = {
    "1": "One",     # keys and values must all be in strings format eg. "1"
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

Input_num = input("Number(s): ")   # Request user to provide the numeric numbers.

output_word = ""    # Set the var output_word to a empty string first.

for num in Input_num:
    output_word += Numbers.get(num, "!") + " "

print(output_word)

