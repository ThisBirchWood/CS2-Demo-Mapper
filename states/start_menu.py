from states.game_state import GameState
from widgets.button import Button
from models.match import Match
from models.player import Player
from models.team import Team
import demoparser2
import pygame
import pygame_gui

class StartMenu(GameState):
    def __init__(self, switch_state_callback, context):
        super().__init__(switch_state_callback, context)
        self.manager = pygame_gui.UIManager((self.screen.get_width(), self.screen.get_height()))

        self.default_button_start_x = self.screen.get_width() * 0.1
        self.default_button_width = self.screen.get_width() * 0.8

        # logo
        self.logo = pygame.image.load("assets/images/logo.png").convert_alpha() 
        self.logo_scale = 0.7
        self.logo = pygame.transform.smoothscale(self.logo, (self.logo.get_rect().size[0] * self.logo_scale, self.logo.get_rect().size[1] * self.logo_scale))

        # buttons
        self.upload_demo_button = Button(self.default_button_start_x, 
                  250, 
                  self.default_button_width, 
                  50, 
                  self._get_demo)
        self.upload_demo_button.set_text("Upload Demo")
        self.upload_demo_button.set_font(self.styling["font"])
        self.upload_demo_button.set_font_size(40)
        self.upload_demo_button.set_colour(self.styling["button_colour"])
        self.upload_demo_button.set_pressed_colour(self.styling["pressed_button_colour"])

        self.settings_button = Button(self.default_button_start_x,
                    350, 
                    self.default_button_width, 
                    50, 
                    lambda: self.switch_state("settings_menu"))
        self.settings_button.set_text("Settings")
        self.settings_button.set_font(self.styling["font"])
        self.settings_button.set_font_size(40)
        self.settings_button.set_colour(self.styling["button_colour"])
        self.settings_button.set_pressed_colour(self.styling["pressed_button_colour"])

        self.quit_button = Button(self.default_button_start_x,
                                  450,
                                  self.default_button_width,
                                  50,
                                  pygame.quit)
        self.quit_button.set_text("Quit")
        self.quit_button.set_font(self.styling["font"])
        self.quit_button.set_font_size(40)
        self.quit_button.set_colour(self.styling["button_colour"])
        self.quit_button.set_pressed_colour(self.styling["pressed_button_colour"])

        # file dialog
        self.file_dialog = None
        self.file_dialog_width = 440
        self.file_dialog_height = 500
        self.file_dialog_x = (self.screen.get_width()//2)-(self.file_dialog_width//2)
        self.file_dialog_y = (self.screen.get_height()//2)-(self.file_dialog_height//2)

        self.demo_file = None


    def _get_demo(self):
        """Loads a demo file."""
        self.file_dialog = pygame_gui.windows.UIFileDialog(
            rect=pygame.Rect(self.file_dialog_x, self.file_dialog_y, self.file_dialog_width, self.file_dialog_height),
            manager=self.manager,
            window_title='Pick a .dem file',
            allowed_suffixes=['.dem']
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
                                            "kills_total", "deaths_total", "assists_total", "inventory",
                                            "health", "armor_value", "active_weapon_name"])
        header_info = demo_parser.parse_header()
        map_name = header_info['map_name']
        players = demo_parser.parse_player_info()

        team_1 = Team()
        team_2 = Team()
        team_2.set_ct()
        m = Match(map_name, game_info, team_1, team_2, self.options)
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
            if not self.file_dialog:
                self.upload_demo_button.handle_event(event)
                self.settings_button.handle_event(event)
                self.quit_button.handle_event(event)
            self.manager.process_events(event)
               
            if event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                self.file_dialog = None
                self.demo_file = event.text
                self._start_game_callback()
            elif event.type == pygame_gui.UI_WINDOW_CLOSE:
                self.file_dialog = None
                self.demo_file = None

    def update(self):
        self.manager.update(0.01)

    def draw(self):
        """Draws everything on screen."""
        self.screen.fill(self.styling["background_colour"])  # Clear screen
        self.upload_demo_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        self.screen.blit(self.logo, ((self.screen.get_width() // 2) - (self.logo.get_width() // 2), 30))
        self.manager.draw_ui(self.screen)

    

    