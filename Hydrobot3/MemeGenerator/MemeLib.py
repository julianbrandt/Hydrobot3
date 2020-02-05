from enum import Enum
from PIL import ImageFont
from MemeGenerator.MemeModel import MemeImage, TextZone

class MemeImages(Enum):
    MeAlsoMe = MemeImage(
        "mealsome.png",
        [TextZone(
            (60, 0),
            400,
            0,
            ImageFont.truetype("arial.ttf", 24),
            (False, False)
        ), TextZone(
            (120, 100),
            350,
            0,
            ImageFont.truetype("arial.ttf", 24),
            (False, False)
        )]
    ),
    ItsRetarded = MemeImage(
        "itsretarded.png",
        [TextZone(
            (253, 3),
            220,
            0,
            ImageFont.truetype("arial.ttf", 20),
            (False, True)
        )]
    ),
    Headache = MemeImage(
        "headache.png",
        [TextZone(
            (190, 490),
            200,
            0,
            ImageFont.truetype("impact.ttf", 54),
            (True, False)
        )]
    ),
    ItsTime = MemeImage(
        "itstime.png",
        [TextZone(
            (60, 60),
            200,
            0,
            ImageFont.truetype("arial.ttf", 36),
            (True, True)
        ),
        TextZone(
            (380, 95),
            110,
            0,
            ImageFont.truetype("arial.ttf", 24),
            (True, True)
        )]
    ),
    ClassNote = MemeImage(
        "classnote.png",
        [TextZone(
            (585, 545),
            175,
            30,
            ImageFont.truetype("arial.ttf", 24),
            (True, True)
        )]
    ),
    FirstWord = MemeImage(
        "firstword.png",
        [TextZone(
            (100, 30),
            500,
            0,
            ImageFont.truetype("comic.ttf", 60),
            (False, False)
        ),
        TextZone(
            (100, 485),
            500,
            0,
            ImageFont.truetype("comic.ttf", 60),
            (False, True)
        )]
    ),
    NutButton = MemeImage(
        "nutbutton.jpg",
        [TextZone(
            (133, 300),
            175,
            10,
            ImageFont.truetype("arial.ttf", 56),
            (False, True)
        )]
    ),
    SwuUok = MemeImage(
        "swu_uok.png",
        [TextZone(
            (20,22),
            220,
            0,
            ImageFont.truetype("arial.ttf", 36),
            (False, True)
        ),
        TextZone(
            (20, 300),
            220,
            0,
            ImageFont.truetype("arial.ttf", 36),
            (False, True)
        )]
    )