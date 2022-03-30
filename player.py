import random

class Player:

    def __init__(self, name, cpu):
        self.name = name
        self.cpu = cpu
        self.cards = []
        self.win = 0
        self.used = []

    def execute_turn(self, place, suit, tryumph):
        print(f"Im {self.name} playing")
        if self.cpu:
            contin = True
            while contin:
                idx = random.randint(0, len(self.cards) - 1)
                if idx not in self.used:
                    contin = False
                else:
                    idx = random.randint(0, len(self.cards) - 1)
                    print(idx)
            self.cards[idx].used = True
            self.used.append(idx)
            return self.cards[idx]
        else:
            val = 0
            for card in self.cards:
                if not card.used:
                    print(f"{val}:")
                    print(card)
                val += 1
            idx = int(input("Select card number: "))
            self.cards[idx].used = True
            return self.cards[idx]


    def print(self):
        print(f"Im {self.name}, cpu: {self.cpu} and this are my cards:")
        for card in self.cards:
            print(card)
        print()