import random
import pygame

def rps():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Rock, Paper, Scissors")
    rock_img = pygame.image.load('rock.png')
    paper_img = pygame.image.load('paper.png')
    scissors_img = pygame.image.load('scissors.png')
    options = {'rock': rock_img, 'paper': paper_img, 'scissors': scissors_img}
    player1_choice = input("Tejas, Enter rock, paper, or scissors: ").lower()
    while player1_choice not in options:
        player1_choice = input("Invalid option. Tejas, Please enter rock, paper, or scissors: ").lower()
    print("Tejas chose: ", player1_choice)
    screen.blit(options[player1_choice], (50, 50))
    pygame.display.update()
    computer_choice = random.choice(list(options.keys()))
    print("Computer chose: ", computer_choice)
    screen.blit(options[computer_choice], (250, 50))
    pygame.display.update()
    if player1_choice == computer_choice:
        print("It's a tie!")
    elif player1_choice == 'rock' and computer_choice == 'scissors':
        print("Tejas wins!")
    elif player1_choice == 'paper' and computer_choice == 'rock':
        print("Tejas wins!")
    elif player1_choice == 'scissors' and computer_choice == 'paper':
        print("Tejas wins!")
    else:
        print("Computer wins.")
    pygame.time.wait(3000)
    pygame.quit()

rps()
