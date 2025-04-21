from states.game_state import GameState
from widgets.button import Button
from widgets.switch import Switch
import pygame

class SettingsMenu(GameState):
    def __init__(self, switch_state_callback, context):
        super().__init__(switch_state_callback, context)

        # Buttons
        self.back_button = Button(10, 10, 50, 50, lambda: self.switch_state(self.context["previous_states"].pop()))   
        self.back_button.set_text("Back")

        self.show_yaw_text = self.font.render("Show Yaw: ", True, (255, 255, 255))
        self.show_yaw_button = Switch(100, 100, 50, 50, self.options["show_yaw"])

        self.show_health_text = self.font.render("Show Health: ", True, (255, 255, 255))
        self.show_health_button = Switch(100, 150, 50, 50, self.options["show_health"])

    def handle_events(self, events):
        """Handles user inputs."""
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.switch_state("start_menu")
            self.show_yaw_button.handle_event(event)
            self.show_health_button.handle_event(event)
            self.back_button.handle_event(event)

    def update(self):
        """Updates settings based on user input."""
        if self.show_yaw_button.get_is_toggled():
            self.options["show_yaw"] = True
        else:
            self.options["show_yaw"] = False

        if self.show_health_button.get_is_toggled():
            self.options["show_health"] = True
        else:
            self.options["show_health"] = False

        # Save settings to context
        self.context["options"] = self.options

    def draw(self):
        """Renders the settings menu."""
        self.screen.fill((30, 30, 30))  # Clear screen
        self.screen.blit(self.show_yaw_text, (self.show_yaw_button.x + self.show_yaw_button.width + 10, 
                                               self.show_yaw_button.y))
        self.show_yaw_button.draw(self.screen)

        self.screen.blit(self.show_health_text, (self.show_health_button.x + self.show_health_button.width + 10,
                                                 self.show_health_button.y))
        self.show_health_button.draw(self.screen)

        self.back_button.draw(self.screen)


