from random import randint

choices = ["rock","paper", "scissors"]
player_lives = 2
computer_lives = 2
total_lives = 2


player_choice = input ("What do you want to choose? ROCK, PAPER OR SCISSORS? ")
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


print("Player lives: ", player_lives)
print("Computer lives: ", computer_lives)
