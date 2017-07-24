from generic_player import Generic_Player

class Dealer(Generic_Player):

    def __init__(self):
        super(Dealer, self).__init__([], 'Dealer')

    def shouldStop(self):
        return self.getSingleCount() >= 17