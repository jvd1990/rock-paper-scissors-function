import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

# Function to get the user's choice
def get_user_choice():
    user_input = input("Please enter your choice (Rock, Paper, or Scissors): ")
    while user_input not in ['Rock', 'Paper', 'Scissors']:
        user_input = input("Invalid input. Please enter your choice again (Rock, Paper, or Scissors): ")
    return user_input

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print("Computer choice:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
    
    print("Thank you for playing!")

# Start the game
play_game()
