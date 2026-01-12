#!/bin/python3

'''
In English, ordinal numerals have suffixes such as the “th” in “30th” or “nd” in “2nd”. Write an ordinalSuffix() function with an integer parameter named number and returns a string of the number with its ordinal suffix.
For example, ordinalSuffix(42) should return the string '42nd'.
You may use Python’s str() function to convert the integer argument to a string. 
Python’s endswith() string method could be useful for this exercise, but to maintain the challenge in this exercise, don’t use it as part of your solution.
These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.
Prerequisite concepts: strings, in operator, slices, string concatenation
'''

ruleOne = ("11", "12", "13")
ruleTwo = ("1", "2", "3")

def ordinalSuffix(number):
    number = str(number)
    endTwo = number[-2:]
    endOne = number[-1:]
    if endTwo in ruleOne:
        return number+"th"
    elif endOne in ruleTwo:
        if endOne == "1":
            return number+"st"
        elif endOne == "2":
            return number+"nd"
        else:
            return number+"rd"
    else:
        return number+"th"


assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
