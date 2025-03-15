from utils import mapped_value
import math

class ImageCoordController:
    def __init__(self, image_width, image_height, screen_width, screen_height, ingame_zero_x, ingame_zero_y):
        self.image_width = image_width
        self.image_height = image_height
        self.ingame_zero_x = ingame_zero_x
        self.ingame_zero_y = ingame_zero_y

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen_middle_x = screen_width / 2
        self.screen_middle_y = screen_height / 2

        self.scaler = 1.0
        self.rotation_degrees = 0

    def scale(self, scaler):
        self.scaler = scaler

    def rotate(self, degree):
        ## validate for multiples of 90 degrees and convert to 0-360
        if degree % 90 != 0:
            raise ValueError("Degree v must be a multiple of 90")
        self.rotation_degrees = degree % 360
    
    def top_left_screen(self):
        if self.rotation_degrees == 0:
            x = self.screen_middle_x - (self.ingame_zero_x * self.scaler)
            y = self.screen_middle_y - (self.ingame_zero_y * self.scaler)
        elif self.rotation_degrees == 270:
            x = self.screen_middle_x - ((self.image_width - self.ingame_zero_y) * self.scaler)
            y = self.screen_middle_y - (self.ingame_zero_x * self.scaler)
        elif self.rotation_degrees == 180:
            x = self.screen_middle_x - ((self.image_width - self.ingame_zero_x) * self.scaler)
            y = self.screen_middle_y - ((self.image_height - self.ingame_zero_y) * self.scaler)
        elif self.rotation_degrees == 90:
            x = self.screen_middle_x - (self.ingame_zero_y * self.scaler)
            y = self.screen_middle_y - ((self.image_height - self.ingame_zero_x) * self.scaler)
        return x, y




    

'''
ingame zero maps to 0,0,0 in game, and needs to map to middle of pygame window

'''
if __name__ == "__main__":
    image_coord_controller = ImageCoordController(1024, 1024, 640, 360)
    image_coord_controller.scale(4)
    print(image_coord_controller.image_to_screen(0,0))
    




