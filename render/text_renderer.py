import pygame

class TextRenderer:
    def __init__(self, screen, match):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.match = match

        self.colour = (255, 255, 255)

    def _render_current_tick(self, match_tick, max_tick):
        text = self.font.render(f"Tick: {match_tick}/{max_tick}", True, self.colour)
        self.screen.blit(text, (10, 10))

    def _render_team_scores(self, team_1_score, team_2_score):
        text = self.font.render(f"Score: {team_1_score} - {team_2_score}", True, self.colour)
        self.screen.blit(text, (10, 40))

    def render(self):
        self._render_current_tick(self.match.tick, self.match.max_tick)
        self._render_team_scores(self.match.team_1.score, self.match.team_2.score)
