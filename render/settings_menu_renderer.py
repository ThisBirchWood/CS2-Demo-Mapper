import pygame
from widgets.button import Button
from widgets.switch import Switch

class SettingsMenuRenderer:
    def __init__(self, screen, options, font):
        self.screen = screen
        self.options = options
        self.font = font
        self.text_start_x = 100
        self.widget_start_x = 500

        # Text
        self.show_yaw_text = self.font.render("Show Yaw: ", True, (255, 255, 255))
        self.show_health_text = self.font.render("Show Health: ", True, (255, 255, 255))
        self.show_names_text = self.font.render("Show Names: ", True, (255, 255, 255))

        # Buttons
        self.back_button = Button(10, 10, 50, 50, None)   
        self.back_button.set_image("assets/arrow.png")

        # Switches
        self.show_yaw_button = Switch(self.widget_start_x, 100, 100, self.show_yaw_text.get_rect().height, self.options["show_yaw"])
        self.show_health_button = Switch(self.widget_start_x, 150, 100, self.show_health_text.get_rect().height, self.options["show_health"])
        self.show_names_button = Switch(self.widget_start_x, 200, 100, self.show_names_text.get_rect().height, self.options["show_names"])

    def render(self):
        """Renders the settings menu."""
        self.screen.fill((30, 30, 30))  # Clear screen
        self.screen.blit(self.show_yaw_text, (self.text_start_x, self.show_yaw_button.y))
        self.show_yaw_button.draw(self.screen)

        self.screen.blit(self.show_health_text, (self.text_start_x, self.show_health_button.y))
        self.show_health_button.draw(self.screen)

        self.screen.blit(self.show_names_text, (self.text_start_x, self.show_names_button.y))
        self.show_names_button.draw(self.screen)

        self.back_button.draw(self.screen)
