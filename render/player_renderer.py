import pygame, math
from models.match import Match
from models.player import Player
from utils.map_coord_converter import MapCoordConverter
from utils.utils import mapped_value

class PlayerRenderer:
    def __init__(self, screen, match: Match, map_coord_converter: MapCoordConverter, options: dict, styling: dict):
        self.screen = screen
        self.match = match
        self.map_coord_converter = map_coord_converter
        self.options = options
        self.styling = styling
        self.player_font = pygame.font.Font(None, 15)

        self.player_radius = 5
        self.hovered_radius = 10

        self.health_bar_foreground = (0, 255, 0)
        self.health_bar_background = (255, 0, 0)

    ## Getters 
    def get_radius(self) -> int:
        return self.player_radius
    
    def get_health_bar_foreground_colour(self) -> tuple[int, int, int]:
        return self.health_bar_foreground
    
    def get_health_bar_background_colour(self) -> tuple[int, int, int]:
        return self.health_bar_background
    
    ## Setters
    def set_radius(self, radius: int) -> None:
        self.player_radius = radius

    def set_health_bar_foreground_colour(self, colour: tuple[int, int, int]):
        self.health_bar_foreground = colour

    def set_health_bar_background_colour(self, colour: tuple[int, int, int]):
        self.health_bar_background = colour

    ## Private Methods
    def _render_circle(self, player: Player, team):
        if player.is_hovered:
            radius = self.hovered_radius
        else:
            radius = self.player_radius

        x, y = self.map_coord_converter.map_to_screen(player.x, player.y)
        pygame.draw.circle(self.screen, team.colour, (x, y), radius)

    def _render_text(self, player):
        if player.is_selected:
            text = self.player_font.render(player.name, True, self.styling["player_selected_colour"])
        else:
            text = self.player_font.render(player.name, True, (255, 255, 255))

        x, y = self.map_coord_converter.map_to_screen(player.x, player.y)
        self.screen.blit(text, (x-(text.get_width()/2), y+5))

    def _render_yaw(self, player, team):
        if player.is_shooting:
            yaw_length = 100
        else:
            yaw_length = 20

        mapped_x, mapped_y = self.map_coord_converter.map_to_screen(player.x, player.y)
        player_yaw = math.radians(player.yaw)
        end_x = mapped_x + (yaw_length * math.cos(player_yaw))
        end_y = mapped_y - (yaw_length * math.sin(player_yaw))
        pygame.draw.line(self.screen, team.colour, (mapped_x, mapped_y), (end_x, end_y), 2)

    def _render_health(self, player):
        x, y = self.map_coord_converter.map_to_screen(player.x, player.y)
        pygame.draw.rect(self.screen, self.health_bar_background, (x-10, y-10, 20, 5))
        pygame.draw.rect(self.screen, self.health_bar_foreground, (x-10, y-10, mapped_value(player.health, 0, 100, 0, 20), 5))

    ## Public Methods
    def render(self):
        for team in self.match.get_teams():
            for player in team.players:
                if player.dead:
                    continue

                self._render_circle(player, team)

                if self.options["show_names"]:
                    self._render_text(player)

                if self.options["show_yaw"]:
                    self._render_yaw(player, team)

                if self.options["show_health"]:
                    self._render_health(player)