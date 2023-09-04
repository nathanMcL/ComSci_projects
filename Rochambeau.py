# This program plays a game of Rock, Paper, Scissors
# between the user and the computer.
# Prompts to play again.
# Display score at the end of the game.

import random

# Initialize scores
# Declare global variables so that they can be accessed by all functions
user_wins = 0  # Number of times the user has won
computer_wins = 0  # Number of times the computer has won
ties = 0  # Number of ties


def get_user_choice():
    """
    Get the user's choice of rock, paper, or scissors.
    """

    print("Enter your choice: rock, paper, or scissors")
    user_choice = input().lower()
    # Validate the user's choice
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input().lower()
    return user_choice


def get_computer_choice():
    """
    Get the computer's choice of rock, paper, or scissors.
    """

    # Use the random library to generate a random choice
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user, computer):
    """
    Return the winner of the game.
    """

    global user_wins, computer_wins, ties
    # Check for a tie
    if user == computer:
        ties += 1
        return 'It\'s a tie!'
    # Check for a win
    elif (user == 'rock' and computer == 'scissors') or \
            (user == 'scissors' and computer == 'paper') or \
            (user == 'paper' and computer == 'rock'):
        user_wins += 1
        return 'You Win!!!'
    else:
        computer_wins += 1
        return 'The Computer Wins!'


if __name__ == "__main__":
    print("Welcome to Rochambeau!")

    # Play the game until the user quits
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")
        print(determine_winner(user_choice, computer_choice))

        # Ask if the player wants to play again
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Game Score: You - {user_wins}, Computer - {computer_wins}, Ties - {ties}")
            print("Thank you for playing!")
            break
