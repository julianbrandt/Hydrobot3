from PIL import Image, ImageDraw
from MemeMaker.MemeLib import MemeImages
from MemeMaker.MemeModel import MemeImage
from enum import Enum
from io import BytesIO
import requests
import shutil


def split_line(text, font, width):
    if len(text) > 200:
        raise ValueError("Text input must not be longer than 150 characters")
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
    width_margin = round((maxSize[0] - drawer.textsize(text, font)[0])/2)
    height_margin = round((maxSize[1] - drawer.textsize(text, font)[1])/2)
    return width_margin, height_margin


def download_image(address):
    resp = requests.get(address, stream=True)
    file = BytesIO()
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, file)
    del resp
    return Image.open(file)


class TextType(Enum):
    Text = 0,
    Image = 1


class MemeGenerator:
    def __init__(self, meme_image:MemeImage, texts):
        self.meme_image = meme_image
        self.image = Image.open("MemeMaker/ImageLibrary/" + meme_image.image_file_name)
        self.initial_dimensions = self.image.size
        self.texts = texts
        if len(texts) != len(meme_image.text_zones):
            raise Exception("Invalid arguments: Expected " + str(len(meme_image.text_zones)) +
                            " arguments, but received " + str(len(texts)))
        self.apply_modification()


    @staticmethod
    def generator_from_command(name, texts):
        try:
            for m in MemeImages:
                if name.lower() == m.name.lower():
                    return MemeGenerator(m.value[0], texts)
            raise ValueError("The meme template \"" + name + "\" does not exist")
        except Exception as e:
            raise e


    def apply_rotation(self, angle):
        self.image = self.image.rotate(angle, expand=True)


    def calculate_margins(self):
        return (
            (self.image.size[0] - self.initial_dimensions[0])/2,
            (self.image.size[1] - self.initial_dimensions[1])/2
        )


    def post_rotation_crop(self):
        (horizontal_margin, vertical_margin) = self.calculate_margins()
        self.image = self.image.crop((
            horizontal_margin,
            vertical_margin,
            horizontal_margin + self.initial_dimensions[0],
            vertical_margin + self.initial_dimensions[1]
        ))


    def apply_modification(self):
        drawer = ImageDraw.Draw(self.image)
        for i in range(len(self.meme_image.text_zones)):
            text_type = TextType.Text
            if str.startswith(self.texts[i], "<https://") and str.endswith(self.texts[i], ">"):
                text_type = TextType.Image

            zone = self.meme_image.text_zones[i]
            if zone.angle == 0:
                self.draw_text_zone(zone, self.texts[i], text_type, drawer)
            else:
                self.apply_rotation(zone.angle)
                drawer = ImageDraw.Draw(self.image)
                self.draw_text_zone(zone, self.texts[i], text_type, drawer)
                self.apply_rotation(-zone.angle)
                self.post_rotation_crop()


    def draw_text_zone(self, text_zone, text, text_type, drawer):
        if text_type == TextType.Text:
            self.draw_text(text_zone, text, drawer)
        else:
            self.draw_image(text_zone, text)


    def draw_image(self, text_zone, text):
        text = text[1:-1]
        img = download_image(text)
        resize_dimensions = list(text_zone.dimensions)
        for i in range(2):
            if img.size[i] < resize_dimensions[i]:
                resize_dimensions[i] = img.size[i]
        img = img.resize(resize_dimensions, Image.ANTIALIAS)
        self.image.paste(img, text_zone.pos)


    @staticmethod
    def draw_text(text_zone, text, drawer):
        margins = list(get_textbox_margins(
            split_line(text, text_zone.font, text_zone.dimensions[0]),
            text_zone.font,
            text_zone.dimensions,
            drawer
        ))
        for i in range(2):
            if margins[i] < 0 or not text_zone.centering[i]:
                margins[i] = 0

        pos = (
            text_zone.pos[0] + margins[0],
            text_zone.pos[1] + margins[1]
        )
        drawer.text(
            pos,
            split_line(text, text_zone.font, text_zone.dimensions[0]),
            (0, 0, 0),
            text_zone.font
        )