from random import randint

choices = ["rock","paper", "scissors"]
player_lives = 1
computer_lives = 1
total_lives = 2
player_choice = False

def winorlose(status):
	print("You",status," Would you like to try again?")
	choice = input("Y / N ?")

	if choice == "N" or choice =="n":
		print("You chose to finish the game. See you next time!")
		exit()
	elif choice == "Y" or choice =="y":
		print("Okay! Let's try again!")
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives

	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N? ")




while player_choice is False:

	player_choice = input("What do you want to choose? ROCK, PAPER OR SCISSORS? ")
	print( "user chose: " + player_choice)

	computer_choice = choices[randint(0, 2)]
	print("computer chose: " + computer_choice)

	if computer_choice == player_choice:
		print("tie")

	elif computer_choice == "rock":
		if player_choice == "scissors":
			print("You lose!:(")
			player_lives -= 1
		else:
			print("You win!:)")
			computer_lives -= 1

	elif computer_choice == "paper":
		if player_choice == "scissors":
			print("You win!:)")
			computer_lives -= 1
		else:
			print("You lose!:(")
			player_lives -= 1

	elif computer_choice == "scissors":
		if player_choice == "rock":
			print("You win!:(")
			computer_lives -= 1
		else:
			print("You lose!:(")
			player_lives -= 1

	if player_lives == 0:
		winorlose("loh")
		
	if computer_lives == 0:
		winorlose("won")
		
	print("Player lives: ", player_lives)
	print("Computer lives: ", computer_lives)

	player_choice = False 
