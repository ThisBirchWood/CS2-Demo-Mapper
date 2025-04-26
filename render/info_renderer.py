import pygame

class InfoRenderer:
    def __init__(self, screen, styling):
        self.screen = screen
        self.styling = styling
        self.font = self.styling["small_font"]

        self.selected_player = None

    # Private methods
    def _draw_player_info(self):
        """Draws the player info on the screen."""
        if self.selected_player is None:
            return

        player_info = f"Player: {self.selected_player.name}\n"
        player_info += f"Active Weapon: {self.selected_player.current_weapon}\n"
        player_info += f"Health: {self.selected_player.health}\n"

        text_surface = self.font.render(player_info, True, self.styling["text_colour"])
        self.screen.blit(text_surface, (10, 100))

    # Public methods
    def render(self):
        """Renders the info on the screen."""
        self._draw_player_info()