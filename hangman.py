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

    # The var 'rletters' (remaining letters) is a list containing each character in the
    # var 'word' that keeps track of which letters are left to guess. Or letters in the var
    # 'word' that the player hasn't guessed correctly yet.
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

        # If the player guessed correctly any letters in the var 'word', then need to
        # update the 'board' list (x), which is used later in the game to display the
        # letters remaining.
        if guess in rletters:           # To do this we use the index method on 'rletters'
            x = rletters.index(guess)   # list to get the first index of the letter Player
            board[x] = guess            # Two guessed, and use it to replace the underscore
                                        # in 'board' at the index with the correctly guessed
                                        # letter.
            """ There is one problem with this. Because 'index' only returns the first index
            of the character you are looking for, your code will not work if the var
            'word' has more than one of the same character. To get around this, modify
            'rletters' by replacing the character that was correctly guessed with a dollar
            sign, so that the next time round the loop, the 'index' function will find the
            next occurrence of the letter (if there is one) and it won't stop at the first
            occurrence. """
            rletters[x] = "$"
        else:
            wrong += 1              # On the other hand if the player guessed an incorrect
                                    # letter, you increment 'wrong' by 1.

        # Next we print the scoreboard and your hangman using the 'board' and 'stages' lists.
        print((" ".join(board)))

        """ You can create the entire hangman by printing eg. '\n'.join(stages), which adds
        a new line to each string in the 'stages' list so that each string in the list prints
        on a separate line.
        And to print your hangman at whatever stage the game is at, you slice your 'stages'
        list. You start at 0, and slice up to the stage you are at (represented by the var
        'wrong') plus one.
        You add one because when you are slicing, the end slice does not get included in the
        result. This slice gives you only the strings you need to print the version of the
        hangman you are currently at. """
        y = wrong + 1
        print("\n".join(stages[0: y]))

        if "__" not in board:       # Finally, you check if Player Two won the game. If no
            print("You win!")       # more underscores in the 'board' list, they guessed all
            print(" ".join(board))  # the letters and won the game.
            win = True              # You also then set the var 'win' to True which breaks
            break                   # out of your while loop.

    if not win:     # If they lose, var 'win' in this function is still set at False,
        print("\n".join(stages[10: wrong]))     # then print out the entire 'stages' list.
        print("You lose! It was {}.".format(word))

hangman("cat")  # Calls the hangman function and parse in the string (word answer).

