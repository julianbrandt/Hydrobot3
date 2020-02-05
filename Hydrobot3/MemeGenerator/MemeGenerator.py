from PIL import Image, ImageFont, ImageDraw
from MemeGenerator.MemeLib import MemeImages
from MemeGenerator.MemeModel import MemeImage, TextZone

def generate_meme():
    meme = None
    return meme


def split_line(text, font, width):
    text = text
    returntext = ""
    while text:
        if (font.getsize(text)[0]) < width:
            returntext += text
            break
        for i in range(len(text), 0, -1):
            if (font.getsize(text[:i])[0]) < width:
                if ' ' not in text[:i]:
                    returntext += text[:i] + "-\n"
                    text = text[i:]
                else:
                    for l in range(i, 0, -1):
                        if text[l] == ' ':
                            returntext += text[:l]
                            returntext += "\n"
                            text = text[l + 1:]
                            break
                break
    if returntext[-3] == "-":
        returntext = returntext[:-3]
    return returntext


class MemeGenerator:
    def __init__(self, memeImage:MemeImage, texts):
        self.memeImage = memeImage
        self.texts = texts
        if len(texts) != len(memeImage.textZones):
            raise Exception("Invalid arguments: Expected " + str(len(memeImage.textZones)) +
                            "arguments, but received " + str(len(texts)))


    def apply_rotation(self, angle):
        self.memeImage.image.rotate(angle)


    def post_rotation_crop(self, angle):



    def apply_modification(self):
        drawer = ImageDraw.Draw(self.memeImage.image)
        for i in range(len(self.memeImage.textZones)):
            zone = self.memeImage.textZones[i]
            if zone.angle == 0:
                self.draw_text(zone, self.texts[i], drawer)
            else:
                self.apply_rotation(zone.angle)
                self.draw_text(zone, self.texts[i], drawer)
                self.apply_rotation(-zone.angle)


    def draw_text(self, textZone, text, drawer):
        drawer.text(
            textZone.pos,
            split_line(text, textZone.font, textZone.width),
            (0, 0, 0),
            textZone.font
        )


    def get_dimensions(self):
        return self.memeImage.image.size