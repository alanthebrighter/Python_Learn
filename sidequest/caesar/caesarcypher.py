#! /bin/python3

def caesar_cipher(s: str, k: int) -> str:
    result = ""
    #print(s)
    for char in s:
        if char.isalpha():
            if char.isupper():
                upperOffset = ord(char) - ord('A')
                newchar = (upperOffset + k) % 26
                result += chr(newchar + ord('A'))
            else:
                
                lowerOffset = ord(char) - ord('a')
                newchar = (lowerOffset + k) % 26
                result += chr(newchar + ord('a'))
                
        else:
            result += char
    return result

# Testes para validar seu código
print(caesar_cipher("Hello, World!", 3)) # Esperado: "Khoor, Zruog!"
print(caesar_cipher("abc", 2))           # Esperado: "cde"
