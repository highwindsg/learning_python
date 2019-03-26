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


"""
A class to represent each player in the group to keep track of
their cards and how many rounds they've won.
"""
class Player:
    def __init__(self, name):
        # instance var 'wins' to keep track of how many rounds
        # a player has won.
        self.wins = 0
        # instance var 'card' to represent the card a player is
        # currently holding.
        self.card = None
        # instance var 'name' to keep track of a player's name.
        self.name = name


"""
When you create the game obj class, Python calls the __init__
method and collects the names of the two players and stores them
in the vars name1 and name2.
Next, create a new Deck object and store it in the instance var
deck, and create two Player objs using the names in name1 and name2.
"""
class Game:
    def __init__(self):
        name1 = input("Type in player one's name: ")
        name2 = input("Type in player two's name: ")
        # From self, set deck to an instance of class Deck.
        self.deck = Deck()
        # From self, set p1 and p2 to player name1 and name2.
        self.p1 = Player(name1) # p1 is-a name1
        self.p2 = Player(name2) # p2 is-a name2

    def wins(self, winner):
        w = "{} wins this round."
        w = w.format(winner)
        print(w)

    # p1n - player1 name; p1c - player1 card.
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {}, and {} drew {}."
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    """
    The play_game in the Game class starts the game.
    The loop in the method keeps the game going as long as there
    are two or more cards left in the deck, and as long as the
    var response does not equal to q.
    """
    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        """
        Each time around the loop, you assign the var response to
        the input of the user. The game continues until either the
        user types "q", or when there are less than two cards left
        in the deck.
        """
        while len(cards) >= 2:
            m = "Type q to quit or any key to play: "
            response = input(m)
            if response == "q":
                break
            """
            Two cards are drawn each time through the loop.
            The play_game method assigns the first card to p1, and
            the second card to p2.
            """
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            """
            Then it prints the name of each player and the card they
            drew, compares the two cards to see which card is greater,
            increments the 'wins' instance var for the player with
            the greater card, and prints a message that says who won.
            """
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        """
        When the Deck obj runs out of cards, the 'play_game' method
        prints a message saying the war is over, calls the 'winner'
        method (passing in both p1 and p2), and prints a message with
        the results--the name of the player who won.
        """
        win = self.winner(self.p1, self.p2)

        print("War is over. {} wins.".format(win))

    """
    The Game class also has a method called 'winner' that takes two
    player objs, looks at the number of rounds they won, and returns
    the player who won the most rounds.
    """
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        else:   # This else line can be redundant/omitted.
            return "It was a tie!"


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
    print("")

# Start of the full game.
game = Game()       # Set var game to an instance of class Game.
game.play_game()    # From game, call the 'play_game' method.

