from PIL import Image, ImageFont

class TextZone:
    def __init__(self, pos, dimensions,font, angle=0, text_color=(0,0,0), centering=(False, False)):
        self.pos = pos
        self.dimensions = dimensions
        self.angle = angle
        self.font = font
        self.text_color = text_color
        self.centering = centering

class MemeImage:
    def __init__(self, imageFileName, text_zones, override_options=None):
        self.image_file_name = imageFileName
        self.text_zones = text_zones
        self.override_options = override_options
