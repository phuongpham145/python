import random

def getChoice(choice):
    if choice == "R":
        return "Rock"
    elif choice == "P":
        return "Paper"
    elif choice == "S":
        return "Scissor"
    else:
        return "No a value choice"
def main():
    print("Welcome to Rock, Paper, Scissor Game")
    print("[R] = Rock, [P] = Paper, [S] = Scissor, [Q] = Quit Game")
    choices = ["R", "P", "S", "Q"]
    counter = 1
    game_oh = True
    while game_oh:
        userChoice = input(f"Game #{counter}. Please enter your choice: ")
        userChoice = userChoice.upper()
        if userChoice == "Q":
            print("Thank for joining")
            game_oh = False
        else:
            randomIndex = random.randint(0, 2)
            computerChoice = choices[randomIndex]
            print(f"You selected {getChoice(userChoice)} vs computer selected {getChoice(computerChoice)}")
        if userChoice == "R" and computerChoice == "S":
            print("You win")
        elif userChoice == "P" and computerChoice == "R":
            print("You win")
        elif userChoice == "S" and computerChoice == "P":
            print("You win")
        elif userChoice == "R" and computerChoice == "P":
            print("You lose")
        elif userChoice == "S" and computerChoice == "R":
            print("You lose")
        elif userChoice == computerChoice:
            print("You have a same result")
        else:
            print("Invalue option")
        counter += 1;


if __name__ == "__main__":
    main()