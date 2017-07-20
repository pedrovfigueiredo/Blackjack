import random
from card import Card

class Deck:
    deck = []

    def __init__(self):
        self.resetDeck()

    def resetDeck(self):
        self.deck.clear()

        suit = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        type = ['clubs','diamonds','hearts','spades']

        for type_ in type:
            for value in suit:
                self.deck.append(Card(type_,value))

        random.shuffle(self.deck)

    def requestCard(self):
        return self.deck.pop()

    def shuffleCards(self):
        random.shuffle(self.deck)
