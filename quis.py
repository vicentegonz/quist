from player import Player
from deck import Deck

class Quist:

    def __init__(self, name , n_players):
        i = 1
        self.players = [Player(name, False)]
        while i < n_players:
            player = Player(f"CPU{i}", True)
            self.players.append(player)
            i += 1
        self.deck = Deck(n_players)
        self.scores = {}
        for player in self.players:
            self.scores[player.name] = []
        self.tryumph = None
        self.played = []

    def play(self):
        while self.deck.round <= self.deck.game_rounds:
            print(f"Round: {self.deck.round}\n")
            self.shufle(self.deck.give_cards())
            print(f"The tryumph is -> {self.tryumph.suit}\n")
            self.order()
            self.turns()
            for c in self.played:
                print(c)
            self.recive_cards()
            self.rotate()

    def turns(self):
        count = 1
        for player in self.players:
            self.played.append(player.execute_turn(count, self.played, self.tryumph.suit))
            count += 1

    def order(self):
        for player in self.players:
            player.print()
        print()

    def recive_cards(self):
        for player in self.players:
            player.cards = []
            player.used = []
        for card in self.deck.cards:
            card.used = False


    def rotate(self):
        back = self.players.pop(0)
        self.players.append(back)

    def shufle(self, sample):
        self.tryumph = self.deck.cards[sample[len(sample)-1]]
        i = 0
        for s in sample[:len(sample) - 1]:
            self.players[i].cards.append(self.deck.cards[s])
            i += 1
            if i == len(self.players):
                i = 0            
    
    def print(self):
        print(self.scores)

Name = input("Username: ")
n_players = int(input("Select number of players: "))
print()
quist = Quist(Name, n_players)
quist.print()
quist.play()
print("THE GAME HAS ENDED!!")
