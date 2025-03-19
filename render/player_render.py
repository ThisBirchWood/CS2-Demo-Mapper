import pygame, math
from models.match import Match
from utils.utils import mapped_value

class PlayerRender:
    def __init__(self, screen, match: Match, map_coord_controller, player_font):
        self.screen = screen
        self.match = match
        self.map_coord_controller = map_coord_controller
        self.player_font = player_font

        self.player_radius = 5

        self.health_bar_foreground = (0, 255, 0)
        self.health_bar_background = (255, 0, 0)

    def _render_circle(self, player, team):
        x, y = self.map_coord_controller.map_to_screen(player.x, player.y)
        pygame.draw.circle(self.screen, team.colour, (x, y), self.player_radius)

    def _render_text(self, player):
        x, y = self.map_coord_controller.map_to_screen(player.x, player.y)
        text = self.player_font.render(player.name, True, (255, 255, 255))
        self.screen.blit(text, (x-(text.get_width()/2), y+5))

    def _render_yaw(self, player, team):
        if player.is_shooting:
            mapped_x, mapped_y = self.map_coord_controller.map_to_screen(player.x, player.y)
            player_yaw = math.radians(player.yaw)
            end_x = mapped_x + (100 * math.cos(player_yaw))
            end_y = mapped_y - (100 * math.sin(player_yaw))
            pygame.draw.line(self.screen, team.colour, (mapped_x, mapped_y), (end_x, end_y), 2)

    def _render_health(self, player):
        x, y = self.map_coord_controller.map_to_screen(player.x, player.y)
        pygame.draw.rect(self.screen, self.health_bar_background, (x-10, y-10, 20, 5))
        pygame.draw.rect(self.screen, self.health_bar_foreground, (x-10, y-10, mapped_value(player.health, 0, 100, 0, 20), 5))
     

    def render(self):
        for team in self.match.get_teams():
            for player in team.players:
                if player.dead:
                    continue

                self._render_circle(player, team)
                self._render_text(player)
                self._render_yaw(player, team)
                self._render_health(player)