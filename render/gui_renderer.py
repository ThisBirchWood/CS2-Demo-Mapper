import pygame
from widgets.slider import HorizontalSlider
from widgets.button import Button

class GUIRenderer:
    def __init__(self, screen, match):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.match = match

        self.slider = HorizontalSlider(self.screen, 50, 650, self.screen.get_width()-100, 20, 1, self.match.max_tick)
        
        # Buttons
        self.settings_button = Button(self.screen.get_width()-40, 10, 30, 30, None)
        self.settings_button.set_image("assets/setting.png")

        self.back_button = Button(self.screen.get_width()-80, 10, 30, 30, None)
        self.back_button.set_image("assets/arrow.png")

        self.colour = (255, 255, 255)

    def _render_current_tick(self, match_tick, max_tick):
        text = self.font.render(f"Tick: {match_tick}/{max_tick}", True, self.colour)
        self.screen.blit(text, (10, 10))

    def _render_team_scores(self, team_1_score, team_2_score):
        text = self.font.render(f"Score: {team_1_score} - {team_2_score}", True, self.colour)
        self.screen.blit(text, (10, 40))

    def _render_buttons(self):
        self.settings_button.draw(self.screen)
        self.back_button.draw(self.screen)

    def _render_slider(self):
        # Update slider value
        if self.slider.dragging:
            # Set match tick if slider is being dragged
            self.match.set_tick(int(self.slider.value))
        else:
            # Set slider value if slider is not being dragged
            self.slider.set_value(self.match.tick)
        self.slider.draw()

    def render(self):
        self._render_current_tick(self.match.tick, self.match.max_tick)
        self._render_team_scores(self.match.team_1.score, self.match.team_2.score)
        self._render_buttons()
        self._render_slider()
