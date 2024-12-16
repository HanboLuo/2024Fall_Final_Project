from function import *
import matplotlib.pyplot as plt
import random

def simulate_capture_by_turn(pokemon, pokeballs, num_simulations=20000, max_turns=50):
    """
    Simulate capture success rates by turn for a Pokemon using various Poke Balls.

    Args:
        pokemon (Pokemon): The Pokemon being simulated.
        pokeballs (list[PokeBall]): A list of Poke Balls' settings.
        num_simulations (int): Number of simulations to perform per turn. Default is 20,000.
        max_turns (int): Maximum number of turns to simulate. Default is 50.

    Returns:
        dict: A nested dictionary where keys are turn numbers, and values are dictionaries
              with Poke Ball names and their corresponding capture rates.

    Example:
        >>>simulate_capture_by_turn(pokemon_list[0], pokeballs, num_simulations=1000, max_turns=10)
        This will simulate the capture rates for Mewtwo over 10 turns using 1000 simulations per ball.
    """
    turn_results = {turn: {} for turn in range(1, max_turns + 1)}

    for turn in range(1, max_turns + 1):
        for pokeball in pokeballs:
            # Skip Quick Ball if Pokemon is not at full HP and it's not turn 1
            if pokemon.current_hp < pokemon.max_hp and pokeball.name == 'Quick Ball':
                continue

            successes = 0
            for _ in range(num_simulations):
                if random.random() < calculate_catch_rate(pokemon, pokeball, turn):
                    successes += 1
            success_rate = successes / num_simulations
            turn_results[turn][pokeball.name] = success_rate

    return turn_results


def find_best_strategy(turn_results):
    """
    Identify the best capture strategy for each turn.

    Args:
        turn_results (dict): Results from simulate_capture_by_turn, containing capture rates.

    Returns:
        dict: A dictionary where keys are turns, and values are tuples containing the best
              Poke Ball and its corresponding capture rate.

    Example:
        >>>turn_results = {1: {"Quick Ball": 0.1, "Ultra Ball": 0.08}, 2: {"Timer Ball": 0.2}}
        find_best_strategy(turn_results)
        This will return a dictionary showing the best Poke Ball for each turn based on capture rate.
    """
    best_strategy = {}
    for turn, results in turn_results.items():
        if results:  # Ensure there are results for this turn
            best_ball = max(results, key=results.get)
            best_strategy[turn] = (best_ball, results[best_ball])
    return best_strategy


def plot_dynamic_results(turn_results, pokemon):
    """
    Plot dynamic capture rates over turns for a given Pokemon.

    Args:
        turn_results (dict): Results from simulate_capture_by_turn, containing capture rates.
        pokemon (Pokemon): The Pokemon being analyzed.

    Returns:
        None: This function only plots the results.

    Example:
        >>>turn_results = {1: {"Quick Ball": 0.1, "Ultra Ball": 0.08}, 2: {"Timer Ball": 0.2}}
        >>>plot_dynamic_results(turn_results, pokemon_list[0])
        This will generate a line plot showing capture rate trends for each Poke Ball over time.
    """
    plt.figure(figsize=(12, 6))

    all_balls = set(ball for results in turn_results.values() for ball in results)
    for pokeball in all_balls:
        rates = [turn_results[turn].get(pokeball, 0) for turn in turn_results]
        plt.plot(range(1, len(turn_results) + 1), rates, label=pokeball)

    plt.title(f"Dynamic Capture Rates for {pokemon.name}")
    plt.xlabel("Turn")
    plt.ylabel("Capture Rate")
    plt.legend()
    plt.grid(True)
    plt.show()


def analyze_conditions(pokemon, pokeballs, num_simulations=20000, max_turns=50):
    """
    Analyze capture strategies under different conditions: Full HP and Low HP with Paralysis.

    Args:
        pokemon (Pokemon): The Pokemon to capture.
        pokeballs (list[PokeBall]): A list of Poke Balls' settings.
        num_simulations (int): Number of simulations to perform per condition. Default is 20,000.
        max_turns (int): Maximum number of turns to simulate. Default is 50.

    Returns:
        None: This function prints and plots the results for each condition.

    Example:
        >>>analyze_conditions(pokemon_list[0], pokeballs, num_simulations=1000, max_turns=10)
        This will analyze capture strategies for Mewtwo under Full HP and Low HP with Paralysis,
        and plot the results for each condition.
    """
    # Full HP analysis
    pokemon.current_hp = pokemon.max_hp  # Full HP
    pokemon.status = None
    print(f"\nAnalyzing capture strategy for {pokemon.name} at full HP:")
    turn_results_full_hp = simulate_capture_by_turn(pokemon, pokeballs, num_simulations, max_turns)
    best_strategy_full_hp = find_best_strategy(turn_results_full_hp)
    for turn, (ball, rate) in best_strategy_full_hp.items():
        if turn % 10 == 0 or turn == 1:
            print(f"Turn {turn}: Best Ball = {ball}, Capture Rate = {rate:.2%} (Full HP)")
    plot_dynamic_results(turn_results_full_hp, pokemon)

    # Low HP with paralysis
    pokemon.current_hp = pokemon.max_hp // 10  # Low HP
    pokemon.status = 'paralysis'
    print(f"\nAnalyzing capture strategy for {pokemon.name} at low HP with paralysis:")
    turn_results_low_hp = simulate_capture_by_turn(pokemon, pokeballs, num_simulations, max_turns)
    best_strategy_low_hp = find_best_strategy(turn_results_low_hp)
    for turn, (ball, rate) in best_strategy_low_hp.items():
        if turn % 10 == 0 or turn == 1:
            print(f"Turn {turn}: Best Ball = {ball}, Capture Rate = {rate:.2%} (Low HP & Paralysis)")
    plot_dynamic_results(turn_results_low_hp, pokemon)