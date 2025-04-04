# Calculating compound
amount = 0
rate = 0
time = 0

while True:
  amount = float(input("Enter the principle amount: "))
  if amount < 0:
    print("Principle amount can't not be less than zero.")
  else:
    break
while True:
  rate = float(input("Enter the interest rate: "))
  if rate < 0:
    print("Interest rate can't be less than zero.")
  else:
    break
while True:
  time = int(input("Enter the time in years: "))
  if time < 0:
    print("Time can't be less than zero.")
  else:
    break

compound = amount * pow((1+ rate/100), time)
print(f"The compound after {time} years, with the rate {rate}/y, is equal to ${compound:.2f}")
