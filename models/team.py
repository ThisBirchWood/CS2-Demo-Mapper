from models.player import Player

class Team:
    def __init__(self, is_ct=False):
        self.players = []
        self.is_ct = is_ct
        self.score = 0

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.remove(player)