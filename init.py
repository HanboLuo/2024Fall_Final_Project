class Pokemon:
    '''
    Represents a Pokemon with attributes for its name, catch rate, max health points (HP), current HP, and status.

    Attributes:
        name: The name of the Pokemon.
        catch_rate: The catch rate of the Pokemon.
        max_hp: The maximum HP of the Pokemon.
        current_hp: The current HP of the Pokemon.
        status: The negative status applied to the Pokemon.
    '''

    def __init__(self, name, catch_rate, max_hp):
        self.name = name
        self.catch_rate = catch_rate
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.status = None


class PokeBall:
    '''
    Represents a Poke Ball with its catch rate multiplier and price.

    Attributes:
        name: The name of the Poke Ball.
        catch_rate_multiplier: The multiplier for the catch rate.
        price: The price of the Poke Ball.
    '''

    def __init__(self, name, catch_rate_multiplier, price):
        self.name = name
        self.catch_rate_multiplier = catch_rate_multiplier
        self.price = price

# 20,000 simulations with 50 turns maximum
ns = 20000 # num_simulations
dt = 50 # default_turn

# Create Pokemon and Poke Balls based on Serebii's data
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

# Run simulations and analyze minimum cost for each Pokemon
pokemon_list = [mewtwo, pikachu, charizard, snorlax, gyarados, gengar, dragonite]
