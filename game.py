from random import randint

choices = ["rock","paper", "scissors"]

player_choice = input ("What do you want to choose? ROCK, PAPER OR SCISSORS? ")
print( "user chose: " + player_choice)

computer_choice = choices[randint(0, 2)]
print("computer chose: " + computer_choice)

if computer_choice == player_choice:
	print("tie")

elif computer_choice == "rock":
	if player_choice == "scissors":
		print("You lose!:(")
	else:
		print("You win!:)")

elif computer_choice == "paper":
	if player_choice == "scissors":
		print("You win!:)")
	else:
		print("You lose!:(")

elif computer_choice == "scissors":
	if player_choice == "rock":
		print("You win!:(")
	else:
		print("You lose!:)")
