import pygame
from widgets.break_slider import BreakSlider

class ControlRenderer:
    def __init__(self, screen, match):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.match = match
        self.colour = (255, 255, 255)

        self.slider = BreakSlider(self.screen, 50, 0, self.screen.get_width()-50, 20, 1, self.match.max_tick)
        self.slider.fill = True
        self.slider.set_breakpoints(self.match.round_start_times)
        self.slider.set_fill_colour((0,0,0))

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