import random
import os


class Name():
    special_suffixes = {
        "kitten": "kit",
        "apprentice": "paw",
        "medicine cat apprentice": "paw",
        "mediator apprentice": "paw",
        "leader": "star"
    }
    normal_suffixes = [  # common suffixes
        "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur",
        'pelt', "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt",
        "claw", "claw", "claw", "claw", "claw", "claw", "claw", "claw", "claw", "claw",
        "whisker", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker",
        "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", 'heart',

        # regular suffixes
        None
    ]

    pelt_suffixes = {
        'TwoColour': ['patch', 'spot', 'splash', 'patch', 'spots'],
        'Mackerel': ['stripe', 'feather', 'leaf', 'stripe', 'fern'],
        'Classic': ['stripe', 'feather', 'leaf', 'stripe', 'fern'],
        'Spotted': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'Ticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'Agouti': ['back', 'pelt', 'fur'],
        'Marbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Rosetted': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'Tortie': ['dapple', 'speckle', 'spot', 'dapple'],
        'Calico': ['stripe', 'dapple', 'patch', 'patch']
    }

    tortie_pelt_suffixes = {
        'tortiesolid': ['dapple', 'speckle', 'spots', 'splash'],
        'tortiemackerel': ['stripe', 'feather', 'fern', 'shade'],
        'tortieclassic': ['stripe', 'feather', 'fern'],
        'tortiespotted': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'tortieticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'tortieagouti': ['back', 'pelt', 'fur', 'dapple', 'splash'],
        'tortiemarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortierosetted': ['dapple', 'speckle', 'spots', 'dapple', 'fern', 'freckle']
    }

    normal_prefixes = [
        None
    ]

    colour_prefixes = {
        'BLACK': [
            'Ant', 'Bat', 'Beetle', 'Black', 'Coal', 'Coot', 'Cormorant', 'Crow', 'Dark', 'Dipper',
            'Ebony', 'Fly', 'Falcon', 'Ivy', 'Juniper', 'Mole', 'Night', 'Privet', 'Rat', 'Raven',
            'Rook', 'Sedge', 'Shade', 'Shadow', 'Sloe', 'Slug', 'Soot', 'Spider', 'Starling', 'Swift'
        ],
        'CHOCOLATE': [
            'Alder', 'Bat', 'Beetle', 'Bramble', 'Briar', 'Brown', 'Buzzard', 'Chestnut', 'Cypress', 'Dark',
            'Deer', 'Dipper', 'Duck', 'Eagle', 'Eel', 'Elm', 'Falcon', 'Frog', 'Goose', 'Ivy',
            'Lamprey', 'Lizard', 'Mink', 'Otter', 'Rat', 'Sedge', 'Spider', 'Twig', 'Umber', 'Weasel'
        ],
        'CINNAMON': [
            'Acorn', 'Argus', 'Autumn','Bat', 'Bramble', 'Briar', 'Brown', 'Cedar', 'Cinnamon', 'Deer',
            'Duck', 'Falcon', 'Grouse', 'Hare', 'Harrier', 'Hazel', 'Kestral', 'Linnet', 'Mouse', 'Moth',
            'Muntjac', 'Oak', 'Owl', 'Pine', 'Rail', 'Rat', 'Rust', 'Sedge', 'Sparrow', 'Whinchat'
        ],
        'GINGER': [
            'Ant', 'Apple', 'Ash', 'Asphodel', 'Brambling', 'Chanterelle', 'Cherry', 'Deer', 'Ember', 'Fire',
            'Fox', 'Fritillary', 'Frog', 'Ginger', 'Honey', 'Kestral', 'Larch', 'Linnet', 'Marigold', 'Moth',
            'Muntjac', 'Orange', 'Pheasant', 'Plum', 'Poppy', 'Red', 'Robin', 'Snail', 'Viper', 'Weevil'
        ],
        'GRAY': [
            'Blue', 'Boulder', 'Burdock', 'Cinder', 'Comfrey', 'Cuckoo', 'Dace', 'Duck', 'Falcon', 'Goose',
            'Gray', 'Harrier', 'Hazel', 'Juniper', 'Mist', 'Moth', 'Partridge', 'Pebble', 'Pigeon', 'Pine',
            'Quail', 'Rain', 'Rock', 'Slate', 'Slug', 'Snake', 'Squirrel', 'Stone', 'Storm', 'Thistle'
        ],
        'LILAC': [
            'Boulder', 'Burnet', 'Campion', 'Cherry', 'Chicory', 'Dust', 'Deer', 'Fritillary', 'Heather', 'Larch',
            'Lark', 'Lavender', 'Lilac', 'Lily', 'Maple', 'Moth', 'Mouse', 'Pebble', 'Poppy', 'Quail',
            'Rock', 'Rose', 'Rush', 'Sorrel', 'Stone', 'Teasel', 'Thistle', 'Thrift', 'Valerian', 'Wisteriae'
        ],
        'FAWN': [
            'Brambling', 'Brown', 'Curlew', 'Deer', 'Doe', 'Dipper', 'Dust', 'Fawn', 'Lark', 'Limpet',
            'Linnet', 'Mosquito', 'Moth', 'Mouse', 'Nightingale', 'Pheasant', 'Pink', 'Rabbit', 'Rat', 'Reed',
            'Sand', 'Sedge', 'Shrew', 'Stag', 'Slug', 'Snail', 'Snake', 'Toad', 'Twite', 'Vole'
        ],
        'CREAM': [
            'Apple', 'Asphodel', 'Bee', 'Buff', 'Carp', 'Chanterelle', 'Comfrey', 'Cream', 'Curlew', 'Daisy',
            'Elder', 'Gecko', 'Hazel', 'Hornet', 'Larch', 'Maple', 'Minnow', 'Moth', 'Ochre', 'Perch',
            'Poppy', 'Privet ', 'Reed', 'Rose', 'Snail', 'Sun', 'Tan', 'Trout', 'Wasp', 'Weevil'
        ],
        'CARAMEL': [
            'Ash', 'Bat', 'Beech', 'Birch', 'Boulder', 'Chub', 'Curlew', 'Cypress', 'Deer', 'Dipper',
            'Duck', 'Elder', 'Elm', 'Frog', 'Goose', 'Gravel', 'Moth', 'Owl', 'Pebble', 'Pigeon',
            'Pine', 'Privet', 'Rat', 'Robin', 'Rock', 'Sedge', 'Sparrow', 'Stone', 'Thistle', 'Worm'
        ],
        'TAUPE': [
            'Argus', 'Bone', 'Boulder', 'Brown', 'Curlew', 'Cypress', 'Dawn', 'Deer', 'Dunock', 'Dusk',
            'Dust', 'Jay', 'Juniper', 'Lark', 'Pebble', 'Pine', 'Quail', 'Rat', 'Rock', 'Sedge',
            'Skipper', 'Sparrow', 'Stone', 'Thistle', 'Thrush', 'Twite', 'Wheat', 'Whimbrel', 'Wren', 'Yew'
        ],
        'FAWNTAUPE': [
            'Aspen', 'Beige', 'Bone', 'Brown', 'Curlew', 'Dawn', 'Deer', 'Dipper', 'Doe', 'Dusk',
            'Dust', 'Fawn', 'Lark', 'Moth', 'Mouse', 'Oat', 'Olive', 'Tawny', 'Pearl', 'Pink',
            'Thistle', 'Twite', 'Sand', 'Sedge', 'Shrew', 'Sparrow', 'Stag', 'Wheat', 'Whinchat'
        ],
        'APRICOT': [
            'Apple', 'Apricot', 'Asphodel', 'Bee', 'Buff', 'Chanterelle', 'Coral', 'Cream', 'Daisy', 'Ember',
            'Fire', 'Flame', 'Ginger', 'Honey', 'Larch', 'Marigold', 'Moth', 'Nightingale', 'Ochre', 'Orange',
            'Peach', 'Poppy', 'Red', 'Salmon', 'Shell', 'Snail', 'Sun', 'Tan', 'Wasp', 'Weevil'
        ]}

    eye_prefixes = {
        None
    }

    loner_names = [
        "Abyss", "Ace", "Adam", "Admiral", "Ah", "Agatha", "Alcina", "Alec", "Alfie", "Alice", "Alonzo", "Amber", "Amelia",
        "Amity", "Amy", "Angel", "Anita", "Anubis", "Armageddon", "Armin", "Apple Cider", "April", "Apu", "Ash", "Archie", "Aurora", "Azula",
        "Aries", "Aquarius", "Baba Yaga", "Bagel", "Bagheera", "Bailey", "Baisel", "Bandit", "Baphomet", "Bastet", "Bean",
        "Beanie Baby", "Beanie", "Beans", "Bebe", "Bede", "Belle", "Ben", "Benny", "Bently", "Bentley", "Beverly",
        "Bibelot", "Big Man", "Bigwig", "Bill Bailey", "Binx", "Birb", "Birdie", "Blinky Stubbins", "Blu",  "Bluebell", "Bologna", "Bolt",
        "Bonbon", "Bongo", "Bonnie", "Bonny", "Boo", "Booker", "Bombalurina", "Brandywine", "Bren", "Broccoli", "Buddy", "Bullwinkle",
        "Bumblebee", "Bunny", "Burger", "Burm", "Bustopher Jones", "Bub", "Cake", "Callie", "Calvin", "Cancer", "Cannelloni", "Capricorn",
        "Caramel", "Cardamom", "Carmen", "Carmin", "Carolina", "Caroline", "Carrie", "Cassandra", "Catie", "Catty", "Catrick",
        "Cayenne", "Cece", "Chance", "Chanel", "Chansey", "Chaos", "Captain", "Charles", "Charlie", "Charlotte", "Charm",
        "Chase", "Chip", "Cheese", "Cheesecake", "Cheeto", "Cheetoman", "Chef", "Cherry", "Chester", "Cheshire", "Chewie", "Chewy",
        "Chicco", "Chief", "Chinook", "Chip", "Chloe", "Chocolate", "Chocolate Chip", "Chris", "Chrissy", "Crumpet",
        "Chub", "Cinder", "Cinderblock", "Cloe", "Cloud", "Clover", "Cocoa", "Cocoa Puff", "Coffee", "Conan", "Cookie",
        "Coral", "Coricopat", "Cosmo", "Cowbell", "Cowboy", "Crab", "Cracker", "Cream", "Crispy", "Crow", "Crunchwrap", "Crunchy",
        "Cupcake", "Cutie", "Cooper", "Confetti", "Cyprus", "Dakota", "Dan", "Dandelion", "Danger Dave", "Daliah", "Dave", "Deli",
        "Delilah", "Della", "Demeter", "Dewey", "Digiorno", "Dinah", "Dirk", "Distinguished Gentleman", "Diona", "Dizzy", "Dolly", "Donald", "Donuts", "Dorian",
        "Dorothy", "Double Trouble", "Dova", "Dragonfly", "Dreamy", "Duchess", "Dune", "Dunnock", "Dust Bunny", "Dusty Cuddles",
        "Eclipse", "Daisy Mae", "Eda", "Eddie", "Eevee", "Egg", "Elden", "Elton", "Ember", "Emerald", "Emeline", "Emi", "Emma",
        "Emy", "Erica", "Esme", "Espresso", "Eve", "Evelyn", "Evie", "Evilface", "Erebus", "Fallow", "Fang", "Fawn",
        "Feather", "Felix", "Fern", "Ferret", "Ferry", "Figaro", "Finch", "Finnian", "Firefly", "Fishleg", "Fishtail", "Fiver",
        "Flabby", "Flamenco", "Flower", "Fluffy", "Flutie", "Fork", "Foxtrot", "Frank", "Frankie", "Frannie", "Fred",
        "Freddy", "Free", "French", "French Fry", "Frito", "Frumpkin", "Fry", "Frye", "Fuzziwig", "Galahad", "Gamble",
        "Gargoyle", "Garfield", "Garnet", "General Erasmus Dickinson", "Geode", "George", "Ghost", "Gibby",
        "Gilded Lily",  "Gingersnap", "Gir", "Gizmo", "Glass", "Glory", "Goose", "Good Sir", "Grace", "Grain",
        "Grasshopper", "Gravy", "Grizabella", "Guinness", "Gus", "Gust", "Gwendoline", "Gwynn", "Gemini", "Habanero", "Haiku", "Haku", "Harvey",
        "Havoc", "Hawkbit", "Hawkeye", "Hazel", "Henry", "Heathcliff", "Herbert", "Herc", "Hercules", "Hiccup", "Highness", "Hlao", "Hocus Pocus", "Hobbes", "Holly", "Hop",
        "Hot Sauce", "Hotdog", "Hubert", "Hughie", "Human", "Humphrey", "Hunter", "Harlequin", "Ice", "Icecube", "Ice Cube", "Icee", "Igor",
        "Ike", "Indi", "Insect", "Ipsy", "Isabel", "Itsy Bitsy", "Jack", "Jade", "Jaiden", "Jake", "James", "Jasper", "Jaxon", "Jay",
        "Jelly Jam", "Jellylorum", "Jenny", "Jennyanydots", "Jesse", "Jessica", "Jester", "Jethro", "Jewel", "Jewels", "Jimmy", "Jiminy Cricket",
        "Jinx", "John", "Johnny", "Joker", "Jolly", "Jolly Rancher", "Joob", "Jubie", "Judas", "Jude", "Judy", "Juliet",
        "June", "Jupiter", "KD", "Kate", "Katjie", "Katy", "Kelloggs", "Ken", "Kendra", "Kenny", "Kermit", "Kerry",
        "Ketchup", "Kettlingur", "Ketsl", "King", "Kingston", "Kip", "Kisha", "Kitty", "Kitty Cat", "Klondike", "Knox",
        "Kodiak", "Kong", "Kyle", "L", "Lacy", "Lady", "Lady Liberty", "Lady Figment", "Lakota", "Laku", "Lark",
        "Larch", "Lee", "Lemon", "Lemmy", "Leo", "Leon", "Lester", "Levon", "Lex", "Lil Baby", "Lilac", "Lilith",
        "Lily", "Linden", "Little Lady", "Little Nicky", "Little One", "Loaf", "Lobster", "Lola", "Lollipop", "Loona", "Lora",
        "Lorado", "Louie", "Louis", "Luchasaurus", "Lucky", "Lucy", "Luci-Purr", "Lugnut", "Luigi", "Luna", "Lupo",
        "Loyalty", "Libra", "Macavity", "Madi", "Maddy", "Makwa", "Maleficent", "Maggie", "Majesty", "Manda", "Mange", "Mango", "Marathon",
        "Marceline", "Mario", "Marny", "Matcha", "Matador", "Maverick", "Max", "May", "McChicken", "McFlurry", "Mick", "Meatlug",
        "Medusa", "Melody", "Meow-Meow", "Meowyman", "Mera", "Mew", "Midnight Goddess", "Miles", "Milhouse", "Millie",
        "Milo", "Milque", "Mimi", "Minette", "Mini", "Minna", "Minnie", "Mint", "Minty", "Missile Launcher", "Misty", "Mitzy Moo Moo",
        "Mitski", "Mittens", "Mochi", "Mocha", "Mojo", "Mollie", "Molly", "Molly Murder Mittens", "Monika", "Monster",
        "Monte", "Monzi", "Moon", "Mop", "Morel", "Moxie", "Mr. Kitty", "Mr. Kitty Whiskers", "Mr. Mistoffolees", "Mr. Whiskers", "Mr. Wigglebottom",
        "Mucha", "Munkustrap", "Mungojerrie", "Murder", "Mushroom", "Mitaine", "Myko", "Neel", "Nagi", "Nakeena", "Neil", "Nemo", "Nessie", "Nick",
        "Nightmare", "Nikki", "Niles", "Ninja", "Nintendo", "Nisha", "Nitro", "Noodle", "Nottingham", "Norman", "Nova",
        "Nugget", "Nuggets", "Nuka", "Nutella", "O'Leary", "Oakley", "Oapie", "Obi Wan", "Odetta", "Old Deuteronomy", "Old Man Sam",
        "Oleander", "Olga", "Oliver", "Oliva", "Ollie", "Omelet", "Onyx", "Oops", "Oopsy Dazey", "Ophelia", "Oreo",
        "Orion", "Oscar", "Otto", "Owen", "Pangur", "Patience", "Paulina", "Peach", "Peanut", "Peanut Wigglebutt", "Pear", "Pearl",
        "Pecan", "Penny", "Peony", "Pepper", "Pepita", "Pichi", "Pickles", "Pierre", "Pikachu", "Ping", "Ping Pong", "Pip",
        "Piper", "Pipsqueak", "Pipkin", "Pixel", "Plato", "Pocket", "Pochito", "Poki", "Polly", "Pong", "Ponyboy", "Poopy", "Porsche",
        "Potato", "Pouncival", "President", "Prickle", "Princess", "Private Eye", "Pudding", "Pumpernickel", "Punk", "Purdy",
        "Purry", "Pisces", "Pushee", "Quagmire", "Quake", "Queen", "Queenie", "Queeny", "Queso", "Queso Ruby", "Quest",
        "Quickie", "Quimby", "Quinn", "Quino", "Quinzee", "Quesadilla", "Radar", "Ramble", "Randy", "Rapunzel",
        "Raptor", "Rarity", "Rat", "Ray", "Reese", "Reeses Puff", "Ren", "Rio", "Riot", "River", "Riya", "Rocket", "Rodeo",
        "Rolo", "Roman", "Roomba", "Rooster", "Rory", "Rose", "Roselie", "Ruby", "Rudolph", "Rufus", "Rue", "Ruffnut", "Rum", "Rumpleteazer", "Rum Tum Tugger", "Russel",
        "Sadie", "Sagwa", "Sailor", "Saki", "Salmon", "Salt", "Sam", "Samantha", "Sandwich", "Sandy", "Sarge", "Sassy", "Sashimi", "Sausage", "Schmidt",
        "Scotch", "Scrooge", "Seamus", "Sekhmet", "Sega", "Seri", "Shamash", "Shampoo", "Shamwow", "Shay", "Sherman",
        "Shimmer", "Shiver", "Sillabub", "Silva", "Silver", "Slinky", "Skimbleshanks", "Skrunkly", "Sloane", "Slug", "Slushie", "Smarty Pants",
        "Smoothie", "Smores", "Sneakers", "Snek", "Snotlout", "Snoots", "Socks",  "Sofa", "Sol", "Sonata", "Sonic",
        "Sophie", "Sorbet", "Sox", "Spam", "Sparky", "Speedwell", "Spots", "Stan", "Star", "Starfish", "Stella",
        "Steve", "Steven", "Stinky", "Stripes", "Stolas", "Strawberry", "Stripes", "Sundae", "Sunny", "Sunset", "Sweet",
        "Sweet Marmalade", "Sweet Leon", "Sweet Creature", "Sweetie", "Scorpio", "Sagittarius", "Sylvester", "Tabatha", "Tabby",
        "Tabbytha", "Taco", "Taco Bell", "Tasha", "Tantomile", "Tamagotchi", "Tay", "Teacup", "Teddie", "Tempest", "Tetris",
        "Tesora", "Teufel", "Theo", "Thumbelina", "Tiana", "Tiny", "Tin Man", "Tigger", "Tikka", "Timmy", "Toast",
        "Toffee", "Tom", "Tomato", "Tomato Soup", "Toni", "Toothless", "Top Hat", "Torque", "Tortilla", "Treasure",
        "Trinket", "Trip", "Triscuit", "Trixie", "Trouble", "Trouble Nuggets", "Troublemaker", "Tucker", "Tuffnut",
        "Tumble", "Tumblebrutus", "Turbo", "Twilight", "Twinkle Lights", "Twister", "Twix", "Toastee", "Taurus", "Ula", "Ulyssa", "Victoria",
        "Union", "Uriel", "Vanilla", "Van Pelt", "Vaxx", "Venture", "Via", "Victor", "Vida", "Viktor", "Vinnie", "Vinyl",
        "Velociraptor", "Violet", "Vivienne", "Void", "Voltage", "Vox", "Virgo", "Wanda", "Warren Peace", "Webby", "Wendy", "Whiskers",
        "Whisper", "Wigglebutt", "Wiggity Wacks", "Windy", "Wishbone", "Wisp", "Wisteria", "Whiz Kid", "Worm", "X'ek",
        "Xelle", "Yaoyao", "Yen", "Yeza", "Yoshi", "Zelda", "Zim", "Zoe", "Zorro",
        ]
    if os.path.exists('saves/prefixlist.txt'):
        with open('saves/prefixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_prefixes.append(new_name)

    if os.path.exists('saves/suffixlist.txt'):
        with open('saves/suffixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_suffixes.append(new_name)

    def __init__(self,
                 status="warrior",
                 prefix=None,
                 suffix=None,
                 colour=None,
                 eyes=None,
                 pelt=None,
                 tortiepattern=None):
        self.status = status
        self.prefix = prefix
        self.suffix = suffix
        
        # Set prefix
        if prefix is None:
            named_after_appearance = not random.getrandbits(3)  # Chance for True is '1/8'.
            # Add possible prefix categories to list.
            possible_prefix_categories = []
            if eyes in self.eye_prefixes:
                possible_prefix_categories.append(self.eye_prefixes[eyes])
            if colour in self.colour_prefixes:
                possible_prefix_categories.append(self.colour_prefixes[colour])
            # Choose appearance-based prefix if possible and named_after_appearance because True.
            if named_after_appearance and possible_prefix_categories:
                prefix_category = random.choice(possible_prefix_categories)
                self.prefix = random.choice(prefix_category)
            else:
                self.prefix = random.choice(self.normal_prefixes)
                    
        # Set suffix
        while self.suffix is None or self.suffix == self.prefix.casefold() or\
         str(self.suffix) in self.prefix.casefold() and not str(self.suffix) == '':
            if pelt is None or pelt == 'SingleColour':
                self.suffix = random.choice(self.normal_suffixes)
            else:
                named_after_pelt = not random.getrandbits(3) # Chance for True is '1/8'.
                # Pelt name only gets used if there's an associated suffix.
                if (named_after_pelt
                    and pelt in ["Tortie", "Calico"]
                    and tortiepattern in self.tortie_pelt_suffixes):
                    self.suffix = random.choice(self.tortie_pelt_suffixes[tortiepattern])
                elif named_after_pelt and pelt in self.pelt_suffixes:
                    self.suffix = random.choice(self.pelt_suffixes[pelt])
                else:
                    self.suffix = random.choice(self.normal_suffixes)

    def __repr__(self):
        if self.status in ["deputy", "warrior", "medicine cat", "elder", "mediator"]:
            return self.prefix + self.suffix
        elif self.status in ["kittypet", "loner", "rogue"]:
            return self.prefix
        else:
            return self.prefix + self.special_suffixes[self.status]



names = Name()
