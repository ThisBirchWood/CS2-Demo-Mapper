from models.player import Player

CT_COLOUR = 'blue'
T_COLOUR = 'brown'

class Team:
    def __init__(self):
        self.players = []
        self.score = 0
        self.set_t()

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def set_ct(self):
        self.is_ct = True
        self.colour = CT_COLOUR

    def set_t(self):
        self.is_ct = False
        self.colour = T_COLOUR