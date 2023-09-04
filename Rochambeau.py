# This program plays a game of Rock, Paper, Scissors
# between the user and the computer.

import random


# This function gets the user's choice.
def get_user_choice():
    """
    Get the user's choice of rock, paper, or scissors.

    Raises:
        ValueError: If the user's choice is invalid.

    Returns:
        str: The user's choice.
    """
    print("Enter your choice: rock, paper, or scissors")
    user_choice = input().lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        raise ValueError("Invalid choice. Please enter rock, paper, or scissors.")
    return user_choice


# This function gets the computer's choice.
def get_computer_choice():
    """
    Get the computer's choice of rock, paper, or scissors.

    Returns:
        str: The computer's choice.
    """
    return random.choice(["rock", "paper", "scissors"])


# This function determines the winner of the game.
def determine_winner(user, computer):
    """
    Determines the winner of the game based on the user's choice and the computer's choice.

    Args:
        user (str): The user's choice.
        computer (str): The computer's choice.

    Returns:
        str: A message indicating the winner of the game.
    """
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "You Win!!!"
    else:
        return "The Computer Wins!"


# This is the main function.
if __name__ == "__main__":
    print("Welcome to Rochambeau!")

    # Play the game until the user quits.
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")
        print(determine_winner(user_choice, computer_choice))

        # Ask if the player wants to play again.
        play_again = input("would you like to play again? (yes/no)").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break