import pygame

class Switch:
    def __init__(self, x, y, width, height, default_value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect_offset = 0

        ## Default values
        self.is_toggled = default_value
        self.background_colour = (211,211,211)
        self.foreground_colour = (150, 150, 150)
        self.active_border_colour = (255, 0, 0)
        self.border_width = 1
        self.border_radius = 3
        self.toggle_speed = 5

    ## Getters and Setters
    def get_is_toggled(self):
        return self.is_toggled

    def get_background_colour(self):
        return self.background_colour
    
    def get_foreground_colour(self):
        return self.foreground_colour
    
    def get_border_width(self):
        return self.border_width
    
    def get_border_radius(self):
        return self.border_radius
    
    def get_toggle_speed(self):
        return self.toggle_speed
    
    def set_is_toggled(self, value: bool):
        self.is_toggled = value
    
    def set_background_colour(self, colour):
        self.background_colour = colour

    def set_foreground_colour(self, colour):
        self.foreground_colour = colour

    def set_border_width(self, width):
        self.border_width = width

    def set_border_radius(self, radius):
        self.border_radius = radius

    def set_toggle_speed(self, speed):
        self.toggle_speed = speed

    ## Private methods
    def _press(self):
        """Toggle the switch state."""
        if self.is_toggled == True:
            self.is_toggled = False
        else:
            self.is_toggled = True

    ## Public methods
    def handle_event(self, event):
        """Handle mouse events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                self._press()

    def draw(self, screen):
        # Move the rectangle to right over time if toggled
        if self.is_toggled and self.rect_offset < (self.width // 2):
            self.rect_offset += self.toggle_speed
        elif not self.is_toggled and self.rect_offset > 0:
            # Move the rectangle to left over time if not toggled
            self.rect_offset -= self.toggle_speed
        elif self.is_toggled:
            # Draw border
            pygame.draw.rect(screen, self.active_border_colour, (self.x-self.border_width, 
                                        self.y-self.border_width, 
                                        self.width+(self.border_width*2), 
                                        self.height+(self.border_width*2)), 
                                        border_radius=self.border_radius)
        # Draw the switch background
        pygame.draw.rect(screen, self.background_colour, (self.x, self.y, self.width, self.height), border_radius=self.border_radius)

        # Draw the switch foreground
        pygame.draw.rect(screen, self.foreground_colour, (self.x + self.rect_offset, self.y, self.width // 2, self.height), border_radius=self.border_radius)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    switch = Switch(100, 100, 50, 25, False)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            switch.handle_event(event)

        screen.fill((0, 0, 0))
        switch.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



