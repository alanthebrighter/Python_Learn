import random
import string

string = " " + string.punctuation + string.digits + string.ascii_letters
string = list(string)
key = string.copy()

random.shuffle(key)

plain_text = input("Enter your text: ")
encrypt_text = ""

for char in plain_text:
    index = string.index(char)
    encrypt_text += key[index]


#print(f"Original: {plain_text}")
print(f"Enc: {encrypt_text}")

encrypt_text = input("Enter your text: ")
plain_text = ""

for char in encrypt_text:
    index = key.index(char)
    plain_text += string[index]

print(f"Dec: {plain_text}")

