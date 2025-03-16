import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from models.match import Match
from models.player import Player
from models.team import Team
from controllers.map_coord_controller import MapCoordController
from controllers.image_coord_controller import ImageCoordController
from utils.json_object import JSONObject

class Renderer:
    def __init__(self, match: Match, screen):
        self.screen = screen
        self.match = match
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 15)

        try:
            self.json_object = JSONObject(f"maps/{match.map_name}.json")
        except FileNotFoundError:
            raise NotImplementedError(f"Map {match.map_name} not implemented.")
        
        self.image_path = self.json_object.get("image_path")
        self.image_path = self.json_object.get("image_path")
        self.image_width = self.json_object.get("image_width")
        self.image_height = self.json_object.get("image_height")
        self.ingame_zero_x = self.json_object.get("middle_x")
        self.ingame_zero_y = self.json_object.get("middle_y")
        self.rotation_degrees = self.json_object.get("rotation")
        self.scaler = self.json_object.get("scale")
    
        self.map_coord_controller = MapCoordController(self.screen.get_width(), self.screen.get_height(), 
                                                       -3000, 3000, -3000, 3000)
        self.image_coord_controller = ImageCoordController(self.image_width, self.image_height,
                                                           self.screen.get_width(), self.screen.get_height(), 
                                                           self.ingame_zero_x, self.ingame_zero_y)
        self.image_coord_controller.scale(self.scaler)
        self.image_coord_controller.rotate(self.rotation_degrees)

    def render_players(self):
        """Draws everything on screen."""
        for player in self.match.get_players():
            if player.dead:
                continue
            mapped_x, mapped_y = self.map_coord_controller.map_to_screen(player.x, player.y)
            pygame.draw.circle(self.screen, (255, 255, 255), (mapped_x, mapped_y), 5)

            # Draw player name
            text = self.small_font.render(player.name, True, (255, 255, 255))
            self.screen.blit(text, (mapped_x + 10, mapped_y))

        pygame.display.flip()  # Update display

    def render_text(self):
        # Draw current tick
        text = self.font.render(f"Tick: {self.match.tick}/{self.match.max_tick}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        # Draw team scores
        text = self.font.render(f"Score: {self.match.team_1.score} - {self.match.team_2.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 40))

    def render_map(self):
        # Draw map from image
        map_image = pygame.image.load(self.image_path)

        # Scale and rotate map image
        map_image = pygame.transform.scale(map_image, (self.image_width*self.scaler, self.image_height*self.scaler))
        map_image = pygame.transform.rotate(map_image, self.rotation_degrees)

        # Draw map image
        self.screen.blit(map_image, self.image_coord_controller.top_left_screen())

    '''
        def render_slider(self):
            # Create slider
            slider = Slider(self.screen, 100, 100, 400, 20, min=1, max=self.match.max_tick, step=1, initial=self.match.tick, 
                                            handleRadius=10, handleColour=(255, 255, 255), handleOutline=(255, 255, 255), 
                                            sliderColour=(100, 100, 100), sliderMarkColour=(150, 150, 150), 
                                            font=pygame.font.Font(None, 36), textColour=(255, 255, 255), 
                                            valueColour=(255, 255, 255), valueOutlineColour=(255, 255, 255), 
                                            onSlide=self.on_slide, sliderMark=0)
    '''

    def render(self):
        self.screen.fill((30, 30, 30))  # Clear screen
        self.render_map()
        self.render_text()
        self.render_players()