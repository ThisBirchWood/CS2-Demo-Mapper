from states.game_state import GameState
from render.renderer import Renderer
from controllers.player_controller import PlayerController
import pygame

class Game(GameState):
    def __init__(self, switch_state_callback, context):
        super().__init__(switch_state_callback, context)

        self.renderer = Renderer(self.match, self.screen)
        self.player_controller = PlayerController(self.renderer.player_render, self.match)

    def handle_events(self, events):
        """Handles user inputs."""
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.switch_state("menu")
            self.renderer.slider.handle_event(event)
            self.player_controller.update(event)

    def update(self):
        """Updates game objects."""
        self.match.next_tick()

    def draw(self):
        """Draws everything on screen."""
        self.renderer.render()
        pygame.display.flip()