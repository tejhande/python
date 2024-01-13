import random

def game():
    options = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice not in options:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(options)
        print("Computer chooses:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie.")
        elif player_choice == "rock" and computer_choice == "scissors":
            print("You win!")
        elif player_choice == "paper" and computer_choice == "rock":
            print("You win!")
        elif player_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins.")

        play_again = input("Do you want to play again (yes/no)? ").lower()
        if play_again != "yes":
            break

print("Welcome to Rock-Paper-Scissors")
game()
