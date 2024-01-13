import random

options = ("Rock", "Paper", "Scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice(Rock, Paper, Scissors): ")

print(f"Player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("It's a Tie")
elif player == "Rock" and computer == "Scissors":
    print("You Win!")
elif player == "Paper" and computer == "Rock":
    print("You Win!")
elif player == "Scissors" and computer == "Paper":
    print("You Win!")    
else:
    print("You Lose!")
    
