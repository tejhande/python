print("\n***************************************************************************************************")
print("\n****************************************  SNAKE WATER GUN  ****************************************")
print("\n***************************************************************************************************")
print("\n\nEnter 1 To Play")
print("Enter 2 For Rules")
print("Enter 3 To Know About Devloper")
print("Enter 4 To Exit ")
rules = ("Game Rules:\t 1] Gun(g) > Snake(s)\n\t\t 2] Snake(s) > Water(w)\n\t\t 3] Water(w) > Gun(g)")
Dev = ("Tejas Hande\n 8600828734 \n INSTAGRAM ID:- tejashande0 \n Email:- tejasamolhande@gmail.com \n WhatsApp:- wa.me/918600828734")
while True:
    try:
        options = int(input("Enter Option Number: \n\t")) 
    except ValueError:
        print("Invalid Input....")  
        continue
    if options == 1:
        while True:
            player_1 = input("Enter First Player Name: \n\t")
            if player_1.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Input....")
        while True:
            player_2 = str(input("Enter Second Player Name: \n\t"))
            if player_2.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Input....")  
        def gameWin(player_1,player_2):
            if player_1_choice == player_2_choice:
                return None
            elif player_1_choice == 's':
                if player_2_choice == 'w':
                    return False
                elif player_2_choice == 'g':
                    return True
            elif player_1_choice == 'w':
                if player_2_choice == 'g':
                    return False
                elif player_2_choice == 's':
                    return True
            elif player_1_choice == 'g':
                if player_2_choice == 's':
                    return False
                elif player_2_choice == 'w':
                    return True
        while True:
            player_1_choice = input(f"{player_1}'s Turn : Snake(s) Water(w) or Gun(g)?\n\t")
            if len(player_1_choice) == 1 and player_1_choice.isalpha() and player_1_choice in "swg":
                break
            else:
                print("Invalid input. Please enter a single alphabet.")
        while True:
            player_2_choice = input(f"{player_2}'s Turn : Snake(s) Water(w) or Gun(g)?\n\t")
            if len(player_2_choice) == 1 and player_2_choice.isalpha() and player_2_choice in "swg":
                break
            else:
                print("Invalid input. Please enter a single alphabet.")
        c = gameWin(player_1_choice, player_2_choice)
        print(f"{player_1} Choose :\t {player_1_choice}")
        print(f"{player_2} Choose :\t {player_2_choice}")
        if c == None :
            print("The Game Is Tie !")
        elif c == False :
            print(f"{player_2} Lose {player_1} Win")
        else:
            print(f"Congratulations!, {player_2} Win {player_1} Lose")
        break
    elif options == 2:     
        print("You have selected option 2 - Game Rules")     
        print(rules)
    elif options == 3:
        print("You have selected option 3 - Game Developer")
        print(Dev)
    elif options == 4:
        print("You have selected option 4 - Game Exited")
        exit()
    else:
        print("Invalid Input....")
print("Done")
