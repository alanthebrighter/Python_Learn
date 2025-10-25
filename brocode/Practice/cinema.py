menu = {
  "jennifer":5.50,
  "isabela":6.75,
  "isadora":8.00,
  "martina":3.50,
  "karita":6.80,
  "rinala":9.5
}
cart = []
total = 0
print("------ MENU ------")
for key, value in menu.items():
  print(f"{key:10}: ${value:.2f}")
print("------------------")

while True:
  food = input("Select your food (q for quit): ").lower()
  if food == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)

print("------- YOUR ORDER --------")
for item in cart:
  total += menu.get(item)
  print(item, end=" ")

print()
print(f"Total: ${total:.2f}")
