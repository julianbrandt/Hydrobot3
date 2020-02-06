from enum import Enum
from PIL import ImageFont
from MemeMaker.MemeModel import MemeImage, TextZone

class MemeImages(Enum):
    def __str__(self):
        return str(self.value)

    MeAlsoMe = MemeImage(
        "mealsome.png",
        [TextZone(
            (60, 0),
            (400, 300),
            0,
            ImageFont.truetype("arial.ttf", 24),
            (False, False)
        ), TextZone(
            (120, 100),
            (350, 300),
            0,
            ImageFont.truetype("arial.ttf", 24),
            (False, False)
        )]
    ),
    ItsRetarded = MemeImage(
        "itsretarded.png",
        [TextZone(
            (253, 3),
            (220, 100),
            0,
            ImageFont.truetype("arial.ttf", 20),
            (False, True)
        )]
    ),
    Headache = MemeImage(
        "headache.png",
        [TextZone(
            (250, 490),
            (400, 50),
            0,
            ImageFont.truetype("impact.ttf", 54),
            (True, False)
        )]
    ),
    ItsTime = MemeImage(
        "itstime.png",
        [TextZone(
            (60, 50),
            (200, 150),
            0,
            ImageFont.truetype("arial.ttf", 36),
            (True, True)
        ),
        TextZone(
            (95, 380),
            (110, 75),
            0,
            ImageFont.truetype("arial.ttf", 24),
            (True, True)
        )]
    ),
    ClassNote = MemeImage(
        "classnote.png",
        [TextZone(
            (585, 545),
            (175, 140),
            30,
            ImageFont.truetype("arial.ttf", 24),
            (True, True)
        )]
    ),
    FirstWord = MemeImage(
        "firstword.png",
        [TextZone(
            (100, 30),
            (500, 50),
            0,
            ImageFont.truetype("comic.ttf", 60),
            (False, False)
        ),
        TextZone(
            (100, 485),
            (500, 200),
            0,
            ImageFont.truetype("comic.ttf", 60),
            (False, True)
        )]
    ),
    NutButton = MemeImage(
        "nutbutton.jpg",
        [TextZone(
            (133, 300),
            (175, 100),
            10,
            ImageFont.truetype("arial.ttf", 56),
            (False, True)
        )]
    ),
    SwuUok = MemeImage(
        "swu_uok.png",
        [TextZone(
            (20,22),
            (220, 220),
            0,
            ImageFont.truetype("arial.ttf", 36),
            (False, True)
        ),
        TextZone(
            (20, 300),
            (220, 220),
            0,
            ImageFont.truetype("arial.ttf", 36),
            (False, True)
        )]
    )