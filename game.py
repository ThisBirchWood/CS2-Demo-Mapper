import pygame
from match import Match
from player import Player
from map_coord_controller import MapCoordController
from image_coord_controller import ImageCoordController
from json_object import JSONObject
from utils import mapped_value

WIDTH, HEIGHT = 700, 700
MAP_WIDTH, MAP_HEIGHT = 1024,1024
MAP_MIDDLE_X, MAP_MIDDLE_Y = 650, 320
MAP_SCALE = 0.6
MAP_ROTATION = 270
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

        try:
            self.json_object = JSONObject(f"maps/{match.map_name}.json")
        except FileNotFoundError:
            raise NotImplementedError(f"Map {match.map_name} not implemented.")
        
        self.image_path = self.json_object.get("image_path")
        self.image_width = self.json_object.get("image_width")
        self.image_height = self.json_object.get("image_height")
        self.ingame_zero_x = self.json_object.get("middle_x")
        self.ingame_zero_y = self.json_object.get("middle_y")
        self.rotation_degrees = self.json_object.get("rotation")
        self.scaler = self.json_object.get("scale")
    
        self.map_coord_controller = MapCoordController(WIDTH, HEIGHT, -3000, 3000, -3000, 3000)
        self.image_coord_controller = ImageCoordController(self.image_width, self.image_height, WIDTH, HEIGHT, self.ingame_zero_x, self.ingame_zero_y)
        self.image_coord_controller.scale(self.scaler)
        self.image_coord_controller.rotate(self.rotation_degrees)

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
        
        # Draw map from image
        map_image = pygame.image.load(self.image_path)

        # Scale and rotate map image
        map_image = pygame.transform.scale(map_image, (self.image_width*self.scaler, self.image_height*self.scaler))
        map_image = pygame.transform.rotate(map_image, self.rotation_degrees)

        # Draw map image
        self.screen.blit(map_image, self.image_coord_controller.top_left_screen())

        # Draw current tick
        text = self.font.render(f"Tick: {self.match.tick}/{self.match.max_tick}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        # Draw current round
        text = self.font.render(f"Round: {self.match.round}", True, (255, 255, 255))
        self.screen.blit(text, (10, 50))

        for player in self.match.players:
            if player.dead:
                continue
            mapped_x, mapped_y = self.map_coord_controller.map_to_screen(player.x, player.y)
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
    game_info = demo_parser.parse_ticks(["X", "Y", "Z", "pitch", "yaw", "is_alive", "team", "player_steamid", "team_rounds_total"])
    header_info = demo_parser.parse_header()
    map_name = header_info['map_name']
    players = demo_parser.parse_player_info()

    start_tick = int(input())
    m = Match(map_name, game_info)
    m.tick = start_tick
    for index, row in players.iterrows():
        m.add_player(Player(row["name"], row["steamid"]))

    game = Game(m)
    
    game.run()
