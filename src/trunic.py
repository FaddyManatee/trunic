import os
from PIL import ImageFont, Image, ImageDraw


class Trunic:
    vowels = {
        "æ":"a",      # back, sad
        "ɑː":"ar",    # arm, large
        "ɒ":"ah",     # swan, box
        "eɪ":"ay",    # bay, game 
        "ɛ":"e",      # end, pet
        "iː":"ee",    # bee, team
        "ɪəʳ":"eer",  # near, here 
        "ə":"eh",     # the, about 
        "eəʳ":"ere",  # air, vary
        "ɪ":"i",      # bit, rich 
        "aɪ":"ie",    # guy, life
        "ɜːʳ":"ir",   # bird, work 
        "oʊ":"oh",    # toe, over
        "ɔɪ":"oi",    # toy, avoid    
        "uː":"oo",    # too, june
        "ʊ":"ou",     # wolf, good
        "aʊ":"ow",    # how, your
        "ʊəʳ":"ore"   # your, cure
    }

    conson = {
        "b":"b",      # boss, baby 
        "tʃ":"ch",    # chat, catch
        "d":"d",      # dog, dad
        "f":"f",      # fox, fail 
        "g":"g",      # gun, bag
        "h":"h",      # hop, house
        "dʒ":"j",     # jam, judge 
        "k":"k",      # cat, skip 
        "l":"l",      # live, leaf
        "m":"m",      # man, mime 
        "n":"n",      # net, nun
        "ŋ":"ng",     # rink, sing 
        "p":"p",      # poppy, pip
        "ɹ":"r",      # run, borrow    
        "s":"s",      # sit, sass
        "ʃ":"sh",     # shut, shoe
        "t":"t",      # tunic, stop
        "θ":"th",     # think, bath
        "ð":"th",     # this, the
        "v":"v",      # vine, verge
        "w":"w",      # wow, worry
        "j":"y",      # you, yes
        "z":"z",      # zoo
        "ʒ":"zh"      # vision
    }

    font = os.path.join(os.path.dirname(__file__), "trunic.otf")

    def __init__(self, text: str) -> None:
        pass


    """
    Returns the string in the format specified by
    https://github.com/dirdam/fonts/tree/main/tunic#how-to-use-the-font
    """
    def to_string(self):
        pass


    def to_image(self, 
                output: str,
                img_size,
                color: str,
                font_size: int,
                font_color: str) -> None:

        trunic = ImageFont.truetype(Trunic.font, font_size)
        img = Image.new("RGBA", size=img_size, color=color)
        draw = ImageDraw.Draw(img)
        draw.text(xy=(10, 0), text=self.to_string(), fill=font_color, font=trunic)
        img.save(output + ".png")
