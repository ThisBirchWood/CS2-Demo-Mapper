from models.player import Player

class Team:
    def __init__(self):
        self.players = []
        self.is_ct = False
        self.colour = 'brown'
        self.score = 0

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def set_ct(self):
        self.is_ct = True
        self.colour = 'blue'

    def set_t(self):
        self.is_ct = False
        self.colour = 'brown'