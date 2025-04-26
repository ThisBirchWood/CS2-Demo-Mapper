class InfoController:
    def __init__(self, info_renderer, player_controller):
        self.info_renderer = info_renderer
        self.player_controller = player_controller

    def update(self, event):
        self.info_renderer.selected_player = self.player_controller.selected_player

