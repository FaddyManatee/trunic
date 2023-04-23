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
        self.phonemes = phonemize(text, language="en-gb-x-rp", strip=True, separator=sep, preserve_punctuation=True)
        self.phonemes = [i.split() for i in self.phonemes.split("-")]


    def to_ipa(self) -> str:
        output = "/"
        for word in self.phonemes:
            for i in range(0, len(word)):
                output += word[i]
            output += " "
        return output.strip() + "/"
    

    """
    Prints a list of words broken down into their phonemes.
    """
    def to_string(self) -> str:
        return str(self.phonemes)


    """
    Returns the string in the format specified by
    https://github.com/dirdam/fonts/tree/main/tunic#how-to-use-the-font
    """
    def decode(self) -> str:
        output = ""
        for word in self.phonemes:
            for i in range(0, len(word)):
                if word[i] in dict.keys(Trunic.vowels):
                    word[i] = Trunic.vowels.get(word[i])
                else:
                    word[i] = Trunic.consts.get(word[i])
                
                output += word[i]
            output += " "
        return output.strip()


    def to_png(self, 
               output: str,
               font_size: int,
               img_size: tuple[int, int],
               back_color: str | tuple[int, int, int],
               font_color: str | tuple[int, int, int]) -> None:

        trunic = ImageFont.truetype(Trunic.font, font_size)
        img = Image.new("RGBA", size=img_size, color=back_color)
        draw = ImageDraw.Draw(img)
        draw.text(xy=(10, 0), text=self.decode(), fill=font_color, font=trunic)
        img.save(output + ".png")
