#!/usr/bin/env python3

"""
Part 1: Asking the user to enter Y or N as the input to a question.
"""

def get_yes_or_no(message):
    valid_input = False
    while not valid_input:  # not False = True.
        answer = input(message)
        answer = answer.upper() # Convert to upper case.
        if answer == "Y" or answer == "N":
            valid_input = True
        else:
            print("Please enter Y for yes or N for no.")
    return answer

"""
Part 2: So after user provided an answer, print out the correct
response to the answer provided.
"""

# Func call with a str question param, and assign it to a var.
response = get_yes_or_no("Do you like lima beans? Y)es or N)o: ")
if response == "Y":
    print("Great! They are very healthy.")
else:
    print("Too bad. If cooked right, they are quite tasty.")

print("")
