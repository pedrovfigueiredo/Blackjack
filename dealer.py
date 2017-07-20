from generic_player import Generic_Player

class Dealer(Generic_Player):

    def __init__(self, total_money):
        super(Dealer, self).__init__([],total_money, 'Dealer')

    def shouldStop(self):
        return self.getSingleCount() >= 17