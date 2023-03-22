from random import choice


class SolidColour():
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


class Smoke():
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"


class Singlestripe():
    name = "Singlestripe"
    sprites = {1: 'singlestripe', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} singlestripe{self.length}"
        else:
            return f"{self.colour} singlestripe{self.length}"


class Tabby():
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"


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


class Sokoke():
    name = "Sokoke"
    sprites = {1: 'sokoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} sokoke tabby{self.length}"
        else:
            return f"{self.colour} sokoke tabby{self.length}"


class Bengal():
    name = "Bengal"
    sprites = {1: 'bengal', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bengal{self.length}"
        else:
            return f"{self.colour} bengal{self.length}"


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
    'PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED',
    'BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK',
    'LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE',
    'PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON',
    'PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE',
    'PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY',
    'PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC',
    'PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN',
    'PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME',
    'ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL',
    'GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY',
    'PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE',

]
pelt_c_no_white = [
    'PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED',
    'BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK',
    'LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE',
    'PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON',
    'PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE',
    'PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY',
    'PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC',
    'PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN',
    'PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME',
    'ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL',
    'GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY',
    'PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE',
]
pelt_c_no_bw = [
    'PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED',
    'LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE',
    'PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON',
    'PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE',
    'PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY',
    'PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC',
    'PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN',
    'PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME',
    'ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL',
    'GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY',
    'PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE',
]

tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMAL1', 'MINIMAL2', 'MINIMAL3', 'MINIMAL4',
                  'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE',
                  'ROBIN', 'BRINDLE', 'PAIGE']
tortiebases = ['solid', 'smoke',
               'singlestripe', 'tabby', 'mackerel', 'classic',
               'ticked', 'agouti',
               'spotted', 'rosetted',
               'marbled', 'sokoke', 'bengal']

pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 
    'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER']
yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'GOLD', 'COPPER', 'GREENYELLOW', 'BRONZE', 'SILVER']
blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'COBALT', 'SUNLITICE', 'GREY']
green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL']
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
# bite scars by @wood pank on discord
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
          "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
          "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
          "FROSTSOCK", ]

# make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                     "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                     "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
                     ]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
                    ]
tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS"]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON",
    "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON",
    "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON",
]

tabbies = ["Tabby", "Mackerel", "Classic", "Ticked", "Agouti", "Sokoke"]
spotted = ["Spotted", "Rosetted"]
plain = ["SolidColour", "TwoColour", "Smoke", "Singlestripe"]
exotic = ["Marbled", "Bengal"]
torties = ["Tortie", "Calico"]
pelt_categories = [tabbies, spotted, plain, exotic, torties]

# SPRITE NAMES
single_colours = [
    'PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED',
    'BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK',
    'LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE',
    'PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON',
    'PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE',
    'PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY',
    'PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC',
    'PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN',
    'PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME',
    'ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL',
    'GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY',
    'PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE',
]
ginger_colours = ['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']
black_colours = ['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']
chocolate_colours = ['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']
cinnamon_colours = ['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']
cream_colours = ['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']
blue_colours = ['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']
lilac_colours = ['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']
fawn_colours = ['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']
apricot_colours = ['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']
caramel_colours = ['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']
taupe_colours = ['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']
tan_colours = ['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']
colour_categories = [ginger_colours, black_colours, chocolate_colours, cinnamon_colours,
                    cream_colours, blue_colours, lilac_colours, fawn_colours,
                    apricot_colours, caramel_colours, taupe_colours, tan_colours]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
    'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT',
    'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER'
]
little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'LUNA',
                'EXTRA']
mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR',
             'WINGS']
high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
              'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
              'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED']
mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO']
point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

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
    if pelt == 'SolidColour':
        if colour is None and not white:
            return SolidColour(choice(pelt_colours), length)
        elif colour is None:
            return SolidColour("WHITE", length)
        else:
            return SolidColour(colour, length)
    elif pelt == 'TwoColour':
        if colour is None:
            return TwoColour(choice(pelt_c_no_white), length)
        else:
            return TwoColour(colour, length)
    elif pelt == 'Smoke':
        if colour is None and white is None:
            return Smoke(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Smoke(choice(pelt_colours), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == 'Singlestripe':
        if colour is None and white is None:
            return Singlestripe(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Singlestripe(choice(pelt_colours), white, length)
        else:
            return Singlestripe(colour, white, length)
    elif pelt == 'Tabby':
        if colour is None and white is None:
            return Tabby(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Tabby(choice(pelt_colours), white, length)
        else:
            return Tabby(colour, white, length)
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
    elif pelt == 'Ticked':
        if colour is None and white is None:
            return Ticked(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == 'Agouti':
        if colour is None and white is None:
            return Agouti(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Agouti(choice(pelt_colours), white, length)
        else:
            return Agouti(colour, white, length)
    elif pelt == 'Spotted':
        if colour is None and white is None:
            return Spotted(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Spotted(choice(pelt_colours), white, length)
        else:
            return Spotted(colour, white, length)
    elif pelt == 'Rosetted':
        if colour is None and white is None:
            return Rosetted(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rosetted(choice(pelt_colours), white, length)
        else:
            return Rosetted(colour, white, length)
    elif pelt == 'Marbled':
        if colour is None and white is None:
            return Marbled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Marbled(choice(pelt_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == 'Sokoke':
        if colour is None and white is None:
            return Sokoke(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Sokoke(choice(pelt_colours), white, length)
        else:
            return Sokoke(colour, white, length)
    elif pelt == 'Bengal':
        if colour is None and white is None:
            return Bengal(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Bengal(choice(pelt_colours), white, length)
        else:
            return Bengal(colour, white, length)
    elif pelt == 'Tortie':
        if white is None:
            return Tortie(colour, choice([False, True]), length)
        else:
            return Tortie(colour, white, length)
    else:
        return Calico(colour, length)
    
def describe_appearance(cat, short=False):
    
    # Define look-up dictionaries
    if short:
        renamed_colors = {
            "paleginger": "ginger",
            "brightyellow": "ginger",
            "brownblack": "black",
            "pitchblack": "black",
            "jetblack": "black",
            "lightchocolate": "chocolate",
            "darkbrown": "chocolate",
            "darkchocolate": "chocolate",
            "palebrown": "cinnamon",
            "lightcinnamon": "cinnamon",
            "darkcinnamon": "cinnamon",
            "palecream": "cream",
            "palegray": "blue",
            "darkgray": "blue",
            "palelilac": "lilac",
            "darklilac": "lilac",
            "palefawn": "fawn",
            "darkfawn": "fawn",
            "paleapricot": "apricot",
            "lightcaramel": "caramel",
            "darkcaramel": "caramel",
            "ghosttaupe": "taupe",
            "paletaupe": "taupe",
            "lighttaupe": "taupe"
        }
    else:
        renamed_colors = {
            "paleginger": "pale ginger",
            "brightyellow": "bright yellow",
            "brownblack": "brown-black",
            "pitchblack": "pitch black",
            "jetblack": "jet black",
            "lightchocolate": "light chocolate",
            "darkbrown": "dark brown",
            "darkchocolate": "dark chocolate",
            "palebrown": "pale brown",
            "lightcinnamon": "light cinnamon",
            "darkcinnamon": "dark cinnamon",
            "palecream": "pale cream",
            "palegray": "pale gray",
            "darkgray": "dark gray",
            "palelilac": "pale lilac",
            "darklilac": "dark lilac",
            "palefawn": "pale fawn",
            "darkfawn": "dark fawn",
            "paleapricot": "pale apricot",
            "lightcaramel": "light caramel",
            "darkcaramel": "dark caramel",
            "ghosttaupe": "ghost taupe",
            "paletaupe": "pale taupe",
            "lighttaupe": "light taupe"
        }

    pattern_des = {
        "Smoke": "c_n smoke",
        "Singlestripe": "dorsal-striped c_n",
        "Tabby": "c_n tabby",
        "Mackerel": "c_n tabby",
        "Classic": "c_n tabby",
        "Ticked": "c_n ticked",
        "Agouti": "c_n tabby",
        "Spotted": "spotted c_n",
        "Rosetted": "unusually spotted c_n",
        "Marbled": "c_n tabby",
        "Sokoke": "c_n tabby",
        "Bengal": "unusually dappled c_n"
    }

    # Start with determining the base color name. 
    color_name = str(cat.pelt.colour).lower()
    if color_name in renamed_colors:
        color_name = renamed_colors[color_name]
    
    # Replace "white" with "pale" if the cat is 
    if cat.pelt.name not in ["SolidColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
        color_name = "pale"

    # Time to descibe the pattern and any additional colors. 
    if cat.pelt.name in pattern_des:
        color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
    elif cat.pelt.name in torties:
        # Calicos and Torties need their own desciptions. 
        if short:
            # If using short, don't add describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
            # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
            if cat.pelt.colour in black_colours + chocolate_colours + cinnamon_colours + blue_colours + lilac_colours + fawn_colours + caramel_colours + taupe_colours + tan_colours and \
                cat.tortiecolour in black_colours + chocolate_colours + cinnamon_colours + blue_colours + lilac_colours + fawn_colours + caramel_colours + taupe_colours + tan_colours:
                color_name = "mottled"
            else:
                color_name = cat.pelt.name.lower()
        else:
            base = cat.tortiebase.lower()
            if base in tabbies + ['bengal', 'rosetted', 'spotted']:
                base = 'tabby'
            else:
                base = ''

            patches_color = cat.tortiecolour.lower()
            if patches_color in renamed_colors:
                patches_color = renamed_colors[patches_color]
            color_name = f"{color_name}/{patches_color}"
            
            if cat.pelt.colour in black_colours + chocolate_colours + cinnamon_colours + blue_colours + lilac_colours + fawn_colours + caramel_colours + taupe_colours + tan_colours and \
                cat.tortiecolour in black_colours + chocolate_colours + cinnamon_colours + blue_colours + lilac_colours + fawn_colours + caramel_colours + taupe_colours + tan_colours:
                color_name = f"{color_name} mottled"
            else:
                color_name = f"{color_name} {cat.pelt.name.lower()}"

    if cat.white_patches:
        if cat.white_patches == "FULLWHITE":
            # If the cat is fullwhite, discard all other information. They are just white. 
            color_name = "white"
        if cat.white_patches in mostly_white and cat.pelt.name != "Calico":
            color_name = f"white and {color_name}"
        elif cat.pelt.name != "Calico":
            color_name = f"{color_name} and white"
    
    if cat.points:
        color_name = f"{color_name} point"
        if "ginger point" in color_name:
            color_name.replace("ginger point", "flame point")

    if "white and white" in color_name:
        color_name = color_name.replace("white and white", "white")

    # Now it's time for gender
    if cat.genderalign in ["female", "trans female"]:
        color_name = f"{color_name} she-cat"
    elif cat.genderalign in ["male", "trans male"]:
        color_name = f"{color_name} tom"
    else:
        color_name = f"{color_name} cat"

    # Here is the place where we can add some additional details about the cat, for the full non-short one. 
    # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars. 
    if not short:
        
        scar_details = {
            "NOTAIL": "no tail", 
            "HALFTAIL": "half a tail", 
            "NOPAW": "three legs", 
            "NOLEFTEAR": "a missing ear", 
            "NORIGHTEAR": "a missing ear",
            "NOEAR": "no ears"
        }

        additional_details = []
        if cat.vitiligo:
            additional_details.append("vitiligo")
        for scar in cat.scars:
            if scar in scar_details and scar_details[scar] not in additional_details:
                additional_details.append(scar_details[scar])
        
        if len(additional_details) > 1:
            color_name = f"{color_name} with {', '.join(additional_details[:-1])} and {additional_details[-1]}"
        elif additional_details:
            color_name = f"{color_name} with {additional_details[0]}"
    
    
        if len(cat.scars) >= 3:
            color_name = f"scarred {color_name}"
        if cat.pelt.length == "long":
            color_name = f"long-furred {color_name}"

    return color_name
    