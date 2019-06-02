#!/usr/bin/env python3

# Guess the secret word game.

secret_word = "giraffe" # Answer to secret word is 'giraffe'.
guess = ""              # First start off with no guesees.
guess_count = 0         # Initial guess count is set to 0.
guess_limit = 3         # Set the guessing limit to max of 3 tries.
out_of_guesses = False  # Set var 'out_of_guesses' to 'False' so as long as it
                        # is Not True, the guessing can continue within the limit.

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win")
