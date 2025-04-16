# i want to make two games, one of number guessing, and other of guessing who is the impostor
import random

min, max = 1, 30 # for the guessing number
players = ["joao", "cacio", "jaqueline", "marcos", "pamela", "isadora", "isabela", "carlos", "kemili", "gabriel"] # for the guessing impostor

print("Welcome welcome, let's have fun!!!")
print("Games: Guess the number, Guess the impostor")
while True:
  guesses = 0
  maxOfGuesses = 5
  choice = input("Which game do you want to play? (type: number, for the guess the number, or impostor, for the guess the impostor (q for quit)): ").lower()
  if choice == "q":
    print("---------------------------------------")
    print("goodbye... friend.")
    break
  if choice == "number":
    print(f"So... I choose a number between {min} and {max} and your have to guess it!!")
    number = random.randint(min, max)
    print("---------------------------------------")
    while True:
      while guesses <= maxOfGuesses-1:
        print(f"you have {maxOfGuesses-guesses} guesses remaining.")
        guess = int(input(f"Enter your guess!! {min}-{max}: "))
        if guess >= min and guess <= max:
          if guess == number:
            guesses += 1
            print("---------------------------------------")
            print(f"awesome!! You nailed it with {guesses} guesses!")
            break
          elif guess != number:
            guesses += 1
            if guess > number:
              print("wrong answer, try a lil bit lower")
            else:
              print("wrong answer, try a lil bit higher")
          if guesses == maxOfGuesses:
            print("-------------------------------")
            print("ohh nooo, you lost!")
        else:
          print(f"{guess} is not a valid guess!")

      print(f"my number was {number}")
      print("------------ END GAME -------------------")
      break

  if choice == "impostor":
    print("So... There are some players in a room and you have to guess who is the impostor!")
    impostor = random.choice(players)
    print("Here are the names of the players")
    for player in players:
      print(f"Player: {player}")
    print("---------------------------------------")
    while True:
      while guesses <= maxOfGuesses-1:
        print(f"you have {maxOfGuesses-guesses} guesses remaining.")
        guess = input(f"Enter your guess: ")
        if guess in players:
          if guess == impostor:
            guesses += 1
            print("---------------------------------------")
            print("Congratulations!!! you have exposed the imposter!")
            break
          elif guess != impostor:
            guesses += 1
            print("oh, you have exposed the wrong player!")
            players.remove(guess)
            print("---------- Remaining players --------------------")
            for player in players:
              print(f"Player: {player}")
          if guesses == maxOfGuesses:
            print("-------------------------------")
            print("ohh nooo, you lost!")
        else:
          print(f"{guess} is not a valid player!")
      print(f"{impostor} was the impostor!")
      print("------------ END GAME -------------------")
      break
  else:
    print(f"{choice} is not a valid game!")


