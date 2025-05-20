from models.player import Player

CT_COLOUR = 'blue'
T_COLOUR = 'brown'

class Team:
    def __init__(self):
        self.players = []
        self.score = 0
        self.id = 1
        self.set_ct()

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def set_ct(self):
        self.id = 3
        self.colour = CT_COLOUR

    def set_t(self):
        self.id = 2
        self.colour = T_COLOUR