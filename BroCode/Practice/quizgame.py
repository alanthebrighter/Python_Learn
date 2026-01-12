# Quiz game

questions = ("What does the term rootkit refer to?",
            "Which type of rootkit operates at the operating system's core (kernel level)?",
            "What is the primary purpose of a bootkit rootkit?",
            "Which of the following is NOT a common method for detecting rootkits?",
            "Which of the following is a recommended practice to prevent rootkit infections?")
options = (
  ("A. A type of antivirus software", "B. A collection of tools used to gain unauthorized, hidden access to a system", "C. A hardware device used for secure data storage", "D. A programming language"),
  ("A. User-mode rootkit", "B. Kernel-mode rootkit", "C. Bootkit rootkit", "D. Firmware rootkit"),
  ("A. To encrypt files for ransom", "B. To infect the Master Boot Record (MBR) or bootloader and load before the operating system starts", "C. To monitor user activity in real-time", "D. To create a backdoor in web applications"),
  ("A. Behavioral analysis", "B. Signature-based detection", "C. Installing more rootkits to find existing ones", "D. Offline scanning"),
  ("A. Using outdated software to confuse attackers", "B. Keeping software and operating systems updated with the latest patches", "C. Disabling firewalls to reduce system overhead", "D. Granting administrator privileges to all users")
)
answers = ("B", "B", "B", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("-------------------------------------------")
  print(question)
  for option in options[question_num]:
    print(option)


  isValid = False
  while isValid is False:
    guess = input("What is your answer? A, B, C or D: ").upper()
    if (guess in ["A", "B", "C", "D"]):
      guesses.append(guess)
      isValid = True
    else:
      print("Your answer is not valid!")

  if guesses[question_num] == answers[question_num]:
    score +=20
  '''
  else:
    print("Wrong answer!")
    print(f"The correct answer for {question} is {answers[question_num]}")
  '''
  question_num += 1

print("---------------------------------------------")
print("                  RESULTS                    ")
print("---------------------------------------------")
print(f"Your final grade is {score} points.")
if score == 100:
  print("Absolute cinema!! You are a G3N1US!")
elif score >= 60:
  print("Congratulations, you are good!")
else:
  print("I'm sorry, you didn't make it.")
print("---------------------------------------------")
print("Answers:", end=" ")
for answer in answers:
  print(answer, end=" ")
print()
print("Guesses:", end=" ")
for guess in guesses:
  print(guess, end=" ")
