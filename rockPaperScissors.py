import random

# Initialize variables
user_choice = ""
rematch = ""
moveList = ["rock", "paper", "scissors"]
# Function to start the game
def start():
    
    # Get user's choice of rock, paper, or scissors
    user_choice = input("Rock, Paper, or Scissors? ").lower()

    # Validate user input
    if user_choice in moveList:
        # Get the computer's move
        cpu_choice = rand_choice()
        
        # Display choices
        print(f"You chose {user_choice}. Computer chose {cpu_choice}.")

        # Compare choices and determine the winner
        if cpu_choice == user_choice:
            print("It's a Draw!")
        elif (cpu_choice == "rock" and user_choice == "scissors") or (cpu_choice == "paper" and user_choice == "rock") or (cpu_choice == "scissors" and user_choice == "paper"):
            print("You lost.")
        else:
            print("You won!")

        # Ask if the user wants to play again
        try_again()
    else:
        print("You did not give a valid option. Please try again.")
        start()

# Function to get the computer's choice
def rand_choice():
    return random.choice(moveList)

# Function to ask if the user wants to play again
def try_again():
    rematch = input("Would you like to try again? (y/n) ").lower()
    if rematch == "y":
        start()
    else:
        print("Thank you for playing!")

# Start the game
start()