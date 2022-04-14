from player import Player
from deck import Deck
import random

class Quist:

    def __init__(self, name , n_players):
        i = 1
        self.players = [Player(name, False)]
        self.orden = []
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
            print(f"Round: {self.deck.round}--------------------------------\n")
            if self.deck.round == 1:
                for player in self.players:
                    self.orden.append(player)
            self.shufle(self.deck.give_cards())
            self.select_goal(self.tryumph.suit)
            i = 0
            while i < len(self.players[0].cards):
                #self.order()
                print("Turnos:")
                played = self.turns([])
                print("Ganador:")
                winner = self.select_winner(played, self.tryumph.suit)
                name = self.orden[winner[1]].name
                #print("reordenar")
                while self.orden[0].name != name:
                    self.reorder()
                #print(self.orden, self.players)
                i += 1
            self.recive_cards()
            self.rotate()
            self.print()

    def reorder(self):
        back = self.orden.pop(0)
        self.orden.append(back)
        
    def select_winner(self, played, tryumph):
        print(f"the tryumph is {tryumph}")
        winner = (played[0], 0)
        val = 0
        for card in played:
            print(card)
            if card.suit == winner[0].suit:
                if card.value == "A":
                    winner = (card, val)
                elif str(winner[0].value) not in "A" and card.value == "K":
                    winner = (card, val)
                elif str(winner[0].value) not in "AK" and card.value == "Q":
                    winner = (card, val)
                elif str(winner[0].value) not in "AKQ" and card.value == "J":
                    winner = (card, val)
                else:
                    if str(winner[0].value) not in "AKQJ" and card.value > winner[0].value:
                        winner = (card, val)
            elif card.suit == tryumph and winner[0].suit != tryumph:
                winner = (card, val)
            val += 1
        print()
        print(f"The winner is player {self.orden[winner[1]].name} an he played {winner[0]}")
        self.scores[self.orden[winner[1]].name][self.deck.round - 2][1] += 1
        return winner

    def select_goal(self, value):
        max = len(self.players[0].cards)
        val = 0
        print()
        print(f"the tryumph is -> {value}")
        for p in self.players:
            if p.cpu:
                cont = True
                while cont:
                    if self.players[len(self.players) - 1].name == p.name:
                        x = random.randint(0, len(p.cards))
                        if x + val != max:
                            cont = False
                            print(f"{p.name} se quiere llevar {x} basas")
                            val += x
                            self.scores[p.name].append([x, 0])
                    else:
                        x = random.randint(0, len(p.cards))
                        cont = False
                        print(f"{p.name} se quiere llevar {x} basas")
                        val += x
                        self.scores[p.name].append([x, 0])
            else:
                print()
                print("Select the number of turns you will win, this are your cards:")
                for c in p.cards:
                    print(c)
                    cont = True
                while cont:
                    if self.players[len(self.players) - 1].name == p.name:
                        if max - val < 0:
                            x = int(input(f"Select the NUMBER of turns (must be 0 or les than {len(p.cards) + 1}): "))
                        else:
                            x = int(input(f"Select the NUMBER of turns (must be diferent of {max - val}): "))
                        if x + val != max:
                            cont = False
                            val += x
                            self.scores[p.name].append([x, 0])
                    else:
                        x = int(input(f"Select the NUMBER of turns (must be less than {len(p.cards) + 1}): "))
                        if x < len(p.cards) + 1:
                            cont = False
                            val += x
                            self.scores[p.name].append([x, 0])
        print()


    def turns(self, played):
        count = 1
        for player in self.orden:
            if len(played) == len(self.players):
                break
            played.append(player.execute_turn(count, played, self.tryumph.suit))
            count += 1
        print()
        return played

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
        self.played = []


    def rotate(self):
        self.orden = []
        back = self.players.pop(0)
        self.players.append(back)
        for p in self.players:
            self.orden.append(p)

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
#quist.print()
quist.play()
print("THE GAME HAS ENDED!!")
