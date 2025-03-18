import math
import pygame
from widgets.slider import HorizontalSlider
from pygame_widgets.slider import Slider
from models.match import Match
from models.player import Player
from models.team import Team
from controllers.map_coord_controller import MapCoordController
from utils.json_object import JSONObject

class Renderer:
    def __init__(self, match: Match, screen):
        self.screen = screen
        self.match = match
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 15)

        # Load map data from json file
        try:
            self.json_object = JSONObject(f"maps/{match.map_name}.json")
        except FileNotFoundError:
            raise NotImplementedError(f"Map {match.map_name} not implemented.")
        
        # Load map data from json object
        self.top_left_x = self.json_object.get("pos_x")
        self.top_left_y = self.json_object.get("pos_y")
        self.scale = self.json_object.get("scale")
        self.rotation = self.json_object.get("rotate")
        self.image_path = self.json_object.get("material")

        # Load map image
        self.map_image = pygame.image.load(self.image_path)
        self.image_width = self.map_image.get_width()
        self.image_height = self.map_image.get_height()

        # Calculate bottom right coordinates for map coord controller
        self.bottom_right_x = self.top_left_x + (self.image_width * self.scale)
        self.bottom_right_y = self.top_left_y - (self.image_height * self.scale)
        
    
        self.map_coord_controller = MapCoordController(self.screen.get_width(), self.screen.get_height(), 
                                                       self.top_left_x, self.bottom_right_x, self.top_left_y, self.bottom_right_y)
        
        self.slider = HorizontalSlider(self.screen, 50, 650, self.screen.get_width()-100, 20, 1, self.match.max_tick)
        #self.slider.fill = True

    def render_players(self):
        """Draws everything on screen."""
        # Update screen size if it has changed
        self.map_coord_controller.update_screen_size(self.screen.get_width(), self.screen.get_height())

        # loop through the teams and each of their players
        for team in self.match.get_teams():
            for player in team.players:
                # Draw player if they are alive
                if player.dead:
                    continue
                
                self._render_player(player, team)
                self._render_player_yaw(player, team)

    #def render_player_path(self):


    def render_text(self):
        # Draw current tick
        text = self.font.render(f"Tick: {self.match.tick}/{self.match.max_tick}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        # Draw team scores
        text = self.font.render(f"Score: {self.match.team_1.score} - {self.match.team_2.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 40))

    def render_map(self):
        # Scale and rotate map image
        self.map_image = pygame.transform.scale(self.map_image, (self.screen.get_width(), self.screen.get_height()))

        # Draw map image
        self.screen.blit(self.map_image, (0, 0))

    def render_slider(self):
        # Update slider value
        if self.slider.dragging:
            # Set match tick if slider is being dragged
            self.match.set_tick(int(self.slider.value))
        else:
            # Set slider value if slider is not being dragged
            self.slider.set_value(self.match.tick)
        self.slider.draw()

    def _render_player(self, player: Player, team: Team):
        mapped_x, mapped_y = self.map_coord_controller.map_to_screen(player.x, player.y)
        pygame.draw.circle(self.screen, team.colour, (mapped_x, mapped_y), 5)
        text = self.small_font.render(player.name, True, (255, 255, 255))
        self.screen.blit(text, (mapped_x-10, mapped_y-15))

    def _render_player_yaw(self, player: Player, team: Team):
        if player.is_shooting:

            mapped_x, mapped_y = self.map_coord_controller.map_to_screen(player.x, player.y)
            player_yaw = math.radians(player.yaw)
            end_x = mapped_x + (100 * math.cos(player_yaw))
            end_y = mapped_y - (100 * math.sin(player_yaw))
            pygame.draw.line(self.screen, team.colour, (mapped_x, mapped_y), (end_x, end_y), 2)

    def render(self):
        self.screen.fill((30, 30, 30))  # Clear screen
        self.render_map()
        self.render_text()
        self.render_players()
        self.render_slider()