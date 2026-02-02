import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissors): ")  # 1, 2, 3

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3!")
else:
    computerChoice = random.randint(1, 3)

    #    playerChoiceIndex = choices[playerChoice - 1] # ==> 0, 1, 2
    #    computerChoiceIndex = choices[computerChoice - 1]
    #    print(playerChoiceIndex,  computerChoiceIndex)

    # Determine the winner logic using if/elif/else
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You win!")
    else:
        print("You lose!")
