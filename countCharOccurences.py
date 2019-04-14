#!/usr/bin/env python3

def count_characters(string):
    count_dict = {}     # Set the var 'count_dict' to an empty dictionary first.

    for c in string:
        if c in count_dict:     # If the character is already in the dict count_dict,
            count_dict[c] += 1  # increment the value of the character by 1.
        else:
            count_dict[c] = 1   # Otherwise, you add the character to the dict and
                                # set its value to 1.

    print(count_dict)   # Call the print() function to print out the key-value pair
                        # of each character in the string.


# Client call the 'count_characters()' function and pass in the parameter "Dynasty".
count_characters("Dynasty")
