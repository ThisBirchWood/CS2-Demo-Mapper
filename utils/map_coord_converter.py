# Description: This file contains the CoordinateManager class which is responsible for converting coordinates to pixels and vice versa.
import pygame
from utils.utils import mapped_value
from utils.json_object import JSONObject

class MapCoordConverter:
    def __init__(self, screen_width: int, screen_height, json_file: str, map_image_path: str):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # too much for one class, refactor
        self.map_image = pygame.image.load(map_image_path)
        self.image_width = self.map_image.get_width()
        self.image_height = self.map_image.get_height()

        # Load map data from json file
        self.json_object = self._load_json(json_file)
        
        # Load map data from json object
        self.map_min_x = self.json_object.get("pos_x")
        self.map_min_y = self.json_object.get("pos_y")
        self.scale = self.json_object.get("scale")
        
        self.map_max_x = self.map_min_x + (self.image_width * self.scale)
        self.map_max_y = self.map_min_y - (self.image_height * self.scale)

        self.map_width = self.map_max_x - self.map_min_x
        self.map_height = self.map_max_y - self.map_min_y

    def _load_json(self, path: str):
        try:
            return JSONObject(path)
        except FileNotFoundError:
            raise NotImplementedError(f"Map not implemented.")

    def update_screen_size(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def screen_to_map(self, x, y):
        mapped_x = int(mapped_value(x, 0, self.screen_width, self.map_min_x, self.map_max_x))
        mapped_y = int(mapped_value(y, 0, self.screen_height, self.map_min_y, self.map_max_y))
        return mapped_x, mapped_y
    
    def map_to_screen(self, x, y):
        mapped_x = int(mapped_value(x, self.map_min_x, self.map_max_x, 0, self.screen_width))
        mapped_y = int(mapped_value(y, self.map_min_y, self.map_max_y, 0, self.screen_height))
        return mapped_x, mapped_y
    
if __name__ == "__main__":
    map_coord_controller = MapCoordConverter(700, 700, -3000, 3000, -3000, 3000)
    print(map_coord_controller.map_to_screen(0,0))

    