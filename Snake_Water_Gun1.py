import random

print("\n***************************************************************************************************")
print("\n****************************************  SNAKE WATER GUN  ****************************************")
print("\n***************************************************************************************************")
print("\n\nEnter 1 To Play")
print("Enter 2 For Rules")
print("Enter 3 To Know About Developer")
print("Enter 4 To Exit ")

rules = "Game Rules:\n\t 1] Gun(g) > Snake(s)\n\t\t 2] Snake(s) > Water(w)\n\t\t 3] Water(w) > Gun(g)"
developer_info = "Developer: Tejas Hande\n8600828734\nINSTAGRAM ID: tejashande0\nEmail: tejasamolhande@gmail.com\nWhatsApp: wa.me/918600828734"

while True:
    try:
        option = int(input("Enter Option Number: \n\t")) 
    except ValueError:
        print("Invalid Input....")  
        continue
        
    if option == 1:
        while True:
            player_2 = input("Enter Your Name: \n\t")
            if player_2.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Input....")
                
        player_1_choices = ["s", "w", "g"]
        player_1_choice = random.choice(player_1_choices)
        # player_2_choices = ["s", "w", "g"]
        # player_2_choice = random.choice(player_2_choices)
        
        while True:
            player_2_choice = input(f"{player_2}'s Turn : Snake(s) Water(w) or Gun(g)?\n\t")
            if len(player_2_choice) == 1 and player_2_choice.isalpha() and player_2_choice in "swg":
                break
            else:
                print("Invalid input. Please enter a single alphabet.")

        print(f"\nComputer Choose :\t {player_1_choice}")
        print(f"{player_2} Choose :\t {player_2_choice}")
        
        if player_1_choice == player_2_choice:
            print("The Game Is Tie !")
        elif player_1_choice == 's':
            if player_2_choice == 'w':
                print(f"Congratulations!, {player_2} Win")
            elif player_2_choice == 'g':
                print(f"{player_2} Lose, Computer Win")
        elif player_1_choice == 'w':
            if player_2_choice == 'g':
                print(f"Congratulations!, {player_2} Win")
            elif player_2_choice == 's':
                print(f"{player_2} Lose, Computer Win")
        elif player_1_choice == 'g':
            if player_2_choice == 's':
                print(f"Congratulations!, {player_2} Win")
            elif player_2_choice == 'w':
                print(f"{player_2} Lose, Computer Win")
        
    elif option == 2:     
        print("You have selected option 2 - Game Rules")     
        print(rules)
        
    elif option == 3:
        print("You have selected option 3 - Game Developer")
        print(developer_info)
        
    elif option == 4:
        print("You have selected option 4 - Game Exited")
        exit()
        
    else:
        print("Invalid Input....")

print("Done")
