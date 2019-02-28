#!/usr/bin/env python3

# First create two empty lists for songs genre/type.
rock = []
country = []

# Defining the function to request user to enter the song name and assign to var
# 'song', and choose one of the user's choice option and assign to var 'ask'.
def collect_songs():
    song = "Enter a song name: "
    ask = "Type 'r' for rock or 'c' for country. 'q' to quit: "

    # A while loop to ask user to enter their choices.
    while True:     # Condition is True so that the loop will keep running.
        genre = input(ask)
        if genre == "q":    # If user enters 'q', then break out of the loop.
            break

        if genre == "r":        # If user enters 'r', then ask the user to input
            rk = input(song)    # the name of the rock song into the var 'rk'.
            rock.append(rk)     # Then add/append the value of 'rk' into the rock list.

        elif genre == "c":      # If user enters 'c', then ask the user to input
            cy = input(song)    # the name of the country song into the var 'cy'.
            country.append(cy)  # Then add/append the value of 'cy' into the country list.

        else:
            print("Invalid.")

    print(rock)         # Print the list of the rock music.
    print(country)      # Print the list of the country music.

collect_songs()         # Calls or run the 'collect_songs()' function.

