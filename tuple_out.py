import numpy as np

# Player class to keep track of each player's name and score
class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.turn_scores = []

    def add_score(self, points):
        self.total_score += points
        self.turn_scores.append(points)


def roll_dice():
    # use numpy to roll 3 dice with values from 1 to 6
    result = np.random.randint(1, 7, size=3)
    return [int(result[0]), int(result[1]), int(result[2])]


def all_same(dice):
    # check if all three dice are the same value (tuple out)
    return dice[0] == dice[1] == dice[2]


def get_fixed(dice):
    # find which dice are fixed (any two dice with the same value)
    fixed = []
    for i in range(3):
        if dice.count(dice[i]) == 2:
            fixed.append(i)
    return fixed


def display_dice(dice):
    fixed = get_fixed(dice)
    output = "  Dice: "
    for i in range(3):
        if i in fixed:
            output += f"[{dice[i]}*] "
        else:
            output += f"[{dice[i]}]  "
    if len(fixed) > 0:
        output += " (* = fixed, cannot reroll)"
    print(output)


def player_turn(player):
    print(f"\n{player.name}'s turn!")
    input("Press Enter to roll...")

    dice = roll_dice()
    display_dice(dice)

    # if all three dice are the same right away, tuple out
    if all_same(dice):
        print("TUPLE OUT! You score 0 points this turn.")
        return 0

    # keep letting the player reroll until they stop or tuple out
    while True:
        fixed = get_fixed(dice)
        free = []
        for i in range(3):
            if i not in fixed:
                free.append(i)

        if len(free) == 0:
            print("All dice are fixed, turn is over.")
            break

        answer = input("Reroll free dice? (y/n): ").strip().lower()
        if answer != "y":
            break

        # reroll only the free dice
        new_rolls = np.random.randint(1, 7, size=len(free))
        for i in range(len(free)):
            dice[free[i]] = int(new_rolls[i])

        display_dice(dice)

        # check for tuple out after rerolling
        if all_same(dice):
            print("TUPLE OUT! You score 0 points this turn.")
            return 0

    points = sum(dice)
    print(f"  {player.name} scores {points} points this turn!")
    return points


def print_scores(players):
    print("\nCurrent Scores:")
    for p in players:
        print(f"  {p.name}: {p.total_score} points")


if __name__ == "__main__":
    p = Player("Test")
    pts = player_turn(p)
    p.add_score(pts)
    print("Total:", p.total_score)
