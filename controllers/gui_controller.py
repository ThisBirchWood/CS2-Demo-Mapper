from render.gui_renderer import GUIRenderer

class GUIController:
    def __init__(self, gui_renderer: GUIRenderer, callback_function):
        self.callback_function = callback_function

        self.gui_renderer = gui_renderer
        self.settings_button = gui_renderer.settings_button
        self.settings_button.set_action(lambda: self.callback_function("settings_menu"))

        self.back_button = gui_renderer.back_button
        self.back_button.set_action(lambda: self.callback_function("start_menu"))

    def update(self, event):
        self.settings_button.handle_event(event)
        self.back_button.handle_event(event)