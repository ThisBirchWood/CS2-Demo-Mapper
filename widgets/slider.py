import pygame

class HorizontalSlider:
    def __init__(self, screen, x, y, width, height, min_value, max_value):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value

        self.background_colour = (255, 255, 255)
        self.knob_colour = (255, 0, 0)

        self.knob_radius = 10
        self.knob_x = self.x
        self.dragging = False

    def handle_event(self, event):
        """Handle mouse events for dragging"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] >= self.x and event.pos[0] <= self.x + self.width and event.pos[1] >= self.y and event.pos[1] <= self.y + self.height:
                self.knob_x = event.pos[0]
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            if event.pos[0] >= self.x and event.pos[0] <= self.x + self.width:
                self.knob_x = event.pos[0]
                self.value = self.min_value + ((self.max_value - self.min_value) * ((self.knob_x - self.x) / self.width))

    def draw(self):
        pygame.draw.rect(self.screen, self.background_colour, (self.x, self.y, self.width, self.height))
        pygame.draw.circle(self.screen, self.knob_colour, (int(self.knob_x), self.y + self.height // 2), self.knob_radius)

    def set_value(self, value):
        self.value = int(value)
        if value < self.min_value:
            self.value = self.min_value
        elif value > self.max_value:
            self.value = self.max_value
        else:
            self.value = value

        self.knob_x = self.x + (self.width * ((self.value - self.min_value) / (self.max_value - self.min_value)))

    def set_radius(self, radius):
        self.knob_radius = radius

    def set_background_colour(self, colour):
        self.background_colour = colour

    def set_knob_colour(self, colour):
        self.knob_colour = colour

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    slider = HorizontalSlider(screen, 50, 50, 700, 20, 0, 1000)
    running = True

    while running:
        screen.fill((0, 0, 0))
        slider.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            slider.handle_event(event)

    
    