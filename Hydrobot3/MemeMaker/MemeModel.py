from PIL import Image

class TextZone:
    def __init__(self, pos, dimensions, angle, font, centering):
        self.pos = pos
        self.dimensions = dimensions
        self.angle = angle
        self.font = font
        self.centering = centering

class MemeImage:
    def __init__(self, imageFileName, textZones):
        self.imageFileName = imageFileName
        self.textZones = textZones
