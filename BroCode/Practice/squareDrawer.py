# Drawing a square using nested loops

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to draw the square: ")

for r in range(rows):
  for c in range(cols):
    print(symbol, end=" ")
  print()
