import pygame
from widgets.button import Button

class GUIRenderer:
    def __init__(self, screen, match):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.match = match


        # Buttons
        self.settings_button = Button(self.screen.get_width()-40, 10, 30, 30, None)
        self.settings_button.set_image("assets/images/setting.png")

        self.back_button = Button(self.screen.get_width()-80, 10, 30, 30, None)
        self.back_button.set_image("assets/images/arrow.png")

        self.colour = (255, 255, 255)

    def _render_buttons(self):
        self.settings_button.draw(self.screen)
        self.back_button.draw(self.screen)


    def render(self):
        self._render_buttons()
