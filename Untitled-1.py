def rps():
    options = ['rock', 'paper', 'scissors']
    player1_choice = input("Player 1, Enter rock, paper, or scissors: ").lower()
    while player1_choice not in options:
        player1_choice = input("Invalid option. Player 1, Please enter rock, paper, or scissors: ").lower()
    player2_choice = input("Player 2, Enter rock, paper, or scissors: ").lower()
    while player2_choice not in options:
        player2_choice = input("Invalid option. Player 2, Please enter rock, paper, or scissors: ").lower()
    print("Player 1 chose: ", player1_choice)
    print("Player 2 chose: ", player2_choice)
    if player1_choice == player2_choice:
        print("It's a tie!")
    elif player1_choice == 'rock' and player2_choice == 'scissors':
        print("Player 1 wins!")
    elif player1_choice == 'paper' and player2_choice == 'rock':
        print("Player 1 wins!")
    elif player1_choice == 'scissors' and player2_choice == 'paper':
        print("Player 1 wins!")
    else:
        print("Player 2 wins.")

rps()
