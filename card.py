class Card:
    def __init__(self, type, symbol):
        self.type = type
        self.symbol = symbol

    def __str__(self):
        return str(self.type) + " " + str(self.symbol)

    def __repr__(self):
        return str(self)
