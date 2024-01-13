import random
print("\n***************************************************************************************************")
print("\n****************************************  GUESS THE NUMBER  ****************************************")
print("\n***************************************************************************************************")
def guess_the_number():
  print("Welcome to Guess the Number!")
  print("I'm thinking of a number between 1 and 100000.")
  print("Can you guess what it is?")
  secret_number = random.randint(1, 100000)
  guess = None
  attempts = 0  
  with open("HighScore.txt", "r") as f:
    high_score = int(f.read().strip() or 0)
  print(f"The current high score is {high_score} attempts.") 
  while guess != secret_number:
    try:
      guess = int(input("Enter your guess: "))
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      continue
    attempts += 1    
    if guess == 2013272507084040:     #Cheat Code
      print(secret_number, "🤫🤭")
    if guess < secret_number:
      print("The number is higher Than Guess.")
    elif guess > secret_number:
      print("The number is lower Than Guess.")
    else:
      print(f"You got it! It took you {attempts} attempts.")
      if attempts < high_score or high_score == 0:
        with open("HighScore.txt", "w") as f:
          f.write(str(attempts))
          print(f"You set a new high score with {attempts} attempts.")
      else:
        print(f"The high score is {high_score} attempts.")
if __name__ == '__main__':
  guess_the_number()
