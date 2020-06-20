#!/usr/bin/env python3

#def print_lyrics():
#    print("I'm a lumberjack, and I'm okay.")
#    print("I sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


repeat_lyrics()

""" It does not matter if the def print_lyrics() comes after
def repeat_lyrics(). As during function call at line 17, it will
still call the function irregardless of position. """

