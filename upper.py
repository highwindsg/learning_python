print("How are you?")
feeling = input()
if feeling.lower() == "great":  # Whatever case the user enters the word, it will be changed
                                # to lower case. This handles variations or mistakes in user
                                # input.
    print("I feel great too.")
else:
    print("I hope the rest of your day is good.")

