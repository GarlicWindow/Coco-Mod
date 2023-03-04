from random import choice, randint


class SingleColour():
    name = "SolidColour"
    sprites = {1: 'solid'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length

class TwoColour():
    name = "TwoColour"
    sprites = {1: 'solid', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class Marbled():
    name = "Marbled"
    sprites = {1: 'marbled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} marbled"
        else:
            return self.colour + self.length + " marbled"

class Rosetted():
    name = "Rosetted"
    sprites = {1: 'rosetted', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rosetted"
        else:
            return self.colour + self.length + " rosetted"

class Ticked():
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"

class Spotted():
    name = "Spotted"
    sprites = {1: 'spotted', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} spotted{self.length}"
        else:
            return f"{self.colour} spotted{self.length}"

class Mackerel():
    name = "Mackerel"
    sprites = {1: 'mackerel', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} mackerel tabby{self.length}"
        else:
            return f"{self.colour} mackerel tabby{self.length}"

class Classic():
    name = "Classic"
    sprites = {1: 'classic', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} classic tabby{self.length}"
        else:
            return f"{self.colour} classic tabby{self.length}"

class Agouti():
    name = "Agouti"
    sprites = {1: 'agouti', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} agouti{self.length}"
        else:
            return f"{self.colour} agouti{self.length}"

class Tortie():
    name = "Tortie"
    sprites = {1: 'tortie', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"

class Calico():
    name = "Calico"
    sprites = {1: 'calico', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"calico{self.length}"


# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'INK', 'COAL', 'SHADOW', 'EBONY', 'BLACK', 'VOID',
    'CHOCOLATE', 'CHESTNUT', 'COCOA', 'UMBER', 'MUD', 'DARKCHOCOLATE',
    'CASHEW', 'PECAN', 'ALMOND', 'RUST', 'CINNAMON', 'WALNUT',
    'YELLOW', 'EMBER', 'GINGER', 'ORANGE', 'MARMALADE', 'RED',
    'CLOUD', 'MIST', 'GRAY', 'BLUE', 'STONE', 'STORM',
    'HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUSK', 'CEDAR',
    'PINK', 'ECRU', 'DUST', 'STAG', 'DOE', 'FAWN',
    'LIGHT', 'TAN', 'LEMON', 'SUN', 'HONEY', 'OCHRE',
    'PLATINUM', 'PIGEON', 'ASH', 'SOOT', 'ALUMINUM', 'GRAPHITE',
    'BEIGE', 'CANVAS', 'DAWN', 'DARKBEIGE', 'TAUPE', 'TWILIGHT',
    'ROSEGOLD', 'BUFF', 'OAT', 'SEPIA', 'OLIVE', 'TAWNY',
    'PEACH', 'SANDY', 'CORAL', 'APRICOT', 'SALMON', 'FLAME'
]
pelt_c_no_white = [
    'INK', 'COAL', 'SHADOW', 'EBONY', 'BLACK', 'VOID',
    'CHOCOLATE', 'CHESTNUT', 'COCOA', 'UMBER', 'MUD', 'DARKCHOCOLATE',
    'CASHEW', 'PECAN', 'ALMOND', 'RUST', 'CINNAMON', 'WALNUT',
    'YELLOW', 'EMBER', 'GINGER', 'ORANGE', 'MARMALADE', 'RED',
    'CLOUD', 'MIST', 'GRAY', 'BLUE', 'STONE', 'STORM',
    'HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUSK', 'CEDAR',
    'PINK', 'ECRU', 'DUST', 'STAG', 'DOE', 'FAWN',
    'LIGHT', 'TAN', 'LEMON', 'SUN', 'HONEY', 'OCHRE',
    'PLATINUM', 'PIGEON', 'ASH', 'SOOT', 'ALUMINUM', 'GRAPHITE',
    'BEIGE', 'CANVAS', 'DAWN', 'DARKBEIGE', 'TAUPE', 'TWILIGHT',
    'ROSEGOLD', 'BUFF', 'OAT', 'SEPIA', 'OLIVE', 'TAWNY',
    'PEACH', 'SANDY', 'CORAL', 'APRICOT', 'SALMON', 'FLAME'
]
pelt_c_no_bw = [
    'CHOCOLATE', 'CHESTNUT', 'COCOA', 'UMBER', 'MUD', 'DARKCHOCOLATE',
    'CASHEW', 'PECAN', 'ALMOND', 'RUST', 'CINNAMON', 'WALNUT',
    'YELLOW', 'EMBER', 'GINGER', 'ORANGE', 'MARMALADE', 'RED',
    'CLOUD', 'MIST', 'GRAY', 'BLUE', 'STONE', 'STORM',
    'HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUSK', 'CEDAR',
    'PINK', 'ECRU', 'DUST', 'STAG', 'DOE', 'FAWN',
    'LIGHT', 'TAN', 'LEMON', 'SUN', 'HONEY', 'OCHRE',
    'PLATINUM', 'PIGEON', 'ASH', 'SOOT', 'ALUMINUM', 'GRAPHITE',
    'BEIGE', 'CANVAS', 'DAWN', 'DARKBEIGE', 'TAUPE', 'TWILIGHT',
    'ROSEGOLD', 'BUFF', 'OAT', 'SEPIA', 'OLIVE', 'TAWNY',
    'PEACH', 'SANDY', 'CORAL', 'APRICOT', 'SALMON', 'FLAME'
]
tortiepatterns = ['tortiesolid', 'tortietabby', 'tortiebengal', 'tortiemarbled', 'tortieticked',
    'tortiesmoke', 'tortierosette', 'tortiespeckled', 'tortiemackerel', 'tortieclassic',
    'tortiesokoke', 'tortieagouti']
patch_colours = ['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'GOLDONE', 'GOLDTWO',
    'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR', 'CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
    'classic', 'sokoke', 'agouti', 'singlestripe']
tortiecolours = ["SILVER", "GREY", "DARKGREY", "BLACK", "GHOST", "LIGHTBROWN", "BROWN", "DARKBROWN"]

pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 
    'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'BLUE2', 'SUNLITICE', 'GREENYELLOW']
yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'GOLD', 'COPPER', 'GREENYELLOW']
blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'BLUE2', 'SUNLITICE', 'GREY']
green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL']
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
# bite scars by @wood pank on discord
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
          "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK",]

plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                    "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                    "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "PINK", "PURPLE", "MULTI", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW"
]

tabbies = ["Ticked", "Mackerel", "Classic", "Agouti"]
spotted = ["Spotted", "Rosette"]
plain = ["SolidColour", "TwoColour"]
exotic = ["Marbled"]
torties = ["Tortie", "Calico"]
pelt_categories = [tabbies, spotted, plain, exotic, torties]

# SPRITE NAMES
single_colours = [
    'INK', 'COAL', 'SHADOW', 'EBONY', 'BLACK', 'VOID',
    'CHOCOLATE', 'CHESTNUT', 'COCOA', 'UMBER', 'MUD', 'DARKCHOCOLATE',
    'CASHEW', 'PECAN', 'ALMOND', 'RUST', 'CINNAMON', 'WALNUT',
    'YELLOW', 'EMBER', 'GINGER', 'ORANGE', 'MARMALADE', 'RED',
    'CLOUD', 'MIST', 'GRAY', 'BLUE', 'STONE', 'STORM',
    'HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUSK', 'CEDAR',
    'PINK', 'ECRU', 'DUST', 'STAG', 'DOE', 'FAWN',
    'LIGHT', 'TAN', 'LEMON', 'SUN', 'HONEY', 'OCHRE',
    'PLATINUM', 'PIGEON', 'ASH', 'SOOT', 'ALUMINUM', 'GRAPHITE',
    'BEIGE', 'CANVAS', 'DAWN', 'DARKBEIGE', 'TAUPE', 'TWILIGHT',
    'ROSEGOLD', 'BUFF', 'OAT', 'SEPIA', 'OLIVE', 'TAWNY',
    'PEACH', 'SANDY', 'CORAL', 'APRICOT', 'SALMON', 'FLAME'

]
ginger_colours = ['YELLOW', 'EMBER', 'GINGER', 'ORANGE', 'MARMALADE', 'RED']
black_colours = ['INK', 'COAL', 'SHADOW', 'EBONY', 'BLACK', 'VOID']
chocolate_colours = ['CHOCOLATE', 'CHESTNUT', 'COCOA', 'UMBER', 'MUD', 'DARKCHOCOLATE']
cinnamon_colours = ['CASHEW', 'PECAN', 'ALMOND', 'RUST', 'CINNAMON', 'WALNUT']
cream_colours = ['LIGHT', 'TAN', 'LEMON', 'SUN', 'HONEY', 'OCHRE']
gray_colours = ['CLOUD', 'MIST', 'GRAY', 'BLUE', 'STONE', 'STORM']
lilac_colours = ['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUSK', 'CEDAR']
fawn_colours = ['PINK', 'ECRU', 'DUST', 'STAG', 'DOE', 'FAWN']
apricot_colours = ['PEACH', 'SANDY', 'CORAL', 'APRICOT', 'SALMON', 'FLAME']
caramel_colours = ['PLATINUM', 'PIGEON', 'ASH', 'SOOT', 'ALUMINUM', 'GRAPHITE']
taupe_colours = ['BEIGE', 'CANVAS', 'DAWN', 'DARKBEIGE', 'TAUPE', 'TWILIGHT']
fawntaupe_colours = ['ROSEGOLD', 'BUFF', 'OAT', 'SEPIA', 'OLIVE', 'TAWNY']
colour_categories = [ginger_colours, black_colours, chocolate_colours, cinnamon_colours,
                     cream_colours, gray_colours, lilac_colours, fawn_colours,
                    apricot_colours, caramel_colours, taupe_colours, fawntaupe_colours]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
    'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'BLUE2', 
    'SUNLITICE', 'GREENYELLOW'
]
little_white = ['LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS', 
    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY']
mid_white = ['TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR']
high_white = ['ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 
    'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
    'CURVED', 'GLASS', 'MASKMANTLE']
mostly_white = ['VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE']
point_markings = ['COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'KARPATI', 'SEPIAPOINT', 'MINKPOINT', 
    'SEALPOINT']
vit = ['VITILIGO', 'VITILIGO2']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE', 'EXTRA'
]

skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']


# CHOOSING PELT
def choose_pelt(colour=None, white=None, pelt=None, length=None, category=None, determined=False):
    colour = colour
    white = white
    pelt = pelt
    length = length
    category = category
    if pelt is None:
        if category != None:
            pelt = choice(category)
    else:
        pelt = pelt
    if length is None:
        length = choice(pelt_length)
    if pelt == 'SingleColour':
        if colour is None and not white:
            return SingleColour(choice(pelt_colours), length)
        elif colour is None:
            return SingleColour("WHITE", length)
        else:
            return SingleColour(colour, length)
    elif pelt == 'TwoColour':
        if colour is None:
            return TwoColour(choice(pelt_c_no_white), length)
        else:
            return TwoColour(colour, length)
    elif pelt == 'Marbled':
        if colour is None and white is None:
            return Marbled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Marbled(choice(pelt_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == 'Rosetted':
        if colour is None and white is None:
            return Rosetted(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rosetted(choice(pelt_colours), white, length)
        else:
            return Rosetted(colour, white, length)
    elif pelt == 'Ticked':
        if colour is None and white is None:
            return Ticked(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == 'Spotted':
        if colour is None and white is None:
            return Spotted(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Spotted(choice(pelt_colours), white, length)
        else:
            return Spotted(colour, white, length)
    elif pelt == 'Mackerel':
        if colour is None and white is None:
            return Mackerel(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Mackerel(choice(pelt_colours), white, length)
        else:
            return Mackerel(colour, white, length)
    elif pelt == 'Classic':
        if colour is None and white is None:
            return Classic(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Classic(choice(pelt_colours), white, length)
        else:
            return Classic(colour, white, length)
    elif pelt == 'Agouti':
        if colour is None and white is None:
            return Agouti(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Agouti(choice(pelt_colours), white, length)
        else:
            return Agouti(colour, white, length)
    elif pelt == 'Tortie':
        if white is None:
            return Tortie(colour, choice([False, True]), length)
        else:
            return Tortie(colour, white, length)
    else:
        return Calico(colour, length)

def describe_color(pelt, tortiecolour, tortiepattern, white_patches):
        color_name = ''
        color_name = str(pelt.colour).lower()
        if tortiecolour is not None:
            color_name = str(tortiecolour).lower()
        if color_name == 'darkchocolate':
            color_name = 'dark chocolate'
        elif color_name == 'darkbeige':
            color_name = 'dark beige'
        elif color_name == 'rosegold':
            color_name = 'rose gold'
        elif pelt.name == "Spotted":
            color_name = color_name + ' spotted'
        elif pelt.name == "Marbled":
            color_name = color_name + ' marbled tabby'
        elif pelt.name == "Rosetted":
            color_name = color_name + ' rosetted'
        elif pelt.name == "Ticked":
            color_name = color_name + ' ticked tabby'
        elif pelt.name == "Mackerel":
            color_name = color_name + ' mackerel tabby'
        elif pelt.name == "Classic":
            color_name = color_name + ' classic tabby'
        elif pelt.name == "Agouti":
            color_name = color_name + ' agouti'

        elif pelt.name == "Tortie":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' torbie'
            else:
                color_name = color_name + ' tortie'
        elif pelt.name == "Calico":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' tabico'
            else:
                color_name = color_name + ' calico'
        # enough to comment but not make calico
        if white_patches is not None:
            if white_patches in little_white + mid_white:
                color_name = color_name + ' and white'
            # and white
            elif white_patches in high_white:
                if pelt.name != "Calico":
                    color_name = color_name + ' and white'
            # white and
            elif white_patches in mostly_white:
                color_name = 'white and ' + color_name
            # colorpoint
            elif white_patches in point_markings:
                color_name = color_name + ' point'
                if color_name == 'dark ginger point' or color_name == 'ginger point':
                    color_name = 'flame point'
            # vitiligo
            elif white_patches in vit:
                color_name = color_name + ' with vitiligo'
        else:
            color_name = color_name

        if color_name == 'tortie':
            color_name = 'tortoiseshell'

        if white_patches == 'FULLWHITE':
            color_name = 'white'

        if color_name == 'white and white':
            color_name = 'white'

        return color_name
