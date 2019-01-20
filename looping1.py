#!/usr/bin/env python3

looping = True
while looping == True:
    answer = input("Please type the letter 'a': ")
    if answer == "a":
        looping = False     # we're done
    else:
        print("Come on, type an 'a'!")

print("Thanks for typing an 'a'.")

