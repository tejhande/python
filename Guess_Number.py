import random

def display_menu():
    print("\nEnter 1 To Play")
    print("Enter 2 For Rules")
    print("Enter 3 To Know About Developer")
    print("Enter 4 To See High Score")
    print("Enter 5 To Exit")

def play_game():
    print("Welcome to Guess the Number!")
    secret_number = random.randint(1, 100000)
    print("Secret Number Is Between 1 to 100000")
    attempts = 0
    high_score = 0

    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read().strip() or 0)
            print(f"The current high score is {high_score} attempts.")
    except FileNotFoundError:
        print("High score file not found.")
    except Exception as e:
        print(f"Error reading high score file: {e}")
    while True:
        name = input("Please enter your name: ")
        if name.replace(" ", "").isalpha():
            break
        else:
            print("Invalid Input...")
    print(f"Hello {name}! Let's play!")

    while True:
        # guess = input("Enter your guess: ")
        guess = input(f"\nAttempt #{attempts + 1}. Enter your guess: ")

        if guess.lower() == 'exit':
            print("Thanks for playing!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to end the game.")
            continue

        attempts += 1

        if guess < secret_number:
            print("\nThe number is higher than your guess.")
            print("\nYou can do better than this, keep going!")
        elif guess > secret_number:
            print("\nThe number is lower than your guess.")
            print("\nDon't give up, keep trying!")
        else:
            print(f"Congratulations {name}! You got it in {attempts} attempts.")
            if attempts < high_score or high_score == 0:
                try:
                    with open("high_score.txt", "w") as f:
                        f.write(str(attempts))
                        print(f"You set a new high score with {attempts} attempts!")
                except Exception as e:
                    print(f"Error writing high score file: {e}")
            else:
                print(f"The high score is {high_score} attempts.")
            break

def display_rules():
    rules = """Game Rules:
               1] Guess a number between 1 and 100000.
               2] You will be informed if your guess is higher or lower than the actual number.
               3] Keep guessing until you get the number.
               4] You can type 'exit' to end the game at any time.
               """
    print(rules)

def display_developer_info():
    developer_info = """Developer:
                       Name: Tejas Hande
                       Contact: 
                            \t- Email: tejasamolhande@gmail.com 
                            \t- WhatsApp: +918600828734
                            \t- Instagram: @tejashande0
                       """
    print(developer_info)

def display_high_score():
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read().strip() or 0)
            if high_score == 0:
                print("There is no high score yet.")
            else:
                print(f"The current high score is {high_score} attempts.")
    except FileNotFoundError:
        print("High score file not found.")
    except Exception as e:
        print(f"Error reading high score file: {e}")

menu_options = {
    '1': play_game,
    '2': display_rules,
    '3': display_developer_info,
    '4': display_high_score,
    '5': exit
}

print("***********************************************************")
print("*******************  GUESS THE NUMBER  ********************")
print("***********************************************************")

while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice in menu_options:
        menu_options[choice]()

    else:
        print("Invalid input. Please enter a valid choice.")