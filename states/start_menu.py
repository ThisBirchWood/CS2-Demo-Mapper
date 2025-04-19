from states.game_state import GameState
from widgets.button import Button
from models.match import Match
from models.player import Player
from models.team import Team
from pgu import gui
import demoparser2
import pygame
import pygame_gui

class StartMenu(GameState):
    def __init__(self, switch_state_callback, context):
        super().__init__(switch_state_callback, context)
        self.manager = pygame_gui.UIManager((self.screen.get_width(), self.screen.get_height()))

        self.default_button_start_x = self.screen.get_width() * 0.1
        self.default_button_width = self.screen.get_width() * 0.8

        # buttons
        self.button = Button(self.default_button_start_x, 
                  100, 
                  self.default_button_width, 
                  50, 
                  self._get_demo)
        self.button.set_text("Upload Demo")
        self.button.set_font_size(40)

        # file dialog
        self.file_dialog = None
        self.demo_file = None


    def _get_demo(self):
        """Loads a demo file."""
        # pygame-pgu
        self.file_dialog = pygame_gui.windows.UIFileDialog(
            rect=pygame.Rect(160, 50, 440, 500),
            manager=self.manager,
            window_title='Pick a .dem file'
        )
    
    def _start_game_callback(self):
        """Starts the game."""
        match = self._setup_game(self.demo_file)
        self.context["match"] = match
        self.switch_state("game")

    def _setup_game(self, demo_file: str) -> Match:
        demo_parser = demoparser2.DemoParser(demo_file)
        game_info = demo_parser.parse_ticks(["X", "Y", "Z", "pitch", "yaw", "is_alive", "team", "player_steamid", 
                                            "team_rounds_total", "team_num", "total_rounds_played", "shots_fired",
                                            "health"])
        header_info = demo_parser.parse_header()
        map_name = header_info['map_name']
        players = demo_parser.parse_player_info()

        team_1 = Team()
        team_1.set_ct()
        team_2 = Team()
        m = Match(map_name, game_info, team_1, team_2)
        for index, row in players.iterrows():
            if row["team_number"] == 2:
                team_1.add_player(Player(row["name"], row["steamid"]))
            elif row["team_number"] == 3: 
                team_2.add_player(Player(row["name"], row["steamid"]))
  
        return m
    

    def handle_events(self, events):
        """Handles user inputs."""
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            self.button.handle_event(event)
            self.manager.process_events(event)
                    # Handle file dialog interaction
            if event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                self.file_dialog.kill()
                self.demo_file = event.text
                self._start_game_callback()

    def update(self):
        self.manager.update(0.1)

    def draw(self):
        """Draws everything on screen."""
        self.button.draw(self.screen)
        self.manager.draw_ui(self.screen)

    

    