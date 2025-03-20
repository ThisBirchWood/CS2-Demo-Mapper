import pygame

class Button:
    def __init__(self, screen, x, y, width, height, image_path, colour, action):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._load_image(image_path)
        self.colour = colour
        self.action = action

        self.active = False

    def _load_image(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x <= event.pos[0] <= self.x + self.width and self.y <= event.pos[1] <= self.y + self.height:
                self.active = not self.active
                self.action()

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.width, self.height))
        self.screen.blit(self.image, (self.x, self.y))

    def set_image(self, image_path: str):
        self._load_image(image_path)

    def set_action(self, action):
        self.action = action

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((700, 700))

    def play_pause(button):
        if button.active:
            button.set_image("../assets/pause-button.png")
        else:
            button.set_image("../assets/play-button.png")


    button = Button(screen, 100, 100, 100, 100, "../assets/play-button.png", (255, 0, 0), lambda: play_pause(button))

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