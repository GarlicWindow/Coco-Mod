import pygame

try:
    import ujson
except ImportError:
    import json as ujson


class Sprites():
    cat_tints = {}
    white_patches_tints = {}

    def __init__(self, original_size, new_size=None):
        self.size = original_size  # size of a single sprite in a spritesheet
        self.new_size = self.size * 2 if new_size is None else new_size
        self.spritesheets = {}
        self.images = {}
        self.groups = {}
        self.sprites = {}

        self.load_tints()

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", 'r') as read_file:
                Sprites.cat_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Tints")

        try:
            with open("sprites/dicts/white_patches_tint.json", 'r') as read_file:
                Sprites.white_patches_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading White Patches Tints")

    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def find_sprite(self, group_name, x, y):
        """
        Find singular sprite from a group.

        Parameters:
        group_name -- Name of Pygame group to find sprite from.
        x -- X-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        y -- Y-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        """
        # pixels will be calculated automatically, so for x and y, just use 0, 1, 2, 3 etc.
        new_sprite = pygame.Surface((self.size, self.size),
                                    pygame.HWSURFACE | pygame.SRCALPHA)
        new_sprite.blit(self.groups[group_name], (0, 0),
                        (x * self.size, y * self.size, (x + 1) * self.size,
                         (y + 1) * self.size))
        return new_sprite

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=3,
                   sprites_y=7):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a sprite-sheet into groups of sprites that are easily accessible.

        Parameters:
        spritesheet -- Name of spritesheet.
        pos -- (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites.
        name -- Name of group to make.
        
        Keyword Arguments
        sprites_x -- Number of sprites horizontally (default: 3)
        sprites_y -- Number of sprites vertically (default: 3)
        """

        # making the group
        new_group = pygame.Surface(
            (self.size * sprites_x, self.size * sprites_y),
            pygame.HWSURFACE | pygame.SRCALPHA)
        new_group.blit(
            self.spritesheets[spritesheet], (0, 0),
            (pos[0] * sprites_x * self.size, pos[1] * sprites_y * self.size,
             (pos[0] + sprites_x) * self.size,
             (pos[1] + sprites_y) * self.size))

        self.groups[name] = new_group

        # splitting group into singular sprites and storing into self.sprites section
        x_spr = 0
        y_spr = 0
        for x in range(sprites_x * sprites_y):
            new_sprite = pygame.Surface((self.size, self.size),
                                        pygame.HWSURFACE | pygame.SRCALPHA)
            new_sprite.blit(new_group, (0, 0),
                            (x_spr * self.size, y_spr * self.size,
                             (x_spr + 1) * self.size, (y_spr + 1) * self.size))
            self.sprites[name + str(x)] = new_sprite
            x_spr += 1
            if x_spr == sprites_x:
                x_spr = 0
                y_spr += 1

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """
        for a, i in enumerate(
                ["ONE", "TWO", "THREE", "MANLEG", "BRIGHTHEART", "MANTAIL", 
                 "BRIDGE", "RIGHTBLIND", "LEFTBLIND", "BOTHBLIND", "BURNPAWS", "BURNTAIL"]):
            sprites.make_group('scars', (a, 0), f'scars{i}')
        for a, i in enumerate(
                ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE",
                 "FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"]):
            sprites.make_group('scars', (a, 1), f'scars{i}')
        for a, i in enumerate(
                ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY", "TOETRAP", "SNAKE",
                 "LEGBITE", "NECKBITE", "FACE"]):
            sprites.make_group('scars', (a, 2), f'scars{i}')
        # missing parts
        for a, i in enumerate(
                ["LEFTEAR", "RIGHTEAR", "NOTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR", "HALFTAIL", "NOPAW"]):
            sprites.make_group('missingscars', (a, 0), f'scars{i}')

            # Accessories
        for a, i in enumerate([
            "MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"]):
            sprites.make_group('medcatherbs', (a, 0), f'acc_herbs{i}')
        for a, i in enumerate([
            "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"]):
            sprites.make_group('medcatherbs', (a, 1), f'acc_herbs{i}')
        for a, i in enumerate([
            "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]):
            sprites.make_group('medcatherbs', (a, 3), f'acc_herbs{i}')
        sprites.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')

        for a, i in enumerate([
            "RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]):
            sprites.make_group('medcatherbs', (a, 2), f'acc_wild{i}')
        for a, i in enumerate(["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"]):
            sprites.make_group('collars', (a, 0), f'collars{i}')
        for a, i in enumerate(["GREEN", "RAINBOW", "BLACK", "SPIKES", "WHITE"]):
            sprites.make_group('collars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINK", "PURPLE", "MULTI", "INDIGO"]):
            sprites.make_group('collars', (a, 2), f'collars{i}')
        for a, i in enumerate([
            "CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL",
            "LIMEBELL"
        ]):
            sprites.make_group('bellcollars', (a, 0), f'collars{i}')
        for a, i in enumerate(
                ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL"]):
            sprites.make_group('bellcollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINKBELL", "PURPLEBELL", "MULTIBELL", "INDIGOBELL"]):
            sprites.make_group('bellcollars', (a, 2), f'collars{i}')
        for a, i in enumerate([
            "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
            "LIMEBOW"
        ]):
            sprites.make_group('bowcollars', (a, 0), f'collars{i}')
        for a, i in enumerate(
                ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW"]):
            sprites.make_group('bowcollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"]):
            sprites.make_group('bowcollars', (a, 2), f'collars{i}')
        for a, i in enumerate([
            "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON",
            "LIMENYLON"
        ]):
            sprites.make_group('nyloncollars', (a, 0), f'collars{i}')
        for a, i in enumerate(
                ["GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON"]):
            sprites.make_group('nyloncollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON"]):
            sprites.make_group('nyloncollars', (a, 2), f'collars{i}')


sprites = Sprites(50)
#tiles = Sprites(64)

for x in [
    'lightingnew', 'shadersnewwhite',
    'fademask', 'fadestarclan', 'fadedarkforest',
    'lineart', 'lineartdead', 'lineartdf',
    'skin',
    'scars', 'missingscars',
    'eyes', 'eyes2',
    'cocosolidcolours', 'cocosmokecolours',
    'cocosinglestripecolours', 'cocotabbycolours', 'cocomackerelcolours', 'cococlassiccolours',
    'cocotickedcolours', 'cocoagouticolours',
    'cocospottedcolours', 'cocorosettedcolours',
    'cocomarbledcolours', 'cocosokokecolours', 'cocobengalcolours',
    'tortiepatchesmasks',
    'whitepatches',
    'medcatherbs',
    'collars', 'bellcollars', 'nyloncollars', 'bowcollars'
]:
    sprites.spritesheet(f"sprites/{x}.png", x)

# Line art
sprites.make_group('lineart', (0, 0), 'lines')
sprites.make_group('shadersnewwhite', (0, 0), 'shaders')
sprites.make_group('lightingnew', (0, 0), 'lighting')

sprites.make_group('lineartdead', (0, 0), 'lineartdead')
sprites.make_group('lineartdf', (0, 0), 'lineartdf')

# Fading Fog
for i in range(0, 3):
    sprites.make_group('fademask', (i, 0), f'fademask{i}')
    sprites.make_group('fadestarclan', (i, 0), f'fadestarclan{i}')
    sprites.make_group('fadedarkforest', (i, 0), f'fadedf{i}')

for a, i in enumerate(
        ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 
        'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHERBLUE', 'SUNLITICE']):
    sprites.make_group('eyes', (a, 0), f'eyes{i}')
    sprites.make_group('eyes2', (a, 0), f'eyes2{i}')
for a, i in enumerate(
        ['COPPER', 'SAGE', 'COBALT', 'PALEBLUE', 'BRONZE', 'SILVER',
        'PALEYELLOW', 'GOLD', 'GREENYELLOW']):
    sprites.make_group('eyes', (a, 1), f'eyes{i}')
    sprites.make_group('eyes2', (a, 1), f'eyes2{i}')

# white patches
for a, i in enumerate(['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANYTWO',
    'MOON', 'PHANTOM', 'POWDER']):
    sprites.make_group('whitepatches', (a, 0), f'white{i}')
for a, i in enumerate(['EXTRA', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL', 
    'LIGHTSONG', 'VITILIGO', 'BLACKSTAR', 'PIEBALD', 'CURVED', 'PETAL']):
    sprites.make_group('whitepatches', (a, 1), f'white{i}')
# ryos white patches
for a, i in enumerate(['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO', 'GOATEE', 'VITILIGOTWO',
    'PAWS', 'MITAINE', 'BROKENBLAZE', 'SCOURGE']):
    sprites.make_group('whitepatches', (a, 2), f'white{i}')
for a, i in enumerate(['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'HONEY',
    'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TAILTIP', 'TOES']):
    sprites.make_group('whitepatches', (a, 3), f'white{i}')
for a, i in enumerate(
        ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW',
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA']):
    sprites.make_group('whitepatches', (a, 4), f'white{i}')
# beejeans white patches + perrio's point marks, painted, and heart2 + anju's new marks + key's blackstar
for a, i in enumerate(['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT',
    'MAO', 'LUNA', 'CHESTSPECK', 'WINGS', 'PAINTED', 'HEARTTWO']):
    sprites.make_group('whitepatches', (a, 5), 'white' + i)

# Solid
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocosolidcolours', (a, 0), f'solid{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocosolidcolours', (a, 1), f'solid{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocosolidcolours', (a, 2), f'solid{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocosolidcolours', (a, 3), f'solid{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocosolidcolours', (a, 4), f'solid{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocosolidcolours', (a, 5), f'solid{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocosolidcolours', (a, 6), f'solid{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocosolidcolours', (a, 7), f'solid{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocosolidcolours', (a, 8), f'solid{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocosolidcolours', (a, 9), f'solid{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocosolidcolours', (a, 10), f'solid{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocosolidcolours', (a, 11), f'solid{i}')
# Smoke
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocosmokecolours', (a, 0), f'smoke{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocosmokecolours', (a, 1), f'smoke{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocosmokecolours', (a, 2), f'smoke{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocosmokecolours', (a, 3), f'smoke{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocosmokecolours', (a, 4), f'smoke{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocosmokecolours', (a, 5), f'smoke{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocosmokecolours', (a, 6), f'smoke{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocosmokecolours', (a, 7), f'smoke{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocosmokecolours', (a, 8), f'smoke{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocosmokecolours', (a, 9), f'smoke{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocosmokecolours', (a, 10), f'smoke{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocosmokecolours', (a, 11), f'smoke{i}')
# Singlestripe
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocosinglestripecolours', (a, 0), f'singlestripe{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocosinglestripecolours', (a, 1), f'singlestripe{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocosinglestripecolours', (a, 2), f'singlestripe{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocosinglestripecolours', (a, 3), f'singlestripe{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocosinglestripecolours', (a, 4), f'singlestripe{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocosinglestripecolours', (a, 5), f'singlestripe{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocosinglestripecolours', (a, 6), f'singlestripe{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocosinglestripecolours', (a, 7), f'singlestripe{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocosinglestripecolours', (a, 8), f'singlestripe{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocosinglestripecolours', (a, 9), f'singlestripe{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocosinglestripecolours', (a, 10), f'singlestripe{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocosinglestripecolours', (a, 11), f'singlestripe{i}')
# Tabby
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocotabbycolours', (a, 0), f'tabby{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocotabbycolours', (a, 1), f'tabby{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocotabbycolours', (a, 2), f'tabby{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocotabbycolours', (a, 3), f'tabby{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocotabbycolours', (a, 4), f'tabby{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocotabbycolours', (a, 5), f'tabby{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocotabbycolours', (a, 6), f'tabby{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocotabbycolours', (a, 7), f'tabby{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocotabbycolours', (a, 8), f'tabby{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocotabbycolours', (a, 9), f'tabby{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocotabbycolours', (a, 10), f'tabby{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocotabbycolours', (a, 11), f'tabby{i}')
# Mackerel
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocomackerelcolours', (a, 0), f'mackerel{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocomackerelcolours', (a, 1), f'mackerel{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocomackerelcolours', (a, 2), f'mackerel{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocomackerelcolours', (a, 3), f'mackerel{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocomackerelcolours', (a, 4), f'mackerel{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocomackerelcolours', (a, 5), f'mackerel{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocomackerelcolours', (a, 6), f'mackerel{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocomackerelcolours', (a, 7), f'mackerel{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocomackerelcolours', (a, 8), f'mackerel{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocomackerelcolours', (a, 9), f'mackerel{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocomackerelcolours', (a, 10), f'mackerel{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocomackerelcolours', (a, 11), f'mackerel{i}')
# Classic
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cococlassiccolours', (a, 0), f'classic{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cococlassiccolours', (a, 1), f'classic{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cococlassiccolours', (a, 2), f'classic{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cococlassiccolours', (a, 3), f'classic{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cococlassiccolours', (a, 4), f'classic{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cococlassiccolours', (a, 5), f'classic{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cococlassiccolours', (a, 6), f'classic{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cococlassiccolours', (a, 7), f'classic{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococlassiccolours', (a, 8), f'classic{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cococlassiccolours', (a, 9), f'classic{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cococlassiccolours', (a, 10), f'classic{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cococlassiccolours', (a, 11), f'classic{i}')
# Ticked
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocotickedcolours', (a, 0), f'ticked{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocotickedcolours', (a, 1), f'ticked{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocotickedcolours', (a, 2), f'ticked{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocotickedcolours', (a, 3), f'ticked{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocotickedcolours', (a, 4), f'ticked{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocotickedcolours', (a, 5), f'ticked{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocotickedcolours', (a, 6), f'ticked{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocotickedcolours', (a, 7), f'ticked{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocotickedcolours', (a, 8), f'ticked{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocotickedcolours', (a, 9), f'ticked{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocotickedcolours', (a, 10), f'ticked{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocotickedcolours', (a, 11), f'ticked{i}')
# Agouti
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocoagouticolours', (a, 0), f'agouti{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocoagouticolours', (a, 1), f'agouti{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocoagouticolours', (a, 2), f'agouti{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocoagouticolours', (a, 3), f'agouti{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocoagouticolours', (a, 4), f'agouti{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocoagouticolours', (a, 5), f'agouti{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocoagouticolours', (a, 6), f'agouti{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocoagouticolours', (a, 7), f'agouti{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocoagouticolours', (a, 8), f'agouti{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocoagouticolours', (a, 9), f'agouti{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocoagouticolours', (a, 10), f'agouti{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocoagouticolours', (a, 11), f'agouti{i}')
# Spotted
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocospottedcolours', (a, 0), f'spotted{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocospottedcolours', (a, 1), f'spotted{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocospottedcolours', (a, 2), f'spotted{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocospottedcolours', (a, 3), f'spotted{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocospottedcolours', (a, 4), f'spotted{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocospottedcolours', (a, 5), f'spotted{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocospottedcolours', (a, 6), f'spotted{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocospottedcolours', (a, 7), f'spotted{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocospottedcolours', (a, 8), f'spotted{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocospottedcolours', (a, 9), f'spotted{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocospottedcolours', (a, 10), f'spotted{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocospottedcolours', (a, 11), f'spotted{i}')
# Rosetted
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocorosettedcolours', (a, 0), f'rosetted{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocorosettedcolours', (a, 1), f'rosetted{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocorosettedcolours', (a, 2), f'rosetted{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocorosettedcolours', (a, 3), f'rosetted{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocorosettedcolours', (a, 4), f'rosetted{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocorosettedcolours', (a, 5), f'rosetted{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocorosettedcolours', (a, 6), f'rosetted{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocorosettedcolours', (a, 7), f'rosetted{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocorosettedcolours', (a, 8), f'rosetted{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocorosettedcolours', (a, 9), f'rosetted{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocorosettedcolours', (a, 10), f'rosetted{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocorosettedcolours', (a, 11), f'rosetted{i}')
# Marbled
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocomarbledcolours', (a, 0), f'marbled{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocomarbledcolours', (a, 1), f'marbled{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocomarbledcolours', (a, 2), f'marbled{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocomarbledcolours', (a, 3), f'marbled{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocomarbledcolours', (a, 4), f'marbled{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocomarbledcolours', (a, 5), f'marbled{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocomarbledcolours', (a, 6), f'marbled{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocomarbledcolours', (a, 7), f'marbled{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocomarbledcolours', (a, 8), f'marbled{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocomarbledcolours', (a, 9), f'marbled{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocomarbledcolours', (a, 10), f'marbled{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocomarbledcolours', (a, 11), f'marbled{i}')
# Sokoke
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocosokokecolours', (a, 0), f'sokoke{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocosokokecolours', (a, 1), f'sokoke{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocosokokecolours', (a, 2), f'sokoke{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocosokokecolours', (a, 3), f'sokoke{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocosokokecolours', (a, 4), f'sokoke{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocosokokecolours', (a, 5), f'sokoke{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocosokokecolours', (a, 6), f'sokoke{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocosokokecolours', (a, 7), f'sokoke{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocosokokecolours', (a, 8), f'sokoke{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocosokokecolours', (a, 9), f'sokoke{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocosokokecolours', (a, 10), f'sokoke{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocosokokecolours', (a, 11), f'sokoke{i}')
# Bengal
for a, i in enumerate(['PALEGINGER', 'BRIGHTYELLOW', 'ORANGE', 'GINGER', 'COPPER', 'RED']):
    sprites.make_group('cocobengalcolours', (a, 0), f'bengal{i}')
for a, i in enumerate(['BROWNBLACK', 'SOOTY', 'EBONY', 'BLACK', 'PITCHBLACK', 'JETBLACK']):
    sprites.make_group('cocobengalcolours', (a, 1), f'bengal{i}')
for a, i in enumerate(['LIGHTCHOCOLATE', 'CHESTNUT', 'BROWN', 'CHOCOLATE', 'DARKBROWN', 'DARKCHOCOLATE']):
    sprites.make_group('cocobengalcolours', (a, 2), f'bengal{i}')
for a, i in enumerate(['PALEBROWN', 'LIGHTCINNAMON', 'BRONZE', 'CINNAMON', 'TAWNY', 'DARKCINNAMON']):
    sprites.make_group('cocobengalcolours', (a, 3), f'bengal{i}')
for a, i in enumerate(['PALECREAM', 'BUFF', 'CREAM', 'YELLOW', 'BLOND', 'OCHRE']):
    sprites.make_group('cocobengalcolours', (a, 4), f'bengal{i}')
for a, i in enumerate(['PALEGRAY', 'GRAY', 'MALTESE', 'BLUE', 'SLATE', 'DARKGRAY']):
    sprites.make_group('cocobengalcolours', (a, 5), f'bengal{i}')
for a, i in enumerate(['PALELILAC', 'LAVENDER', 'LILAC', 'FROST', 'DOVE', 'DARKLILAC']):
    sprites.make_group('cocobengalcolours', (a, 6), f'bengal{i}')
for a, i in enumerate(['PALLID', 'PALEFAWN', 'DUN', 'DUSTY', 'FAWN', 'DARKFAWN']):
    sprites.make_group('cocobengalcolours', (a, 7), f'bengal{i}')
for a, i in enumerate(['PALEAPRICOT', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cocobengalcolours', (a, 8), f'bengal{i}')
for a, i in enumerate(['ASHEN', 'LIGHTCARAMEL', 'KHAKI', 'SHALE', 'CARAMEL', 'DARKCARAMEL']):
    sprites.make_group('cocobengalcolours', (a, 9), f'bengal{i}')
for a, i in enumerate(['GHOSTTAUPE', 'PALETAUPE', 'LIGHTTAUPE', 'TUFF', 'TAUPE', 'DUSKY']):
    sprites.make_group('cocobengalcolours', (a, 10), f'bengal{i}')
for a, i in enumerate(['PINK', 'BEIGE', 'TAN', 'FALLOW', 'DIJON', 'OLIVE']):
    sprites.make_group('cocobengalcolours', (a, 11), f'bengal{i}')
    
# new new torties
for a, i in enumerate(['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH']):
    sprites.make_group('tortiepatchesmasks', (a, 0), f"tortiemask{i}")
for a, i in enumerate(['MINIMAL1', 'MINIMAL2', 'MINIMAL3', 'MINIMAL4', 'OREO', 'SWOOP']):
    sprites.make_group('tortiepatchesmasks', (a, 1), f"tortiemask{i}")
for a, i in enumerate(['MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE']):
    sprites.make_group('tortiepatchesmasks', (a, 2), f"tortiemask{i}")
for a, i in enumerate(['ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE']):
    sprites.make_group('tortiepatchesmasks', (a, 3), f"tortiemask{i}")

# SKINS
for a, i in enumerate(['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN']):
    sprites.make_group('skin', (a, 0), f"skin{i}")
for a, i in enumerate(['DARK', 'DARKGREY', 'GREY', 'DARKSALMON', 'SALMON', 'PEACH']):
    sprites.make_group('skin', (a, 1), f"skin{i}")
for a, i in enumerate(['DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']):
    sprites.make_group('skin', (a, 2), f"skin{i}")

sprites.load_scars()
