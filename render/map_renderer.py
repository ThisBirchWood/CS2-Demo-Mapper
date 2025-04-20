import pygame
from utils.json_object import JSONObject

class MapRenderer:
    def __init__(self, screen, map_data_path, map_image_path):
        self.screen = screen
        self.map_data_path = map_data_path
        self.map_image_path = map_image_path

        self.map_image = pygame.image.load(self.map_image_path)
        
    def _load_json(self, path: str) -> JSONObject:
        try:
            return JSONObject(path)
        except FileNotFoundError:
            raise NotImplementedError(f"Map not implemented.")

    def render(self):
        # Scale and rotate map image
        self.map_image = pygame.transform.scale(self.map_image, (self.screen.get_width(), self.screen.get_height()))

        # Draw map image
        self.screen.blit(self.map_image, (0, 0))