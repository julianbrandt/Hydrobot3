from PIL import Image, ImageDraw
from MemeMaker.MemeLib import MemeImages
from MemeMaker.MemeModel import MemeImage
from math import sin, pi

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
    if len(returntext) > 3 and returntext[-3] == "-":
        returntext = returntext[:-3]
    return returntext


def get_textbox_margins(text, font, maxSize, drawer):
    widthMargin = round((maxSize[0] - drawer.textsize(text, font)[0])/2)
    heightMargin = round((maxSize[1] - drawer.textsize(text, font)[1])/2)
    return widthMargin, heightMargin


class MemeGenerator:
    def __init__(self, memeImage:MemeImage, texts):
        self.memeImage = memeImage
        self.image = Image.open("MemeMaker/ImageLibrary/" + memeImage.imageFileName)
        self.initialDimensions = self.image.size
        self.texts = texts
        if len(texts) != len(memeImage.textZones):
            raise Exception("Invalid arguments: Expected " + str(len(memeImage.textZones)) +
                            " arguments, but received " + str(len(texts)))
        self.apply_modification()


    @staticmethod
    def generator_from_command(name, texts):
        try:
            for m in MemeImages:
                if name.lower() == m.name.lower():
                    return MemeGenerator(m.value[0], texts)
            raise Exception("The meme template \"" + name + "\" does not exist")
        except Exception as e:
            raise e


    def apply_rotation(self, angle, expand=False):
        self.image = self.image.rotate(angle, expand=expand)


    def post_rotation_crop(self, angle):
        angle = abs(angle)
        horizontalMargin = round(sin((angle*pi)/180) * self.initialDimensions[0])
        verticalMargin = round(sin((angle*pi)/180) * self.initialDimensions[1])
        print(horizontalMargin, verticalMargin)
        self.image = self.image.crop((
            horizontalMargin/2,
            verticalMargin/2,
            self.initialDimensions[0],
            self.initialDimensions[1],
        ))


    def apply_modification(self):
        drawer = ImageDraw.Draw(self.image)
        for i in range(len(self.memeImage.textZones)):
            zone = self.memeImage.textZones[i]
            if zone.angle == 0:
                self.draw_text(zone, self.texts[i], drawer)
            else:
                self.apply_rotation(zone.angle, expand=True)
                self.draw_text(zone, self.texts[i], drawer)
                self.apply_rotation(-zone.angle)
                self.post_rotation_crop(zone.angle)


    @staticmethod
    def draw_text(textZone, text, drawer):
        margins = list(get_textbox_margins(
            split_line(text, textZone.font, textZone.dimensions[0]),
            textZone.font,
            textZone.dimensions,
            drawer
        ))
        for i in range(2):
            if margins[i] < 0 or not textZone.centering[i]:
                margins[i] = 0

        pos = (textZone.pos[0] + margins[0], textZone.pos[1] + margins[1])
        drawer.text(
            pos,
            split_line(text, textZone.font, textZone.dimensions[0]),
            (0, 0, 0),
            textZone.font
        )