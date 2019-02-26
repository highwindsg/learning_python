#!/usr/bin/env python3

def hangman(word):  # Create a function called 'hangman' to store the game.
                    # It accepts a var called 'word' as a param, which Player Two
                    # has to guess.

    wrong = 0   # Use another var called 'wrong' to keep track count of how many
                # incorrect letters Player One has guessed.

    # The var 'stages' is a list filled with strings to draw your hangman.
    # When Python prints each string in the 'stages' list, a hangman gradually appears.
    stages = ["",
              "_________           ",
              "|                   ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
              ]

    # The var 'rletters' is a list containing each character in the var 'word' that
    # keeps track of which letters are left to guess.
    rletters = list(word)

    # The var 'board' is a list of strings used to keep track of the hints you display
    # to Player Two.
    board = ["__"] * len(word)  # e.g, c_t if the word is cat, then Player Two has
                                # already guessed 'c' and 't' correctly.
                                # We use ["__"] * len(word) to populate list, with
                                # an underscore for every character in the var 'word'.
                                # For example, if the word is cat, then 'board' starts
                                # as ["__", "__", "__"].

    # A var called 'win', to keep track of whether Player Two has won the game yet.
    win = False

    print("Welcome to Hangman") # Prints the welcome msg and starts the game.

    """
    The while loop game continues as long as the var 'wrong' is less than the
    'len(stages) - 1'. The var 'wrong' keeps track of the no. of wrong letters
    Player Two has guessed, as soon as Player Two guesses more wrong letters than
    the no. of strings that make up the hangman (the no. of strings in 'stages' list),
    the game is over. You have to subtract 1 from the length of the 'stages' list to
    compensate for the fact that the 'stages' list starts counting from 0, and 'wrong'
    starts counting at 1.
    """
    while wrong < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter: ")   # Ask the user to guess a letter
        guess = guess.lower()               # (case-insensitive) and store it in the
                                            # var 'guess'.
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[10: wrong]))
        print("You lose! It was {}.".format(word))

hangman("cat")

