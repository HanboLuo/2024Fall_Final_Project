from function import *


def main():
    for pokemon in pokemon_list:
        print(f"\nSimulating capture for {pokemon.name} at full HP:")
        plot_results(pokemon, pokeballs)

        print(f"\nSimulating capture for {pokemon.name} at low HP with paralysis:")
        pokemon.current_hp = pokemon.max_hp // 10
        pokemon.status = 'paralysis'
        plot_results(pokemon, pokeballs)

        print(f"\nAnalyzing minimum cost for capturing {pokemon.name}:")
        min_cost_ball, cost_analysis = analyze_min_cost(pokemon, pokeballs)
        for ball, stats in cost_analysis.items():
            print(
                f"{ball}: Success Rate = {stats['success_rate']:.2%}, Avg. Turns = {stats['avg_turns']:.2f}, Avg. Cost = {stats['avg_cost']:.2f}")
        print(f"Recommended Ball: {min_cost_ball} with Avg. Cost = {cost_analysis[min_cost_ball]['avg_cost']:.2f}")

        print(f"\nAnalyzing minimum cost for capturing {pokemon.name} at low HP with status:")
        min_cost_ball, cost_analysis = analyze_min_cost_low_hp_status(pokemon, pokeballs)
        for ball, stats in cost_analysis.items():
            print(
                f"{ball}: Success Rate = {stats['success_rate']:.2%}, Avg. Turns = {stats['avg_turns']:.2f}, Avg. Cost = {stats['avg_cost']:.2f}")
        print(
            f"Recommended Ball at Low HP: {min_cost_ball} with Avg. Cost = {cost_analysis[min_cost_ball]['avg_cost']:.2f}")

        print(f"\nAnalyzing minimum time for capturing {pokemon.name}:")
        min_time_ball, time_analysis = analyze_min_time(pokemon, pokeballs)
        for ball, avg_turns in time_analysis.items():
            print(f"{ball}: Avg. Turns = {avg_turns:.2f}")
        print(
            f"Recommended Ball for Minimum Time: {min_time_ball} with Avg. Turns = {time_analysis[min_time_ball]:.2f}")


if __name__ == "__main__":
    main()