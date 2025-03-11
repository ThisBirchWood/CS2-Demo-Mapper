from player import Player

class Match:
    def __init__(self, map_name, game_info, tick_rate=64):
        self.players = []
        self.map_name = map_name

        self.tick = 1
        self.current_tick = game_info[game_info["tick"] == self.tick]

        self.round = self.current_tick["team_rounds_total"].values[0]

        self.max_tick = game_info.index[-1]
        self.game_info = game_info # pd dataframe sorted by tick
        self.tick_rate = tick_rate

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def next_tick(self) -> None:
        self.tick += 1
        self.current_tick = self.game_info[self.game_info["tick"] == self.tick]
        self._update_player_positions()
        self._update_round()

    def _update_player_positions(self) -> None:
        # inefficient, might need to change
        
        # empty tick
        if self.current_tick.empty:
            return

        for player in self.players:
            player.x = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["Y"].values[0]
            player.y = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["X"].values[0]
            player.z = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["Z"].values[0]
            player.pitch = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["pitch"].values[0]
            player.yaw = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["yaw"].values[0]
            player.dead = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["is_alive"].values[0] == 0

    def _update_round(self) -> None:
        if self.current_tick.empty:	
            return
        self.round = self.current_tick["team_rounds_total"].values[0]