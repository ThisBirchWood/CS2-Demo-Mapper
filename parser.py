import demoparser2
from match import Match
from player import Player

demo_parser = demoparser2.DemoParser("demo.dem")
demo_info = demo_parser.parse_ticks(["X", "Y", "Z"])

class Parser:
    def __init__(self, demo_path):
        self.demo_parser = demoparser2.DemoParser(demo_path)
        self.demo_info = self.demo_parser.parse_ticks(["X", "Y", "Z", "pitch", "yaw", "is_alive", "team", "player_steamid"])

        self.players = self.demo_parser.parse_player_info()

if __name__ == "__main__":
    parser = Parser("demo.dem")
    match = Match("de_dust2", parser.demo_info)

    for index, row in parser.players.iterrows():
        match.add_player(Player(row["name"], row["steamid"]))

    while match.tick < match.max_tick:
        match.next_tick()

    



    
