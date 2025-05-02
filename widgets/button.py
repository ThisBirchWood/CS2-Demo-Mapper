import pygame

class Button:
    def __init__(self, x, y, width, height, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = None
        self.text = None
        self.action = action

        ## Default values
        self.font_size = 20
        self.colour = (255, 255, 255)
        self.pressed_colour = (200, 200, 200)
        self.font = pygame.font.Font(None, self.font_size)
        self.pressed = False
        self.border_radius = 3

    ## Getters and setters
    def get_font_size(self) -> int:
        return self.font_size
    
    def get_font(self) -> pygame.font.Font:
        return self.font
    
    def get_text(self) -> str:
        return self.text
    
    def get_border_radius(self) -> int:
        return self.border_radius
    
    def get_colour(self) -> tuple:
        return self.colour
    
    def get_pressed_colour(self) -> tuple:
        return self.pressed_colour
    
    def set_font_size(self, font_size: int) -> None:
        self.font_size = font_size

    def set_font(self, font: pygame.font.Font) -> None:
        self.font = font

    def set_text(self, text: str) -> None:
        self.text = text

    def set_border_radius(self, border_radius: int) -> None:
        self.border_radius = border_radius

    def set_colour(self, colour: tuple) -> None:
        self.colour = colour

    def set_pressed_colour(self, pressed_colour: tuple) -> None:
        self.pressed_colour = pressed_colour

    def set_image(self, image_path: str) -> None: 
        self._load_image(image_path)

    def set_action(self, action) -> None:
        self.action = action

    ## Private methods
    def _load_image(self, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def _draw_text(self, screen, text: str) -> None:
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def _button_press_down(self) -> None:
        self.pressed = True
        if self.action:
            self.action()

    def _button_press_up(self) -> None:
        self.pressed = False

    ## Public methods
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x <= event.pos[0] <= self.x + self.width and self.y <= event.pos[1] <= self.y + self.height:
                self._button_press_down()
        
        if self.pressed and event.type == pygame.MOUSEBUTTONUP:
                self._button_press_up()

    def draw(self, screen) -> None:
        if self.pressed:
            pygame.draw.rect(screen, self.pressed_colour, (self.x, self.y, self.width, self.height), border_radius=self.border_radius)
        else:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height), border_radius=self.border_radius)

        if self.image:
            screen.blit(self.image, (self.x, self.y))

        if self.text:
            self._draw_text(screen, self.text)
            
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((700, 700))

    def button_action():
        print("Button clicked!")

    button = Button(screen, 100, 100, 200, 50, button_action)
    button.set_text("Click Me")
    button.set_font_size(30)
    #button.set_image("assets/play-button.png")  # Replace with your image path

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button.handle_event(event)

        screen.fill((0, 0, 0))
        button.draw()
        pygame.display.flip()

    pygame.quit()