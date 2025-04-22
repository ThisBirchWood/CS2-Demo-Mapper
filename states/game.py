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

        # Game Box
        self.game_box = pygame.Surface((600, 600), pygame.SRCALPHA)
        self.game_box_top_left = (350, 0)

        # Helper Classes
        self.map_coord_controller = MapCoordConverter(self.game_box.get_width(), self.game_box.get_height(), match_data_path, match_image_path)

        # Renderers
        self.map_renderer = MapRenderer(self.game_box, match_data_path, match_image_path)
        self.player_renderer = PlayerRenderer(self.game_box, self.match, self.map_coord_controller, self.options)
        self.gui_render = GUIRenderer(self.screen, self.match)

        # Controllers
        self.player_controller = PlayerController(self.player_renderer, self.match, self.game_box_top_left)
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
        self.game_box.fill((0, 0, 0, 0))

        self.map_renderer.render()
        self.player_renderer.render()
        self.gui_render.render()
        self.screen.blit(self.game_box, self.game_box_top_left)