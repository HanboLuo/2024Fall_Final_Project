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
![image](https://github.com/user-attachments/assets/bf2712e1-d465-4f24-9bc5-93d8f46c9731)


