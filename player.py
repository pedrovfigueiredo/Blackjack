from generic_player import Generic_Player

class Player(Generic_Player):

    betting_amount = 0

    def __init__(self, total_money, name):
        super(Player,self).__init__([], name)
        self.total_money = total_money
        self.stopped_playing = False

