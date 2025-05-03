from widgets.slider import HorizontalSlider
import pygame

class BreakSlider(HorizontalSlider):
    def __init__(self, screen, x, y, width, height, min_value, max_value):
        super().__init__(screen, x, y, width, height, min_value, max_value)
        self.breakpoints = []

        # defaults
        self.breakpoint_colour = (0, 0, 0)
        self.breakpoint_line_width = 2

    def add_breakpoint(self, breakpoint):
        if breakpoint < self.min_value or breakpoint > self.max_value:
            raise ValueError("Breakpoint must fit between min and max values")

        self.breakpoints.append(breakpoint)

    def set_breakpoints(self, breakpoints):
        self.breakpoints = breakpoints

    def _draw_breakpoints(self):
        for breakpoint in self.breakpoints:
            # create line
            break_x = self._value_to_knob(breakpoint)

            pygame.draw.line(self.screen, 
                             self.breakpoint_colour, 
                             (break_x, self.y), 
                             (break_x, self.y + self.height), 
                             width=self.breakpoint_line_width)

    def draw(self):
        self._draw_slider()
        self._draw_breakpoints()
        self._draw_knob()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    slider = BreakSlider(screen, 50, 50, 700, 20, 0, 1000)
    slider.add_breakpoint(100)
    slider.add_breakpoint(500)
    slider.add_breakpoint(700)
    running = True

    while running:
        screen.fill((0, 0, 0))
        slider.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            slider.handle_event(event)
