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
		gameVars.player_choice = False
	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N? ")