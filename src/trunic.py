import os
from phonemizer import phonemize
from phonemizer.separator import Separator
from PIL import ImageFont, Image, ImageDraw


class Trunic:
    font = os.path.join(os.path.dirname(__file__), "trunic.otf")

    def __init__(self, text: str) -> None:
        sep = Separator(phone=" ", word="-")
        self.gb = phonemize(text, language="en-gb", strip=True, separator=sep, preserve_punctuation=True)
        self.us = phonemize(text, language="en-us", strip=True, separator=sep, preserve_punctuation=True)
        self.gb = [i.split() for i in self.gb.split("-")]
        self.us = [i.split() for i in self.us.split("-")]

        print(self.gb)
        print(self.us)


    def toImage(self, 
                output: str,
                img_size: tuple[int, int],
                color: str | tuple[int, int, int],
                font_size: int,
                font_color: str | tuple[int, int, int]) -> None:

        trunic = ImageFont.truetype(Trunic.font, font_size)
        img = Image.new("RGBA", size=img_size, color=color)
        draw = ImageDraw.Draw(img)
        draw.text(xy=(10, 0), text="hello world", fill=font_color, font=trunic)
        img.save(output + ".png")
