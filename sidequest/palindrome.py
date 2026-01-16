#! /bin/python3

def isPalindrome(text: str):
    cleanText = text.replace(' ', '').lower()
    newText = []
    for ix in range(len(cleanText)):
        ix += 1
        newText.append(cleanText[-ix])

    if cleanText == ''.join(newText):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


        

isPalindrome("Ten animals I slam in a net")
isPalindrome("Eleven animals I slam in a net")
isPalindrome("alan")
