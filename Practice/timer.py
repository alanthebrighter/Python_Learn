# Timer

import time

timerCount = int(input("How many seconds do you want to wait? "))
for remaining in range(timerCount, 0, -1):
  seconds = remaining % 60
  minutes = (remaining // 60) % 60
  hours = remaining // 3600
  print(f"Time remainiging: ({hours:02}:{minutes:02}:{seconds:02})", end="\r")
  time.sleep(1)

print("Time's up!")


