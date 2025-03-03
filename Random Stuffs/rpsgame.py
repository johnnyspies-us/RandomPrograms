# import random

# #random toss from opponent
# def rps():
#     return random.randint(1,3)
# choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
# opponentsplay = choices[rps()]


# userinput = input("""Rock, Paper, Scissors, Shoot!
#             1. Rock
#             2. Paper
#             3. Scissors """)


# userplay = choices[int(userinput)]


# if userplay == opponentsplay:
#     print("Tie! Play Again?")
# elif userplay == "Rock" and opponentsplay == "Scissors":
#     print("Your opponent chose, ", opponentsplay,"You Won!, Play Again?")
# elif userplay == "Rock" and opponentsplay == "Paper":
#     print("Your opponent chose, ", opponentsplay,"You Lost!, Play Again?")
# elif userplay == "Paper" and opponentsplay == "Scissors":
#     print("Your opponent chose, ", opponentsplay,"You Lost!, Play Again?")
# elif userplay == "Paper" and opponentsplay == "Rock":
#     print("Your opponent chose, ", opponentsplay,"You Won!, play again?")
# elif userplay == "Scissors" and opponentsplay == "Rock":
#     print("Your opponent chose, ", opponentsplay,"You Lost!, play Again?")
# elif userplay == "Scissors" and opponentsplay == "Paper":
#     print("Your opponent chose, ", opponentsplay, "You Won!, Play Again?")
# else:
#    print("Fuck ya mother")



# "Your opponent chose, ", opponentsplay
from rich.console import Console

console = Console()
console.print("[bold blue]Welcome to Rock Paper Scissors![/bold blue]")

import random

def play_game():
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    while True:
        # Generate opponent's choice
        opponentsplay = choices[random.randint(1, 3)]
        print("\nOpponent chose:", opponentsplay)

        # Get user input
        try:
            userinput = int(input("""Rock, Paper, Scissors, Shoot!
            1. Rock
            2. Paper
            3. Scissors
            Choose a number: """))
            
            if userinput not in choices:
                print("Invalid choice! Pick 1, 2, or 3.")
                continue  # Restart the loop if input is invalid

            userplay = choices[userinput]
            print("You chose:", userplay, "And your opponent chose, ", opponentsplay)

            # Determine the winner
            if userplay == opponentsplay:
                print("It's a tie!")
            elif (userplay == "Rock" and opponentsplay == "Scissors") or \
                 (userplay == "Paper" and opponentsplay == "Rock") or \
                 (userplay == "Scissors" and opponentsplay == "Paper"):
                print("You win!")
            else:
                print("You lose!")

        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")
            continue  # Restart the loop

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! See you next time.")
            break  # Exit the loop

# Run the game
play_game()