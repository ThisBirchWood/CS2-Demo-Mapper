import pygame
from widgets.slider import HorizontalSlider

class ControlRenderer:
    def __init__(self, screen, match):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.match = match
        self.colour = (255, 255, 255)

        self.slider = HorizontalSlider(self.screen, 50, 0, self.screen.get_width()-50, 20, 1, self.match.max_tick)

    def _render_slider(self):
        # Update slider value
        if self.slider.dragging:
            # Set match tick if slider is being dragged
            self.match.set_tick(int(self.slider.value))
        else:
            # Set slider value if slider is not being dragged
            self.slider.set_value(self.match.tick)
        self.slider.draw()

    def render(self):
        self._render_slider()