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


if __name__ == "__main__":
    # quick test
    d = roll_dice()
    print("rolled:", d)
    display_dice(d)
    print("tuple out:", all_same(d))
