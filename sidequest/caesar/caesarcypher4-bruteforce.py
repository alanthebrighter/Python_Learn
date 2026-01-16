#! /bin/python3

def bruteforce(text: str, n: int):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')

            offset = ord(char) - base
            newOffset = (offset - n) % 26
            result.append(chr(newOffset + base))
        else:
            result.append(char)
    return ''.join(result)
    

msg = "Bzdrzq rdbqds: Gtqn fqzad bzrrzq d rda n ltrbn rdbqdsn"
for i in range(26):
    print(bruteforce(msg, i))

