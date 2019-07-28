#!/usr/bin/env python3

# To find the average from a user's input list of numbers.
numlist = list()    # Create an empty list and assign it to a var 'numlist'.

while True:
    inp = input("Enter a number: ")
    if inp == "done":       # If the user input the word 'done', then the stop the input request.
        break
    value = float(inp)      # Use the float() method to set the 'inp' var to decimal floating point,
                            # and assign it to var 'value'.
    numlist.append(value)   # Then append the value to the empty numlist.

average = sum(numlist) / len(numlist)
print("Average:", average)
