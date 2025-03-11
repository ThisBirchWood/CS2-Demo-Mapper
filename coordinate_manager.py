def mapped_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class CoordinateManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def coord_to_pixel(self, x, y):
        mapped_x = mapped_value(x, -4000, 4000, 0, self.width)
        mapped_y = mapped_value(y, -4000, 4000, 0, self.height)
        return mapped_x, mapped_y