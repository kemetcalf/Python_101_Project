import random
weapon = ["rock", "paper", "scissors"]
player_name = input("What is your name?")
result = f"I want to play a game, {player_name}."
score = {
    "computer": 0,
    "player": 0
}


def its_a_tie():
    result = "It's a tie!"
    print(
        result,
        f"\nComputer: {score['computer']}, {player_name}: {score['player']}")


def player_wins():
    result = f"{player_name} wins!"
    score["player"] = score["player"] + 1
    print(
        result,
        f"\nComputer: {score['computer']}, {player_name}: {score['player']}")


def computer_wins():
    result = "Computer wins!"
    score["computer"] = score["computer"] + 1
    print(
        result,
        f"\nComputer: {score['computer']}, {player_name}: {score['player']}")


def keep_playing():
    answer = input("Do you want to keep playing? y/n: ")
    if answer.lower() in ["y", "yes"]:
        return True
    else:
        return False


def farewell():
    result = f"Awww D: Ok, see you later, {player_name}!"
    print(
        result,
        f"\nFinal Score:\nComputer: {score['computer']}, {player_name}: {score['player']}")


print(result)

while True:
    my_weapon = input("Choose your weapon! Rock, paper, or scissors?")
    my_weapon = my_weapon.lower()
    comp_weapon = random.choice(weapon)

    if comp_weapon == my_weapon:
        its_a_tie()
    elif comp_weapon == "rock" and my_weapon == "paper":
        player_wins()
    elif comp_weapon == "rock" and my_weapon == "scissors":
        computer_wins()
    elif comp_weapon == "paper" and my_weapon == "rock":
        computer_wins()
    elif comp_weapon == "paper" and my_weapon == "scissors":
        player_wins()
    elif comp_weapon == "scissors" and my_weapon == "rock":
        player_wins()
    elif comp_weapon == "scissors" and my_weapon == "paper":
        computer_wins()
    elif my_weapon == "quit":
        farewell()
        break
    else:
        result = "Weapon not allowed! Bad form!"
        print(result)

    if keep_playing():
        continue
    else:
        farewell()
        break
