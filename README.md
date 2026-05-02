# Tuple Out Dice Game

A two or more player dice game written in Python.

## How to Run

First install the required libraries:

```
pip install numpy pandas seaborn matplotlib
```

Then run the game:

```
python tuple_out.py
```

## How to Play

Each player takes turns rolling 3 dice. The goal is to score as many points as possible without "tupling out."

**Tuple Out:** If all three dice show the same number at any point during your turn, you score 0 points for that turn.

**Fixed Dice:** If two of your dice show the same number, those dice are "fixed" (marked with \*) and cannot be rerolled.

**Scoring:** When you decide to stop rolling, your score for that turn is the sum of all three dice.

**Winning:** After everyone takes the same number of turns, the player with the highest total score wins.

## Features

- 2 to 4 players
- Choose how many turns each player gets
- Game history saved to game_history.json
- Score chart generated using seaborn (saved as score_chart.png)

## Example

```
Kennedy's turn!
Press Enter to roll...
  Dice: [5*] [2]  [5*]  (* = fixed, cannot reroll)
Reroll free dice? (y/n): y
  Dice: [5*] [4]  [5*]  (* = fixed, cannot reroll)
Reroll free dice? (y/n): n
  Kennedy scores 14 points this turn!
```
