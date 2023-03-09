import pygame

try:
    import ujson
except ImportError:
    import json as ujson


class Sprites():
    cat_tints = {}

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
                   sprites_y=3):  # pos = ex. (2, 3), no single pixels
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
        scars = 'scars'

        for a, i in enumerate(
                ["ONE", "TWO", "THREE", "LEFTEAR", "RIGHTEAR", "NOTAIL"]):
            sprites.make_group('scars', (a, 0), f'scars{i}')
            sprites.make_group('scarsextra', (a, 0),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["MANLEG", "BRIGHTHEART", "MANTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]):
            sprites.make_group('scars', (a, 1), f'scars{i}')
            sprites.make_group('scarsextra', (a, 1),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["BRIDGE", "RIGHTBLIND", "LEFTBLIND", "BOTHBLIND", "BURNPAWS", "BURNTAIL"]):
            sprites.make_group('scars', (a, 2), f'scars{i}')
            sprites.make_group('scarsextra', (a, 2),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE"]):
            sprites.make_group('scars', (a, 3), f'scars{i}')
            sprites.make_group('scarsextra', (a, 3),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE"]):
            sprites.make_group('Newscars', (a, 0), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 0),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["BELLY", "TOETRAP", "SNAKE"]):
            sprites.make_group('Newscars', (a, 1), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 1),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["LEGBITE", "NECKBITE", "FACE", "HALFTAIL", "NOPAW"]):
            sprites.make_group('Newscars', (a, 2), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 2),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"]):
            sprites.make_group('Newscars', (a, 3), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 3),
                               f'scarsextra{i}',
                               sprites_y=2)

            # Accessories
        for a, i in enumerate([
            "MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"]):
            sprites.make_group('medcatherbs', (a, 0), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 0), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"]):
            sprites.make_group('medcatherbs', (a, 1), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 1), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]):
            sprites.make_group('medcatherbs', (a, 3), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 3), f'acc_herbsextra{i}', sprites_y=2)
        sprites.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')
        sprites.make_group('medcatherbsextra', (5, 2), 'acc_herbsextraDRY HERBS', sprites_y=2)

        for a, i in enumerate([
            "RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]):
            sprites.make_group('medcatherbs', (a, 2), f'acc_wild{i}')
            sprites.make_group('medcatherbsextra', (a, 2), f'acc_wildextra{i}', sprites_y=2)
        for a, i in enumerate(["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"]):
            sprites.make_group('collars', (a, 0), f'collars{i}')
            sprites.make_group('collarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREEN", "RAINBOW", "BLACK", "SPIKES", "WHITE"]):
            sprites.make_group('collars', (a, 1), f'collars{i}')
            sprites.make_group('collarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINK", "PURPLE", "MULTI", "INDIGO"]):
            sprites.make_group('collars', (a, 2), f'collars{i}')
            sprites.make_group('collarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
            "CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL",
            "LIMEBELL"
        ]):
            sprites.make_group('bellcollars', (a, 0), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
                ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL"]):
            sprites.make_group('bellcollars', (a, 1), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBELL", "PURPLEBELL", "MULTIBELL", "INDIGOBELL"]):
            sprites.make_group('bellcollars', (a, 2), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
            "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
            "LIMEBOW"
        ]):
            sprites.make_group('bowcollars', (a, 0), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
                ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW"]):
            sprites.make_group('bowcollars', (a, 1), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"]):
            sprites.make_group('bowcollars', (a, 2), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
            "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON",
            "LIMENYLON"
        ]):
            sprites.make_group('nyloncollars', (a, 0), f'collars{i}')
            sprites.make_group('nyloncollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
                ["GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON"]):
            sprites.make_group('nyloncollars', (a, 1), f'collars{i}')
            sprites.make_group('nyloncollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON"]):
            sprites.make_group('nyloncollars', (a, 2), f'collars{i}')
            sprites.make_group('nyloncollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)


sprites = Sprites(50)
#tiles = Sprites(64)

for x in [
    'lineart', 'lineartdead', 'lineartdf',
    'fadestarclan', 'fadedarkforest', 'fademask',
    'shadersnewwhite', 'lightingnew',
    'whitepatches', 'whiteextra', 'whitepatchesnew', 'whitenewextra',
    'whitepatches3', 'whitepatches3extra', 'whitepatches4', 'whitepatches4extra',
    'eyes', 'eyesextra', 'eyes2', 'eyes2extra', 'eyes_df', 'eyesextra_df',
    'skin', 'skinextra',
    'scars', 'scarsextra', 'scarsdark', 'scarsdarkextra', 'Newscars', 'Newscarsextra',
    'medcatherbs', 'medcatherbsextra',
    'collars', 'collarsextra', 'bowcollars', 'bowcollarsextra',
    'bellcollars', 'bellcollarsextra', 'nyloncollars', 'nyloncollarsextra',
    'cocosolidcolours', 'cocodilutecolours', 'cococaramelcolours',
    'cocosolidextra', 'cocodiluteextra', 'cococaramelextra',
    'cocomackerelcolours', 'cocodilutemackerelcolours', 'cococaramelmackerelcolours',
    'cocomackerelextra', 'cocodilutemackerelextra', 'cococaramelmackerelextra',
    'cococlassiccolours', 'cocodiluteclassiccolours', 'cococaramelclassiccolours',
    'cococlassicextra', 'cocodiluteclassicextra', 'cococaramelclassicextra',
    'cocospottedcolours', 'cocodilutespottedcolours', 'cococaramelspottedcolours',
    'cocospottedextra', 'cocodilutespottedextra', 'cococaramelspottedextra',
    'cocotickedcolours', 'cocodilutetickedcolours', 'cococarameltickedcolours',
    'cocotickedextra', 'cocodilutetickedextra', 'cococarameltickedextra',
    'cocoagouticolours', 'cocodiluteagouticolours', 'cococaramelagouticolours',
    'cocoagoutiextra', 'cocodiluteagoutiextra', 'cococaramelagoutiextra',
    'cocomarbledcolours','cocodilutemarbledcolours','cococaramelmarbledcolours',
    'cocomarbledextra','cocodilutemarbledextra','cococaramelmarbledextra',
    'cocorosettedcolours', 'cocodiluterosettedcolours', 'cococaramelrosettedcolours',
    'cocorosettedextra', 'cocodiluterosettedextra', 'cococaramelrosettedextra',
    'tortiecolourssolid', 'tortiesextrasolid', 'tortiecoloursmackerel', 'tortiesextramackerel',
    'tortiecoloursclassic', 'tortiesextraclassic', 'tortiecoloursspotted', 'tortiesextraspotted',
    'tortiecoloursticked', 'tortiesextraticked', 'tortiecoloursagouti', 'tortiesextraagouti',
    'tortiecoloursmarbled', 'tortiesextramarbled', 'tortiecoloursrosetted', 'tortiesextrarosetted'

]:
    sprites.spritesheet(f"sprites/{x}.png", x)

for sprite in [
    'Paralyzed_lineart', 'singleparalyzed', 'speckledparalyzed',
    'tabbyparalyzed', 'whiteallparalyzed', 'eyesparalyzed',
    'tabbyparalyzed', 'tortiesparalyzed', 'scarsparalyzed', 'skinparalyzed',
    'medcatherbsparalyzed'

]:
    sprites.spritesheet(f"sprites/paralyzed/{sprite}.png", sprite)

# for x in ['dithered']:
#     tiles.spritesheet(f"sprites/{x}.png", x)

# Line art
sprites.make_group('lineart', (0, 0), 'lines', sprites_y=5)
sprites.make_group('Paralyzed_lineart', (0, 0),
                   'p_lines',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('shadersnewwhite', (0, 0), 'shaders', sprites_y=5)
sprites.make_group('lightingnew', (0, 0), 'lighting', sprites_y=5)

sprites.make_group('lineartdead', (0, 0), 'lineartdead', sprites_y=5)
sprites.make_group('lineartdf', (0, 0), 'lineartdf', sprites_y=5)

# Fading Fog
sprites.make_group('fademask', (0, 0), 'fademask', sprites_y=15)
sprites.make_group('fadestarclan', (0, 0), 'fadestarclan', sprites_y=15)
sprites.make_group('fadedarkforest', (0, 0), 'fadedf', sprites_y=15)

for a, i in enumerate(
        ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE']):
    sprites.make_group('eyes', (a, 0), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 0), f'eyesextra{i}', sprites_y=2)
    sprites.make_group('eyes2', (a, 0), f'eyes2{i}')
    sprites.make_group('eyes2extra', (a, 0), f'eyes2extra{i}', sprites_y=2)
for a, i in enumerate(
        ['DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHERBLUE', 'SUNLITICE']):
    sprites.make_group('eyes', (a, 1), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 1), f'eyesextra{i}', sprites_y=2)
    sprites.make_group('eyes2', (a, 1), f'eyes2{i}')
    sprites.make_group('eyes2extra', (a, 1), f'eyes2extra{i}', sprites_y=2)
for a, i in enumerate(
        ['COPPER', 'SAGE', 'BLUE2', 'PALEBLUE', 'BLUEYELLOW', 'BLUEGREEN']):
    sprites.make_group('eyes', (a, 2), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 2), f'eyesextra{i}', sprites_y=2)
    sprites.make_group('eyes2', (a, 2), f'eyes2{i}')
    sprites.make_group('eyes2extra', (a, 2), f'eyes2extra{i}', sprites_y=2)
for a, i in enumerate(
        ['PALEYELLOW', 'GOLD', 'GREENYELLOW']):
    sprites.make_group('eyes', (a, 3), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 3), f'eyesextra{i}', sprites_y=2)
    sprites.make_group('eyes2', (a, 3), f'eyes2{i}')
    sprites.make_group('eyes2extra', (a, 3), f'eyes2extra{i}', sprites_y=2)

# white patches
for a, i in enumerate(['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANY2']):
    sprites.make_group('whitepatches', (a, 0), f'white{i}')
    sprites.make_group('whiteextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([
    'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
    'LIGHTSONG', 'VITILIGO'
]):
    sprites.make_group('whitepatchesnew', (a, 0), f'white{i}')
    sprites.make_group('whitenewextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([
    'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY', 'COLOURPOINTCREAMY',
    'VANCREAMY', 'ANY2CREAMY'
]):
    sprites.make_group('whitepatches', (a, 1), f'white{i}')
    sprites.make_group('whiteextra', (a, 1), f'whiteextra{i}', sprites_y=2)
# extra
sprites.make_group('whitepatches', (0, 2), 'whiteEXTRA')
sprites.make_group('whiteextra', (0, 2), 'whiteextraEXTRA', sprites_y=2)

# ryos white patches
for a, i in enumerate(
        ['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'VITILIGO2']):
    sprites.make_group('whitepatches3', (a, 0), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'PAWS', 'MITAINE']):
    sprites.make_group('whitepatches3', (a, 1), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 1), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'SCOURGE']):
    sprites.make_group('whitepatches3', (a, 2), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 2), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW', 'HONEY']):
    sprites.make_group('whitepatches3', (a, 3), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 3), f'whiteextra{i}', sprites_y=2)

# beejeans white patches + perrio's point marks, painted, and heart2 + anju's new marks + key's blackstar
for a, i in enumerate(['PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED']):
    sprites.make_group('whitepatches4', (a, 0), 'white' + i)
    sprites.make_group('whitepatches4extra', (a, 0), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']):
    sprites.make_group('whitepatches4', (a, 1), 'white' + i)
    sprites.make_group('whitepatches4extra', (a, 1), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['MAO', 'LUNA', 'CHESTSPECK', 'WINGS', 'PAINTED', 'HEART2', 'BLACKSTAR']):
    sprites.make_group('whitepatches4', (a, 2), 'white' + i)
    sprites.make_group('whitepatches4extra', (a, 2), 'whiteextra' + i, sprites_y=2)

# solid
for a, i in enumerate(['EBONY', 'COAL', 'SHADOW', 'CROW', 'RAVEN', 'BLACK']):
    sprites.make_group('cocosolidcolours', (a, 0), f'solid{i}')
    sprites.make_group('cocosolidextra', (a, 0), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['TWIG', 'CHESTNUT', 'COCOA', 'CHOCOLATE', 'UMBER', 'DARKCHOCOLATE']):
    sprites.make_group('cocosolidcolours', (a, 1), f'solid{i}')
    sprites.make_group('cocosolidextra', (a, 1), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['OAK', 'CEDAR', 'AUTUMN', 'RUST', 'CINNAMON', 'PINE']):
    sprites.make_group('cocosolidcolours', (a, 2), f'solid{i}')
    sprites.make_group('cocosolidextra', (a, 2), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['HONEY', 'MARIGOLD', 'EMBER', 'ORANGE', 'GINGER', 'RED']):
    sprites.make_group('cocosolidcolours', (a, 2), f'solid{i}')
    sprites.make_group('cocosolidextra', (a, 2), f'solidextra{i}', sprites_y=2)
# dilute
for a, i in enumerate(['RAIN', 'MIST', 'GRAY', 'BLUE', 'SLATE', 'STORM']):
    sprites.make_group('cocodilutecolours', (a, 0), f'solid{i}')
    sprites.make_group('cocodiluteextra', (a, 0), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUST', 'MOUSE']):
    sprites.make_group('cocodilutecolours', (a, 1), f'solid{i}')
    sprites.make_group('cocodiluteextra', (a, 1), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['PINK', 'SHREW', 'STAG', 'DOE', 'FAWN', 'SAND']):
    sprites.make_group('cocodilutecolours', (a, 2), f'solid{i}')
    sprites.make_group('cocodiluteextra', (a, 2), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['BUFF', 'CREAM', 'DAISY', 'SUN', 'TAN', 'OCHRE']):
    sprites.make_group('cocodilutecolours', (a, 2), f'solid{i}')
    sprites.make_group('cocodiluteextra', (a, 2), f'solidextra{i}', sprites_y=2)
# caramel
for a, i in enumerate(['ASH', 'BIRCH', 'PIGEON', 'WORM', 'CARAMEL', 'GRAVEL']):
    sprites.make_group('cococaramelcolours', (a, 0), f'solid{i}')
    sprites.make_group('cococaramelextra', (a, 0), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['BONE', 'WHEAT', 'DAWN', 'SPARROW', 'TAUPE', 'DUSK']):
    sprites.make_group('cococaramelcolours', (a, 1), f'solid{i}')
    sprites.make_group('cococaramelextra', (a, 1), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['PEARL', 'BEIGE', 'OAT', 'ASPEN', 'TAWNY', 'OLIVE']):
    sprites.make_group('cococaramelcolours', (a, 2), f'solid{i}')
    sprites.make_group('cococaramelextra', (a, 2), f'solidextra{i}', sprites_y=2)
for a, i in enumerate(['SHELL', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococaramelcolours', (a, 2), f'solid{i}')
    sprites.make_group('cococaramelextra', (a, 2), f'solidextra{i}', sprites_y=2)
# mackerel
for a, i in enumerate(['EBONY', 'COAL', 'SHADOW', 'CROW', 'RAVEN', 'BLACK']):
    sprites.make_group('cocomackerelcolours', (a, 0), f'mackerel{i}')
    sprites.make_group('cocomackerelextra', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['TWIG', 'CHESTNUT', 'COCOA', 'CHOCOLATE', 'UMBER', 'DARKCHOCOLATE']):
    sprites.make_group('cocomackerelcolours', (a, 1), f'mackerel{i}')
    sprites.make_group('cocomackerelextra', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['OAK', 'CEDAR', 'AUTUMN', 'RUST', 'CINNAMON', 'PINE']):
    sprites.make_group('cocomackerelcolours', (a, 2), f'mackerel{i}')
    sprites.make_group('cocomackerelextra', (a, 2), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['HONEY', 'MARIGOLD', 'EMBER', 'ORANGE', 'GINGER', 'RED']):
    sprites.make_group('cocomackerelcolours', (a, 2), f'mackerel{i}')
    sprites.make_group('cocomackerelextra', (a, 2), f'mackerelextra{i}', sprites_y=2)
# dilute mackerel
for a, i in enumerate(['RAIN', 'MIST', 'GRAY', 'BLUE', 'SLATE', 'STORM']):
    sprites.make_group('cocodilutemackerelcolours', (a, 0), f'mackerel{i}')
    sprites.make_group('cocodilutemackerelextra', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUST', 'MOUSE']):
    sprites.make_group('cocodilutemackerelcolours', (a, 1), f'mackerel{i}')
    sprites.make_group('cocodilutemackerelextra', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['PINK', 'SHREW', 'STAG', 'DOE', 'FAWN', 'SAND']):
    sprites.make_group('cocodilutemackerelcolours', (a, 2), f'mackerel{i}')
    sprites.make_group('cocodilutemackerelextra', (a, 2), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['BUFF', 'CREAM', 'DAISY', 'SUN', 'TAN', 'OCHRE']):
    sprites.make_group('cocodilutemackerelcolours', (a, 2), f'mackerel{i}')
    sprites.make_group('cocodilutemackerelextra', (a, 2), f'mackerelextra{i}', sprites_y=2)
# caramel mackerel
for a, i in enumerate(['ASH', 'BIRCH', 'PIGEON', 'WORM', 'CARAMEL', 'GRAVEL']):
    sprites.make_group('cococaramelmackerelcolours', (a, 0), f'mackerel{i}')
    sprites.make_group('cococaramelmackerelextra', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['BONE', 'WHEAT', 'DAWN', 'SPARROW', 'TAUPE', 'DUSK']):
    sprites.make_group('cococaramelmackerelcolours', (a, 1), f'mackerel{i}')
    sprites.make_group('cococaramelmackerelextra', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['PEARL', 'BEIGE', 'OAT', 'ASPEN', 'TAWNY', 'OLIVE']):
    sprites.make_group('cococaramelmackerelcolours', (a, 2), f'mackerel{i}')
    sprites.make_group('cococaramelmackerelextra', (a, 2), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['SHELL', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococaramelmackerelcolours', (a, 2), f'mackerel{i}')
    sprites.make_group('cococaramelmackerelextra', (a, 2), f'mackerelextra{i}', sprites_y=2)
# classic
for a, i in enumerate(['EBONY', 'COAL', 'SHADOW', 'CROW', 'RAVEN', 'BLACK']):
    sprites.make_group('cococlassiccolours', (a, 0), f'classic{i}')
    sprites.make_group('cococlassicextra', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['TWIG', 'CHESTNUT', 'COCOA', 'CHOCOLATE', 'UMBER', 'DARKCHOCOLATE']):
    sprites.make_group('cococlassiccolours', (a, 1), f'classic{i}')
    sprites.make_group('cococlassicextra', (a, 1), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['OAK', 'CEDAR', 'AUTUMN', 'RUST', 'CINNAMON', 'PINE']):
    sprites.make_group('cococlassiccolours', (a, 2), f'classic{i}')
    sprites.make_group('cococlassicextra', (a, 2), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['HONEY', 'MARIGOLD', 'EMBER', 'ORANGE', 'GINGER', 'RED']):
    sprites.make_group('cococlassiccolours', (a, 2), f'classic{i}')
    sprites.make_group('cococlassicextra', (a, 2), f'classicextra{i}', sprites_y=2)
# dilute classic
for a, i in enumerate(['RAIN', 'MIST', 'GRAY', 'BLUE', 'SLATE', 'STORM']):
    sprites.make_group('cocodiluteclassiccolours', (a, 0), f'classic{i}')
    sprites.make_group('cocodiluteclassicextra', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUST', 'MOUSE']):
    sprites.make_group('cocodiluteclassiccolours', (a, 1), f'classic{i}')
    sprites.make_group('cocodiluteclassicextra', (a, 1), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['PINK', 'SHREW', 'STAG', 'DOE', 'FAWN', 'SAND']):
    sprites.make_group('cocodiluteclassiccolours', (a, 2), f'classic{i}')
    sprites.make_group('cocodiluteclassicextra', (a, 2), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['BUFF', 'CREAM', 'DAISY', 'SUN', 'TAN', 'OCHRE']):
    sprites.make_group('cocodiluteclassiccolours', (a, 2), f'classic{i}')
    sprites.make_group('cocodiluteclassicextra', (a, 2), f'classicextra{i}', sprites_y=2)
# caramel classic
for a, i in enumerate(['ASH', 'BIRCH', 'PIGEON', 'WORM', 'CARAMEL', 'GRAVEL']):
    sprites.make_group('cococaramelclassiccolours', (a, 0), f'classic{i}')
    sprites.make_group('cococaramelclassicextra', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['BONE', 'WHEAT', 'DAWN', 'SPARROW', 'TAUPE', 'DUSK']):
    sprites.make_group('cococaramelclassiccolours', (a, 1), f'classic{i}')
    sprites.make_group('cococaramelclassicextra', (a, 1), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['PEARL', 'BEIGE', 'OAT', 'ASPEN', 'TAWNY', 'OLIVE']):
    sprites.make_group('cococaramelclassiccolours', (a, 2), f'classic{i}')
    sprites.make_group('cococaramelclassicextra', (a, 2), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['SHELL', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococaramelclassiccolours', (a, 2), f'classic{i}')
    sprites.make_group('cococaramelclassicextra', (a, 2), f'classicextra{i}', sprites_y=2)
# spotted
for a, i in enumerate(['EBONY', 'COAL', 'SHADOW', 'CROW', 'RAVEN', 'BLACK']):
    sprites.make_group('cocospottedcolours', (a, 0), f'spotted{i}')
    sprites.make_group('cocospottedextra', (a, 0), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['TWIG', 'CHESTNUT', 'COCOA', 'CHOCOLATE', 'UMBER', 'DARKCHOCOLATE']):
    sprites.make_group('cocospottedcolours', (a, 1), f'spotted{i}')
    sprites.make_group('cocospottedextra', (a, 1), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['OAK', 'CEDAR', 'AUTUMN', 'RUST', 'CINNAMON', 'PINE']):
    sprites.make_group('cocospottedcolours', (a, 2), f'spotted{i}')
    sprites.make_group('cocospottedextra', (a, 2), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['HONEY', 'MARIGOLD', 'EMBER', 'ORANGE', 'GINGER', 'RED']):
    sprites.make_group('cocospottedcolours', (a, 2), f'spotted{i}')
    sprites.make_group('cocospottedextra', (a, 2), f'spottedextra{i}', sprites_y=2)
# dilute spotted
for a, i in enumerate(['RAIN', 'MIST', 'GRAY', 'BLUE', 'SLATE', 'STORM']):
    sprites.make_group('cocodilutespottedcolours', (a, 0), f'spotted{i}')
    sprites.make_group('cocodilutespottedextra', (a, 0), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUST', 'MOUSE']):
    sprites.make_group('cocodilutespottedcolours', (a, 1), f'spotted{i}')
    sprites.make_group('cocodilutespottedextra', (a, 1), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['PINK', 'SHREW', 'STAG', 'DOE', 'FAWN', 'SAND']):
    sprites.make_group('cocodilutespottedcolours', (a, 2), f'spotted{i}')
    sprites.make_group('cocodilutespottedextra', (a, 2), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['BUFF', 'CREAM', 'DAISY', 'SUN', 'TAN', 'OCHRE']):
    sprites.make_group('cocodilutespottedcolours', (a, 2), f'spotted{i}')
    sprites.make_group('cocodilutespottedextra', (a, 2), f'spottedextra{i}', sprites_y=2)
# caramel spotted
for a, i in enumerate(['ASH', 'BIRCH', 'PIGEON', 'WORM', 'CARAMEL', 'GRAVEL']):
    sprites.make_group('cococaramelspottedcolours', (a, 0), f'spotted{i}')
    sprites.make_group('cococaramelspottedextra', (a, 0), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['BONE', 'WHEAT', 'DAWN', 'SPARROW', 'TAUPE', 'DUSK']):
    sprites.make_group('cococaramelspottedcolours', (a, 1), f'spotted{i}')
    sprites.make_group('cococaramelspottedextra', (a, 1), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['PEARL', 'BEIGE', 'OAT', 'ASPEN', 'TAWNY', 'OLIVE']):
    sprites.make_group('cococaramelspottedcolours', (a, 2), f'spotted{i}')
    sprites.make_group('cococaramelspottedextra', (a, 2), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['SHELL', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococaramelspottedcolours', (a, 2), f'spotted{i}')
    sprites.make_group('cococaramelspottedextra', (a, 2), f'spottedextra{i}', sprites_y=2)
# ticked
for a, i in enumerate(['EBONY', 'COAL', 'SHADOW', 'CROW', 'RAVEN', 'BLACK']):
    sprites.make_group('cocotickedcolours', (a, 0), f'ticked{i}')
    sprites.make_group('cocotickedextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['TWIG', 'CHESTNUT', 'COCOA', 'CHOCOLATE', 'UMBER', 'DARKCHOCOLATE']):
    sprites.make_group('cocotickedcolours', (a, 1), f'ticked{i}')
    sprites.make_group('cocotickedextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['OAK', 'CEDAR', 'AUTUMN', 'RUST', 'CINNAMON', 'PINE']):
    sprites.make_group('cocotickedcolours', (a, 2), f'ticked{i}')
    sprites.make_group('cocotickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['HONEY', 'MARIGOLD', 'EMBER', 'ORANGE', 'GINGER', 'RED']):
    sprites.make_group('cocotickedcolours', (a, 2), f'ticked{i}')
    sprites.make_group('cocotickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
# dilute ticked
for a, i in enumerate(['RAIN', 'MIST', 'GRAY', 'BLUE', 'SLATE', 'STORM']):
    sprites.make_group('cocodilutetickedcolours', (a, 0), f'ticked{i}')
    sprites.make_group('cocodilutetickedextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUST', 'MOUSE']):
    sprites.make_group('cocodilutetickedcolours', (a, 1), f'ticked{i}')
    sprites.make_group('cocodilutetickedextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['PINK', 'SHREW', 'STAG', 'DOE', 'FAWN', 'SAND']):
    sprites.make_group('cocodilutetickedcolours', (a, 2), f'ticked{i}')
    sprites.make_group('cocodilutetickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['BUFF', 'CREAM', 'DAISY', 'SUN', 'TAN', 'OCHRE']):
    sprites.make_group('cocodilutetickedcolours', (a, 2), f'ticked{i}')
    sprites.make_group('cocodilutetickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
# caramel ticked
for a, i in enumerate(['ASH', 'BIRCH', 'PIGEON', 'WORM', 'CARAMEL', 'GRAVEL']):
    sprites.make_group('cococarameltickedcolours', (a, 0), f'ticked{i}')
    sprites.make_group('cococarameltickedextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['BONE', 'WHEAT', 'DAWN', 'SPARROW', 'TAUPE', 'DUSK']):
    sprites.make_group('cococarameltickedcolours', (a, 1), f'ticked{i}')
    sprites.make_group('cococarameltickedextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['PEARL', 'BEIGE', 'OAT', 'ASPEN', 'TAWNY', 'OLIVE']):
    sprites.make_group('cococarameltickedcolours', (a, 2), f'ticked{i}')
    sprites.make_group('cococarameltickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['SHELL', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococarameltickedcolours', (a, 2), f'ticked{i}')
    sprites.make_group('cococarameltickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
# agouti
for a, i in enumerate(['EBONY', 'COAL', 'SHADOW', 'CROW', 'RAVEN', 'BLACK']):
    sprites.make_group('cocoagouticolours', (a, 0), f'agouti{i}')
    sprites.make_group('cocoagoutiextra', (a, 0), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['TWIG', 'CHESTNUT', 'COCOA', 'CHOCOLATE', 'UMBER', 'DARKCHOCOLATE']):
    sprites.make_group('cocoagouticolours', (a, 1), f'agouti{i}')
    sprites.make_group('cocoagoutiextra', (a, 1), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['OAK', 'CEDAR', 'AUTUMN', 'RUST', 'CINNAMON', 'PINE']):
    sprites.make_group('cocoagouticolours', (a, 2), f'agouti{i}')
    sprites.make_group('cocoagoutiextra', (a, 2), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['HONEY', 'MARIGOLD', 'EMBER', 'ORANGE', 'GINGER', 'RED']):
    sprites.make_group('cocoagouticolours', (a, 2), f'agouti{i}')
    sprites.make_group('cocoagoutiextra', (a, 2), f'agoutiextra{i}', sprites_y=2)
# dilute agouti
for a, i in enumerate(['RAIN', 'MIST', 'GRAY', 'BLUE', 'SLATE', 'STORM']):
    sprites.make_group('cocodiluteagouticolours', (a, 0), f'agouti{i}')
    sprites.make_group('cocodiluteagoutiextra', (a, 0), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUST', 'MOUSE']):
    sprites.make_group('cocodiluteagouticolours', (a, 1), f'agouti{i}')
    sprites.make_group('cocodiluteagoutiextra', (a, 1), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['PINK', 'SHREW', 'STAG', 'DOE', 'FAWN', 'SAND']):
    sprites.make_group('cocodiluteagouticolours', (a, 2), f'agouti{i}')
    sprites.make_group('cocodiluteagoutiextra', (a, 2), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['BUFF', 'CREAM', 'DAISY', 'SUN', 'TAN', 'OCHRE']):
    sprites.make_group('cocodiluteagouticolours', (a, 2), f'agouti{i}')
    sprites.make_group('cocodiluteagoutiextra', (a, 2), f'agoutiextra{i}', sprites_y=2)
# caramel agouti
for a, i in enumerate(['ASH', 'BIRCH', 'PIGEON', 'WORM', 'CARAMEL', 'GRAVEL']):
    sprites.make_group('cococaramelagouticolours', (a, 0), f'agouti{i}')
    sprites.make_group('cococaramelagoutiextra', (a, 0), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['BONE', 'WHEAT', 'DAWN', 'SPARROW', 'TAUPE', 'DUSK']):
    sprites.make_group('cococaramelagouticolours', (a, 1), f'agouti{i}')
    sprites.make_group('cococaramelagoutiextra', (a, 1), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['PEARL', 'BEIGE', 'OAT', 'ASPEN', 'TAWNY', 'OLIVE']):
    sprites.make_group('cococaramelagouticolours', (a, 2), f'agouti{i}')
    sprites.make_group('cococaramelagoutiextra', (a, 2), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['SHELL', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococaramelagouticolours', (a, 2), f'agouti{i}')
    sprites.make_group('cococaramelagoutiextra', (a, 2), f'agoutiextra{i}', sprites_y=2)
# solid marbled
for a, i in enumerate(['EBONY', 'COAL', 'SHADOW', 'CROW', 'RAVEN', 'BLACK']):
    sprites.make_group('cocomarbledcolours', (a, 0), f'marbled{i}')
    sprites.make_group('cocomarbledextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['TWIG', 'CHESTNUT', 'COCOA', 'CHOCOLATE', 'UMBER', 'DARKCHOCOLATE']):
    sprites.make_group('cocomarbledcolours', (a, 1), f'marbled{i}')
    sprites.make_group('cocomarbledextra', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['OAK', 'CEDAR', 'AUTUMN', 'RUST', 'CINNAMON', 'PINE']):
    sprites.make_group('cocomarbledcolours', (a, 2), f'marbled{i}')
    sprites.make_group('cocomarbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['HONEY', 'MARIGOLD', 'EMBER', 'ORANGE', 'GINGER', 'RED']):
    sprites.make_group('cocomarbledcolours', (a, 2), f'marbled{i}')
    sprites.make_group('cocomarbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
# dilute marbled
for a, i in enumerate(['RAIN', 'MIST', 'GRAY', 'BLUE', 'SLATE', 'STORM']):
    sprites.make_group('cocodilutemarbledcolours', (a, 0), f'marbled{i}')
    sprites.make_group('cocodilutemarbledextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUST', 'MOUSE']):
    sprites.make_group('cocodilutemarbledcolours', (a, 1), f'marbled{i}')
    sprites.make_group('cocodilutemarbledextra', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['PINK', 'SHREW', 'STAG', 'DOE', 'FAWN', 'SAND']):
    sprites.make_group('cocodilutemarbledcolours', (a, 2), f'marbled{i}')
    sprites.make_group('cocodilutemarbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['BUFF', 'CREAM', 'DAISY', 'SUN', 'TAN', 'OCHRE']):
    sprites.make_group('cocodilutemarbledcolours', (a, 2), f'marbled{i}')
    sprites.make_group('cocodilutemarbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
# caramel marbled
for a, i in enumerate(['ASH', 'BIRCH', 'PIGEON', 'WORM', 'CARAMEL', 'GRAVEL']):
    sprites.make_group('cococaramelmarbledcolours', (a, 0), f'marbled{i}')
    sprites.make_group('cococaramelmarbledextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['BONE', 'WHEAT', 'DAWN', 'SPARROW', 'TAUPE', 'DUSK']):
    sprites.make_group('cococaramelmarbledcolours', (a, 1), f'marbled{i}')
    sprites.make_group('cococaramelmarbledextra', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['PEARL', 'BEIGE', 'OAT', 'ASPEN', 'TAWNY', 'OLIVE']):
    sprites.make_group('cococaramelmarbledcolours', (a, 2), f'marbled{i}')
    sprites.make_group('cococaramelmarbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['SHELL', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococaramelmarbledcolours', (a, 2), f'marbled{i}')
    sprites.make_group('cococaramelmarbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
# solid rosetted
for a, i in enumerate(['EBONY', 'COAL', 'SHADOW', 'CROW', 'RAVEN', 'BLACK']):
    sprites.make_group('cocorosettedcolours', (a, 0), f'rosetted{i}')
    sprites.make_group('cocorosettedextra', (a, 0), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['TWIG', 'CHESTNUT', 'COCOA', 'CHOCOLATE', 'UMBER', 'DARKCHOCOLATE']):
    sprites.make_group('cocorosettedcolours', (a, 1), f'rosetted{i}')
    sprites.make_group('cocorosettedextra', (a, 1), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['OAK', 'CEDAR', 'AUTUMN', 'RUST', 'CINNAMON', 'PINE']):
    sprites.make_group('cocorosettedcolours', (a, 2), f'rosetted{i}')
    sprites.make_group('cocorosettedextra', (a, 2), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['HONEY', 'MARIGOLD', 'EMBER', 'ORANGE', 'GINGER', 'RED']):
    sprites.make_group('cocorosettedcolours', (a, 2), f'rosetted{i}')
    sprites.make_group('cocorosettedextra', (a, 2), f'rosettedextra{i}', sprites_y=2)
# dilute rosetted
for a, i in enumerate(['RAIN', 'MIST', 'GRAY', 'BLUE', 'SLATE', 'STORM']):
    sprites.make_group('cocodiluterosettedcolours', (a, 0), f'rosetted{i}')
    sprites.make_group('cocodiluterosettedextra', (a, 0), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['HEATHER', 'ROSE', 'LILAC', 'LAVENDER', 'DUST', 'MOUSE']):
    sprites.make_group('cocodiluterosettedcolours', (a, 1), f'rosetted{i}')
    sprites.make_group('cocodiluterosettedextra', (a, 1), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['PINK', 'SHREW', 'STAG', 'DOE', 'FAWN', 'SAND']):
    sprites.make_group('cocodiluterosettedcolours', (a, 2), f'rosetted{i}')
    sprites.make_group('cocodiluterosettedextra', (a, 2), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['BUFF', 'CREAM', 'DAISY', 'SUN', 'TAN', 'OCHRE']):
    sprites.make_group('cocodiluterosettedcolours', (a, 2), f'rosetted{i}')
    sprites.make_group('cocodiluterosettedextra', (a, 2), f'rosettedextra{i}', sprites_y=2)
# caramel rosetted
for a, i in enumerate(['ASH', 'BIRCH', 'PIGEON', 'WORM', 'CARAMEL', 'GRAVEL']):
    sprites.make_group('cococaramelrosettedcolours', (a, 0), f'rosetted{i}')
    sprites.make_group('cococaramelrosettedextra', (a, 0), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['BONE', 'WHEAT', 'DAWN', 'SPARROW', 'TAUPE', 'DUSK']):
    sprites.make_group('cococaramelrosettedcolours', (a, 1), f'rosetted{i}')
    sprites.make_group('cococaramelrosettedextra', (a, 1), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['PEARL', 'BEIGE', 'OAT', 'ASPEN', 'TAWNY', 'OLIVE']):
    sprites.make_group('cococaramelrosettedcolours', (a, 2), f'rosetted{i}')
    sprites.make_group('cococaramelrosettedextra', (a, 2), f'rosettedextra{i}', sprites_y=2)
for a, i in enumerate(['SHELL', 'PEACH', 'SALMON', 'APRICOT', 'CORAL', 'FLAME']):
    sprites.make_group('cococaramelrosettedcolours', (a, 2), f'rosetted{i}')
    sprites.make_group('cococaramelrosettedextra', (a, 2), f'rosettedextra{i}', sprites_y=2)
# new torties
# solids
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 0), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 0), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 1), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 1), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 2), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 2), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 3), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 3), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 4), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 4), f'tortiesolidextra{i}', sprites_y=2)
# mackerel
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 0), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 0), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 1), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 1), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 2), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 2), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 3), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 3), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 4), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 4), f'tortiemackerelextra{i}', sprites_y=2)
# classic
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 0), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 0), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 1), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 1), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 2), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 2), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 3), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 3), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 4), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 4), f'tortieclassicextra{i}', sprites_y=2)
# spotted
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursspotted', (a, 0), f'tortiespotted{i}')
    sprites.make_group('tortiesextraspotted', (a, 0), f'tortiespottedextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursspotted', (a, 1), f'tortiespotted{i}')
    sprites.make_group('tortiesextraspotted', (a, 1), f'tortiespottedextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursspotted', (a, 2), f'tortiespotted{i}')
    sprites.make_group('tortiesextraspotted', (a, 2), f'tortiespottedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursspotted', (a, 3), f'tortiespotted{i}')
    sprites.make_group('tortiesextraspotted', (a, 3), f'tortiespottedextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursspotted', (a, 4), f'tortiespotted{i}')
    sprites.make_group('tortiesextraspotted', (a, 4), f'tortiespottedextra{i}', sprites_y=2)
