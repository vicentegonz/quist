import random

class Player:

    def __init__(self, name, cpu):
        self.name = name
        self.cpu = cpu
        self.cards = []
        self.win = 0
        self.used = []

    def execute_turn(self, place, suit, tryumph):
        if self.cpu:
            if place > 1:
                posibles = set()
                posibles = self.check_suit(suit[0].suit, posibles)
                #posible = self.check_suit(tryumph, posible)
                posibles = list(posibles)
                if len(posibles) > 0:
                    idx = random.choice(posibles)
                else:
                    contin = True
                    while contin:
                        idx = random.randint(0, len(self.cards) - 1)
                        if idx not in self.used:
                            contin = False
                        else:
                            idx = random.randint(0, len(self.cards) - 1)
            else:
                contin = True
                while contin:
                    idx = random.randint(0, len(self.cards) - 1)
                    if idx not in self.used:
                        contin = False
                    else:
                        idx = random.randint(0, len(self.cards) - 1)
            print(f"{self.name} selected {self.cards[idx]}")
            self.cards[idx].used = True
            self.used.append(idx)
            return self.cards[idx]
        else:
            print()
            if place == 1:
                val = 0
                posibles = []
                print(f"Your cards for the first turn: trymph -> {tryumph}")
                for card in self.cards:
                    if not card.used:
                        print(f"{val}- {card}")
                        posibles.append(str(val))
                    val += 1
                print()
                idx = input("Select card number: ")
                while (idx not in posibles):
                    print("Out of range or not a number")
                    idx = input("Select card number: ")
                print()
                selection = self.cards[int(idx)]
                print(f"{self.name} selected {selection}")
                selection.used = True
                return selection
            else:
                print(f"Your playable cards: tryumph -> {tryumph}, suit -> {suit[0].suit}")
                posible = set()
                posible = self.check_suit(suit[0].suit, posible)
                posible = list(posible)
                if len(posible) > 0:
                    for p in posible:
                        print(f"{p}- {self.cards[p]}")
                        p = str(p)
                    pass
                else:
                    val = 0
                    posibles = []
                    for card in self.cards:
                        if not card.used:
                            print(f"{val}- {card}")
                            posibles.append(str(val))
                        val += 1
        
                print()
                idx = input("Select card number: ")
                while (idx not in posibles):
                    print("Out of range or not a number")
                    idx = input("Select card number: ")
                print()
                selection = self.cards[int(idx)]
                print(f"{self.name} selected {selection}")
                selection.used = True
                return selection

    def check_suit(self, suit, values):
        v = 0
        for c in self.cards:
            if c.suit == suit:
                values.add(v)
            v += 1
        return values

    def print(self):
        print(f"Im {self.name}, cpu: {self.cpu} and this are my cards:")
        for card in self.cards:
            print(card)
        print()

    def __repr__(self):
        return self.name