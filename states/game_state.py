class GameState:
    def __init__(self, switch_state_callback, screen):
        self.switch_state = switch_state_callback
        self.screen = screen

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self):
        pass