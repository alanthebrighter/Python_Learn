# a simple userBet game with two dices multiples money if the sumOfDices is above a number.
import random

credits = 0

while True:
  userDeposit = float(input("Enter your deposit: "))
  # Check player deposit and credits
  if userDeposit > 0:
    credits += userDeposit
    print(f"You have deposited {userDeposit}")
  elif userDeposit < 0:
    print("Invalid amount! Deposit must be positive or zero.")
    continue

  if credits <= 0:
    print("You do not have enough credits to continue. Game over!")
    break

  print(f"Credits: ${credits}")
  # Check player userBet
  userBet = float(input("Enter your userBet (0 to quit): "))
  if userBet <= 0:
    print(f"End game. Good bye. Credits: ${credits}")
    break
  if userBet > credits:
    print(f"You can't userBet more than ${credits}")
    continue

  # Start the game
  credits -= userBet
  print(f"You have userBet {userBet} units. Remaining credits: {credits}")

  # Roll dices
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  sumOfDices = dice1 + dice2

  print(f"You rolled {dice1} and {dice2}. sumOfDices: {sumOfDices}")

  # Win/Loss Logic
  if sumOfDices in [2, 12]:
    multiplier = 50 # High win
  elif sumOfDices in [3, 11]:
    multiplier = 5 # Medium win
  elif sumOfDices in [4, 10]:
    multiplier = 2 # Low win
  elif sumOfDices in [5, 9]:
    multiplier = 0.5 # Lose half the userBet
  elif sumOfDices in [6, 8]:
    multiplier = 1 # Neutral
  elif sumOfDices == 7:
    multiplier = 0 # Lose everything

  # Calculate the outcome of the userBet
  if multiplier == 0:
    print("You lost everything!")
    win = -userBet # Lose the amount userBet
  elif multiplier == 0.5:
    win = -userBet * 0.5 # Lose half of the userBet
    print(f"You lost half of the userBet ({-win:.2f}).")
  elif multiplier == 1:
    win = 0 # Neutral, neither win nor lose
    print("Neutral outcome. You got your userBet back.")
  else:
    win = userBet * (multiplier - 1) # Net gain
    print(f"You won {win + userBet:.2f} units!")

  # Updates the final credits
  credits += userBet + win # Adds back the initial userBet and win/loss
  print(f"Final credits after the round: {credits:.2f}\n")

  # Checks if the player has run out of credits
  if credits <= 0:
    print("You have run out of credits. Game over!")
    break






