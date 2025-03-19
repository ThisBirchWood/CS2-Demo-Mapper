import pygame
from models.match import Match
from models.player import Player
from models.team import Team
from render.renderer import Renderer

WIDTH, HEIGHT = 700,700
FPS = 60

class Game:
    def __init__(self, match: Match):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 15)

        pygame.display.set_caption("CS2 Demo Mapper")

        self.clock = pygame.time.Clock()
        self.running = True

        self.match = match
        self.renderer = Renderer(self.match, self.screen)
        

    def handle_events(self):
        """Handles user inputs."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.renderer.slider.handle_event(event)

    def update(self):
        """Updates game objects."""
        self.match.next_tick()

    def draw(self):
        """Draws everything on screen."""
        self.renderer.render()

        pygame.display.flip()  # Update display

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.match.tick_rate)

        pygame.quit()

if __name__ == "__main__":
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
