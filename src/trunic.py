import os
from phonemizer import phonemize
from phonemizer.separator import Separator
from PIL import ImageFont, Image, ImageDraw


class Trunic:
    vowels = {        # EXAMPLE       # PRONOUNCIATION
        "æ":"ae",     # back, sad     a
        "ɑː":"ar",    # arm, large    ar
        "ɒ":"o",      # swan, box     ah
        "eɪ":"ei",    # bay, game     ay
        "ɛ":"e",      # end, pet      e
        "iː":"ii",    # bee, team     ee
        "iə":"ir",    # near, here    eer
        "ə":"a",      # the, about    eh
        "ɐ":"a",
        "ʌ":"a",
        "eə":"er",    # air, vary     ere
        "ɪ":"i",      # bit, rich     i
        "aɪ":"ai",    # guy, life     ie
        "ɜː":"xr",    # bird, work    ir
        "əʊ":"ou",    # toe, over     oh
        "ɔɪ":"oi",    # toy, avoid    oi
        "uː":"u",     # too, june     oo
        "ʊ":"x",      # wolf, good    ou
        "aʊ":"au",    # how, hour     ow
        "ɔː":"or"     # your, cure    ore
    }

    consts = {        # EXAMPLE       PRONOUNCIATION
        "b":"b",      # boss, baby    b
        "tʃ":"ch",    # chat, catch   ch
        "d":"d",      # dog, dad      d
        "f":"f",      # fox, fail     f
        "g":"g",      # gun, bag      g
        "h":"h",      # hop, house    h
        "dʒ":"dj",    # jam, judge    j
        "k":"k",      # cat, skip     k
        "l":"l",      # live, leaf    l
        "m":"m",      # man, mime     m
        "n":"n",      # net, nun      n
        "ŋ":"ng",     # rink, sing    ng
        "p":"p",      # poppy, pip    p
        "ɹ":"r",      # run, borrow   r
        "s":"s",      # sit, sass     s
        "ʃ":"sh",     # shut, shoe    sh
        "t":"t",      # tunic, stop   t
        "θ":"th",     # think, bath   th
        "ð":"dh",     # this, the     th
        "v":"v",      # vine, verge   v
        "w":"w",      # wow, worry    w
        "j":"y",      # you, yes      y
        "z":"z",      # zoo           z
        "ʒ":"j"       # vision        zh
    }

    font = os.path.join(os.path.dirname(__file__), "trunic.otf")

    def __init__(self, text: str) -> None:
        sep = Separator(phone=" ", word="-")
        self.ph = phonemize(text, language="en-gb-x-rp", strip=True, separator=sep, preserve_punctuation=True)
        self.ph = [i.split() for i in self.ph.split("-")]
        print(self.ph)


    """
    Returns the string in the format specified by
    https://github.com/dirdam/fonts/tree/main/tunic#how-to-use-the-font
    """
    def to_string(self):
        pass


    def to_image(self, 
                output: str,
                img_size: tuple[int, int],
                color: str | tuple[int, int, int],
                font_size: int,
                font_color: str | tuple[int, int, int]) -> None:

        trunic = ImageFont.truetype(Trunic.font, font_size)
        img = Image.new("RGBA", size=img_size, color=color)
        draw = ImageDraw.Draw(img)
        draw.text(xy=(10, 0), text=self.to_string(), fill=font_color, font=trunic)
        img.save(output + ".png")
