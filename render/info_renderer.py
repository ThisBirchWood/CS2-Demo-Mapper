import pygame

class InfoRenderer:
    def __init__(self, screen, styling, match):
        self.screen = screen
        self.styling = styling
        self.match = match
        self.colour = self.styling["text_colour"]
        self.font = self.styling["font"]
        self.small_font = self.styling["small_font"]
        self.underline_bold_font = self.styling["underline_bold_font"]
        self.selected_player = None

        self.player_info_start_y = 100
        self.match_info_start_y = 400

    # Private methods
    def _render_player_info(self):
        """Draws the player info on the screen."""
        if self.selected_player is None:
            player_info_title = "No player selected\n"
            player_info = ""
        else:
            player_info_title = f"Player: {self.selected_player.name}\n"
            player_info = f"Active Weapon: {self.selected_player.current_weapon}\n"
            player_info += f"Health: {self.selected_player.health}\n"
            player_info += f"Armour: {self.selected_player.armour}\n"
            player_info += f"Kills: {self.selected_player.kills}\n"
            player_info += f"Deaths: {self.selected_player.deaths}\n"
            player_info += f"Assists: {self.selected_player.assists}\n"

        text_surface = self.underline_bold_font.render(player_info_title, True, self.styling["text_colour"])
        self.screen.blit(text_surface, (10, self.player_info_start_y))

        text_surface = self.small_font.render(player_info, True, self.styling["text_colour"])
        self.screen.blit(text_surface, (10, self.player_info_start_y + 50))

    def _render_match_info(self):
        """Draws the match info on the screen."""
        match_info_title = "Match Info\n"
        match_info = f"Map: {self.match.map_name}\n"
        match_info += f"Score: {self.match.team_1.score}-{self.match.team_2.score}\n"

        text_surface = self.underline_bold_font.render(match_info_title, True, self.styling["text_colour"])
        self.screen.blit(text_surface, (10, self.match_info_start_y))

        text_surface = self.small_font.render(match_info, True, self.styling["text_colour"])
        self.screen.blit(text_surface, (10, self.match_info_start_y + 50))

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
        self._render_match_info()