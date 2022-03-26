from random import randint

from gameComponents import gameVars

def winorlose(status):
	print("You", status,"lose! Would you like to try again?")
	choice  = input ("Y / N ?")

	if choice == "N" or choice =="n":
		print("You chose to finish the game. See you next time!")
		exit()
	elif choice == "Y" or choice =="y":
		print("Okay! Let's try again!")
		

		gameVars.player_lives = gameVars.total_lives
		gameVars.computer_lives = gameVars.total_lives
	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N? ")

while gameVars.player_choice is False:
	print("♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡ THE BEST RPS GAME EVER ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡")
	print("\tComputer Lives:".expandtabs(28), gameVars.computer_lives, "/", gameVars.total_lives)
	print("\tPlayer Lives".expandtabs(28), gameVars.player_lives, "/", gameVars.total_lives,)
	print("______________________________________________________________________________")

	print("Choose your weapon! Or type quit to exit\n")		

	gameVars.player_choice = input ("What do you want to choose? ROCK, PAPER OR SCISSORS? ")
	
	if gameVars.player_choice == "quit":
		print("You chose quit")
		exit()

	print( "user chose: " + gameVars.player_choice)	

	gameVars.computer_choice = choices[randint(0, 2)]
	print("computer chose: " + gameVars.computer_choice)

	if gameVars.computer_choice == gameVars.player_choice:
		print("tie")

	elif gameVars.computer_choice == "rock":
		if gameVars.player_choice == "scissors":
			print("You lose!:(")
			gameVars.player_lives -= 1
		else:
			print("You win!:)")
			gameVars.computer_lives -= 1

	elif gameVars.computer_choice == "paper":
		if gameVars.player_choice == "scissors":
			print("You win!:)")
			gameVars.computer_lives -= 1
		else:
			print("You lose!:(")
			gameVars.player_lives -= 1

	elif gameVars.computer_choice == "scissors":
		if gameVars.player_choice == "rock":
			print("You win!:)")
			gameVars.computer_lives -= 1
		else:
			print("You lose!:(")
			gameVars.player_lives -= 1

	if gameVars.player_lives == 0:
		winorlose("lose")
	


	if gameVars.computer_lives == 0:
		winorlose("won")
		

	print("Player lives: ", gameVars.player_lives)
	print("Computer lives: ", gameVars.computer_lives)

	gameVars.player_choice = False 
