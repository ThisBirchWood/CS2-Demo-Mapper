from models.player import Player
from models.team import Team

class Match:
    def __init__(self, map_name, game_info, team_1: Team, team_2: Team, game_events, tick_rate=64):
        self.team_1 = team_1
        self.team_2 = team_2

        self.map_name = map_name
        self.game_events = game_events
        self.round_start_times = list(self.game_events[0][1]["tick"])

        self.tick = 1
        self.current_tick = game_info[game_info["tick"] == self.tick]

        self.round = self.current_tick["total_rounds_played"].values[0]

        self.max_tick = game_info["tick"].max()
        self.game_info = game_info.sort_values(by=["tick", "player_steamid"]) # pd dataframe sorted by tick
        self.tick_rate = tick_rate

    def _update_player(self, player: Player) -> None:
            player.x = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["X"].values[0]
            player.y = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["Y"].values[0]
            player.z = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["Z"].values[0]
            player.pitch = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["pitch"].values[0]
            player.yaw = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["yaw"].values[0]
            player.dead = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["is_alive"].values[0] == 0
            player.is_shooting = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["shots_fired"].values[0]
            player.health = int(self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["health"].values[0])
            player.armour = int(self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["armor_value"].values[0])
            player.current_weapon = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["active_weapon_name"].values[0]
            player.kills = int(self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["kills_total"].values[0])
            player.deaths = int(self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["deaths_total"].values[0])
            player.assists = int(self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["assists_total"].values[0])
            player.inventory = self.current_tick[self.current_tick["player_steamid"] == player.steam_id]["inventory"].values[0]

            if "C4 Explosive" in player.inventory:
                player.has_bomb = True
            else:
                player.has_bomb = False

            if "Defuse Kit" in player.inventory:
                player.has_defuser = True
            else:
                player.has_defuser = False

    def _update_players(self) -> None:
        # empty tick
        if self.current_tick.empty:
            return
        
        for player in self.get_players():
            self._update_player(player)

    def _update_round(self) -> None:
        if self.current_tick.empty:	
            return
        
        self.round = self.current_tick["total_rounds_played"].values[0]
        
        self.team_1.score = int(self.current_tick[self.current_tick["team_num"] == self.team_1.id]["team_rounds_total"].values[0])
        self.team_2.score = int(self.current_tick[self.current_tick["team_num"] == self.team_2.id]["team_rounds_total"].values[0])

    def _update_team_ids(self) -> None:
        # get random player from each team
        if self.current_tick.empty:
            return

        for team in self.get_teams():
            random_player = team.players[0]
            player_team_id = self.current_tick[self.current_tick["player_steamid"] == random_player.steam_id]["team_num"].values[0]

            if player_team_id == 2:
                team.set_t()
            elif player_team_id == 3:
                team.set_ct()

    def next_tick(self) -> None:
        self.tick += 1
        self.current_tick = self.game_info[self.game_info["tick"] == self.tick]
        self._update_players()
        self._update_team_ids()
        self._update_round()

    def set_tick(self, tick: int) -> None:
        self.tick = tick
        self.current_tick = self.game_info[self.game_info["tick"] == self.tick]
        self._update_players()
        self._update_round()

    def get_players(self) -> list[Player]:
        return self.team_1.players + self.team_2.players
    
    def get_teams(self) -> list[Team]:
        return [self.team_1, self.team_2]