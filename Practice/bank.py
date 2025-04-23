def showBalance(balance):
  print(f"Balance: ${balance:.2f}")

def deposit():
  amount = float(input("Enter the amount: $"))
  if amount < 0:
    print("Amount not valid.")
    return 0
  else:
    print(f"Operation: +${amount:.2f}")
    return amount

def withdraw(balance):
  amount = float(input("Enter the amount: $"))
  if amount < 0 or amount > balance:
    print("Amount not valid. Check your balance.")
    return 0
  else:
    print(f"Operation: -${amount:.2f}")
    return amount

def main():
  balance = 0
  is_running = True

  while is_running:
    print("Brighter Bank")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      showBalance(balance)
    elif choice == '2':
      balance += deposit()
      showBalance(balance)
    elif choice == '3':
      balance -= withdraw(balance)
      showBalance(balance)
    elif choice == '4':
      is_running = False
    else:
      print("Not a valid operation.")

  print("Goodbye. Have a nice a day!")

if __name__ == "__main__":
  main()
