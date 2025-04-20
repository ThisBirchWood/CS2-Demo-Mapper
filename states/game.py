from states.game_state import GameState
from controllers.player_controller import PlayerController
from render.map_renderer import MapRenderer
from render.gui_renderer import GUIRenderer
from render.player_renderer import PlayerRenderer
from controllers.map_coord_controller import MapCoordController
from controllers.gui_controller import GUIController
import pygame

class Game(GameState):
    def __init__(self, switch_state_callback, context):
        super().__init__(switch_state_callback, context)

        match_data_path = "maps/" + self.match.map_name + ".json"
        match_image_path = "maps/" + self.match.map_name + ".png"

        #self.renderer = Renderer(self.match, self.screen, self.options)
        self.map_coord_controller = MapCoordController(self.screen.get_width(), self.screen.get_height(), match_data_path, match_image_path)

        # Renderers
        self.map_renderer = MapRenderer(self.screen, match_data_path, match_image_path)
        self.player_render = PlayerRenderer(self.screen, self.match, self.map_coord_controller, self.options)
        self.gui_render = GUIRenderer(self.screen, self.match)

        # Controllers
        self.player_controller = PlayerController(self.player_render, self.match)
        self.gui_controller = GUIController(self.gui_render)


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
        self.player_render.render()
        self.gui_render.render()