import pygame
from widgets.slider import HorizontalSlider
from models.match import Match
from controllers.map_coord_controller import MapCoordController
from render.player_renderer import PlayerRenderer
from render.text_renderer import TextRenderer
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

        self.player_render = PlayerRenderer(self.screen, self.match, self.map_coord_controller, self.small_font)
        self.text_render = TextRenderer(self.screen, self.match)

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

    def render(self):
        self.screen.fill((30, 30, 30))  # Clear screen
        self.map_coord_controller.update_screen_size(self.screen.get_width(), self.screen.get_height())
        self.render_slider()
        self.render_map()
        self.text_render.render()
        self.player_render.render()