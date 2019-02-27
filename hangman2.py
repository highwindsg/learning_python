#!/usr/bin/env python3

# Modifying the game from 'hangman.py', select the word randomly from a list of given words
# in the code.

import random

def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    # Select a random int from the random module and assigns it to var 'random_number'.
    random_number = random.randint(0, 4)
    # Then select a 'random_number' from the 'word_list' list and assigns it to var 'word'.
    word = word_list[random_number]
    wrong_guesses = 0   # Starts number of wrong guess at zero first.
    stages = ["",
              "________      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|"
              ]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman()