# ticked
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 0), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 0), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 1), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 1), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 2), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 2), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 3), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 3), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 4), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 4), f'tortietickedextra{i}', sprites_y=2)
# agouti
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 0), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 0), f'tortieagoutiextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 1), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 1), f'tortieagoutiextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 2), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 2), f'tortieagoutiextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 3), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 3), f'tortieagoutiextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 4), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 4), f'tortieagoutiextra{i}', sprites_y=2)
# marbled
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 0), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 0), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 1), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 1), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 2), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 2), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 3), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 3), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 4), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 4), f'tortiemarbledextra{i}', sprites_y=2)
# rosetted
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursrosetted', (a, 0), f'tortierosetted{i}')
    sprites.make_group('tortiesextrarosetted', (a, 0), f'tortierosettedextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursrosetted', (a, 1), f'tortierosetted{i}')
    sprites.make_group('tortiesextrarosetted', (a, 1), f'tortierosettedextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursrosetted', (a, 2), f'tortierosetted{i}')
    sprites.make_group('tortiesextrarosetted', (a, 2), f'tortierosettedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursrosetted', (a, 3), f'tortierosetted{i}')
    sprites.make_group('tortiesextrarosetted', (a, 3), f'tortierosettedextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursrosetted', (a, 4), f'tortierosetted{i}')
    sprites.make_group('tortiesextrarosetted', (a, 4), f'tortierosettedextra{i}', sprites_y=2)

