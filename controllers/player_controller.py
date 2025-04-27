from models.match import Match
from render.player_renderer import PlayerRenderer
import pygame

class PlayerController:
    def __init__(self, player_renderer: PlayerRenderer, match: Match, game_box_top: tuple[int, int]):
        self.player_renderer = player_renderer
        self.match = match
        self.game_box_top = game_box_top

        self.selected_player = None

    ## Private Methods
    def _is_player_at_mouse(self, player, mouse_x, mouse_y):
        player_x, player_y = self.player_renderer.map_coord_converter.map_to_screen(player.x, player.y)
        distance = ((mouse_x - player_x) ** 2 + (mouse_y - player_y) ** 2) ** 0.5
        
        return distance < self.player_renderer.get_radius()

    def _update_hover_state(self, mouse_x, mouse_y, player):
        if self._is_player_at_mouse(player, mouse_x, mouse_y):
            player.is_hovered = True
        else:
            player.is_hovered = False

    def _select_player(self, mouse_x, mouse_y, player):
        if self._is_player_at_mouse(player, mouse_x, mouse_y):
            if self.selected_player and self.selected_player != player:
                self.selected_player.is_selected = False

            player.is_selected = not player.is_selected

            if player.is_selected:
                self.selected_player = player
            else:
                self.selected_player = None

    ## Public Methods
    def update(self, event):
        if hasattr(event, 'pos'):
            new_x, new_y = event.pos[0] - self.game_box_top[0], event.pos[1] - self.game_box_top[1]
            
        for team in self.match.get_teams():
            for player in team.players:
                if event.type == pygame.MOUSEMOTION:
                    self._update_hover_state(new_x, new_y, player)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._select_player(new_x, new_y, player)
                