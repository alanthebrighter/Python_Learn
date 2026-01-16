#! /bin/python3

def isIn(word, text):
    pos = -1
    possible = True
    word = word.lower()
    text = text.lower()

    for char in word:
        pos = text.find(char, pos+1)

        if pos == -1:
            possible = False
            break

    if possible:
        print("Yes")
    else:
        print("No")

    

isIn("donor", "Nabucodonosor")
isIn("donut", "Nabucodonosor")
isIn("kakarot", "Keyqahtreatok")
