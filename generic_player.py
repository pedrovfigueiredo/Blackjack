import sys

class Generic_Player(object):
    def __init__(self, hand, total_money, name):
        self.hand = hand
        self.total_money = total_money
        self.name = name

    def addCardToHand(self, card):
        self.hand.append(card)

    def hasBusted(self):
        count = self.getHandCount()
        if type(count) == int:
            return count > 21
        else:
            return min(count) > 21

    def getSingleCount(self):
        hand_count = self.getHandCount()
        final_count = sys.maxsize

        if type(hand_count) != int:
            for count in hand_count:
                if count > 21:
                    continue
                if abs(count - 21) < abs(final_count - 21):
                    final_count = count
        else:
            final_count = hand_count

        return final_count


    def getHandCount(self):
        total_count = 0

        if any(card.symbol == "A" for card in self.hand): # returns list with the two possible counts
            total_count = [0,0]
            for card in self.hand:
                if card.symbol == 'J' or card.symbol == 'Q' or card.symbol == 'K':
                    total_count[0] += 10
                    total_count[1] += 10
                elif card.symbol != 'A':
                    total_count[0] += int(card.symbol)
                    total_count[1] += int(card.symbol)
                else: # "A"
                    total_count[0] += 1
                    if total_count[1] > 10:
                        total_count[1] += 1
                    else:
                        total_count[1] += 11
        else: # returns single int
            for card in self.hand:
                if card.symbol == 'J' or card.symbol == 'Q' or card.symbol == 'K':
                    total_count += 10
                else:
                    total_count += int(card.symbol)

        return total_count