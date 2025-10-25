import random

wordsToGuess = ["cat", "fish", "rain", "green", "Sky", "leaf"]

hangmanPhases = {
        0: ("   ",
            "   ",
            "   "
            ),
        1: (" o ",
            "   ",
            "   "
            ),
        2: (" o ",
            " | ",
            "   "
            ),
        3: (" o ",
            "/| ",
            "   "
            ),
        4: (" o ",
            "/|\\",
            "   "
            ),
        5: (" o ",
            "/|\\",
            "/  "
            ),
        6: (" o ",
            "/|\\",
            "/ \\"
            )
        }


def display_hangman(guesses):
    print("======================")
    for line in hangmanPhases[guesses]:
        print(line)
    print("======================")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("======================")
    print(" ".join(answer))
  
def main():
    answer = random.choice(wordsToGuess)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Enter your letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_answer(answer)
            print("Congrats, You win!")
            is_running = False
        elif wrong_guesses >= 6:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("Sorry, You lose!")
            is_running = False

if __name__ == "__main__":
    main()
