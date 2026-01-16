#! /bin/python3

def cypher(text: str, rot: int, mode: str):

    def encrypt(text, rot):
        result = ''
        for char in text:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')

                offset = ord(char) - base
                newOffset = (offset + rot) % 26
                result += chr(newOffset + base)
            else:
                result += char
        return result

    if mode == "enc":
        print("encrypting")
        cryptText = encrypt(text, rot)
        return cryptText 
    elif mode == "dec":
        print("decrypting")
        decryptText = encrypt(text, -rot)
        return decryptText
    else:
        return "Unexpected mode. (enc, dec)"
    


message = cypher("samsung", 6, "enc")
print(message)
message = cypher(message, 6, "dec")
print(message)
