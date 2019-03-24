#!/usr/bin/env python3

from random import shuffle

class Card:

    # suits and values lists are class variables.

    """
    suits are arranged in order of strength--with the strongest
    suit last, and thus assigned the highest index, and the least
    powerful suit assigned the lowest index.
    """
    suits = ["spades",  # spades is the weakest suit at index 0.
             "hearts",
             "diamonds",
             "clubs"]   # while clubs is the strongest suit at index 3.

    """
    The items at the first two indexes of the values list are None,
    so that the strings in the list match up with the index they
    represent--so the string "2" in the values list is at index 2.
    """
    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    """
    Card objs have two instance variables: suit and value---each
    represented by an integer. Together, the instance variables
    represents what kind of card the Card obj is.
    eg. you create a 2 of hearts by creating a Card obj and passing
    it the params 2 (for the suit) and 1 (for the value--1 because
    hearts is at index 1 in the suits list).
    """
    def __init__(self, v, s):
        # suit and value are integers, and are instance variables.
        self.value = v
        self.suit = s

    """
    The magic methods __lt__ and __gt__ allow you to compare two
    Card objs in an expression using the less than and greater than
    operators. The codes in the below two function methods determines
    if the card is less than or greater than the other card passed in
    as a param.
    The codes in these two magic methods can also handle if the cards
    have the same value--for example if both cards are 10s. If this
    occurs, the methods use the index value of the suits to break
    the tie.
    """
    def __lt__(self, c2):   # c2 param represent comparing card two.
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:               # This else line is actually redundant.
            return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:               # This else line is actually redundant.
            return False

    """
    The magic method __repr__ uses the value and suit instance var
    to look up the value and suit of the card in the values and
    suits lists, and returns them so you can print the card, that
    a Card obj represents
    """
    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


"""
When you initialize the Deck obj, the two for-loops in __init__
create Card objs representing all cards in a 52-card deck and
appends them to the cards list. So if 52 divides by 4, we take
the first loop from 2 to 15 because the first value for a card
is 2, and the last value for a card is 14 (the ace).
Each time around the inner loop, a new card is created using
the int from outer loop as the value (i.e. 14 for an ace) and
the int from the inner loop as the suit (i.e. a 2 for hearts).
This process creates 52 cards--one card for every suit and value
combinations. After the method creates the cards, the shuffle
method from the random module rearranges the items in the cards
list; mimicking the shuffling of a deck of cards.
Our deck has one other method called rm_card that removes and
returns a card from the cards list, or returns None if it is
empty.
"""
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):  # up to 15 but not including 15.
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()


# Client call to test out the lesser than function method.
card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2)
print("")

# Client call to test out the greater than function method.
card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 > card2)
print("")

# Client call to test out the representation function method
# to print out what the value and suit represents in the values and
# suits lists.
card = Card(10, 2)
print(card)
print("")

# You can use the Deck class to create a new deck of cards and
# print each card in it.
deck = Deck()
for card in deck.cards:
    print(card)

