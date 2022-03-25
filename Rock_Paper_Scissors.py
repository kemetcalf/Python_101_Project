import random

weapon = ["rock", "paper", "scissors"]

player_name = input("What is your name?")
result = f"I want to play a game, {player_name}."

while True:
    print(result)
    my_weapon = input("Choose your weapon! Rock, paper, or scissors?")
    my_weapon = my_weapon.lower()
    comp_weapon = random.choice(weapon)

    if comp_weapon == my_weapon:
        result = "It's a tie! Try again"
        continue
    elif comp_weapon == "rock" and my_weapon == "paper":
        result = f"{player_name} wins!"
        print(result)
        break
    elif comp_weapon == "rock" and my_weapon == "scissors":
        result = "Computer wins! Try again"
        continue
    elif comp_weapon == "paper" and my_weapon == "rock":
        result = "Computer wins! Try again"
        continue
    elif comp_weapon == "paper" and my_weapon == "scissors":
        result = f"{player_name} wins!"
        print(result)
        break
    elif comp_weapon == "scissors" and my_weapon == "rock":
        result = f"{player_name} wins!"
        print(result)
        break
    elif comp_weapon == "scissors" and my_weapon == "paper":
        result = "Computer wins! Try again"
        continue
    else:
        result = "Weapon not allowed! Bad form!"
