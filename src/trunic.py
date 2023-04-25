import os
import msgspec
from copy import deepcopy
from math import ceil
from PIL import ImageFont, Image, ImageDraw


class Trunic:
    vowels = {          # EXAMPLE       # PRONOUNCIATION
        "æ":"ae",       # back, sad     a
        "ɔ":"ae",
        "ɑː":"ar",      # arm, large    ar
        "ɑːɹ":"ar",
        "ɑɹ":"ar",
        "ɒ":"o",        # swan, box     ah
        "ɑ":"o",
        "eɪ":"ei",      # bay, game     ay
        "ɛ":"e",        # end, pet      e
        "e":"e",
        "ᵻ":"e",
        "iː":"ii",      # bee, team     ee
        "i":"ii",
        "iə":"ir",      # near, here    eer
        "ɪɹ":"ir",
        "ə":"a",        # the, about    eh
        "ʌ":"a",
        "eə":"er",      # air, vary     ere
        "ɛɹ":"er",
        "ɪ":"i",        # bit, rich     i
        "aɪ":"ai",      # guy, life     ie
        "ɜː":"xr",      # bird, work    ir
        "ɝ":"xr",
        "ɐ":"xr",
        "ɚ":"xr",
        "aɪə":"aicxr",  # fire          ire
        "aɪɚ":"aicxr",
        "əʊ":"ou",      # toe, over     oh
        "oʊ":"ou",
        "ɔɪ":"oi",      # toy, avoid    oi
        "uː":"u",       # too, june     oo
        "u":"u",
        "ʊ":"x",        # wolf, good    ou
        "aʊ":"au",      # how, hour     ow
        "ɔː":"or",      # your, cure    ore
        "oːɹ":"or",
        "ɔːɹ":"or",
        "ɔɹ":"or"
    }

    consts = {          # EXAMPLE       PRONOUNCIATION
        "b":"b",        # boss, baby    b
        "tʃ":"ch",      # chat, catch   ch
        "d":"d",        # dog, dad      d
        "f":"f",        # fox, fail     f
        "g":"g",        # gun, bag      g
        "ɡ":"g",
        "h":"h",        # hop, house    h
        "dʒ":"dj",      # jam, judge    j
        "k":"k",        # cat, skip     k
        "l":"l",        # live, leaf    l
        "ɫ":"l",
        "m":"m",        # man, mime     m
        "n":"n",        # net, nun      n
        "ŋ":"ng",       # rink, sing    ng
        "p":"p",        # poppy, pip    p
        "ɹ":"r",        # run, borrow   r
        "s":"s",        # sit, sass     s
        "ʃ":"sh",       # shut, shoe    sh
        "t":"t",        # tunic, stop   t
        "ɾ":"t",
        "θ":"th",       # think, bath   th
        "ð":"dh",       # this, the     th
        "v":"v",        # vine, verge   v
        "w":"w",        # wow, worry    w
        "j":"y",        # you, yes      y
        "z":"z",        # zoo           z
        "ʒ":"j"         # vision        zh
    }

    font = os.path.join(os.path.dirname(__file__), "trunic.otf")
    _ = open(os.path.join(os.path.dirname(__file__), "ipa_dict.json"), "r", encoding="utf-8")
    ipa_dict = msgspec.json.decode(_.read())
    _.close()

    def __init__(self, text: str) -> None:
        self.phonemes = []
        self.symbols = 0

        for word in text.lower().split():
            ipa = Trunic.ipa_dict.get(word)
            if ipa is None:
                msg = "Unrecognised word '{}'".format(word)
                raise RuntimeError(msg)

            self.phonemes.append(ipa[0].split())


    def _build_str(self, word):
        lst = deepcopy(word)
        out = ""

        while True:
            # Break the loop if phonemes are exhausted.
            if lst is not None and len(lst) == 0:
                return out

            # Get a phoneme pair.
            x = lst.pop(0)
            y = None
            if len(lst) > 0:
                y = lst.pop(0)

            if y is not None:
                # CV
                if x in dict.keys(Trunic.consts) and y in dict.keys(Trunic.vowels):
                    out += Trunic.consts.get(x)
                    out += Trunic.vowels.get(y)
                    self.symbols += 1

                # VC
                elif x in dict.keys(Trunic.vowels) and y in dict.keys(Trunic.consts):
                    out += Trunic.consts.get(y)
                    out += Trunic.vowels.get(x)
                    out += "_"
                    self.symbols += 1

                # CC
                elif x in dict.keys(Trunic.consts) and y in dict.keys(Trunic.consts):
                    out += Trunic.consts.get(x)
                    lst.insert(0, y)

                # VV
                elif x in dict.keys(Trunic.vowels) and y in dict.keys(Trunic.vowels):
                    out += Trunic.vowels.get(x)
                    lst.insert(0, y)
            else:
                # C
                if x in dict.keys(Trunic.consts):
                    out += Trunic.consts.get(x)

                # V
                elif x in dict.keys(Trunic.vowels):
                    out += "c"
                    out += Trunic.vowels.get(x)

                self.symbols += 1
 

    """
    Returns the string in the format specified by
    https://github.com/dirdam/fonts/tree/main/tunic#how-to-use-the-font
    """
    def encode(self) -> str:
        output = ""
        self.symbols = 0
        self.spaces = 0

        for word in self.phonemes:
            output += self._build_str(word)
            output += " "

        # Account for spaces between words.
        if len(self.phonemes) > 1:
            self.spaces += len(self.phonemes) - 1

        return output.strip()


    """
    Returns a list containing lists of phonemes for each word in the string.
    """
    def get_phonemes(self) -> list:
        return self.phonemes


    """
    Returns the IPA pronounciation for the string.
    """
    def to_ipa(self) -> str:
        output = ""
        for word in self.phonemes:
            for i in range(0, len(word)):
                output += word[i]
            output += " "
        return "/{}/".format(output.strip())


    """
    Creates a new .png file containing the Trunic text.
    Accepts hex, rgb, hsl and hsv strings with optional alpha channel.
    """
    def to_png(self, 
               path: str,
               file_name: str,
               font_size: int,
               back_color: str | tuple[int, int, int],
               font_color: str | tuple[int, int, int]) -> None:

        # w:66  h:96  sp:30 -> 100
        # w:132 h:192 sp:60 -> 200
        if self.symbols == 1:
            w_factor = 1.31515152
        else:
            w_factor = 1.21515152

        w = ceil(((font_size / w_factor) * self.symbols) + (font_size * 0.3 * self.spaces))
        h = ceil(font_size * 1.45454545)

        trunic = ImageFont.truetype(Trunic.font, font_size)
        img = Image.new("RGBA", size=(w, h), color=back_color)
        draw = ImageDraw.Draw(img)
        draw.text(xy=(font_size / 10, font_size / 6), text=self.encode(), fill=font_color, font=trunic)

        file_name += ".png"
        img.save(fp=os.path.join(path, file_name), bitmap_format="png")
