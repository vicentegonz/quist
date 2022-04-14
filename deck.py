import random
from card import Card
from player import Player

class Deck:

    def __init__(self, n_players):
        self.cards = []
        self.round = 1
        self.n_players = n_players
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        suits = ["Spades", "Dimonds", "Clubs", "Hearts"]
        for val in values:
            for suit in suits:
                card = Card(val, suit)
                self.cards.append(card)
        self.limit = len(self.cards) // n_players
        if self.limit * n_players >= 52:
            self.limit -= 1
        self.game_rounds = (self.limit * 2) -1

    def give_cards(self):
        input("press enter")
        if self.round <= self.limit:
            n_cards = self.round
        elif self.round <= self.game_rounds:
            n_cards = self.game_rounds - self.round + 1
        sample = random.sample(range(0, 52), 1 + (n_cards * self.n_players))
        self.round += 1
        return sample

    def print(self):
        for card in self.cards:
            card.print()