# SKINS
sprites.make_group('skin', (0, 0), 'skinBLACK')
sprites.make_group('skin', (1, 0), 'skinRED')
sprites.make_group('skin', (2, 0), 'skinPINK')
sprites.make_group('skin', (3, 0), 'skinDARKBROWN')
sprites.make_group('skin', (4, 0), 'skinBROWN')
sprites.make_group('skin', (5, 0), 'skinLIGHTBROWN')
sprites.make_group('skin', (0, 1), 'skinDARK')
sprites.make_group('skin', (1, 1), 'skinDARKGREY')
sprites.make_group('skin', (2, 1), 'skinGREY')
sprites.make_group('skin', (3, 1), 'skinDARKSALMON')
sprites.make_group('skin', (4, 1), 'skinSALMON')
sprites.make_group('skin', (5, 1), 'skinPEACH')
sprites.make_group('skin', (0, 2), 'skinDARKMARBLED')
sprites.make_group('skin', (1, 2), 'skinMARBLED')
sprites.make_group('skin', (2, 2), 'skinLIGHTMARBLED')
sprites.make_group('skin', (3, 2), 'skinDARKBLUE')
sprites.make_group('skin', (4, 2), 'skinBLUE')
sprites.make_group('skin', (5, 2), 'skinLIGHTBLUE')
sprites.make_group('skinparalyzed', (0, 0),
                   'skinparalyzedPINK',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('skinparalyzed', (1, 0),
                   'skinparalyzedRED',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('skinparalyzed', (2, 0),
                   'skinparalyzedBLACK',
                   sprites_x=1,
                   sprites_y=1)

sprites.make_group('skinextra', (0, 0), 'skinextraBLACK', sprites_y=2)
sprites.make_group('skinextra', (1, 0), 'skinextraRED', sprites_y=2)
sprites.make_group('skinextra', (2, 0), 'skinextraPINK', sprites_y=2)
sprites.make_group('skinextra', (3, 0), 'skinextraDARKBROWN', sprites_y=2)
sprites.make_group('skinextra', (4, 0), 'skinextraBROWN', sprites_y=2)
sprites.make_group('skinextra', (5, 0), 'skinextraLIGHTBROWN', sprites_y=2)
sprites.make_group('skinextra', (0, 1), 'skinextraDARK', sprites_y=2)
sprites.make_group('skinextra', (1, 1), 'skinextraDARKGREY', sprites_y=2)
sprites.make_group('skinextra', (2, 1), 'skinextraGREY', sprites_y=2)
sprites.make_group('skinextra', (3, 1), 'skinextraDARKSALMON', sprites_y=2)
sprites.make_group('skinextra', (4, 1), 'skinextraSALMON', sprites_y=2)
sprites.make_group('skinextra', (5, 1), 'skinextraPEACH', sprites_y=2)
sprites.make_group('skinextra', (0, 2), 'skinextraDARKMARBLED', sprites_y=2)
sprites.make_group('skinextra', (1, 2), 'skinextraMARBLED', sprites_y=2)
sprites.make_group('skinextra', (2, 2), 'skinextraLIGHTMARBLED', sprites_y=2)
sprites.make_group('skinextra', (3, 2), 'skinextraDARKBLUE', sprites_y=2)
sprites.make_group('skinextra', (4, 2), 'skinextraBLUE', sprites_y=2)
sprites.make_group('skinextra', (5, 2), 'skinextraLIGHTBLUE', sprites_y=2)

# tiles.make_group('dithered', (0, 0), 'terrain')
# tiles.make_group('dithered', (1, 0), 'terraintwo')

sprites.load_scars()
