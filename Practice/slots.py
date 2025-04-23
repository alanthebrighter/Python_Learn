import random

def spin_row():
  symbols = ['7','3','1','5','2']
  results = []

  return [random.choice(symbols) for _ in range(3)]


def print_row(row):
  print("---------")
  print(" | ".join(row))
  print("---------")

def get_payout(row, bet):
  if row[0] == row[1] == row[2]:
    if row[0] == "7":
      return bet * 99
    elif row[0] == "3":
      return bet * 33
    elif row[0] == "1":
      return bet * 11
    elif row[0] == "2":
      return bet * 2
    elif row[0] == "5":
      return bet * 5
  return 0


def main():
  balance = 100
  print("-----------------------------------------")
  print("----- Welcome to the Brighter Slots -----")
  print("----- Symbols:  7,3,1,5,2 ---------------")
  print("-----------------------------------------")

  while balance > 0:
    print(f"Current balance: ${balance}")
    bet = input("Enter your bet amount: ")

    if not bet.isdigit():
      print("Enter a valid amount.")
      continue

    bet = int(bet)

    if bet <=0:
      print("The best must be greater than 0.")
      continue

    if bet > balance:
      print("Not sufficient funds.")
      continue

    balance -= bet

    row = spin_row()
    print("Spinning...\n")

    print_row(row)

    payout = get_payout(row, bet)

    if payout > 0:
      print(f"Your profit: ${payout}")
    else:
      print("Sorry, you lost.")

    balance += payout

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.upper() != "Y":
      print(f"Goodbye. Balance: ${balance}")
      break



if __name__ == "__main__":
  main()
