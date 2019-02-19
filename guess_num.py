#!/usr/bin/env python3

"""
Write a program with an infinite loop (with the option to type
'q' to quit) and a list of numbers. Each time through the loop
ask the user to guess a number on the list and tell them
whether or not they guessed correctly.
"""

numlist = [1, 2, 3, 4, 5]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break

    """ If the user just press enter without a number and a
    ValueError occurs, treat it as an exception and ask the
    user to please type a number again.
    """
    try:
        answer = int(answer)
    except ValueError:
        print("Please type a number or q to quit.")

    if answer in numlist:
        print("You guessed correctly!")
    else:
        print("You guessed wrongly!")
