class SettingsController:
    def __init__(self, settings_renderer, callback, context):
        self.settings_renderer = settings_renderer
        self.switch_state = callback
        self.context = context

        self.show_yaw_button = settings_renderer.show_yaw_button
        self.show_health_button = settings_renderer.show_health_button
        self.show_names_button = settings_renderer.show_names_button
        self.back_button = settings_renderer.back_button
        self.back_button.set_action(lambda: self.switch_state(self.context["previous_states"].pop()))

    def update(self, event):
        """Handles user inputs."""
        self.show_yaw_button.handle_event(event)
        self.show_health_button.handle_event(event)
        self.show_names_button.handle_event(event)
        self.back_button.handle_event(event)