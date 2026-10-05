import random


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print("Dice 1:", dice1)
    print("Dice 2:", dice2)
    print("Total:", total)

    return total


def play_craps():
    print("Welcome to Craps!")
    print("Press Enter to roll the dice.")
    input()

    first_roll = roll_dice()

    if first_roll == 7 or first_roll == 11:
        print("You WIN!")
        return

    if first_roll == 2 or first_roll == 3 or first_roll == 12:
        print("Craps! Casino WINS!")
        return

    goal = first_roll

    print("Your goal number is", goal)
    print("Keep rolling until you get your goal number.")
    print("If you roll 7 first, you lose!")

    while True:
        input("Press Enter to roll again...")

        roll = roll_dice()

        if roll == goal:
            print("You rolled your goal number!")
            print("YOU WIN!")
            break

        if roll == 7:
            print("You rolled 7!")
            print("YOU LOSE!")
            break

        print("Keep going! Your goal is still", goal)


play_craps()

# Good job