from PIL import Image

class TextZone:
    def __init__(self, pos, width, angle, font, centering):
        self.pos = pos
        self.width = width
        self.angle = angle
        self.font = font
        self.centering = centering

class MemeImage:
    def __init__(self, imageFileName, textZones):
        self.image = Image.open("imagelibrary/" + imageFileName)
        self.textZones = textZones
