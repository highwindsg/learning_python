#!/usr/bin/env python3

# Guess the number game

import random       # Because we wanted to choose a random number,
                    # we imported the random package

MAX_GUESSES = 5     # setting/assigning the maximum number of guesses allowed
MAX_RANGE = 20      # setting/assigning the highest possible number allowed

# Show introduction
print("Welcome to my Guess the Number program.")
print("Guess my number between 1 and", MAX_RANGE)
print("You will have", MAX_GUESSES, "guesses.")
print("")

def playOneRound():
    # Select a random target number from a random range.
    # Starting from 1 to the 'MAX_RANGE + 1 because the argument needs to be an
    # 'up to but not including' value.
    # In this case, we want to get a number in the range of 1 to 20,
    # so we need to pass in value 1 and 21.
    target = random.randrange(1, MAX_RANGE + 1)

    # Below hint is the answer, else you will never know what is the random number answer.
    #print("Hint:, the answer is", target)
    #print("")

    # Initialize a guess counter
    guessCounter = 0

    # Loop forever
    while True:
        # Ask the user to provide a number for a guess
        userGuess = int(input("Take a guess: "))

        # Increment guess counter
        guessCounter = guessCounter + 1

        # If user's guess is correct, congratulate user, we're done
        if userGuess == target:
            print("You got it!")
            print("It only took you", guessCounter, "guess(es).")
            break       # This will end the while loop

        # If user's guess is too low, tell user
        elif userGuess < target:
            print("Your guess was too low.")

        # If user's guess is too high, tell user
        else:
            print("Your guess was too high.")

        # If reached max guesses, tell user the correct answer, we're done
        if guessCounter == MAX_GUESSES:
            print("Sorry, you did not get it in", MAX_GUESSES, "guesses.")
            print("The number was:", target)
            break   # since the maximum guesses has been tried, the while loop ends

while True:
    playOneRound()      # call the function to play one round of the game
    goAgain = input("Play again? (Press ENTER to continue, or q to quit):")
    if goAgain == "q":
        break

print("Thanks for playing.")
