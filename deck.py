import random
suits = {"Hearts", "Diamonds", "Clubs", "Spades"}
ranks = {"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"}
values = {"Ace" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}

class Deck:
    def __init__(self):
        self.draw = []
        for rank in ranks:
            for suit in suits:
                self.draw.append(Card(rank, suit))
    def shuffle(self):
        random.shuffle(self.draw)

    def deal(self):
        return self.draw.pop(0)

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
