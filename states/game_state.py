import pygame

class GameState:
    def __init__(self, switch_state_callback, context: dict):
        self.switch_state = switch_state_callback
        self.context = context
        self.screen = self.context.get("screen")
        self.match = self.context.get("match", None)
        self.small_font = self.context.get("small_font", pygame.font.Font(None, 15))
        self.options = self.context.get("options", {
            "show_yaw": True
        })
        self.styling = self.context.get("styling", None)

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self):
        pass