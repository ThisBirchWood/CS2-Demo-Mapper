from models.match import Match
from render.player_renderer import PlayerRenderer
import pygame

class PlayerController:
    def __init__(self, player_renderer: PlayerRenderer, match: Match, game_box_top: tuple[int, int]):
        self.player_renderer = player_renderer
        self.match = match
        self.game_box_top = game_box_top

    ## Private Methods
    def _update_hover_state(self, event, player):
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            player_x, player_y = self.player_renderer.map_coord_converter.map_to_screen(player.x, player.y)

            # Adjust for game box position
            player_x += self.game_box_top[0]
            player_y += self.game_box_top[1]

            distance = ((mouse_x - player_x) ** 2 + (mouse_y - player_y) ** 2) ** 0.5
            
            if distance < self.player_renderer.get_radius():
                player.is_hovered = True
            else:
                player.is_hovered = False
    
    ## Public Methods
    def update(self, event):
        for team in self.match.get_teams():
            for player in team.players:
                self._update_hover_state(event, player)
                