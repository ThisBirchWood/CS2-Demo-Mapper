import time
from states.game_state import GameState
from controllers.player_controller import PlayerController
from render.map_renderer import MapRenderer
from render.gui_renderer import GUIRenderer
from render.player_renderer import PlayerRenderer
from render.info_renderer import InfoRenderer
from render.control_renderer import ControlRenderer
from utils.map_coord_converter import MapCoordConverter
from controllers.gui_controller import GUIController
from controllers.info_controller import InfoController
from controllers.control_controller import ControlController
import pygame

class Game(GameState):
    def __init__(self, switch_state_callback, context):
        super().__init__(switch_state_callback, context)

        self.match_data_path = f"assets/maps/config/{self.match.map_name}.json"
        self.match_image_path = f"assets/maps/overview/{self.match.map_name}.png"
        
        self.game_update_interval = 1 / self.match.tick_rate
        self.elapsed_time = 0
        self.last_time = time.perf_counter()

        self.__init_screen_areas()
        self.__init_utils()
        self.__init_renderers()
        self.__init_controllers()

    def __init_screen_areas(self):
        self.info_box = pygame.Surface((350, self.screen.get_height()), pygame.SRCALPHA)
        self.info_box_top_left = (0, 0)

        self.game_box = pygame.Surface((650, 650), pygame.SRCALPHA)
        self.game_box_top_left = (350, 0)

        self.control_box = pygame.Surface((650, 120), pygame.SRCALPHA)
        self.control_box_top_left = (350, 650)

    def __init_utils(self):
        self.map_coord_controller = MapCoordConverter(self.game_box.get_width(), self.game_box.get_height(), self.match_data_path, self.match_image_path)

    def __init_renderers(self):
        self.map_renderer = MapRenderer(self.game_box, self.match_data_path, self.match_image_path)
        self.player_renderer = PlayerRenderer(self.game_box, self.match, self.map_coord_controller, self.options, self.styling)
        self.gui_render = GUIRenderer(self.screen, self.match)
        self.info_render = InfoRenderer(self.info_box, self.styling, self.match)
        self.control_render = ControlRenderer(self.control_box, self.match)

    def __init_controllers(self):
        self.player_controller = PlayerController(self.player_renderer, self.match, self.game_box_top_left)
        self.gui_controller = GUIController(self.gui_render, self.switch_state)
        self.info_controller = InfoController(self.info_render, self.player_controller)
        self.control_controller = ControlController(self.control_render, self.control_box_top_left)

    def handle_events(self, events):
        """Handles user inputs."""
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.switch_state("menu")
            self.player_controller.update(event)
            self.gui_controller.update(event)
            self.info_controller.update(event)
            self.control_controller.update(event)

    def update(self):
        """Fixed-timestep update decoupled from frame rate."""
        now = time.perf_counter()
        delta = now - self.last_time
        self.last_time = now
        self.elapsed_time += delta

        while self.elapsed_time >= self.game_update_interval:
            self.match.next_tick()
            self.elapsed_time -= self.game_update_interval

    def draw(self):
        """Draws everything on screen."""
        self.screen.fill(self.styling["background_colour"])
        self.game_box.fill(self.styling["background_colour"])
        self.info_box.fill(self.styling["foreground_colour"])
        self.control_box.fill(self.styling["background_colour"])

        self.map_renderer.render()
        self.player_renderer.render()
        self.gui_render.render()
        self.info_render.render()
        self.control_render.render()
        self.screen.blit(self.info_box, self.info_box_top_left)
        self.screen.blit(self.control_box, self.control_box_top_left)
        self.screen.blit(self.game_box, self.game_box_top_left)