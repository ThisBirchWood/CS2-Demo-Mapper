from player import Player

class Match:
    def __init__(self, map_name, game_info):
        self.players = []
        self.map_name = map_name
        self.round = 0
        self.tick = 0
        self.max_tick = game_info.index[-1]
        self.game_info = game_info # pd dataframe sorted by tick

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def next_tick(self) -> None:
        self.tick += 1
        self._update_player_positions()

    def _update_player_positions(self) -> None:
        # inefficient, might need to change
        current_tick = self.game_info[self.game_info["tick"] == self.tick]
        for player in self.players:
            print("Updated player position of ", player.name)
            player.x = current_tick[current_tick["player_steamid"] == player.steam_id]["X"].values[0]
            player.y = current_tick[current_tick["player_steamid"] == player.steam_id]["Y"].values[0]
            player.z = current_tick[current_tick["player_steamid"] == player.steam_id]["Z"].values[0]
            player.pitch = current_tick[current_tick["player_steamid"] == player.steam_id]["pitch"].values[0]
            player.yaw = current_tick[current_tick["player_steamid"] == player.steam_id]["yaw"].values[0]
            player.dead = current_tick[current_tick["player_steamid"] == player.steam_id]["is_alive"].values[0] == 0
