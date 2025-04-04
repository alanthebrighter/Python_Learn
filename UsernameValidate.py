# Validate user input exercise
# username <= 12
# username no spaces
# username no digits

username = input("Enter  your username: ")
isLess = True if len(username) <=12 else False
noSpace = True if username.find(" ") == -1 else False
noDigits = username.isalpha()

if isLess and noSpace and noDigits:
  print(f'{username} is valid')
else:
  print(f"{username} is not valid, can't be more than 12 characters, have spaces and digits")
