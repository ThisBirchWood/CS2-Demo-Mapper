import pygame
import copy

class ControlController:
    def __init__(self, control_renderer, box_top: tuple[int, int]):
        self.control_renderer = control_renderer
        self.box_top = box_top
        
        self.slider = control_renderer.slider

    def update(self, event):
        new_event = pygame.event.Event(event.type, event.__dict__)
        if hasattr(new_event, 'pos'):
            new_event.pos = (event.pos[0] - self.box_top[0], event.pos[1] - self.box_top[1])
        
        self.slider.handle_event(new_event)