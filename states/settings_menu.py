from states.game_state import GameState
from widgets.button import Button
from widgets.switch import Switch
from controllers.settings_controller import SettingsController
from render.settings_menu_renderer import SettingsMenuRenderer
import pygame

class SettingsMenu(GameState):
    def __init__(self, switch_state_callback, context):
        super().__init__(switch_state_callback, context)

        self.settings_renderer = SettingsMenuRenderer(self.screen, self.context["options"], self.font)
        self.settings_controller = SettingsController(self.settings_renderer, self.switch_state, context)

    def handle_events(self, events):
        """Handles user inputs."""
        for event in events:
            self.settings_controller.update(event)

    def update(self):
        """Updates settings based on user input."""
        if self.settings_renderer.show_yaw_button.get_is_toggled():
            self.options["show_yaw"] = True
        else:
            self.options["show_yaw"] = False

        if self.settings_renderer.show_health_button.get_is_toggled():
            self.options["show_health"] = True
        else:
            self.options["show_health"] = False

        if self.settings_renderer.show_names_button.get_is_toggled():
            self.options["show_names"] = True
        else:
            self.options["show_names"] = False

        # Save settings to context
        self.context["options"] = self.options

    def draw(self):
        """Renders the settings menu."""
        self.settings_renderer.render()


