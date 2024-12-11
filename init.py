class Pokemon:
    def __init__(self, name, catch_rate, max_hp):
        self.name = name
        self.catch_rate = catch_rate
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.status = None


class PokeBall:
    def __init__(self, name, catch_rate_multiplier, price):
        self.name = name
        self.catch_rate_multiplier = catch_rate_multiplier
        self.price = price


# Create Pokémon and Poké Balls based on Serebii's data
# Real Catch Rate = catch_rate / 255
mewtwo = Pokemon("Mewtwo", 3, 200)
pikachu = Pokemon("Pikachu", 190, 100)
charizard = Pokemon("Charizard", 45, 180)
snorlax = Pokemon("Snorlax", 25, 250)
gyarados = Pokemon("Gyarados", 45, 190)
gengar = Pokemon("Gengar", 45, 150)
dragonite = Pokemon("Dragonite", 45, 200)

pokeballs = [
    PokeBall("Poke Ball", 1, 200),
    PokeBall("Great Ball", 1.5, 600),
    PokeBall("Ultra Ball", 2, 800),
    PokeBall("Quick Ball", 5, 1000),  # Enhanced on Turn 1
    PokeBall("Timer Ball", 1, 1000),  # Improves with turns passed (up to x4 multiplier)
]

# Run simulations and analyze minimum cost for each Pokémon
pokemon_list = [mewtwo, pikachu, charizard, snorlax, gyarados, gengar, dragonite]
