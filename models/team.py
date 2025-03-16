from models.player import Player

class Team:
    def __init__(self):
        self.players = []
        self.is_ct = False
        self.score = 0

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def set_ct(self, is_ct: bool):
        self.is_ct = is_ct