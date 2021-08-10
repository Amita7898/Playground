from random import randint
# Play options: Rock, Paper, Scissors
# GOAL 1 :computer to randomly select one of these options

# First step: Create a list of these play options
t = ["Rock", "Paper", "Scissors"]

# Second step: Assign a rqndom play option to the computer
computer = t[randint(0,2)]

# Third step: Make a condition so that the game continues
player = False

# Fourth step: Make the game
#first if statement -> if player and computer are same then it is TIE!
# elif statement #1 -> if player is rock and computer is paper -> You lose! 
#                   -> if player is rock and computer is scissors
while player == False:
# Set player to True
  player = input("Rock, Paper or Scissors? ")
  if player == computer:
    print("Tie!")
  elif player == "Rock":
    if computer == "Paper":
      print("You lose!",computer, "covers", player)
    else:
      print("You win!", player, "smashes", computer)
  elif player == "Paper":
    if computer == "Scissors":
      print("You lose!", computer, "cut", player)
    else:
      print("You win!", player, "covers", computer)
  elif player == "Scissors":
    if computer == "Rock":
      print("You lose!", computer, "smashes", player)
    else:
      print("You win!", player, "cut", computer)
  else:
    print("That's not a valid play.Check your spelling")
  # player was set to True, but we want it to be False so that the loop continues
  player = False
  computer = t[randint(0,2)]
  