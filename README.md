# Pokémon Capture Rate Monte Carlo Simulation


## **Team Members:**  

[Jingchen Liu](https://github.com/ljc690106) - NetID: jl288  
[David Luo](https://github.com/HanboLuo) - NetID: hanbol3  

Github Repository: [[2024Fall_Final_Project]](https://github.com/HanboLuo/2024Fall_Final_Project)  

## Introduction
Pokémon is a popular franchise created by Satoshi Tajiri and Ken Sugimori, first released in 1996. In the game, players take on the role of a Pokémon Trainer, capturing various wild Pokémon to build a powerful team. Players use Poké Balls to catch Pokémon they encounter in the wild, and the success of the capture depends on the Pokémon’s health, Ball types and other factors.

Our project aims to develop a Monte Carlo simulation to analyze and optimize **Pokémon capture strategies** in the popular Pokémon video game series. We will simulate various factors that affect **capture rates**, including different **Poké Ball types, Pokémon status conditions, remaining HP, and Pokémon species rarity**. The goal is to determine the most effective capture strategies for different scenarios.

## Rules
1.Pokémon battles operate on a turn-based system, where each participant (trainer or wild Pokémon) performs one action per turn

2.Trainers and wild Pokémon execute their chosen actions, one at a time:
Using a move

3.The battle progresses to the next turn if neither side wins, escapes, or successfully catches the wild Pokémon.
## Hypotheses
1. Using Ultra Balls on legendary Pokémon with low HP and a status condition will result in a capture rate twice as high as using standard Poké Balls on the same Pokémon.
2. The capture rate for common Pokémon species will be less affected by Poké Ball type compared to rare or legendary Pokémon.
3. The most cost-effective method of capturing Pokémon is using Great Balls, regardless of the Pokémon's species, HP level, or status condition.
4. The shortest average time to capture Pokémon is achieved by using Quick Balls, regardless of the Pokémon's species or condition.

## Simulation Design
Our Monte Carlo simulation will incorporate the following random variables:  
* Pokémon species (common, rare, legendary) with associated base capture rates  
* Pokémon's current HP (percentage of max HP)  
* Pokémon's status condition (none, paralyzed, asleep, etc.)  
* Poké Ball type (standard, Great Ball, Ultra Ball, etc.)  
* Used turns

The simulation will run through multiple iterations, simulating capture attempts under various combinations of these factors. We will analyze the aggregate results to determine the most effective strategies for different scenarios.

## Planned Experiments
1. Compare capture rates across different Poké Ball types for each Pokémon rarity category.
2. Analyze the impact of status conditions on capture rates for different Pokémon species.
3. Investigate the relationship between remaining HP and capture success rate.
4. Determine the most cost-effective Poké Ball choice for different Pokémon types and situations.

## Data Sources
While our simulation will be based on the mechanics of the Pokémon games, we will use estimated probabilities and formulas derived from various fan-made resources and official game guides.  

Some key resources include:  
**Bulbapedia** - for base capture rates and formulas: [https://bulbapedia.bulbagarden.net/wiki/Catch_rate](https://bulbapedia.bulbagarden.net/wiki/Catch_rate)  
**Serebii.net** - for Poké Ball statistics: [https://www.serebii.net/games/capture.shtml](https://www.serebii.net/games/capture.shtml)

## Hypotheses 1
Using Ultra Balls on legendary Pokémon with low HP and a status condition results in a significantly higher capture rate compared to using standard Poké Balls on the same Pokémon.

From the graph shown below, when the legendary Pokémon is at full HP and has no status condition, Ultra Balls have a success rate that is much higher than standard Poké Balls, nearly twice as effective as Poké Balls.
![image](https://github.com/user-attachments/assets/bf2712e1-d465-4f24-9bc5-93d8f46c9731)
Similarly, a different graph shows that when the legendary Pokémon has low HP and is affected by paralysis, Ultra Balls also have a significantly higher capture rate compared to Poké Balls.
![image](https://github.com/user-attachments/assets/c3fc96c5-35ba-48e2-8e11-f24aa11f6bc9)
So hypotheses 1 is ture based on our experiment.

## Hypotheses 2
The capture rate for common Pokémon species will be less affected by Poké Ball type compared to rare or legendary Pokémon.
Compared to rare and common pokemon graphs below, we can see the results.

When the Pokémon is at full HP and has no status condition (see the graph below), the capture rates of both rare and common Pokémon are significantly affected by the type of Poké Ball used, especially when comparing Timer Balls and standard Poké Balls.
![image](https://github.com/user-attachments/assets/e4eb28a5-d887-4441-a043-db3960d19f95)
![image](https://github.com/user-attachments/assets/5966dc35-d055-4520-b5cc-a516cba43853)
However, when the pokemon has low HP and paralysis status condition(see the graph below), we can see common pokemon are not affected by poke ball types any more. all kinds of poke balls' success rate is close to 80%. 
![image](https://github.com/user-attachments/assets/84bd1d5b-5429-43a4-9da2-3d3865b1a1bc)
![image](https://github.com/user-attachments/assets/6ac5bfa7-5b5c-4c87-9bca-032ad284dc71)
Thus, our hypotheses are partially supported depending on different conditions. For instance, if the common Pokémon has low HP and is affected by paralysis, the hypotheses can hold true.


## Hypotheses 3
The most cost-effective method of capturing Pokémon is using Great Balls, regardless of the Pokémon's species, HP level, or status condition.

Here is our data analysis. As shown in the data, Poké Balls are the most cost-effective option, regardless of the Pokémon species or its condition.
![image](https://github.com/user-attachments/assets/233a36bf-a74a-4e94-bff8-6d239d6c6005)
So the Hypotheses 3 is unture based on our analysis, the most cost effective method of capturing pokemon would be using standrd poke balls.
## Hypotheses 4
The shortest average time to capture Pokémon is achieved by using Quick Balls, regardless of the Pokémon's species or condition.

Based on our data analysis, as shown in the data below, Ultra Balls require the fewest turns to capture a Pokémon, regardless of the Pokémon's species or condition..
![image](https://github.com/user-attachments/assets/c5d08a12-28b7-44fb-a8e3-30f94c9095c1)
Thus, Hypothesis 4 is untrue: Quick Balls are not the most time-efficient option. Ultra Balls are the best choice if the primary consideration is the shortest time to capture a Pokémon.
## Discussion
1. For common species, first mitigate their HP and then just use the most basic Poke Ball! The effects are almost at the same level.
2. Most of the time, the more expensive ball works better.
3. Great Balls are not always ‘great’, and Quick Balls are not always ‘quick’.
4. Applying negative status conditions provides a more stable outcome.

## Limitations and future works

Make a more powerful and realistic design: 
1.Escape Rate: A pokemon may escape from a battle after a certain turns;
2.Status condition duration: Some Pokémon may have resistances to certain status conditions, causing the applied status conditions to wear off after a few turns.

Code improvement:
1.Write doctests and detailed docstrings for each function;
2.Optimize the code logic to reduce redundant calculations in similar situations.






