import pygame
from match import Match
from player import Player
from utils import mapped_value

WIDTH, HEIGHT = 800, 600
FPS = 60

class Game:
    def __init__(self, match: Match):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 15)

        pygame.display.set_caption("CS2 Demo Mapper")

        self.clock = pygame.time.Clock()
        self.running = True

        self.match = match

    def handle_events(self):
        """Handles user inputs."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Updates game objects."""
        self.match.next_tick()

    def draw(self):
        """Draws everything on screen."""
        self.screen.fill((30, 30, 30))  # Clear screen

        # Draw current tick
        text = self.font.render(f"Tick: {self.match.tick}/{self.match.max_tick}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        for player in self.match.players:
            if player.dead:
                continue
            mapped_x = mapped_value(player.x, -4000, 4000, 0, WIDTH)
            mapped_y = mapped_value(player.y, -4000, 4000, 0, HEIGHT)
            pygame.draw.circle(self.screen, (255, 255, 255), (mapped_x, mapped_y), 5)

            # Draw player name
            text = self.small_font.render(player.name, True, (255, 255, 255))
            self.screen.blit(text, (mapped_x + 10, mapped_y))

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
    game_info = demo_parser.parse_ticks(["X", "Y", "Z", "pitch", "yaw", "is_alive", "team", "player_steamid"])
    players = demo_parser.parse_player_info()

    m = Match("de_dust2", game_info)
    for index, row in players.iterrows():
        m.add_player(Player(row["name"], row["steamid"]))

    game = Game(m)
    
    game.run()
