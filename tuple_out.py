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


def play_game():
    print("\n=== New Game of Tuple Out ===")

    # ask how many players
    while True:
        try:
            num = int(input("How many players? (2-4): "))
            if num >= 2 and num <= 4:
                break
            else:
                print("Please enter 2, 3, or 4.")
        except ValueError:
            print("Please enter a valid number.")

    # get each player's name
    players = []
    for i in range(num):
        name = input(f"Enter name for player {i + 1}: ").strip()
        while name == "":
            name = input("Name can't be empty, try again: ").strip()
        players.append(Player(name))

    # ask how many turns
    while True:
        try:
            turns = int(input("How many turns each? (default is 10): ") or "10")
            if turns > 0:
                break
            else:
                print("Must be at least 1 turn.")
        except ValueError:
            print("Please enter a valid number.")

    # main game loop
    for turn_num in range(1, turns + 1):
        print(f"\n--- Round {turn_num} of {turns} ---")
        for player in players:
            points = player_turn(player)
            player.add_score(points)
        print_scores(players)

    # find the winner
    winner = players[0]
    for p in players:
        if p.total_score > winner.total_score:
            winner = p

    print(f"\n{winner.name} wins with {winner.total_score} points!")


def main():
    print("Welcome to Tuple Out!")
    print("Roll 3 dice and score points without getting three of a kind.\n")

    while True:
        print("Menu:")
        print("1. Play a game")
        print("2. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please enter 1 or 2.")


if __name__ == "__main__":
    main()
