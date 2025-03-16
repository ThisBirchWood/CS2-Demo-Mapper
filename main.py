from models.game import Game
from models.match import Match
from models.player import Player
from models.team import Team

def main():
    import demoparser2

    demo_parser = demoparser2.DemoParser("demo.dem")
    game_info = demo_parser.parse_ticks(["X", "Y", "Z", "pitch", "yaw", "is_alive", "team", "player_steamid", "team_rounds_total"])
    header_info = demo_parser.parse_header()
    map_name = header_info['map_name']
    players = demo_parser.parse_player_info()

    start_tick = int(input())
    team_1 = Team()
    team_2 = Team()
    m = Match(map_name, game_info, team_1, team_2)
    m.tick = start_tick
    for index, row in players.iterrows():
        if row["team_number"] == 1:
            team_1.add_player(Player(row["name"], row["steamid"]))
        else: 
            team_2.add_player(Player(row["name"], row["steamid"]))

    game = Game(m)
    
    game.run()

if __name__ == "__main__":
    main()