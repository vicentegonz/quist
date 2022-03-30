class Card:

    def __init__(self, val, suit):
        self.value = val
        self.suit = suit
        self.used = False
    
    def __str__(self):
        return f"{self.value}, of {self.suit}"