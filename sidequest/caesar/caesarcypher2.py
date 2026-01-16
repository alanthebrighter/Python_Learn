#! /bin/python3

def caesar_cipher(s: str, k: int) -> str:
    result = ""
    
    # Read each character in s
    for char in s:
        # Verify if char is a letter to apply the cypher
        if char.isalpha():
            # Verify if it is uppercase and get unicode of uppercaseA
            if char.isupper():
                base = ord('A')
            # Otherwise get unicode of lowercaseA
            else:
                base = ord('a')
            
            # Map unicode to 26 letters alphabet
            offset = ord(char) - base
            # Make alphabet loop zyx -> abc
            newOffset = (offset + k) % 26
            # Mount the result with looped offset plus base
            result += chr(newOffset + base)
        else:
            result += char
    
    return result

# Testes para validar seu código
print(caesar_cipher("Hello, World!", 3)) # Esperado: "Khoor, Zruog!"
print(caesar_cipher("abc", 2))           # Esperado: "cde"
