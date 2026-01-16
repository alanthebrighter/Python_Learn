#! /bin/python3

def isAnagram(word1: str, word2: str):
    list1 = list(word1.lower())
    list1.sort()
    list2 = list(word2.lower())
    list2.sort()
    #print(list1, list2)
    if list1 == list2:
        print("Anagrams")
    else:
        print("Not anagrams")


isAnagram("Listen", "Silent")
isAnagram("modern", "norman")
