import random
import matplotlib.pyplot as plt

from init import *


def calculate_catch_rate(pokemon, pokeball, turn):
    '''
    :param pokemon: Pokemon to catch.
    :param pokeball: the Poke Ball being used. 
    :param turn: The number of the current turn.
    :return: the calculated catch_rate of this attempt.
    
    >>> pokemon = pokemon_list[0]   # Mewtwo
    >>> pokeball = pokeballs[3] # Quick Ball
    >>> rate_1, rate_2 = calculate_catch_rate(pokemon, pokeball, 1), calculate_catch_rate(pokemon, pokeball, 2)
    >>> rate_1 / rate_2
    5.0

    >>> pokemon.status = 'sleep'
    >>> calculate_catch_rate(pokemon, pokeball, 2) / rate_2
    2.5

    '''
    # HP factor calculation based on Serebii's formula
    hp_factor = (3 * pokemon.max_hp - 2 * pokemon.current_hp) / (3 * pokemon.max_hp)

    # Status condition bonus
    status_bonus = 2.5 if pokemon.status in ['sleep', 'freeze'] \
        else 1.5 if pokemon.status in ['paralysis', 'poison', 'burn'] \
        else 1

    # Base capture rate calculation
    base_catch_rate = pokemon.catch_rate * pokeball.catch_rate_multiplier * status_bonus * hp_factor / 255

    # Special Poké Ball effects
    if pokeball.name == 'Quick Ball' and turn != 1:
        base_catch_rate /= 5
    elif pokeball.name == 'Timer Ball':
        base_catch_rate *= min((turn + 10) / 10, 4)

    return min(base_catch_rate, 1)


def attempt_capture(pokemon, pokeball, turn):
    catch_rate = calculate_catch_rate(pokemon, pokeball, turn)

    # Simulate the shake checks using Serebii's mechanics
    shake_chance = int(65536 / ((255 / catch_rate) ** 0.1875))

    shakes = 0
    for _ in range(4):  # Four shake checks
        if random.randint(0, 65535) < shake_chance:
            shakes += 1
        else:
            break

    return shakes == 4


def simulate_capture(pokemon, pokeball, num_simulations=ns, default_turn=dt):
    turns_to_capture = []

    for _ in range(num_simulations):
        turns = 0
        while turns < default_turn + 1:  # Set maximum turns limit
            turns += 1
            if attempt_capture(pokemon, pokeball, turns):
                if turns <= default_turn:
                    turns_to_capture.append(turns)
                break

    success_rate = len(turns_to_capture) / num_simulations
    avg_turns = sum(turns_to_capture) / len(turns_to_capture)

    return success_rate, avg_turns, turns_to_capture


def analyze_min_cost(pokemon, pokeballs, num_simulations=ns, default_turn=dt):
    cost_analysis = {}

    for pokeball in pokeballs:
        success_rate, avg_turns, _ = simulate_capture(pokemon, pokeball, num_simulations, default_turn)
        avg_cost = avg_turns * pokeball.price
        cost_analysis[pokeball.name] = {
            'success_rate': success_rate,
            'avg_turns': avg_turns,
            'avg_cost': avg_cost
        }

    # Find the minimum cost option
    min_cost_ball = min(cost_analysis, key=lambda ball: cost_analysis[ball]['avg_cost'])
    return min_cost_ball, cost_analysis


def analyze_min_cost_low_hp_status(pokemon, pokeballs, num_simulations=ns, default_turn=dt):
    pokemon.current_hp = pokemon.max_hp // 10  # Set low HP
    pokemon.status = 'paralysis'  # Apply status condition
    return analyze_min_cost(pokemon, pokeballs, num_simulations, default_turn)


def analyze_min_time(pokemon, pokeballs, num_simulations=ns, default_turn=dt):
    time_analysis = {}

    for pokeball in pokeballs:
        _, avg_turns, _ = simulate_capture(pokemon, pokeball, num_simulations, default_turn)
        time_analysis[pokeball.name] = avg_turns

    # Find the minimum time option
    min_time_ball = min(time_analysis, key=time_analysis.get)
    return min_time_ball, time_analysis


def plot_results(pokemon, pokeballs, num_simulations=ns, default_turn=dt):
    plt.figure(figsize=(12, 6))

    max_turns = default_turn  # Use the same maximum limit as the simulation

    for pokeball in pokeballs:
        success_rate, avg_turns, turns_to_capture = simulate_capture(pokemon, pokeball, num_simulations)

        # Count capture occurrences for each turn
        turn_counts = [0] * (max_turns + 1)
        for turn in turns_to_capture:
            if turn <= max_turns:
                turn_counts[turn] += 1

        # Prepare x and y values for the scatter plot
        x_values = range(1, max_turns + 1)
        y_values = turn_counts[1:]  # Exclude the 0th turn (not possible)

        # Plot as a scatter chart
        plt.scatter(x_values, y_values,
                    label=f"{pokeball.name} (Success Rate: {success_rate:.2%}, Avg. Turns: {avg_turns:.2f})")

        print(f"{pokeball.name} - Success Rate: {success_rate:.2%}, Average Turns: {avg_turns:.2f}")

    plt.title(
        f"{pokemon.name} Capture Simulation (HP: {pokemon.current_hp}/{pokemon.max_hp}, Status: {pokemon.status or 'None'})"
    )
    plt.xlabel("Turns to Capture")
    plt.ylabel("Numbers of Success")
    plt.legend()
    plt.grid(True)
    plt.show()
