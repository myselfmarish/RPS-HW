from random import randint

from gameComponents import gameVars, winLose

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

	gameVars.computer_choice = gameVars.choices[randint(0, 2)]
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
		winLose.winorlose("lose")
	


	if gameVars.computer_lives == 0:
		winLose.winorlose("won")
		

	print("Player lives: ", gameVars.player_lives)
	print("Computer lives: ", gameVars.computer_lives)

	gameVars.player_choice = False 
