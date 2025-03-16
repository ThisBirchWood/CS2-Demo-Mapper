from models.game import Game
from models.match import Match
from models.player import Player
from models.team import Team

def main():
    import demoparser2

    demo_parser = demoparser2.DemoParser("demo.dem")
    game_info = demo_parser.parse_ticks(["X", "Y", "Z", "pitch", "yaw", "is_alive", "team", "player_steamid", "team_rounds_total", "team_num"])
    header_info = demo_parser.parse_header()
    map_name = header_info['map_name']
    players = demo_parser.parse_player_info()

    team_1 = Team()
    team_1.set_ct()
    team_2 = Team()
    m = Match(map_name, game_info, team_1, team_2)
    m.tick = 1800
    for index, row in players.iterrows():
        if row["team_number"] == 2:
            team_1.add_player(Player(row["name"], row["steamid"]))
        elif row["team_number"] == 3: 
            team_2.add_player(Player(row["name"], row["steamid"]))

    game = Game(m)
    game.run()

if __name__ == "__main__":
    main()