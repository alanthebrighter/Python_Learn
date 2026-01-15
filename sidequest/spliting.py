#! /bin/python3

def splting(phrase):
    if phrase.isspace():
        return []

    splt_phrase = []
    word = ""

    for char in phrase:
        if char.isspace():
            if word:
                splt_phrase.append(word)
                word = ""
        else:
            word += char
    
    splt_phrase.append(word)
    return splt_phrase



i_phrase = "Humankind cannot gain anything without first giving something in return. To obtain, something of equal value must be lost. That is alchemy's first law of Equivalent Exchange."

print(splting(i_phrase))
