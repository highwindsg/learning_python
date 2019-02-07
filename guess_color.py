#!/usr/bin/env python3

colors = ["purple",
          "orange",
          "green"]

guess = input("Guess a color:")

if guess.lower() in colors:         # Using the lower case method ensures that
                                    # whatever upper or lower case entered, the input
                                    # will also be taken into consideration.
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")
