from models.player import Player
from models.team import Team

class Match:
    def __init__(self, map_name, game_info, team_1: Team, team_2: Team, tick_rate=64):
        self.team_1 = team_1
        self.team_2 = team_2

        self.map_name = map_name

        self.tick = 1
        self.current_tick = game_info[game_info["tick"] == self.tick]

        self.round = self.current_tick["team_rounds_total"].values[0]

        self.max_tick = game_info["tick"].max()
        self.game_info = game_info.sort_values(by=["tick", "player_steamid"]) # pd dataframe sorted by tick
        self.tick_rate = tick_rate

    def _update_player_positions(self) -> None:
        # inefficient, might need to change
        
        # empty tick
        if self.current_tick.empty:
            return

        for player in self.get_players():
            player.x = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["X"].values[0]
            player.y = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["Y"].values[0]
            player.z = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["Z"].values[0]
            player.pitch = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["pitch"].values[0]
            player.yaw = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["yaw"].values[0]
            player.dead = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["is_alive"].values[0] == 0

    def _update_round(self) -> None:
        if self.current_tick.empty:	
            return
        
        self.round = self.current_tick["team_rounds_total"].values[0]
        
        if self.round >= 8:
            self.team_1.set_t()
            self.team_2.set_ct()
            self.team_1.score = int(self.current_tick[self.current_tick["team_num"] == 3]["team_rounds_total"].values[0])
            self.team_2.score = int(self.current_tick[self.current_tick["team_num"] == 2]["team_rounds_total"].values[0])
        else:
            self.team_1.set_ct()
            self.team_2.set_t()
            self.team_1.score = int(self.current_tick[self.current_tick["team_num"] == 2]["team_rounds_total"].values[0])
            self.team_2.score = int(self.current_tick[self.current_tick["team_num"] == 3]["team_rounds_total"].values[0])

    def next_tick(self) -> None:
        self.tick += 1
        self.current_tick = self.game_info[self.game_info["tick"] == self.tick]
        self._update_player_positions()
        self._update_round()

    def get_players(self) -> list[Player]:
        return self.team_1.players + self.team_2.players
    
    def get_teams(self) -> list[Team]:
        return [self.team_1, self.team_2]