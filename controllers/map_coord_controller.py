# Description: This file contains the CoordinateManager class which is responsible for converting coordinates to pixels and vice versa.

import math
from utils.utils import mapped_value

class MapCoordController:
    def __init__(self, screen_width: int, screen_height: int, map_min_x: int, map_max_x, map_min_y, map_max_y):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_min_x = map_min_x
        self.map_max_x = map_max_x
        self.map_min_y = map_min_y
        self.map_max_y = map_max_y
        self.map_width = map_max_x - map_min_x
        self.map_height = map_max_y - map_min_y

    def update_screen_size(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def screen_to_map(self, x, y):
        mapped_x = mapped_value(x, 0, self.screen_width, self.map_min_x, self.map_max_x)
        mapped_y = mapped_value(y, 0, self.screen_height, self.map_min_y, self.map_max_y)
        return mapped_x, mapped_y
    
    def map_to_screen(self, x, y):
        mapped_x = mapped_value(x, self.map_min_x, self.map_max_x, 0, self.screen_width)
        mapped_y = mapped_value(y, self.map_min_y, self.map_max_y, 0, self.screen_height)
        return mapped_x, mapped_y
    
if __name__ == "__main__":
    map_coord_controller = MapCoordController(700, 700, -3000, 3000, -3000, 3000)
    print(map_coord_controller.map_to_screen(0,0))

    