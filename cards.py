#!/usr/bin/env python3

class Card:

    # suits and values are class variables.

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
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False


    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
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

# Client call to test out the lesser than function method.
card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2)

# Client call to test out the greater than function method.
card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 > card2)

# Client call to test out the representation function method
# to print out what the value and suit represents in the values and
# suits lists.
card = Card(10, 2)
print(card)

