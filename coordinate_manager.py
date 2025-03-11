# Description: This file contains the CoordinateManager class which is responsible for converting coordinates to pixels and vice versa.

class CoordinateManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def mapped_value(self, value, in_min, in_max, out_min, out_max):
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def coord_to_pixel(self, x, y):
        mapped_x = self.mapped_value(x, -3000, 3000, 0, self.width)
        mapped_y = self.mapped_value(y, -3000, 3000, 0, self.height)
        return mapped_x, mapped_y
    
    def get_top_left(self, width, height, scale):
        return (width - scale) // 2, (height - scale) // 2