from states.game_state import GameState
from controllers.player_controller import PlayerController
from render.map_renderer import MapRenderer
from render.gui_renderer import GUIRenderer
from render.player_renderer import PlayerRenderer
from utils.map_coord_converter import MapCoordConverter
from controllers.gui_controller import GUIController
import pygame

class Game(GameState):
    def __init__(self, switch_state_callback, context):
        super().__init__(switch_state_callback, context)

        match_data_path = f"maps/{self.match.map_name}.json"
        match_image_path = f"maps/{self.match.map_name}.png"

        # Map Coordinate Helper Class
        self.map_coord_controller = MapCoordConverter(self.screen.get_width(), self.screen.get_height(), match_data_path, match_image_path)

        # Renderers
        self.map_renderer = MapRenderer(self.screen, match_data_path, match_image_path)
        self.player_renderer = PlayerRenderer(self.screen, self.match, self.map_coord_controller, self.options)
        self.gui_render = GUIRenderer(self.screen, self.match)

        # Controllers
        self.player_controller = PlayerController(self.player_renderer, self.match)
        self.gui_controller = GUIController(self.gui_render, self.switch_state, self.context["previous_states"])


    def handle_events(self, events):
        """Handles user inputs."""
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.switch_state("menu")
            self.player_controller.update(event)
            self.gui_controller.update(event)

    def update(self):
        """Updates game objects."""
        self.match.next_tick()

    def draw(self):
        """Draws everything on screen."""
        self.screen.fill((0, 0, 0))
        self.map_renderer.render()
        self.player_renderer.render()
        self.gui_render.render()