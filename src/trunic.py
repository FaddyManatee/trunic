import os
from phonemizer import phonemize
from phonemizer.separator import Separator
from PIL import ImageFont, Image, ImageDraw


class Trunic:
    vowels = {"ʌ":"a", "aɪ":"ai", "aʊ":"au", "dʒ":"dj", "oʊ":"ou"}
    conson = {"ɹ":"r"}
    font = os.path.join(os.path.dirname(__file__), "trunic.otf")

    def __init__(self, text: str) -> None:
        sep = Separator(phone=" ", word="-")
        self.gb = phonemize(text, language="en-gb", strip=True, separator=sep, preserve_punctuation=True)
        self.us = phonemize(text, language="en-us", strip=True, separator=sep, preserve_punctuation=True)
        self.gb = [i.split() for i in self.gb.split("-")]
        self.us = [i.split() for i in self.us.split("-")]

        print(self.gb)
        print(self.us)


    def _check_locale(self, locale: str):
        if locale != "gb" and locale != "us":
            msg = "Unknown locale. Use either 'gb' or 'us'." 
            raise ValueError(msg)
        
        if locale == "gb":
            return self.gb
        elif locale == "us":
            return self.us


    def to_ipa(self, locale: str):
        loc = self._check_locale(locale)

        string = "/"
        for i in loc:
            for j in i:
                string += j
            string += " "

        return string.strip() + "/"


    """
    Returns the string in the format specified by
    https://github.com/dirdam/fonts/tree/main/tunic#how-to-use-the-font
    """
    def to_string(self, locale: str):
        loc = self._check_locale(locale)

        string = ""
        for i in loc:
            if i in dict.keys(Trunic.vowels):
                pass
            elif i in dict.keys(Trunic.conson):
                pass
            string += " "

        return string.strip()


    # def to_image(self, 
    #             output: str,
    #             img_size: tuple[int, int],
    #             color: str | tuple[int, int, int],
    #             font_size: int,
    #             font_color: str | tuple[int, int, int]) -> None:

    #     trunic = ImageFont.truetype(Trunic.font, font_size)
    #     img = Image.new("RGBA", size=img_size, color=color)
    #     draw = ImageDraw.Draw(img)
    #     draw.text(xy=(10, 0), text=string, fill=font_color, font=trunic)
    #     img.save(output + ".png")
