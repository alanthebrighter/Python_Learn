#! /bin/python3

def digitOfYear(date: int):

    def adding(input):
        numbersStr = list(str(input))
        sumCarry = 0
        for n in numbersStr:
            sumCarry += int(n)
        
        if len(str(sumCarry)) != 1:
            adding(sumCarry)
        else:
            print(sumCarry)
    
    adding(date)
    




digitOfYear(19991229)
digitOfYear(20000101)
