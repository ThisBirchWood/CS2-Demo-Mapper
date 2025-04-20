from render.gui_renderer import GUIRenderer

class GUIController:
    def __init__(self, gui_renderer: GUIRenderer):
        self.gui_renderer = gui_renderer
        self.slider =  gui_renderer.slider

    def update(self, event):
        self.slider.handle_event(event)