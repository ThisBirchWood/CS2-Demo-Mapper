import pygame

class InfoRenderer:
    def __init__(self, screen, styling, match):
        self.screen = screen
        self.styling = styling
        self.match = match
        self.colour = self.styling["text_colour"]
        self.font = self.styling["font"]
        self.small_font = self.styling["small_font"]

        self.selected_player = None

    # Private methods
    def _render_player_info(self):
        """Draws the player info on the screen."""
        if self.selected_player is None:
            return

        player_info = f"Player: {self.selected_player.name}\n"
        player_info += f"Active Weapon: {self.selected_player.current_weapon}\n"
        player_info += f"Health: {self.selected_player.health}\n"

        text_surface = self.small_font.render(player_info, True, self.styling["text_colour"])
        self.screen.blit(text_surface, (10, 100))

    def _render_current_tick(self, match_tick, max_tick):
        text = self.font.render(f"Tick: {match_tick}/{max_tick}", True, self.colour)
        self.screen.blit(text, (10, 10))

    def _render_team_scores(self, team_1_score, team_2_score):
        text = self.font.render(f"Score: {team_1_score} - {team_2_score}", True, self.colour)
        self.screen.blit(text, (10, 40))

    # Public methods
    def render(self):
        """Renders the info on the screen."""
        self._render_player_info()
        self._render_current_tick(self.match.tick, self.match.max_tick)
        self._render_team_scores(self.match.team_1.score, self.match.team_2.score)